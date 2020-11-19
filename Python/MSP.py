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

while guessList != word:
    guessLetter = str(input("\nPlayer 2, guess a letter: ").lower())
    correct = False
    same = False

    for t in guessList:
        if guessLetter == t:
            same = True

    for i in word:
        if(i == guessLetter) and (same == False):
            correct = True
    
    if correct == True:
        indices = [i for i, x in enumerate(word) if x == guessLetter]

        for u in range(0, len(indices)):
            guessList.insert(indices[u], guessLetter)
            guessList.pop(indices[u] + 1)

        
        for y in range(0, len(guessList)):
            print(guessList[y], end=" ")

            
    elif(same == False):
        print("Guess again!")
    else:
        print("You already guessed that letter")
    
