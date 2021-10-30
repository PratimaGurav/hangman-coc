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


# function for the game
def hangman(word):
    """Play the game"""
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print("Let's play Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")

def display_hangman(attempts):
    stages = [  # final state: head, neck, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, neck, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, neck, torso, and both arms
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, neck, torso, and one arm
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head, neck and torso
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |      |
                   |      |
                   |     
                   -
                """,
                # head and neck
                """
                   --------
                   |      |
                   |      O
		           |      |	
                   |    
                   |      
                   |     
                   -
                """,
		        # head 
                """
                   --------
                   |      |
                   |      O	
                   |    
                   |      
                   |
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |
                   |     
                   -
                """
    ]
    return stages[attempts]




# call the start game function
start_game()