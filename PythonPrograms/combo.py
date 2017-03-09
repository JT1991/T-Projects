# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
def combo(iterable_1, iterable_2):
    List = []
    for index, item in enumerate(iterable_2):
        List.append((iterable_1 [index], item))
    return List
