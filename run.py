import random


# Color codes to be used within the game
COLOURS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "pink": "\033[95m",
    "cyan": "\033[36m",
    "purple": "\033[35m"
}

# Collection of words to be used in the game
words = ['lagos', 'sweet', 'friend', 'japan', 'elephant', 'mountain', 'bicycle', 'taxi', 'fruit', 'bank']


# List of hangman stages
hangman_stages = [
    """
    +---+
        |
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
    |   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
   /|   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\  |
        |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\  |
   /    |
        |
       ===
    """,
    """
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
    return random.choice(words)


def initiate_game(word):
    """
    This function sets up the initial variables to enable the game to be played
    """
    guessed_letters = []
    guessed_max = 6
    num_guesses = 0
    hangman_stage = 0
    
    # After initiating variables the game will print out 
    # its welcome statements to the user
    print(COLOURS["pink"] + "Welcome to the Hangman game!")
    print("The word has", COLOURS["cyan"], len(word), "letters.")
    print(" ".join("_" * len(word)))
    
    return guessed_letters, guessed_max, num_guesses, hangman_stage


def guess_word(word):
    """
    This function accepts user input and returns feedback 
    on whether the input is correct or not
    """
    guessed_letters, guessed_max, num_guesses, hangman_stage = initiate_game(word)
    game_over = False
    
    # loop until game is over
    while not game_over:
        guess = input("Guess a letter:\n ").lower()
        
        # Check if guess has already been made
        if guess in guessed_letters:
            print("You already guessed that letter")
        else:
            guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
        else:
            print(f"{COLOURS['red']} That is not the right option!")
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
            print(f"{COLOURS['red']}You lose! The word was {word}")
            game_over = True


def play_again():
    """
    This functions keeps the game running without 
    having to restart the program eanbling user
    to have a continuos gaming experience
    """
    while True:
        choice = input("Do you want to play again? (y/n): ")
        if choice.lower() == "y":
            guess_word(word)
        elif choice.lower() == "n":
            raise SystemExit("Game Over..\n")
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


# Play Game


word = pick_a_word(words)
initiate_game(word)
guess_word(word)
play_again()
