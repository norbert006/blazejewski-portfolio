import random

def game():
    game_number = random.randint(1,9)
    exit = False
    attempts = 0
    while exit != True:
        user_choice = input("Choose a number between 1 and 9: ")
        if user_choice == "exit":
            print("Thanks for playing!")
            exit = True
        elif game_number == int(user_choice):
            print("You guessed correct!")
            attempts += 1
        elif game_number > int(user_choice):
            print("Try a bigger number!")
            attempts += 1
        else:
            print("Try a smaller number!")
            attempts += 1

    print("Total attempts = " + attempts)
game()