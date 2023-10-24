import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []

rand_list1=[]
rand_list2=[]
n=10
for i in range(n):
    rand_list1.append(random.randint(0,9))
    rand_list2.append(random.randint(0,9))

def program():
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                new_list.append(a[i])
    print(set(new_list))

    #Another way to do this is:

    # Convert the lists to sets to remove duplicates
    set_a = set(a)
    set_b = set(b)

    # Find the common elements by taking the intersection of the sets
    common_elements = set_a.intersection(set_b)

    # Convert the result back to a list
    result_list = list(common_elements)

    #In one line:
    result_list = list(set(a) & set(b))

program()

