def program():
    user_number = int(input("Enter a number: "))
    user_number2 = int(input("Enter a second number: "))
    if user_number % 2 == 0 and user_number % 4 == 0:
        print(str(user_number) + " is even and is a multiple of 4")
    elif user_number % 2 == 0:
        print(str(user_number) + " is even") 
    else:
        print(str(user_number) + " is odd")

    if user_number % user_number2 == 0:
        print(str(user_number) + " and " + str(user_number2) + " divide exactly")
    else:
        print(str(user_number) + " and " + str(user_number2) + " do not divide exactly")

program()