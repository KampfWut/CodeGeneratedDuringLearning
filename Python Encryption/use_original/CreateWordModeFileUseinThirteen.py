# Create the Word Mode File

import pprint

# get one word mode
def getOneWordMode(word):
    word = word.upper()
    nextMode = 0
    letterMode = {}     # dictionary for "LETTER-NUMBER"
    wordMode = []       # words Mode by "N.N.N.N. ... .N"

    for letter in word:
        if letter not in letterMode:
            letterMode[letter] = str(nextMode)
            nextMode = nextMode + 1
        wordMode.append(letterMode[letter])

    return ".".join(wordMode)

# get all word mode
def getAllWordMode():
    allWordsMode = {}
    
    # get the English dictionary
    f = open("7_EnglishDictionary.txt")
    wordList = f.read().split('\n')
    f.close()

    for word in wordList:
        mode = getOneWordMode(word)
        if mode not in allWordsMode:
            allWordsMode[mode] = [word]
        else:
            allWordsMode[mode].append(word)

    # save as "12_wordMode.txt"
    f = open("12_wordMode.txt",'w')
    f.write(pprint.pformat(allWordsMode))
    f.close

    # save as "12_wordMode.py"
    f = open("12_wordMode.py",'w')
    f.write("allWordMode = ")
    f.write(pprint.pformat(allWordsMode))
    f.close

    return allWordsMode

if __name__ == "__main__":
    Mode = getAllWordMode()
    pprint.pprint(Mode)

