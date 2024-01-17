'''
Credit to: Cory Althoff (https://github.com/calthoff/self_taught/blob/master/python_ex239.py/)
'''

import random
random_word = random.choice(open("words.txt").read().split())

#Hangman function to store the game.
#Word variable is the word that the player tries to guess.
def hangman(word): 
    wrong = 0 #Number of incorrect guesses.
    stages = ["",
             "________        ",
             "|        |      ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "| X X X X X X X "
              ] #Elements needed to draw the hangman.
    rletters = list(word) #A list containing each character in the variable word that keeps track of which letters are left to guess.
    board = ["__"] * len(word) #Underscore for each unguessed letter in the game.
    win = False #Keep track if player has won or not.
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        message = "Guess a letter: "
        char = input(message)
        times = word.count(char) #Count how many times the guessed character appears in the word.
        if char in rletters: #If user guesses a letter correctly.
            for i in range(times): #Repeat the processes of unveiling the letter so that all of its instances are unveiled.
                cind = rletters.index(char) #Get the first index of the letter guessed by the player.
                board[cind] = char #Replace the corresponding underscore with the correct letter.
                rletters[cind] = '$' #Replace the letter in rletters with $ so that the game can go through the whole word in case a letter repeats.
        else:
            wrong += 1

        print((" ".join(board))) #Print the scoreboard (the underscores / correctly guessed letters).
        e = wrong + 1
        print("\n".join(stages[0: e])) #Print hangman stages sequentially based on amount of wrong answers.

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: e])) #Print whole hangman.
        print("You lose! It was {}.".format(word))

hangman(random_word)
