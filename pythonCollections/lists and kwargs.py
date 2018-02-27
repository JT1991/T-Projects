dicts = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(dicts, string):

  #make a blank list I can add each sentence to
  result = []

  #loop through each pair of {name,food} in dicts and set them to key
  for key in dicts:

    #add the sentence once formatted using the variables from the string
    result.append(string.format(**key))

  #finally return the list with all the sentences
  print(result)
