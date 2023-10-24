a = [1, 3, 5, 30, 42, 43, 500]
b = 3

def func1(a_list, a_number):
    print(a_number in a_list)

func1(a,b)

def binary_search(ordered_list, element_to_look_for):
    start_index = 0
    end_index = len(ordered_list) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        middle_element = ordered_list[middle_index]

        if middle_element == element_to_look_for:
            return True
        elif middle_element < element_to_look_for:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1

    return False

print(binary_search(a, b))