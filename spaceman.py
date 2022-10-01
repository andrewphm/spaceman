from operator import truediv
import random


def load_word():
    """
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    """
    f = open("words.txt", "r")
    words_list = f.readlines()
    f.close()

    # comment this line out if you use a words.txt file with each word on a new line
    words_list = words_list[0].split(" ")
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    """
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    has_won = False
    for letter in secret_word:
        if letter in letters_guessed:
            has_won = True
        else:
            has_won = False

    return has_won


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
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

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    """
    # TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False


def prompt_letter():
    while True:
        user_letter = input("Enter a letter: ")
        if len(user_letter) > 1:
            print("Please only enter one letter at a time.")
            continue
        else:
            return user_letter


def unguessed_letters(guessed_letters):
    # Returns letters not guessed yet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_array = [i for i in alphabet]
    index = 0
    for letter in alphabet_array:
        if letter in guessed_letters:
            alphabet_array[index] = ""
        index += 1
    return "".join(alphabet_array)


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    """
    num_of_guesses = 7
    guesses = []
    print(f"secret word: {secret_word}")
    # TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print(f"The secret word contains: {len(secret_word)} letters.")

    print(f"You have {7} incorrect guesses, please enter one letter per round.")
    while num_of_guesses > 0:
        print("-" * 37)
        # TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = prompt_letter()
        guesses.append(guess)

        # TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("Your guess appears in the word!")
            # TODO: show the guessed word so far
            print(f"Guessed word so far: {get_guessed_word(secret_word, guesses)}")
            print(
                f"These letters haven't been guessed yet: {unguessed_letters(guesses)}"
            )
        else:
            print("Sorry your guess was not in the word, try again.")
            num_of_guesses -= 1
            print(f"You have {num_of_guesses} incorrect guesses left.")
            print(f"Guessed word so far: {get_guessed_word(secret_word, guesses)}")
            print(
                f"These letters haven't been guessed yet: {unguessed_letters(guesses)}"
            )
        # TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, guesses):
            print("You guessed all the words")


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
