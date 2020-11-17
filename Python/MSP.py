# Man shaped pinata 
# by Lukas Hange

programFinished = False
guessLetter = ""
guessList = []
word = str(input(" What's the word, player 1: ").lower())
word = list(word)
print(word)
print ("\n" * 50)
for i in range(0, len(word)):
    guessList.append("_")

while programFinished is False:
    guessLetter = str(input("Player 2, guess a letter: ").lower())
    counter = -1
    for i in word:
        if(i == guess):
            guessList.insert(word.index(guessLetter), guessLetter)
            guessList.pop(word.index(guessLetter) + 1)
    ProgramFinished = True
