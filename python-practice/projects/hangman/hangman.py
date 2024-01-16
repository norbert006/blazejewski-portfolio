#Hangman function to store the game.
#Word variable is the word that the player tries to guess.
def hangman(word): 
    wrong = 0 #Number of incorrect guesses.
    stages = ["", "________ ", "| ", "| | ", "| 0 ", "| /|\ ", "| / \ ", "| " ] #Elements needed to draw the hangman.
    rletters = list(word) #A list containing each character in the variable word that keeps track of which letters are left to guess.
    board = ["__"] * len(word) #Underscore for each unguessed letter in the game.
    win = False #Keep track if player has won or not.
    print("Welcome to Hangman")

