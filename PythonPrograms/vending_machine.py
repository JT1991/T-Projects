soda = ["Sprite", "Dr Pepper", "Coke", "Tizer"]
crisps = ["Walkers", "Pringles", "Skips"]
sweets = ["Haribo", "Mars Bar", "Maltesars"]

while True:
  choice = input("Would you like a soda, some crisps, or some sweets? ").lower()
  
  try:
    if choice == 'soda':
      snack = soda.pop()
    elif choice == 'crisps':
      snack = crisps.pop()
    elif choice == 'sweets':
      snack = sweets.pop()
    else:
      print("Sorry, I didn't understand that")
      continue
  except IndexError:
    print("Sorry, there are no {}".format(choice))
  else:
    print("Here's your {}: {}".format(choice, snack))
    