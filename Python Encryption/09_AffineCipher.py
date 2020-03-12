# Affine Cipher

import sys, random, os
import use_original.cryptomath as cm

symbols = "1234567890!@#$%^&*()_+|-=\\`~abcdefghijklmnopqrstuvwxyz[];\',./{}:\"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

    # which mode?
    mode = 0
    while mode == 0:
        print("> lock(1) or unlock(2)?")
        mode_str = input("<<< ")
        try:
            mode = int(mode_str)
        except ValueError:
            print("> You should input a number, not letter...")

    # which key?
    key = 0
    
    print("> Use random Key?(Y/N)")
    back = input(">>> ")
    if back.upper().startswith('Y'):
        key = randonKey()
        print("> Your random key is {}.".format(key))

    while key == 0:
        print("> input your cipher code:")
        key_str = input("<<< ")
        try:
            key = int(key_str)
        except ValueError:
            print("> You should input a number, not letter...")
    
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

#    get 2 key
def getKeyPart(key):
    keyA = key // len(symbols)
    keyB = key % len(symbols)
    return (keyA, keyB)

#    check the key
def checkKey(keyA, keyB, mode):
    if keyA == 1 and mode == 1:
        sys.exit("The affine cipher becomes incredibly weak when key A is set to 1.")
    if keyB == 0 and mode == 1:
        sys.exit("The affine cipher becomes incredibly weak when key B is set to 0.")
    if keyA < 0:
        sys.exit("Key A must greater than 0!")
    if keyB < 0 or keyB > len(symbols) - 1:
        sys.exit("Key B must between 0 and {}".format(len(symbols) - 1))
    if cm.gcd(keyA, len(symbols)) != 1:
        sys.exit("Key A and symbols set are not relatively prime.")
    
#   Encryption
def encryptMessage(key, message):
    keyA, keyB = getKeyPart(key)
    checkKey(keyA, keyB, 1)
    translate = ""
    for symbol in message:
        if symbol in symbols:
            symIndex = symbols.find(symbol)
            translate = translate + symbols[(symIndex * keyA + keyB) % len(symbols)]
        else:
            translate = translate + symbol

    return translate

#    Decrypyion
def decryptMessage(key, message):
    keyA, keyB = getKeyPart(key)
    checkKey(keyA, keyB, 2)
    translate = ""
    modInverseKeyA = cm.findModInverse(keyA, len(symbols))

    for symbol in message:
        if symbol in symbols:
            symIndex = symbols.find(symbol)
            translate = translate + symbols[(symIndex - keyB) * modInverseKeyA % len(symbols)]
        else:
            translate = translate + symbol
    
    return translate

#    Get a random key
def randonKey():
    while True:
        keyA = random.randint(2, len(symbols))
        keyB = random.randint(2, len(symbols))
        if cm.gcd(keyA, len(symbols)) == 1:
            return keyA * len(symbols) + keyB

if __name__ == "__main__":
    Processing()
    