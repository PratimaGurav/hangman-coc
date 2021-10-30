import random
from words import words_list


def start_game():
    """
    Function for logo
    """
    print(
        """
         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                            |___/
        """
    )
    # print the welcome message
    name = input("What is your name?\n")
    print(f"Hello, {name}")
    if input("Would you like to play Hangman? (Y)").upper() == "Y":
        hangman()

    else:
        print("You need to enter a username to continue...\n")  
        start_game()

# function to get random word from the list
def get_word():
    """Picks a random word from words.py"""
    word = random.choice(words_list)
    return word.upper()


def hangman():
    """Play the game"""





# call the start game function
start_game()