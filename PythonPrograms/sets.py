COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    list = []
    for key, value in COURSES.items():
      if value | topic:
        list.append(key)
    return list
  
def covers_all(topic):
    covers_all = []
    for keys, values in COURSES.items():
        if topic <= values:
            covers_all.append(keys)
    return covers_all
  
  