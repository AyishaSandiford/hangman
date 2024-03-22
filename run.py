import random

print('Welcome to hangman')
  
hidden_word_list_level_one = [
'the',
'about',
'great',
'learn',
'of',
'many',
'where',
'should',
'some',
'through',
'world',
'would',
'right',
'high',
'look',
'too',
'every',
'you',
'two',
'any',
'near',
'was',
'more',
'want',
'school',
'could',
'also',
'father',
'people',
'around',
'earth',
'they',
'put',
'eye',
'water',
'does',
'light',
'have',
'been',
'another',
'thought',
'from',
'who',
'large',
'head',
'one',
'find',
'even',
'saw',
'because',
'what',
'come',
'here',
'along',
'all',
'only',
'move',
'might',
'were',
'work',
'kind',
'something',
'when',
'know',
'again',
'always',
'your',
'year',
'change',
'both',
'said',
'give',
'off',
'often',
'there',
'most',
'night',
'very',
'away'
]


random_word = random.choice(hidden_word_list_level_one).upper()

print(f'The random word is {random_word}.')

# guessed_word represented by "_" by default is as long as the hidden random_word 
guessed_word = '_' * len(random_word)

# convert guessed_word to array
guessed_word = list(guessed_word)
print(' '.join(guessed_word))

user_letter = ""
pre_guessed_letters = ""


# loop until the user guesses the word but allow the loop to break with a . 
while '_' in guessed_word and user_letter != '.' and :
  user_letter = input('Enter a letter: ').upper()
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