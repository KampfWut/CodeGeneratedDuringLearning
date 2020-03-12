# Simple Substitution Cipher Hacker

import copy
import os
import pprint
import re
import sys

import use_original.CreateWordModeFileUseinThirteen as CWM
import use_original.SimpleSubtitutionCipherUseinThirteen as SSC
import use_original.wordModeUseinThirtten as WM
import use_original.ProcessingBar as PB

'''
if not os.path.exists("12_wordMode.py"):
    CWM.getAllWordMode()
'''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
clearFormat = re.compile('[^A-Z\s]')

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
    letterMatch = hackSimpleSubtitution(message)

    print("\n> Matching:")
    pprint.pprint(letterMatch)

    translate = decryptWithMatch(message, letterMatch)
    
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

# hack and get the letter match
def hackSimpleSubtitution(message):
    print("> Hacking...")
    intersected = backBlankMatch()
    cipherList = clearFormat.sub('', message.upper()).split()

    count = 0
    for cipherWord in cipherList:
        count = count + 1
        newMatch = backBlankMatch()

        wordMode = CWM.getOneWordMode(cipherWord)
        if wordMode not in WM.allWordMode:
            continue
            # This word not in dictionary
        
        for possibleWord in WM.allWordMode[wordMode]:
            newMatch = addLetter2Match(newMatch, cipherWord, possibleWord)
            # Push possible word into Match map
        
        intersected = intersectMatch(intersected, newMatch)
        # print("> {}".format(intersected))
        PB.symbolBar(count, len(cipherList))

    '''
    pprint.pprint(intersected)
    input()
    '''

    return removeSolvedLetters(intersected)

# back blank match map
def backBlankMatch():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

# add letter to match
def addLetter2Match(match, cipherWord, possibleWord):
    match = copy.deepcopy(match)

    for i in range(len(cipherWord)):
        if possibleWord[i] not in match[cipherWord[i]]:
            match[cipherWord[i]].append(possibleWord[i])

    return match

# intersect two matches
def intersectMatch(matchA, matchB):
    final = backBlankMatch()

    for letter in LETTERS:
        if matchA[letter] == []:
            final[letter] = copy.deepcopy(matchB[letter])
            # exist in A but not in B
        elif matchB[letter] == []:
            final[letter] = copy.deepcopy(matchA[letter])
            # exist in B but not in A
        else:
            for matchLetter in matchA[letter]:
                if matchLetter in matchB[letter]:
                    final[letter].append(matchLetter)
            # AB all exist. choose (A and B)

    return final

# remove the solved letter
def removeSolvedLetters(match):
    match = copy.deepcopy(match)
    loopFlag = True

    while loopFlag:
        loopFlag = False
        solvedLetter = []

        '''
        print("Match: ")
        pprint.pprint(match)
        '''

        for cipherLetter in LETTERS:
            if len(match[cipherLetter]) == 1:
                solvedLetter.append(match[cipherLetter][0])
                # print(solvedLetter)

        for cipherLetter in LETTERS:
            for symbol in solvedLetter:
                if (len(match[cipherLetter]) != 1) and (symbol in match[cipherLetter]):
                    match[cipherLetter].remove(symbol)
                    # print(">> remove")
                    if len(match[cipherLetter]) == 1:
                        loopFlag = True
                        # print("{} >> again".format(cipherLetter))

        '''
        print("Solved: ")
        pprint.pprint(solvedLetter)
        input()
        '''

    return match

# decryption message
def decryptWithMatch(message, letterMatch):
    print("> LetterMatch get, start translate...")
    key = ['x'] * len(LETTERS)
    for cipherLetter in LETTERS:
        if len(letterMatch[cipherLetter]) == 1:
            keyIndex = LETTERS.find(letterMatch[cipherLetter][0])
            key[keyIndex] = cipherLetter
        else:
            message = message.replace(cipherLetter.lower(), '_')
            message = message.replace(cipherLetter.upper(), '_')

    key = ''.join(key)
    print("> Using key : {}".format(key))

    '''
    for i in range(len(key)):
        if key[i] == 'x':
            message = message.replace(LETTERS[i].upper(), '_')
            message = message.replace(LETTERS[i].lower(), '_')
    '''

    return SSC.decryptMessage(key, message)

if __name__ == "__main__":
    Processing()
