def packer(name=None, **kwargs):
  print(kwargs)
  
def unpacker(first_name=None, last_name=None):
  if first_name and last_name:
    print("Hi {} {}".format(first_name, last_name))
  else:
    print("Hi no name!")

packer(name = "Josh", num=42, bolton = "ipswich")
unpacker(**{'first_name': 'Josh', 'last_name': 'Thorn'})
            
course_minutes = {"Python Basics": 232, "Djano Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
  print("{} is {} minutes long".format(course,minutes))