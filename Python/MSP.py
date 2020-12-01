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


def draw(n):
    f = open("graham.txt", "r")
    for x in range(0, (5-n) * 4 + 1):
        print(f.readline(), end="")

while True:
    print("-" * 40)
    letter = input("Player 2, guess a letter: ")

    if letter.upper() in already_guessed:
        letter = ""
        print("Player 2, you already guessed this letter")

    elif letter.upper() in word:
        already_guessed.append(letter.upper())
        index = word.index(letter.upper())
        guessed[index] = letter.upper()
        word[index] = "_"
        print("".join(guessed))

    elif letter.upper() not in word:
        already_guessed.append(letter.upper())
        num_guesses -= 1
        print("Wrong! Guesses left: " + str(num_guesses))
        print("")
        draw(num_guesses)
        print("")

        if num_guesses == 0:
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessList:
        print("Player 2, you won")
        break
