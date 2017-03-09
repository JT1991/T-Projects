def unpacker(first_name, last_name, notches):
  if first_name and last_name:
    print("Hi {} {}, I hear you've been busy! Conquests: {}".format(first_name, last_name, notches))
  else:
    print("Get to work, slacker!")
          
def pack (**kwargs):
  print(kwargs)
          

pack(first_name="josh", last_name="thorn", learning = ['python', 'css', 'web design'])
unpacker(**{'last_name': 'galore', 'first_name': 'pussy', 'notches':['lily','petra','susan','heather','lucy','gillian','willow']})                                                                                                                                        
