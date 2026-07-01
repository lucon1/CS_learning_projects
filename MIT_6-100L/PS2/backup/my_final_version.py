# Problem Set 2, hangman.py
# Name: Lucas Harlien
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
        
        
def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    revealed_word = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            revealed_word += '*'
        else:
            revealed_word += letter
                       
    return revealed_word

def choose_to_reveal(secret_word, letters_guessed):
    
    valid_letters = ''
    for letter in secret_word:
        if letter not in letters_guessed:
            valid_letters += letter
    
    return random.choice(valid_letters)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available = ''
    
    for letter in alphabet:
        if letter not in letters_guessed:
            available += letter

    return available

def calculate_score(secret_word, guesses):
    unique_letters = ''
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter
    total_score = (guesses + 4 * len(unique_letters)) + (3 * len(secret_word))
    return total_score

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    letters_guessed = []
    
    while not has_player_won(secret_word, letters_guessed) and guesses > 0:
        print('--------------')
        print(f"You have {guesses} guesses remaining.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        current_guess = input("Please guess a letter: ").lower()
        
        if len(current_guess) != 1 or current_guess not in string.ascii_lowercase and current_guess != "!":
            print("Invaluid entry. Please select a single letter of the alphabet")
            continue
        if current_guess in letters_guessed:
            print("This letter has been guessed already.")
            continue
        if current_guess == '!':
            if guesses > 3:
                print('This is a tough one, let me help you')
                current_guess = choose_to_reveal(secret_word, letters_guessed)
                letters_guessed += current_guess
                guesses -= 3
                print(get_word_progress(secret_word, letters_guessed))
                continue
            else:
                print('Sorry, not enough guesses remaining, try a new letter. You can do this!')
                continue
        
        letters_guessed += current_guess
        
        if current_guess in secret_word:
            print("You got one right!")
        elif current_guess in 'aeiou':
            print("That letter is not in the word. Loose 2 guesses because it is a vowel")
            guesses -= 2
        else:
            print("That letter is not in the word.")
            guesses -= 1
            
        print(get_word_progress(secret_word, letters_guessed))
        
    if has_player_won(secret_word, letters_guessed):
        print(f"You Won! You guessed the secret word. Your score is {calculate_score(secret_word, guesses)}")
    else:
        print(f"Game Over. The word was {secret_word}. Try again next time!")
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    wordlist = load_words()
    secret_word = choose_word(wordlist)
    with_help = True
    print("Lets play Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("if you wish for some help type '!'")
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

