import random

cpu_choices = ["rock", "paper", "scissors"]

def game():
    game_again = "Y"
    while game_again == "Y":
        user_choice = input("Rock, Paper, Scissors? ")
        cpu_choice = cpu_choices[random.randint(0,2)]
        if user_choice ==  cpu_choice:
            print("It's a draw")
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
            (user_choice == "paper" and cpu_choice == "rock") or \
            (user_choice == "scissors" and cpu_choice == "paper"):
            print("User wins")
        else:
            print("cpu won")
        print("Player choice = " + user_choice + ", cpu_choice = " + cpu_choice)
        game_again = str(input("Play another game? [Y/N]"))
        if game_again == "N":
            break
    print("Thanks for playing!")

game()