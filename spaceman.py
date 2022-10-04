import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def load_word():

    """
    A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    Returns:  string: The secret word to be used in the spaceman guessing game
    """

    infile = open("words.txt", "r")
    words_list = infile.readlines()
    infile.close()

    # comment this line out if you use a words.txt file with each word on a new line
    words_list = words_list[0].split(" ")
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    """
    Checks to see if the player has won yet. It checks to see if all the letters in the secret_word are in the letters_guesed array.

    Parameters: secret_word and letters_guessed

    Returns: A boolean if won or not.

    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Parameters:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    """

    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guess_so_far = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guess_so_far += letter
        else:
            guess_so_far += "_"

    return guess_so_far


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word
    Parameters::
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    """

    # TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True

    return False


def prompt_letter(guessed_letters):
    """
    Prompts user for a letter to guess. Validates if it's only one letter and if it has been guessed before.
    Parameters:
        guessed_letters (string): the letters previously guessed
    Returns:
        user_letter: a character the user guesses
    """
    while True:
        user_letter = input("Enter a letter: ")
        if len(user_letter) > 1:
            print("Please only enter one letter at a time.")
            continue
        elif user_letter in guessed_letters:
            print(
                f"{bcolors.FAIL}You have already guessed this, choose a different letter.{bcolors.ENDC}"
            )
        else:
            return user_letter


def unguessed_letters(guessed_letters):
    """
    A function to return a string of unguessed letters.
    Paramters:
        guessed_letters (list): a list of letters already guessed.
    Returns:
        letters_unguessed (string) showing letters the user has not guessed yet.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters_unguessed = ""

    for letter in alphabet:
        if letter not in guessed_letters:
            letters_unguessed += letter
    return letters_unguessed


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Parameters:
      secret_word (string): the secret word to guess.
    """

    num_of_guesses = 7
    guesses = []

    # TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print(f"The secret word contains: {len(secret_word)} letters.")

    print(f"You have {7} incorrect guesses, please enter one letter per round.")
    while num_of_guesses > 0:
        print("-" * 70)
        # TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = prompt_letter(guesses)
        guesses.append(guess)

        # TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print(f"{bcolors.OKGREEN}Your guess appears in the word!{bcolors.ENDC}")
            # TODO: show the guessed word so far
            print(
                f"Guessed word so far: {bcolors.OKBLUE}{bcolors.BOLD}{get_guessed_word(secret_word, guesses)}{bcolors.ENDC}"
            )
            print(
                f"These letters haven't been guessed yet: {unguessed_letters(guesses)}"
            )
        else:
            num_of_guesses -= 1

            if num_of_guesses == 0:
                print("Sorry your guess was not in the word.")
                print("Sorry you didn't win, try again!")
                print(f"The word was: {secret_word}")
                break

            print(
                f"{bcolors.WARNING}Sorry your guess was not in the word, try again."
            )
            print(
                f"{bcolors.FAIL}You have {num_of_guesses} incorrect guesses left.{bcolors.ENDC}"
            )
            print(
                f"Guessed word so far: {bcolors.OKBLUE}{bcolors.BOLD}{get_guessed_word(secret_word, guesses)}{bcolors.ENDC}"
            )
            print(
                f"These letters haven't been guessed yet: {unguessed_letters(guesses)}"
            )
        # TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, guesses):
            print(f"{bcolors.OKGREEN}You won!")
            break


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
