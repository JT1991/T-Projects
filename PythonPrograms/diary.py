from collections import OrderedDict
import datetime
import sys
import os

from peewee import *


db = SqliteDatabase('diary.db')

class Entry(Model):
  content = TextField()
  timestamp = DateTimeField(default=datetime.datetime.now)
  #content
  #timestamp
  
  class Meta():
    database = db
  
def initialize():
  """Create the database and the tables if not exits"""
  db.connect()
  db.create_tables([Entry], safe=True)
  
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
def menu_loop():
  """Show the menu"""
  choice = None
  
  while choice != 'q':
    clear()
    print("Enter 'q' to quit.")
    for key, value in menu.items():
      print('{}) {}'.format(key, value.__doc__))
    choice = input('Action:  ').lower().strip()
    
    if choice in menu:
      clear()
      menu[choice]()
    
          
    
def add_entry():
    """Add an entry"""
    print("Enter your entry. Press CTRL+D when finished")
    data = sys.stdin.read().strip()
    
    if data:
      if input("Save entry? [Yn]  ").lower() != 'n':
        Entry.create(content=data)
        print("Saved sucessfully!")
              
  

def view_entry(search_query=None):
    """View an entry"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
      entries = entries.where(Entry.content.contains(search_query))
                              
    for entry in entries:
      timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
      clear()
      print(timestamp)
      print('='*len(timestamp))
      print(entry.content)
      print('\n\n'+'='*len(timestamp))
      print('n) for next entry')
      print('d) delete entry')
      print('q) to return to main menu')
      
      next_action = input('Action: [Ndq]  ').lower().strip()
      if next_action == 'q':
        break
      if next_action == 'd':
        delete_entry(entry)
        

def search_entries():
  """Search through saved entries"""
  view_entry(input('Search query:  '))
                              


def delete_entry(entry):
    """Delete an entry"""
    if input("Are you sure? [Yn]  ").lower() == 'y':
             entry.delete_instance()
             print("ENTRY DELETED")
    
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entry),
    ('s', search_entries)
  ])
    

if __name__ == '__main__':
  initialize()
  menu_loop()
