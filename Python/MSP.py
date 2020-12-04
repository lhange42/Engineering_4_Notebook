# Man shaped pinata 
# by Lukas Hange

guessList = [] # creates a list that will hold the world as a guess
word = str(input(" What's the word, player 1: ").upper()) #gets a input from user to input a word
word = list(word) # turns that word into a list
print ("\n" * 50) # clears screen by printing blank space
for i in range(0, len(word)): # turns the guess into "_"
    guessList.append("_")
guessLetter = "" # sets up guess Letter as a string 
sameGuess = [] # creates a list tha will hold guesses so they can read for whats been guessed
guessNum = 7 # sets the number of guesses to 7


def draw(t): # this is the function that will print the picture that represents the loss
    r = open("Lucas_Fuller.txt", "r") # acceses the file holding the image i ASCii form
    for f in range(0, (7-t) * 4 + 1): # goes through the image in sections
        print(r.readline(), end="")


while True:
    print("-" * 40)
    guessLetter = input("Player 2, guess a letter: ").upper()

    if guessLetter in sameGuess:
        guessletter = ""
        print("Player 2, you already guessed this letter")

    elif guessLetter in word:
        sameGuess.append(guessLetter)
        indices = [i for i, x in enumerate(word) if x == guessLetter]
        for x in range(0,len(indices)):
            guessList[indices[x]] = guessLetter
            word[indices[x]] = "_"
        print("".join(guessList))

    elif guessLetter not in word:
        sameGuess.append(guessLetter)
        guessNum -= 1
        print("Guess again, Guesses left: " + str(guessNum))
        print("")
        draw(guessNum)
        print("")

        if guessNum == 0:
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessList:
        print("Player 2, you won")
        break
