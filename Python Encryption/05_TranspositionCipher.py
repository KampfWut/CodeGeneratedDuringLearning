# Transposition Cipher

import math, random, sys

def work():
    #    input message
    print("\n> Transposition Cipher, input your message:")
    message = input("<<< ") 

    #    input key
    key = 0
    while key == 0:
        print("> input your cipher code:")
        key_str = input("<<< ")
        try:
            key = int(key_str)
        except ValueError:
            print("> You should input a number, not letter...")
    
    #    input mode
    mode = 0
    while mode == 0:
        print("> lock(1) or unlock(2)?")
        mode_str = input("<<< ")
        try:
            mode = int(mode_str)
        except ValueError:
            print("> You should input a number, not letter...")

    if mode == 1:
        translate = doEncrypt(key, message)
    elif mode == 2:
        translate = doDecrypt(key, message)

    print("> Finish! Answer is this:\n" + translate + "|")


def doEncrypt(key, message):
    translate = [""] * key

    for col in range(key):
        pointer = col
        
        while pointer < len(message):
            translate[col] += message[pointer]
            pointer = pointer + key
        
    return "".join(translate)


def doDecrypt(key, message):
    col = math.ceil(len(message) / key)
    col = int(col)
    row = key
    box = col * row - len(message)

    translate = [""] * col

    c, r = 0, 0
    for symbol in message:
        translate[c] = translate[c] + symbol
        c = c + 1

        if (c == col) or (c == col - 1 and r >= row - box):
            c = 0
            r = r + 1

    # print(translate)

    return "".join(translate)


def testWork():
    random.seed(42)

    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4,40)
        message = list(message)
        random.shuffle(message)
        message = "".join(message)

        print("Test #{0:2d}: \"{1}\"".format(i+1, message))

        for key in range(1, len(message)):
            Encrypt = doEncrypt(key, message)
            Decrypt = doDecrypt(key, Encrypt)

            if message != Decrypt:
                print("Mismatch!!key is {0:2d} and message is \"{1}\"".format(key, message))
                print("Decrypt is \"{}\"".format(Decrypt))
                sys.exit()
    
    print("Test passes!")


if __name__ == '__main__':
    work()
    # testWork()







