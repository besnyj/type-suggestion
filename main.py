optionsList = []
outputText = ""
    
def wordSuggestion():
    global optionsList
    global outputText
    
    wordsList = open("words.txt", "+r")
    optionsList.clear()
    letterOrWord = input().lower()
    
    optionCounter = 1
    optionsPrintOutput = ""
    
    
    
    for word in wordsList:
        if word.strip() == letterOrWord:
            wordsList.close()
            outputText = f'{outputText} {letterOrWord}'
            print(outputText)
            return wordSuggestion()
        
        elif f'{word[0:len(letterOrWord)]}' == letterOrWord:
            optionsList.append(word.strip())
    
    
    
    for option in optionsList[0:5]:
        optionsPrintOutput = optionsPrintOutput + f'{optionCounter}. {option}\n'
        optionCounter += 1
    print(optionsPrintOutput)
    wordsList.close()
    wordSelection()

        
def wordSelection():
    global outputText
    
    selectedWord = input()     
    try:
        selectedWord = int(selectedWord)-1
        outputText = f'{outputText} {optionsList[selectedWord]}'
        print(f'{outputText}')
        wordSuggestion()           
    except:
        outputText = f'{outputText} {selectedWord}'
        print(outputText)
        wordSuggestion()


wordSuggestion()


#to be implemented
# recognizes we typed an existing word and the not suggest anything and wait for the next input
# create rank system to adapt to more used words by user
