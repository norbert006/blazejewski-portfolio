a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
new_list2 = []

def program():
    user_number = int(input("Enter a number: "))
    for element in a:
        if element < user_number:
            new_list.append(element)
    print(new_list)

    #If you wanted to write this in a single line, you could write this:
    new_list2 = [element for element in a if element < 5]

program()