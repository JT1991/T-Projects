#further improvements- 
#list is saved so user can access previously saved list or create a new list
#user could edit or delete items or lists,
#search the items online etc.
#items could be paired with images of the item
#app could suggest user items they they have previously used often.
#user could be emailed coupons for supermarkets (or given through the app? coupons earned through a points system?)

#shopping list program
#needs to: 
#make list for items 
shopping_list = []

#print instructions
print ("Welcome to UrList, please enter your food shopping list")
print ("Enter 'DONE' to stop adding items")

#ask for new items
while True:
  new_item = input(">  ")
  
  #enable user to quit app
  if new_item == 'DONE':
    break
    
  #add new items to list
  shopping_list.append(new_item)
  
#print the list
print ("Here's your shopping list: ")
for item in shopping_list:
  print(item)
  