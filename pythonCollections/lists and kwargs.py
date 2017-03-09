values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
template = "Hi, I'm {name} and I love to eat {food}!"
def string_factory(values):
    strings =[]
    for d in values:
       strings.append(template.format(**d)) 
    return strings