# Simple Substitution Cipher

import os
import random
import sys
import time

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = LETTERS.lower()

# Process
def Processing():
    # file or message?
    print("> input (M)essage or (F)ile ?")
    back = input("<<< ")
    smode = 0

    if back.lower().startswith('m'):
        smode = 1
        print("> input message: ")
        message = input("<<< ")

    elif back.lower().startswith('f'):
        smode = 2
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

    # what mode?
    mode = 0
    while mode == 0:
        print("> lock(1) or unlock(2)?")
        mode_str = input("<<< ")
        try:
            mode = int(mode_str)
        except ValueError:
            print("> You should input a number, not letter...")

    # what key?
    key = ""
    
    if mode == 1:
        print("> [ Suggested use ]Use random Key?(Y/N)")
        back = input(">>> ")
        if back.upper().startswith('Y'):
            key = randomKey()
            print("> Your random key is \"{}\".".format(key))

    while not checkkey(key):
        print("> input your key:")
        key = input("<<< ")
        if not checkkey(key):
            print("> Illegal input!")

     # start work
    if mode == 1:
        translate = encryptMessage(key, message)
    elif mode == 2:
        translate = decryptMessage(key, message)
    
    # finish output
    print("> Key : {0}".format(key))
    print("> Final message :")
    if smode == 2:
        FileName = inputFileName[:len(inputFileName) - 4]
        outputFileName = FileName + "_trans.txt"
        print("{}...".format(translate[:300]))
        print("> Save as {}.".format(outputFileName))
        f = open(outputFileName, 'w')
        f.write(translate)
        f.close()
    else:
        print("> {}".format(translate))

'''
# Encrypt Message
def encryptMessage(key, message):
    print("> Encrypt the Message...")
    translate = ""

    for symbol in message:

        if symbol in LETTERS:
            symIndex = LETTERS.find(symbol)
            translate = translate + key[symIndex]
        
        elif symbol in letters:
            symIndex = letters.find(symbol)
            translate = translate + key[symIndex].lower()

        else:
            translate = translate + symbol    
    
    return translate

# Decrypt Message
def decryptMessage(key, message):
    print("> Decrypt the Message...")
    translate = ""

    for symbol in message:

        if symbol in key:
            symIndex = key.find(symbol)
            translate = translate + LETTERS[symIndex]

        elif symbol in key.lower():
            symIndex = key.lower().find(symbol)
            translate = translate + letters[symIndex]

        else:
            translate = translate + symbol

    return translate
'''

# Encrypt Message 2
def encryptMessage(key, message):
    return translateMessage(key, message, 1)

# Decrypt Message 2
def decryptMessage(key, message):
    return translateMessage(key, message, 2)

# Translate message
def translateMessage(key, message, mode):
    translate = ""
    charA = LETTERS
    charB = key
    if mode == 2:
        charA, charB = charB, charA
    
    for symbol in message:
        if symbol.upper() in charA:
            symIndex = charA.find(symbol.upper())
            if symbol.isupper():
                translate = translate + charB[symIndex].upper()
            else:
                translate = translate + charB[symIndex].lower()
        else: 
            translate = translate + symbol

    return translate

# check key is not illegal
def checkkey(key):
    if key == "":
        return False

    # key = key.upper()
    if sorted(list(key)) == sorted(list(LETTERS)):
        return True
    else:
        return False

# get random key
def randomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)


if __name__ == "__main__":
    Processing()