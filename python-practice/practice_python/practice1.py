def program():
    name = input("What is your name? ")    
    age = input("What is your age? ")
    turn_100 = (100 - int(age)) + 2023
    number = int(input("Enter a number: "))
    print(number * (name + ", you will turn 100 in " + str(turn_100) + "\n"))

program()