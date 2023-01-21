###Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules
#Both players are given the same string, both players have to make substrings using the letters of the string .
#The game ends when both players have made all possible substrings. A player gets +1 point for each occurrence of the substring in the string.

import functions
import sys
vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"

print("Welcome to the Minion Game")
print("Bob and Stuart are ready to play; Stuart has to make words starting with consonants and Bob with vowels")

word = input("Please type the word in order to begin the Game= > ").upper()

if word.isalpha():
  stuart_findings, result_stuart = functions.minion_game(word, consonants)
  print("\nStuart finds: ")
  for i in stuart_findings:
    print(i)
  bob_findings, result_bob = functions.minion_game(word, vowels)
  print("\nBob finds: ")
  for i in bob_findings:
    print(i)
  message = functions.who_wins(result_stuart, result_bob)
  print(f"\n{message}")
  
else:
  print("T\his is not a word, please check it. The game only works with words. Please try again ")
  sys.exit()