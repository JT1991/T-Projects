#further improvements
#make the computer guesses smarter by having the guess range change e.g pc guess 7 high variable is set to 6 etc.
#have the computer not make the same guess twice. could this be done with a list? check against list before each guess?
import random
def game():
  try:
    user_num = int(input("Give me a number to guess!"))
    pc_trys = int(input("How many tries will you give me? Be Kind!"))
    low = int(input("Enter min: "))
    high = int(input("Enter max: "))
  except ValueError:
    print("Hey no cheating! Numbers only please.")

                   
  while pc_trys > 0:
    pc_trys -= 1
    pc_guess = random.randint(low,high)
    if pc_guess == user_num:
      print("Your number was {}. HA! Too easy! Give me another.".format(pc_guess))
      play_again = input("C'mon lets play again! Y/n ")
      if play_again.lower() != 'n':
        game()
      else:
        print("Bye!")
      #break
    elif pc_guess < user_num:
      print("""---PC Guess {} was too low. PC has {} guesses remaining---
      Too low? Hmmm...""".format(pc_guess,pc_trys))
    else:
      print("""---PC Guess {} was too high. PC has {} guesses remaining---
      Too low? Argh...""".format(pc_guess,pc_trys))
      
            
  else:
    print("""
        ---Game Over. PC Failed to guess {}---
        Game over? That's not fair I nearly had it!
        """.format(user_num))
    play_again = input("C'mon lets play again! Y/n ")
    if play_again.lower() != 'n':
      game()
    else:
      print("Bye!")

game()