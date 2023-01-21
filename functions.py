def minion_game(word, rule):
  iterator = 1
  findings = []
  position_initial = 0
  position_final = 1
  result = 0

  while iterator <= len(word):

    while position_final <= len(word):
      sub_string = word[position_initial:position_final]
      if sub_string[0] in rule: 
        dict_find = {sub_string: word.count(sub_string)}
        if find_key(findings,sub_string):    
          findings.append(dict_find)
          position_initial += 1
          position_final += 1
          
        position_initial += 1
        position_final += 1
      else:
        position_initial += 1
        position_final += 1

    iterator += 1
    position_initial = 0
    position_final = iterator

  for i in findings:
    result+=(i[tuple(i)[0]])
    
  return findings, result



def find_key(dict, key):
  if len(dict) == 0:
    return True
  else:
    for character in dict:
      if key in character:
        return False
    return True

def who_wins(result_stuart, result_bob):
  if result_stuart ==  result_bob:
    return f"Both of them have the same result, {result_bob} points"
  elif result_stuart>result_bob:
    return f"Stuart is the winner with {result_stuart} points"
  else:
    return f"Bob is the winner with {result_bob} points"