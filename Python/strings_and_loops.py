sentence = str(input("Enter a sentence: "))# makes a string input of a sentence 


sentence = sentence.replace(" ", "-")# replaces all the spaces with minus symbols

sentenceList = list(sentence)# makes the sentence string a list by letter

sentenceList.append("-") # adds a minus symbol to the end of the sentence list so it will be printed
for i in sentenceList:# this will make this function repeat for how ever many sections of the list there are
    print(i)# This will print each character of the sentence in the list as the for loop goes on
