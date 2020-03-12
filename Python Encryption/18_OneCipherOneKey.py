# One cipher, One key

import os
import pprint
import sys
import time
import random
import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# processing
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
            bit = len(message)
            key = randomKey(bit)
            print("> Your random key is \"{}\".".format(key))

    while not checkkey(key, len(message)):
        print("> input your key:")
        key = input("<<< ")
        if not checkkey(key, len(message)):
            print("> Illegal input!")

    key = key.upper()

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

# get random key
def randomKey(bit):
    key = ""

    while len(key) < bit:
        randoms = os.urandom(1)
        if (ord(randoms) >= 65 and ord(randoms) <= 90):
            key = key + chr(ord(randoms))

    return key

# check key is legal
def checkkey(key, num):
    if len(key) == num:
        return True
    else:
        return False

# [Same with 14.py]
# Encrypt Message 
def encryptMessage(key, message):
    return translateMessage(key, message, 1)

# Decrypt Message 
def decryptMessage(key, message):
    return translateMessage(key, message, 2)

# Translate message
def translateMessage(key, message, mode):
    translate = []
    keyIndex = 0
    
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 1:
                num = num + LETTERS.find(key[keyIndex])
            elif mode == 2:
                num = num - LETTERS.find(key[keyIndex])

            num = num % len(LETTERS)

            if symbol.isupper():
                translate.append(LETTERS[num])
            elif symbol.islower():
                translate.append(LETTERS[num].lower())

            keyIndex = keyIndex + 1
            if keyIndex == len(key):
                keyIndex = 0

        else:
            translate.append(symbol)

    return "".join(translate)

if __name__ == "__main__":
    Processing()
