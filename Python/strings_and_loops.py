sentence = str(input("Enter a sentence: "))


sentence = sentence.replace(" ", "-")

sentenceList = list(sentence)

print(sentence)
sentenceList.append("-")
for i in sentenceList:
    print(i)
