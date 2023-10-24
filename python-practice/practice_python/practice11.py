def program():
    user_number = int(input("Enter a number: "))
    if user_number == 1:
        print(user_number, "is not a prime number")
    elif user_number == 2:
        print(user_number, "is a prime number")
    elif user_number > 2:
    # check for factors
        for i in range(2,user_number):
            if (user_number % i) == 0:
                print(user_number,"is not a prime number")
                print(i,"times",user_number//i,"is",user_number)
                break
            else:
                print(user_number,"is a prime number")
                break
program()