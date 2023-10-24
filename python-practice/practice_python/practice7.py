a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def program():
    new_list = [element for element in a if element % 2 == 0]
    print(new_list)

program()