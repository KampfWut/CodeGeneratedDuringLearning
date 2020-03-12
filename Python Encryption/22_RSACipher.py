# RSA Cipher

import os
import sys

import use_original.ProcessingBar as PB

DEFAULT_BLOCK_SIZE = 128    # 128 byts = 128*8 =1024 bits
BYTE_SIZE = 256             # 2 ** 8 = 256

# Main process
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

    # start main work
    if mode == 1:
        pubKeyFilename = "RSA_public.txt"
        translate = doEncrypt(pubKeyFilename, message)
    elif mode == 2:
        priKeyFilename = "RSA_private.txt"
        translate = doDecrypt(priKeyFilename, message)

    # finish output
    print("\n> Final message :")
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

# Mode1: do Encryption
def doEncrypt(pubKeyFilename, message, blockSize = DEFAULT_BLOCK_SIZE):
    print("> do Encryption...")
    keySize, n, e = readKeyFile(pubKeyFilename)
    
    if keySize < blockSize * 8:
        sys.exit("> ERROR! Block size bigger than key size!")

    encryptionBlock = encryptionMessage(message, (n, e), blockSize)

    count, limited = 0, len(encryptionBlock)
    for i in range(len(encryptionBlock)):
        count = count + 1
        PB.symbolBar(count, limited)
        encryptionBlock[i] = str(encryptionBlock[i])
    translate = ",".join(encryptionBlock)

    translate = "{}_{}_{}".format(len(message), blockSize, translate)
    return translate


# Mode2: do Decryption
def doDecrypt(priKeyFilename, message, blockSize = DEFAULT_BLOCK_SIZE):
    print("> do Decryption...")
    keySize, n, d = readKeyFile(priKeyFilename)
    messageLength, blockSize, encryptMessage = message.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if keySize < blockSize * 8:
        sys.exit("> ERROR! Block size bigger than key size!")

    count, limited = 0, len(encryptMessage.split(','))
    encryptedBlock = []
    for block in encryptMessage.split(','):
        count = count + 1
        PB.symbolBar(count, limited)
        encryptedBlock.append(int(block))

    return decryptionMessage(encryptedBlock, messageLength, (n, d), blockSize)


#   Step 1 : read key File
def readKeyFile(KeyFilename):
    f = open(KeyFilename)
    content = f.read()
    f.close()
    keySize, n, eord = content.split(',')
    return (int(keySize), int(n), int(eord))

#   Step 2 for encryption: encryption message
def encryptionMessage(message, key, blockSize):
    n, e = key
    encryptionBlock = []

    for block in getBlocksFromText(message, blockSize):
        encryptionBlock.append(pow(block, e, n))
        # encryptionBlock = messageBlock ^ e % n

    return encryptionBlock

#       Using in "encryptionMessage"
def getBlocksFromText(message, blockSize):
    messageBytes = message.encode('ascii')
    blockInts = []

    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt = blockInt + messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)

    return blockInts

#   Step 2 for decryption: decryption message
def decryptionMessage(encryptedBlock, messageLength, key, blockSize):
    decryptedBlock = []
    n, d = key

    for block in encryptedBlock:
        decryptedBlock.append(pow(block, d, n))
        # messageBlock = encryptionBlock ^ d % n
        # Pow faster than "**" in big date caculation

    return getTextFromBlock(decryptedBlock, messageLength, blockSize)

#       Using in "decryptionMessage"
def getTextFromBlock(decryptedBlock, messageLength, blockSize = DEFAULT_BLOCK_SIZE):
    message = []
    for blockInt in decryptedBlock:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                asciiNum = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNum))
        message.extend(blockMessage)

    return "".join(message)

# Blocks same as the binary system principle.
#   in 10-bin:   9 * (10**3) + 0 * (10**2) + 8 * (10**1) + 1 * (10**0) = 9081 [lock]
#                                   [unlock]
#               9081 // (10**3) = 9,    9081 % (10**3) = 81
#               81 // (10**2) = 0,      81 % (10**2) = 81
#               81 // (10**1) = 8,      81 % (10**1) = 1
#               1 // (10**0) = 1
#                               Orignal num = 9081
#   in block(256-bin):   
#               'a' -ascii-> 97,  'n' -ascii-> 110
#               97 * (256**0) + 110 * (256**1) = 28257 [lock]
#                                   [unlock]
#               28257 // (256**1) = 110,    28257 % (256**1) = 97
#               97 // (256**0) = 97
#                           Orignal num = 97，110 -char-> 'an'

if __name__ == "__main__":
    Processing()
