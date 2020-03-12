# Affinr Cipher Hacker

import os
import sys
import time

import use_original.AffineCipherUseinTen as Ac
import use_original.CheckEnglishUseinEight as Ce
import use_original.cryptomath as Cm


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
    translate = hackAffine(message)

    # result output
    if translate == None:
        print("> Hacking Failed!")
    else :
        print("> Hacking Answer:")
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

#    hacking Process
def hackAffine(message):
    starttime = time.time()
    print("> May use lot of time, use \'Ctrl-D\' quit at any time")
    print("> Hacking...")

    for key in range(len(Ac.symbols) ** 2):
        keyA = Ac.getKeyPart(key)[0]
        if Cm.gcd(keyA, len(Ac.symbols)) != 1:
            continue

        translate = Ac.decryptMessage(key, message)
        print("> Trying key #{}...".format(key))

        if Ce.isEnglish(translate)[0]:
            print("> \n> possible result: key #{}".format(key))
            print(">\n{}".format(translate[:300]))
            totaltime = round(time.time() - starttime, 4)
            print("> Now use time: {} second.".format(totaltime))
            print("> Enter \'D\' to done, or continue hacking...")
            back = input("<<< ")
            if back.strip().upper().startswith('D'):
                return translate

    return None

if __name__ == "__main__":
    Processing()
