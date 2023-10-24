a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def program1(list_1):
    set_1 = set(list_1)
    print(set_1)

program1(a)

def program2(list_2):
    y = []
    for i in list_2:
        if i not in y:
            y.append(i)
    print(y)

program2(a)
