import random
import string
from words import words
from hangman_display import display_hangman

# Stack overflow was referred to add color scheme to the project
# (https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal)


class tcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WARN = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'


def title_msg():
    """
    Function for title
    """
    print(
        """
         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                            |___/
        """ + tcolors.BLUE +
        """
        How to play:
       * Enter username to start the game.
       * Select difficulty level either Easy or Hard.
       * Guess the hidden name of the Country or City represented by _ _ _ _
       * On each incorrect guess one life is deducted & hangman starts building
       * Game is over either when you have correctly guessed the word
       * Or when you have run out of lives.
       * Good Luck!
        """ + tcolors.WHITE
    )


def start_game():
    """
    Starts the game, retreives username and
    option to select difficulty levels.
    """
    # print the welcome message
    title_msg()

    name = input("Please enter your username:\n>")
    if name == "":
        print(tcolors.WARN + "Please enter a username:\n>" + tcolors.WHITE)
        start_game()
    else:
        print(f"Hello, {name}")
        select_difficulty()


def select_difficulty():
    """
    Let player set difficulty
    """
    selected_diff = input("Select difficulty\n"
                          "Please enter E - Easy or H - Hard:\n>")
    selected_diff = selected_diff.upper()
    print("You have chosen: ", selected_diff)
    if selected_diff == 'H':
        lives = 5
        hangman(lives)
    elif selected_diff == 'E':
        lives = 7
        hangman(lives)
    else:
        print(tcolors.WARN + "You have selected E or H\n" + tcolors.WHITE)
        select_difficulty()


# function to get random word from the list
def get_word():
    """Picks a random word from words.py"""
    word = random.choice(words)
    return word.upper()


# function for game
def hangman(lives):
    """Play the game"""
    word = get_word()
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left')
        print('You have used these letters: ' + ', '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(display_hangman[lives])
        print('Guess the word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n>').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print(tcolors.WARN + "Letter is not in the word" +
                      tcolors.WHITE)

        elif user_letter in used_letters:
            print(tcolors.WARN + "You have already used that letter."
                  "Please try again." + tcolors.WHITE)
        else:
            print(tcolors.WARN + "Invalid letter. Please try again." +
                  tcolors.WHITE)

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(display_hangman[lives])
        print(tcolors.RED + 'Game Over! The correct word was', word +
              tcolors.WHITE)
        restart_game()
    else:
        print(tcolors.GREEN + "You have correctly guessed the word", word,
              "\nCongratulations!!" + tcolors.WHITE)
        restart_game()


def restart_game():
    """ Gives player an option to restart, otherwise returns to title screen
    """
    game_restart = False

    while not game_restart:
        restart = input(tcolors.BOLD + "Would you like to play Hangman again?"
                        "(Y/N)\n").upper()

        if restart == "Y":
            game_restart = True
            select_difficulty()

        elif restart == "N":
            game_restart = True
            print(tcolors.BLUE + "Thank You for playing Hangman-CoC."
                  "Goodbye!" + tcolors.WHITE)
        else:
            print(tcolors.WARN + "You must select Y or N."
                  "Please try again." + tcolors.WHITE)


if __name__ == "__main__":
    start_game()
