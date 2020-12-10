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
    print("-" * 40)#prints a barrier to purely aesthetically seperate the code
    guessLetter = input("Player 2, guess a letter: ").upper()# prompts a user input for a guessed letter.

    if guessLetter in sameGuess:# reads if the letter you guessed is in a list of previous guesses
        guessletter = ""
        print("Player 2, you already guessed this letter")

    elif guessLetter in word:# then if it's not previously guessed and is in the word it runs this
        sameGuess.append(guessLetter)# adds the new letter to the same guess list
        indices = [i for i, x in enumerate(word) if x == guessLetter]# creates an indices list which is a for where finds all the indices of that letter in the word by enumerating the word and seeing which equal the guessed letter
        for x in range(0,len(indices)):# then runs a for that goes through the length of the enumerated list of indices of the correct word
            guessList[indices[x]] = guessLetter# adds each index to guess list
            word[indices[x]] = "_"# makes the indices in the word a _
        print("".join(guessList))# prints out the guess List so far

    elif guessLetter not in word:# finally, if the letter is not in the word then this if runs
        sameGuess.append(guessLetter)# adds the letter guessed to the same guess list
        guessNum -= 1# subtracts one from your number of guesses
        print("Guess again, Guesses left: " + str(guessNum)) # prints the amount of guesses the user has
        print("")# prints a space
        draw(guessNum)# runs the draw function which will print a percentage of the textfile depending on number of guesses left
        print("")# prints another space

        if guessNum == 0:#when there are no more guesses it prints that they lose and ends the loop
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessList:# Reads if there is anymore not guessed letters in the word and if not then it prints the player won and breaks the loop
        print("Player 2, you won")
        break
