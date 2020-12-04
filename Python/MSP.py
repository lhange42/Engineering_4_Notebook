# Man shaped pinata 
# by Lukas Hange

programFinished = False
guessLetter = ""
guessList = []
word = str(input(" What's the word, player 1: ").upper())
word = list(word)
print(word)
print ("\n" * 50)
for i in range(0, len(word)):
    guessList.append("_")
guessLetter = str(input("\nPlayer 2, guess a letter: ").upper())
sameGuess = []
guessNum = 7


def draw(t):
<<<<<<< HEAD
    r = e in  
        print
=======
    r = open("Lucas_Fuller.txt", "r")
    for f in range(0, (5-t) * 4 + 1):
        print(f.readline(), end="")
>>>>>>> 199541a3dbb1be3239ebbf1de5fb3a3d08ab9470

while True:
    print("-" * 40)
    guessLetter = input("Player 2, guess a letter: ")

    if guessLetter in sameGuess:
        guessletter = ""
        print("Player 2, you already guessed this letter")

    elif guessLetter in word:
        sameGuess.append(guessLetter)
        index = word.index(guessLetter)
        guessList[index] = guessLetter
        word[index] = "_"
        print("".join(guessList))

    elif guessLetter not in word:
        sameGuess.append(guessLetter)
        guessNum -= 1
        print("Wrong! Guesses left: " + str(guessNum))
        print("")
        draw(guessNum)
        print("")

        if guessNum == 0:
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessList:
        print("Player 2, you won"
