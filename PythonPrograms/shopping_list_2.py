#further improvements- 
#list is saved so user can access previously saved list or create a new list
#user could edit or delete items or lists,
#items could be paired with images of the item 
#app could suggest user items they they have previously used often.
#user could be emailed coupons for supermarkets (or given through the app? coupons earned through a points system?)

#shopping list program
#needs to: 
#make list for items 
import os
shopping_list = []

def clear():
  os.system("cls" if os.name =="nt" else "clear")
  
  
def show_help():
  clear()
  #print instructions
  print ("Welcome to UrList, please enter your food shopping list")
  print ("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show welcome message.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list."
Enter 'SAVE' to save your shopping list.
ENTER 'LOAD' to load a saved list.""")
    
    
def show_list():
  clear()
  print ("Here's your shopping list: ")
# old code
#  index =1
#  for item in shopping_list:
#    print("{}. {}".format(index,item))
#    index += 1
    
  for index, item in enumerate(shopping_list):
    print("{}, {}".format(index+1, item))
          
  print("-"*10)
  
def append_to_list(item):
  show_list()
  if len(shopping_list):
    position = input("Where should I add {}?\n"
                     "Press enter to add to enter to the list\n"
                     ">  ".format(item))
  else:
    position = 0    
  try:
    position = abs(int(position))
  except ValueError:
    position = None
  if position is not None:
    shopping_list.insert(position-1, item)
  else:
    shopping_list.append(item)
  show_list()

  
def remove_item():
  show_list()
  unwanted_item = input("What item would you like to delete?\n")
  try:
    shopping_list.remove(unwanted_item)
  except ValueError:
    pass
  show_list()
  
def save(shopping_list):
  with open("saved_list.txt", 'w') as file_handler:
    for item in shopping_list:
        file_handler.write("{}\n".format(item))
    print("Shopping list saved")
    
def load():
  with open('saved_list.txt') as f:
    for line in f:
        shopping_list.append(line)

def main():
  show_help()

  while True:
    new_item = input(">  ")
    
    if new_item.upper() == 'DONE' or new_item == 'QUIT':
      break
    elif new_item.upper() == 'HELP':
      show_help()
      continue
    elif new_item.upper() == 'SHOW':
      show_list()
      continue
    elif new_item.upper() == 'REMOVE':
      remove_item()
      continue
    elif new_item.upper() == 'SAVE':
      save(shopping_list)
      continue
    elif new_item.upper() == 'LOAD':
      load()
      continue
    else:
      append_to_list(new_item)
  show_list()  
main()