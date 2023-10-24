def program():
    user_number = int(input("Enter a number: "))
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            print(i)
program()