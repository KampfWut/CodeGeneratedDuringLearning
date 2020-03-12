# Vigenere Cipher Frequency Hacker

import itertools
import os
import re
import sys

import use_original.CheckEnglishUseinEight as CE
import use_original.FrequencyFinderUseinSeventeen as FF
import use_original.VigenereCipherUseinSixteen as VC
import use_original.ProcessingBar as PB

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SILENT_MODE = True
NUM_MOST_FRE_LETTERS = 3
MAX_KEY_LENGTH = 16
CLEAR_FORMAT = re.compile('[^A-Z]')

# Main Process
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
    translate = hackVigenerebyFrequency(message)
    
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

# Hack Vigenere by Frequency
def hackVigenerebyFrequency(message):
    print("> Hacking...")
    allPossibleKeyLengths = kasiskiExam(message)

    keyLengthStr = ''
    for keyLength in allPossibleKeyLengths:
        keyLengthStr = keyLengthStr + "%s " % (keyLength)
    print("\n> KasisKi Examination result: most likely key length is {}.".format(keyLengthStr))

    print("\n> Step 2/2: Attemp Hack With Key Length")
    for keyLength in allPossibleKeyLengths:
        # if not SILENT_MODE:
        print("\n> Attempiiing hack with key length {}, total possible is {} keys ".format(keyLength, NUM_MOST_FRE_LETTERS ** keyLength))
        translate = attempHackWithKeyLength(message, keyLength)
        if translate != None:
            break
    return translate


#  Step 1: KasisKi Examination: Get the Possible Key Lengths
def kasiskiExam(message):
    print("> Step 1/2: KasisKi Examination")
    repeatSS = findRepeatSequencesSpacings(message)

    seqFactors = {}
    print("\n>   Get all the factors of the number...")
    count, limited = 0, len(repeatSS)
    for seq in repeatSS:
        count = count + 1
        PB.symbolBar(count, limited)

        seqFactors[seq] = []
        for spacing in repeatSS[seq]:
            seqFactors[seq].extend(getAllFactors(spacing))
            # extend not attend, a = [a,b,c], b = [1,2,3]
            # extend = [a,b,c,1,2,3], attend = [[a,b,c], [1,2,3]]

    factorByCount = getMostCommonFacters(seqFactors)
    # [eg g.txt] factorByCount = [(3, 556), (2, 541), (6, 529), (4, 331), (12, 325), (8, 171), (9, 156), (16, 105), (5, 98), (11, 86), (10, 84), (15, 84), (7, 83), (14, 68), (13, 52)]

    allPossibleKeyLengths = []
    for pairs in factorByCount:
        allPossibleKeyLengths.append(pairs[0])
    # [eg g.txt] allPossibleKeyLengths = [3, 2, 6, 4, 12, 8, 9, 16, 5, 11, 10, 15, 7, 14, 13]

    return allPossibleKeyLengths

#    Find Repeat Sequences Spacings, Use in "kasiskiExam"
def findRepeatSequencesSpacings(message):
    # [eg. g.txt] 
    message = CLEAR_FORMAT.sub("", message.upper())
    print(">   Find Repeat Sequences Spacings...")

    seqSpacings = {}
    count, limited = 0, (len(message) - 3) + (len(message) - 4) + (len(message) - 5)
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            count = count + 1
            PB.symbolBar(count, limited)
            seq = message[seqStart:seqStart + seqLen]

            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    if seq not in seqSpacings:
                        seqSpacings[seq] = []
                    seqSpacings[seq].append(i - seqStart)
    
    return seqSpacings

#    Get all the factors of the number, Use in "kasiskiExam"
def getAllFactors(num):
    if num < 2:
        return []

    factors = []
    for i in range(2, MAX_KEY_LENGTH + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)

    return list(set(factors))
    # Use set: Remove duplicate values

#    Get the most common facter, Use in "kasiskiExam"
def getMostCommonFacters(seqFactors):
    print("\n>   Get the most common facter...")
    factorCounts = {}

    count, limited = 0, len(seqFactors)
    for seq in seqFactors:
        count = count + 1
        PB.symbolBar(count, limited)

        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

        factorsByCount = []
        for factor in factorCounts:
            if factor <= MAX_KEY_LENGTH:
                factorsByCount.append((factor, factorCounts[factor]))

        factorsByCount.sort(key = getIndex, reverse = True)

    return factorsByCount


#           Fuction help "sort" index, Use in "getMostCommonFacters"
def getIndex(x):
    return x[1]

#  Step 2: Attemp Hack With Key Length 
def attempHackWithKeyLength(message, keyLength):
    Message = message.upper()

    allFreScores = []
    for nth in range(1,keyLength + 1):
        nthLetters = getNthSubkeyLetters(nth, keyLength, Message)
        freScores = []
        for possibleKey in LETTERS:
            translate = VC.decryptMessage(possibleKey, nthLetters)
            
            matchPair = (possibleKey, FF.englishFrequencyMatch(translate))
            # Frequency analysis determines which sub key is decrypted after the original text is more consistent with the "standard English alphabet frequency".
            
            freScores.append(matchPair)
        freScores.sort(key = getIndex, reverse = True)
        allFreScores.append(freScores[:NUM_MOST_FRE_LETTERS])
    # [eg. g.txt] allFreScores = [[('A', 9), ('E', 5), ('O', 4)], [('S', 10), ('D', 4), ('G', 4)], [('I', 11), ('V', 4), ('X', 4)], [('M', 10), ('Z', 5), ('Q', 4)], [('O', 11), ('B', 4), ('Z', 4)], [('V', 10), ('I', 5), ('K', 5)]]

    for i in range(len(allFreScores)):
        print(">   Possible key for letter: {} -- ".format(i+1), end = '')
        for freScores in allFreScores[i]:
            print("{} ".format(freScores[0]), end = '')
        print()

    '''
    # [eg. g.txt] output>   >   Possible key for letter: 1 -- A E O
                            >   Possible key for letter: 2 -- S D G
                            >   Possible key for letter: 3 -- I V X
                            >   Possible key for letter: 4 -- M Z Q
                            >   Possible key for letter: 5 -- O B Z
                            >   Possible key for letter: 6 -- V I K
    '''

    count, limited = 0, NUM_MOST_FRE_LETTERS ** keyLength
    for index in itertools.product(range(NUM_MOST_FRE_LETTERS), repeat = keyLength):
        count = count + 1
        PB.symbolBar(count,limited)
        
        possibleKey = ''
        for i in range(keyLength):
            possibleKey = possibleKey + allFreScores[i][index[i]][0]
        # Descartes product combination gets all possible keys.
        # Descartes product --> itertools.product

        if not SILENT_MODE:
            print("> Attemping with key : {}".format(possibleKey))
        translate = VC.decryptMessage(possibleKey, message)

        if CE.isEnglish(translate)[0]:
            origCase = []
            for i in range(len(message)):
                if message[i].isupper():
                    origCase.append(translate[i].upper())
                else: 
                    origCase.append(translate[i].lower())
            translate = "".join(origCase)

            print("\n> Possible answer:")
            print(">   Key: {}\n>   Translate: ".format(possibleKey))
            print(translate[:300])
            print("> Enter \'D\' to done, or continue hacking...")
            back = input("<<< ")
            if back.strip().upper().startswith('D'):
                return translate

    return None


#    Get n-th subkey letters, Use in "attempHackWithKeyLength"
def getNthSubkeyLetters(nth, keyLength, Message):
    Message = CLEAR_FORMAT.sub("", Message)

    i = nth - 1
    letters = [] 

    while i < len(Message):
        letters.append(Message[i])
        i = i + keyLength

    return ''.join(letters)


if __name__ == "__main__":
    Processing()