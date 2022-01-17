import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in words:
      word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word 
    abc = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
      print('You have', lives, 'lives left and you used these letters: ', ' '.join(used_letters))

      word_list = [letter if letter in used_letters else '-' for letter in word]

      print('Current word: ', ' '.join(word_list))
      

      user_letter = input('Guess a letter: ').upper() #getting user input
      if user_letter in abc - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        else: 
          lives = lives - 1 #takes away a life if wrong
          print('Letter is not in word.')

      
      elif user_letter in used_letters:
        print('You have already used that character. Please try again.')

      else: 
        print('Invalid charater. Please try again')

    #gets here when len(word_letters) == 0
    if lives == 0:
        print('YOu died, sorry. The word was', word)
    else:
        print("You guessed the word", word, "!!!")


hangman()

#user_input = input("Type something: ")
#print(user_input)

