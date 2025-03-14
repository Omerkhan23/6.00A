# Problem Set 2, hangman.py
# Name:MUHAMMAD OMER KHAN
# Collaborators:None
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = r"c:\Users\It Zone\Desktop\omer_kHn\6.001A\prob_sets\mit6_100l_f22_ps2_code\1_ps2\words.txt"

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
    for e in secret_word:
        if e not in letters_guessed:
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
    progress = []
    for e in secret_word:
        if e not in letters_guessed:
            progress.append('*')
        else:
            progress.append(e)
                   
    return ''.join(progress)
        



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    letters_list = list(letters)
    for e in letters_guessed:
        if e in letters_list:
          letters_list.remove(e)
    return ''.join(letters_list)    




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
    print(f"Welcome to the Hangman!")
    print(f"I am thinking of the word that is {len(secret_word)} letters long")

    all_letters = string.ascii_lowercase + string.ascii_uppercase
    total_number_guesses = 10
    help_operator = '!'
    vowels = 'aeiou'
    consonants = all_letters.replace(vowels,'')
    letters_guessed = []
    

    def unique_letters(secret_word):
        unique = []
        for i in secret_word:
            if i not in unique:
                unique.append(i)
        return unique

    

    while total_number_guesses > 0:
        
        print('------------')

        print(f'You have {total_number_guesses} guesses left')

        available_letters = get_available_letters(letters_guessed)
        print(f'Available letters: {available_letters}')


        
        guess = input('Please guess a letter: ').lower()
        
        if len(guess) > 1:
            print('Oops! invalid output, Only a single character from the alphabet is acceptable')
        

        elif guess in letters_guessed:
            print(f'Letter have already been guessed: {get_word_progress(secret_word,letters_guessed)}')
            
        
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f'Good guess: {get_word_progress(secret_word,letters_guessed)}')
			
            if has_player_won(secret_word, letters_guessed):
                print('------------')
                print(f'Congrats! You Won')
                return print(f'Your total score is: {(total_number_guesses + 4 * len(unique_letters(secret_word))) + (3 * len(secret_word))}')

             

        elif with_help == True and guess == help_operator:
            # Check if there are enough guesses left
            if total_number_guesses >= 3:
                # Find letters in the secret word that have not been guessed
                remaining_letters = [i for i in secret_word if i not in letters_guessed]
                if not remaining_letters:
                    print('No more letters to reveal')
                else:
                    # Reveal a random letter
                    new = random.choice(remaining_letters)
                    letters_guessed.append(new)
                    total_number_guesses -= 3 # Deduct 3 guesses
                    print(f'Letter revealed: {new}')
                    if has_player_won(secret_word,letters_guessed):
                        print(f'Good guess: {secret_word}')
                        break
                    print(get_word_progress(secret_word, letters_guessed))
            else:
                # Not enough guesses left
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")

            
            
                
        elif guess not in all_letters   :
            print(f'OOps! invalid input, Please select the letter from the alphabet: {get_word_progress(secret_word,letters_guessed)}')
            
        
        
        elif guess in vowels:
            
            letters_guessed.append(guess)
            
            if total_number_guesses <= 2:
                print('------------')
                print(f'Sorry! You ran out of guesses')
                return print(f'The secret word was: {secret_word}')
            else:
                print(f'Oops! that vowel is not my word: {get_word_progress(secret_word,letters_guessed)}')
                total_number_guesses -= 2
                
            
        elif guess in consonants :
            
            letters_guessed.append(guess)
            print(f'Oops! that consonant is not in my word: {get_word_progress(secret_word, letters_guessed)}')
            total_number_guesses -= 1    
			
	#after the loop has ended
    
    if has_player_won(secret_word,letters_guessed) == True:
        print('------------')
        print(f'Congrats! You won')
        return print(f'Your total score of the game is: {(total_number_guesses + 4 * len(unique_letters(secret_word))) + (3 * len(secret_word))}' )
    else:
        print('------------')
        return print(f'Sorry you ran out of guesses,the word was: {secret_word}')       
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist) 
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.


