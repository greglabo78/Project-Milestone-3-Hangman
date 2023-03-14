import random


# Color codes to be used within the game
ALERT = "\033[91m"
RESPONSE = "\033[92m"
TEXT = "\033[0m"
HIGHLIGHT = "\033[7m"

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

# print(random.choice(words))

def play_game(word):
    """
    The is functiuon sets up the initial variables to enable the game to be played
    """
    guessed_letters = []
    guessed_max = 6
    num_guesses = 0
    game_over = False

# After initiating variables the game will print out its welcome statements to the user
print(COLOURS["pink"] + "Welcome, to the Hangman game!")