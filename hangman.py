# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
BOLD = '\033[1m'
END = '\033[0m'

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded...")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
   
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_word = ""

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter 
        else:
            guessed_word = guessed_word + " _ "
    return guessed_word





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter + " "
    return available_letters


def get_unique_letters(secrect_word):
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)
            
    return len(letters)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    runs = 0
    
    guesses_left = 6
    warnings = 3

    message = " "
    have = "You have"

    letters_guessed = []
    print()
    print("Welcome to the game Hangman!")
    print()
    print("I am thinking of a word that is" , len(secret_word), "letters long.")
    print()
    print(have, warnings, "warnings left.")
    
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        runs += 1
        print()
        print("-" * 13, "-" * 13, "-" * 13) 
        print()
        print(have, guesses_left, "guesses left.")
        print()
        print("Available letters:" , get_available_letters(letters_guessed))
        print()
        guess = input("Please guess a letter: ")
       

        if not str.isalpha(guess):
            message = "Oops! That is not a valid letter."

            if warnings > 0:
                warnings -= 1
                message += have, warnings, "left:"

            else:
                guesses_left -= 1
                message += " You have no warnings left so you lose one guess:"
       
        else:
            guess = guess.lower()
            
            if guess in letters_guessed:
                message = "Oops! You've already guessed that letter. "
                
                if warnings > 0:
                  warnings -= 1
                  message = f"Oops! You've already guessed that letter. You now have {warnings} warnings left. "

                else:
                 guesses_left -= 1
                 message += "You have no warnings left so you lose one guess: "
            else:
                
                letters_guessed.append(guess)

                if guess in secret_word:
                    message = "Good guess: "
                
                else:

                  if guess in 'aeiou':
                     guesses_left -= 2
                     message = "Oops! That vowel is not in my word, so you lose 2 guesses: "
                  else:
                     guesses_left -= 1
                     message = f"Oops! {BOLD}{guess.upper()}{END} is not in my word: "
            print()
            print(message, get_guessed_word(secret_word, letters_guessed))
            print()
            if runs > 1 and guesses_left > 0:
                yes_or_no = input("Would you like to guess the word? (Y)es or (N)o: ")
                yes_or_no = yes_or_no.lower()
                print()
                if yes_or_no == "y" :
                   print()
                   final_guess = input("Please input your final guess if you have one: ")
                   print()
                   if final_guess == secret_word:
                       break
                   else: 
                       print()
                       print(f"{BOLD}{final_guess.upper()}{END} was not my word!")
                       print()
                       print("You have lost the game and ran out of guesses.")
                       print()
                       print(f"The word was {BOLD}{secret_word.upper()}{END}.")
                       print()
                       quit()
         
      
    if is_word_guessed(secret_word, letters_guessed) or final_guess == secret_word:
      print()
      print("Congratulations, you won!")
      score =  get_unique_letters(secret_word) * guesses_left
      print()
      print("Your total score for this game is:", score)
      print()
    else:
      print()
      print(f"Sorry, you ran out of guesses. The word was {BOLD}{secret_word.upper()}{END}.")
      print()
        
    

        




       

          
            



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #secret_word = random.choice(wordlist)
    secret_word = "house"
    hangman(secret_word)




