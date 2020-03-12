# Check English

#    read dictionary
def loadDictionary():
    df = open('7_EnglishDictionary.txt')
    EnglishWord = {}
    for word in df.read().split('\n'):
        EnglishWord[word] = None
    df.close()
    return EnglishWord

EnglishWord = loadDictionary()

#    match the word
def getEnglish(message):
    message = message.upper()
    message = onlyLetters(message)
    pick = message.split()

    if pick == []:
        return 0.0
    
    matches = 0
    for word in pick:
        if word in EnglishWord:
            matches = matches + 1

    return float(matches) / len(pick)

#    clear other symbol
def onlyLetters(message):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_and_space = letter + letter.lower() + " \t\n"

    changestring = []
    for symbol in message:
        if symbol in letter_and_space:
            changestring.append(symbol)
    
    return "".join(changestring)

#    work function
def isEnglish(message, wordPercent = 35, letterPercent = 90):
    wordMatch = getEnglish(message) * 100 >= wordPercent
    numLetter = len(onlyLetters(message))
    letterMatch = float(numLetter) / len(message) * 100 >= letterPercent
    return (wordMatch and letterMatch, getEnglish(message) * 100, float(numLetter) / len(message) * 100)

#   just test
if __name__ == "__main__":
    print("> input message: ")
    message = input("<<< ")
    print("> Result: {0}".format(isEnglish(message)[0]))
    print(">         WordMatchPercent - {0:2.4f}%, LetterMatchPercent - {1:2.4f}%".format(isEnglish(message)[1],isEnglish(message)[2]))