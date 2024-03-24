import random

from word_list import hidden_word_list_level_one
from hang_stage import stages
from how_to_play import how_to_play_game


print("""
__        __   _                            _____      
\\ \\      / /__| | ___ ___  _ __ ___   ___  |_   _|__   
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\   | |/ _ \\  
  \\ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) | 
 _ \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|   |_|\\___/  
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __          
| |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\         
|  _  | (_| | | | | (_| | | | | | | (_| | | | |        
|_|_|_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|        
 / ___| __ _ _ __ _|___/___                            
| |  _ / _` | '_ ` _ \\ / _ \\                           
| |_| | (_| | | | | | |  __/                           
 \\____|\\__,_|_| |_| |_|\\___|                           
                                                
""")


# Initialise game state
gameState = {
  "random_word": "",
  "guessed_letters": [],
  "guessed_letter": "",
  "guessed_word": "",
  "bad_guesses_count": 0, 
}

def lines(numberOfLines = 1):
  print('\n' * numberOfLines)

# Line to separate each turn
def turnLine():
  print('-' * 50)

# Print the state of the guessed word. E.g. H _ L L O
def printGuessedWord(gameState):
  print(' '.join(gameState["guessed_word"]))
  lines()
  print('Guessed letters: ' + ', '.join(gameState["guessed_letters"]))

  # Check if the guess is valid. E.g. it is a single letter
def validateGuess(gameState):
  if len(gameState["guessed_letter"]) > 1:
    print('Please enter a single letter')
    return False

  if gameState["guessed_letter"] == ".":
    return False

  if gameState["guessed_letter"].isalpha() is False:
    print('Please enter a letter')
    return False

  if gameState["guessed_letter"] in gameState["guessed_letters"]:
    print('You have already guessed this letter')
    printGuessedWord(gameState)
    return False

  return True
