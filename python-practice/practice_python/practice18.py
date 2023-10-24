import random

def cows_bulls():
    cows = 0
    bulls = 0
    game_numbers = random.sample(range(0, 9), 4)
    print(game_numbers)
    print("Welcome to the Cows and Bulls game!")
    user_input = input("Enter a number: ")
    for i in range(0,4):
        if int(game_numbers[i]) == int(user_input[i]):
            cows += 1
        elif int(user_input[i]) in game_numbers:
            bulls += 1
    print("Cows = ", cows)
    print("Bulls = " ,bulls)
cows_bulls()

