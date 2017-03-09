def word_count(string):
  lowString = string.lower()
  letters = lowString.split()
  diction = {}
  for letter in letters:
    if letter not in diction:
      diction.update({letter : 1})
    else:
      diction[letter] += 1
  return diction

string = input("Enter a sentence.")
word_count(string)