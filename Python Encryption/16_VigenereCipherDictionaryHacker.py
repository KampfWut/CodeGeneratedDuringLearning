# Vigenere Cipher Dictionary Hacker

import sys, os

import use_original.CheckEnglishUseinEight as CE
import use_original.VigenereCipherUseinSixteen as VE
import use_original.ProcessingBar as PB

# process
def Processing():
    # file or message?
    print("> input (M)essage or (F)ile ?")
    back = input("<<< ")
    mode = 0

    if back.lower().startswith('m'):
        mode = 1
        print("> input message: ")
        message = input("<<< ")

    elif back.lower().startswith('f'):
        mode = 2
        print("> input your input File Name:")
        inputFileName = input("<<< ")

        if not os.path.exists(inputFileName):
            print("> [ERROR] There is no \"{}\" File. ".format(inputFileName))
            sys.exit()

        f = open(inputFileName)
        message = f.read()
        f.close()

    else :
        print("[ERROR] Don\'t know what you input...")
        sys.exit()

    # main work
    translate = hackVigenerebyDictionary(message)
    
    # result output
    if translate == None:
        print("\n> Hacking Failed!")
    else :
        print("\n> Hacking Answer:")
        if mode == 2:
            FileName = inputFileName[:len(inputFileName) - 4]
            outputFileName = FileName + "_trans.txt"
            print(">\n{}...".format(translate[:300]))
            print("> Save as {}.".format(outputFileName))
            f = open(outputFileName, 'w')
            f.write(translate)
            f.close()

        else:
            print("> {}".format(translate))

# Hack Vigenere by Dictionary
def hackVigenerebyDictionary(message):
    print("> Hacking...")
    f = open("7_EnglishDictionary.txt")
    words = f.readlines()
    f.close()

    count = 0
    for word in words:
        word = word.strip()
        # remove "\n"

        count = count + 1
        limited = len(words)
        PB.symbolBar(count, limited)

        translate = VE.decryptMessage(word, message)
        if CE.isEnglish(translate, wordPercent = 60)[0]:
            print("> Possible answer:")
            print(">   Key: {}".format(word.upper()))
            print(">   Translate:")
            print(translate[:300])
            print("> Enter \'D\' to done, or continue hacking...")
            back = input("<<< ")
            if back.strip().upper().startswith('D'):
                return translate

    return None

if __name__ == "__main__":
    Processing()
