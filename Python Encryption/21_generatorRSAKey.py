# RSA key generator

import os
import random
import sys

import use_original.RabinMiller as RM
import use_original.cryptomath as CM

# Main process
def Processing():
    print("> RSA key generator start!")

    print("> Input your key File save name: ")
    name = input(">>> ")

    makeKeyFile(name, 1024)

    print("> Finish!")


def makeKeyFile(name, keySize):
    publicFile = name + "_public.txt"
    privateFile = name + "_private.txt"

    if os.path.exists(publicFile) or os.path.exists(privateFile):
        sys.exit("> Warning! The file is exist!")

    publicKey, privateKey = generateKey(keySize)

    print("> \nPublice key length is {} and {} .".format(len(str(publicKey[0])),len(str(publicKey[1]))))
    f = open(publicFile, 'w')
    f.write("{},{},{}".format(keySize, publicKey[0], publicKey[1]))
    f.close()


    print("> Private key length is {} and {} .".format(len(str(privateKey[0])),len(str(privateKey[1]))))
    f = open(privateFile, 'w')
    f.write("{},{},{}".format(keySize, privateKey[0], privateKey[1]))
    f.close()

# Generate RSA key
def generateKey(keySize):
    # p & q
    print("> Generating P prime ...")
    p = RM.generateLargePrime(keySize)
    print("> Generating Q prime ...")
    q = RM.generateLargePrime(keySize)
    n = p * q

    # e
    print("> Generating E, which is relatively prime to (P-1)*(Q-1) ...")
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** keySize)
        if CM.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # d
    print("> Generating D, which is mod inverse of E ...")
    d = CM.findModInverse(e, (p - 1) * (q - 1))

    # finish
    publicKey = (n, e)
    privateKey = (n, d)
    print("\n> publicKey :")
    print(publicKey)
    print("> privateKey : ")
    print(privateKey)

    return (publicKey, privateKey)

if __name__ == "__main__":
    Processing()
