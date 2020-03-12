# Frequency Finder

import pprint

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN =  'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# Letter Counter
def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    
    if __name__ == "__main__":
        print("> letter count :")
        pprint.pprint(letterCount)

    return letterCount

# Back index[0] (Use in sort)
def getIndex(x):
    return x[0]

# Letter Frequency Order
def getFrequencyOrder(message):
    # [eg.] message = "Hello everyone!It is a nice day again, so what do we do?"

    letter2Fre = getLetterCount(message)
    # [eg.] letter2Fre = {'A': 5, 'B': 0, 'C': 1, 'D': 3, 'E': 6, 'F': 0, 'G': 1, 'H': 2, 'I': 4, 'J': 0, 'K': 0, 'L': 2, 'M': 0, 'N': 3, 'O': 5, 'P': 0, 'Q': 0, 'R': 1, 'S': 2, 'T': 2, 'U': 0, 'V': 1, 'W': 2, 'X': 0, 'Y': 2, 'Z': 0}
    #       letter2Fre = {'Letter': Frequency}

    fre2Letter = {}
    for letter in  LETTERS:
        if letter2Fre[letter] not in fre2Letter:
            fre2Letter[letter2Fre[letter]] = [letter]
        else:
            fre2Letter[letter2Fre[letter]].append(letter)
    # [eg.] fre2Letter = {5: ['A', 'O'], 0: ['B', 'F', 'J', 'K', 'M', 'P', 'Q', 'U', 'X', 'Z'], 1: ['C', 'G', 'R', 'V'], 3: ['D', 'N'], 6: ['E'], 2: ['H', 'L', 'S', 'T', 'W', 'Y'], 4: ['I']}
    #       fre2Letter = {Frequency: ['Letter', ...]}

    for fre in fre2Letter:
        fre2Letter[fre].sort(key = ETAOIN.find, reverse = True)
        fre2Letter[fre] = "".join(fre2Letter[fre])
    # [eg.] fre2Letter = {5: 'OA', 0: 'ZQXJKBPFMU', 1: 'VGCR', 3: 'DN', 6: 'E', 2: 'YWLHST', 4: 'I'}
    #       Arrange each key in fre2Letter in reverse order in the order of ETAOIN.

    frePairs = list(fre2Letter.items())
    frePairs.sort(key = getIndex, reverse = True)
    # [eg.] frePairs = [(6, 'E'), (5, 'OA'), (4, 'I'), (3, 'DN'), (2, 'YWLHST'), (1, 'VGCR'), (0, 'ZQXJKBPFMU')]
    #       Sorted by frequency

    freOrder = []
    for frePair in frePairs:
        freOrder.append(frePair[1])
    # [eg.] freOrder = ['E', 'OA', 'I', 'DN', 'YWLHST', 'VGCR', 'ZQXJKBPFMU']
    #       Keep only letters

    if __name__ == "__main__":
        print("> Letter Frequency Order : {}".format("".join(freOrder)))

    return "".join(freOrder)
    # [eg.] return 'EOAIDNYWLHSTVGCRZQXJKBPFMU'

# Caculate match number
def englishFrequencyMatch(message):
    freOrder = getFrequencyOrder(message)

    matchScore = 0
    for letter in ETAOIN[:6]:
        if letter in freOrder[:6]:
            matchScore = matchScore + 1
    for letter in ETAOIN[-6:]:
        if letter in freOrder[-6:]:
            matchScore = matchScore + 1
    
    return matchScore

if __name__ == "__main__":
    print("> input message:")
    message = input("<<< ")
    print("> Match Score : {}".format(englishFrequencyMatch(message)))

