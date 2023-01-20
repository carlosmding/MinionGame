###Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules
#Both players are given the same string, both players have to make substrings using the letters of the string .
#The game ends when both players have made all possible substrings. A player gets +1 point for each occurrence of the substring in the string.





# Stuart has to make words starting with consonants.
def stuart_game(word):
  iterator = 1
  findings = []
  position_initial = 0
  position_final = 1
  
  while iterator <= len(word):

    while position_final<=len(word):
      sub_string = word[position_initial:position_final]
      if not sub_string[0] in "AEIOU":
        dict_find = {sub_string : word.count(sub_string)}
        print(dict_find)
        findings.append(dict_find)
        position_initial +=1
        position_final += 1
      else:
        position_initial +=1
        position_final += 1

    iterator +=1
    position_initial = 0
    position_final = iterator
    
      

    
# Kevin has to make words starting with vowels.
def kevin_game(word):
  iterator = 1

if __name__ == "__main__":
  stuart_game("BANANA")
