#Step 5

import random
from hangman_words import word_list
from hangman_art import stages
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list)-1)]
cwl = list(chosen_word)
display = []
for ch in chosen_word:
  display.append('_')
graceattempts = 6
wordcompleted = False
stagecount = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)
#Testing code
print("Chosen word is: " + chosen_word)

while (graceattempts > 0 and not wordcompleted):
  if '_' in display:
    wordcompleted = False
    guess=input("Enter your guess: ").lower()
    correctguess = False    
    for i in range(0, len(cwl)):
        if cwl[i] == guess:
          display[i] = guess
          correctguess = True
    if correctguess:
      graceattempts -= 1
    else:
      graceattempts -= 1      
      stagecount -= 1
      print(f"You guessed the letter {guess}, that's not in the word. You lose a life.")
      print(stages[stagecount]) 
    displaystr = ''      
    for ch in display:
      # print(f"{ch} ")
      displaystr += ch + ' '
    displaystr += '\n'
    print(displaystr) 
    print(f"Attempts left: {graceattempts}")
    print("-----------------")
  else:
    wordcompleted = True
if wordcompleted:
  print(f"You win! You guessed the word {chosen_word} ")
else:
  if stagecount <= 0:
    print(f"You hang! The word was {chosen_word} ")  
  else:
    print(f"You lose! The word was {chosen_word} ")