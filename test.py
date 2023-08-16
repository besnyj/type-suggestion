import wordsByLetters

outputText = ""
optionsList = []

while True:
    optionsList.clear()
    letter = input().lower()
    for lettersList in wordsByLetters.listOfWordsIndex:
            if lettersList[0][0] == f'{letter[0]}':
                listOfWords = lettersList
                for word in listOfWords:
                    if f'{word[0:len(letter)]}' == letter:
                        optionsList.append(word)
    print(optionsList[0:5])