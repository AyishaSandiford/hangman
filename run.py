import random

from word_list import hidden_word_list_level_one
from hang_stage import stages

print('Welcome to hangman')
  

random_word = random.choice(hidden_word_list_level_one).upper()

print(f'The random word is {random_word}.')

# guessed_word represented by "_" by default is as long as the hidden random_word 
guessed_word = '_' * len(random_word)

# convert guessed_word to array
guessed_word = list(guessed_word)
print(' '.join(guessed_word))

user_letter = ""
pre_guessed_letters = ""
bad_guesses = 0


# loop until the user guesses the word but allow the loop to break with a . 
while '_' in guessed_word and user_letter != '.' and bad_guesses < 6:
  user_letter = input('Enter a letter: ').upper()
  if len(user_letter) > 1:
    print('Please enter a single letter')
    continue
  if user_letter in pre_guessed_letters:
    print('You have already guessed this letter')
    print(' '.join(guessed_word))
    continue
  else:
    pre_guessed_letters += user_letter

  if user_letter in random_word:
    print(f"You guessed the letter {user_letter} correctly!")
    indexes = [i for i, x in enumerate(random_word) if x == user_letter]
    for letterLocation in indexes:
      guessed_word[letterLocation] = user_letter
      print(' '.join(guessed_word))
  else:
    print(' '.join(guessed_word))
    print(f"You guessed the letter {user_letter} incorrectly!")
  if user_letter not in random_word:
    print(stages[bad_guesses])
    bad_guesses += 1
  if bad_guesses == 6:
    print('You Lost! The word was ' + random_word)
      