"""
This is a module for generating random numbers
"""
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangmangame')

auth = SHEET.worksheet('auth')


def authenticate():
    """
    This function authenticates the player to get access to the game
    it provides the player with the username and password and authenticates via
    google sheet api
    """
    print("Username: player1")
    print("password:password")
    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        try:
            username = input("Enter your username:\n")
            password = input("Enter your password:\n")

            user_data = auth.find(username)
            if password == auth.cell(user_data.row, user_data.col + 1).value:
                print("Authentication successful!")
                return
            elif user_data is None:
                attempts += 1
                print("Invalid username or password. Please try again")
            else:
                print("Invalid username or password. Please try again")

        except AttributeError:
            print("Invalid username or password. Please try again")
        attempts += 1

    print("Maximum authentication attempts reached....Exiting")
    raise SystemExit


# Color to enhance user experience
UX = {
    "red": "\033[31m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[95m",
    "cyan": "\033[36m",
    "purple": "\033[35m"
}

# Collection of words to be used in the game
words = [
    'lagos', 'rhino', 'friend', 'zebra', 'pelican', 'stingray',
    'rockies', 'taxi', 'fruit', 'bank'
]

# List of hangman stages
hangman_stages = [
    r"""
    +---+
        |
        |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
        |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
    |   |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|   |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
        |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
   /    |
        |
       ===
    """,
    r"""
    +---+
    O   |
   /|\  |
   / \  |
        |
       ===
    """
]


def pick_a_word(words):
    """
    This function will select a random word from the list of words
    for the user to guess
    """
    random.shuffle(words)
    return words[0]


def initiate_game(word):
    """
    This function sets up the initial variables to enable the game to be played
    """
    guessed_letters = []
    guessed_max = 6
    num_guesses = 0
    hangman_stage = 0

    return guessed_letters, guessed_max, num_guesses, hangman_stage


def guess_word(word):
    """
    This function will print welcome statements
    Print the number of letters for the secret word
    provide blank spaces to be guessed
    will provide a quitting experience if "q" is selected
    while game is running
    run the main function of the game
    """
    print(UX["pink"] + "Welcome to the Hangman game!")
    print("The word has", UX["cyan"], len(word), "letters.")
    print(" ".join("_" * len(word)))

    guessed_letters, guessed_max, num_guesses, hangman_stage = \
        initiate_game(word)
    game_over = False

    # loop until game is over
    while not game_over:
        try:
            guess = input("Guess a letter (enter 'q' to quit):\n").lower()
            if guess == "q":
                raise SystemExit(f"{UX['yellow']}quitting game....")
            if not guess.isalpha() or len(guess) != 1:
                raise TypeError
        except TypeError:
            print(
                f"{UX['yellow']}Please enter a single alphabetic letter!")
            continue

        # Check if guess has already been made
        if guess in guessed_letters:
            print("You already guessed that letter")
        else:
            guessed_letters.append(guess)

        if guess in word:
            print(f"{UX['blue']}Correct!")
            num_guesses += 1
        else:
            print(f"{UX['red']} That is not the right option!")
            num_guesses += 1
            hangman_stage += 1

        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print()

        print(hangman_stages[hangman_stage])

        # Check if the player won or lost
        if set(word) == set(guessed_letters):
            print("You win!")
            game_over = True
        elif num_guesses == guessed_max:
            print(f"{UX['red']}You lose! The word was {word}")
            game_over = True


def play_again():
    """
    This function keeps the game running without
    having to restart the program, enabling the user
    to have a continuous gaming experience
    """
    while True:
        choice = input("Do you want to play again? (y/n): ")
        if choice.lower() == "y":
            word = pick_a_word(words)
            initiate_game(word)
            guess_word(word)
        elif choice.lower() == "n":
            raise SystemExit(f"{UX['pink']}Game Over..\n")
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

# Play Game


authenticate()
word = pick_a_word(words)
initiate_game(word)
guess_word(word)
play_again()
