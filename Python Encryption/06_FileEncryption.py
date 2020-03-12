# File Encryption

import os, sys, time
import use_original.TranspositionCipherUseinSix as TC

def fileEncryption():

    #    input file name
    print("> input your input File Name:")
    inputFileName = input("<<< ")
    FileName = inputFileName[:len(inputFileName) - 4]
    outputFileName = FileName + "_trans.txt"

    if not os.path.exists(inputFileName):
        print("> [ERROR] There is no \"{}\" File. ".format(inputFileName))
        sys.exit()
    
    if os.path.exists(outputFileName):
        print("> [Warning] There exists a same name file, will be overwrite. ")
        print(">           (C)ontinue or (Q)uit ? ")
        back = input("<<< ")
        if not back.lower().startswith('c'):
            sys.exit()

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

    #    open file
    f = open(inputFileName)
    content = f.read()
    f.close()

    #    start work
    print("> Loading...")

    startTime = time.time()
    if mode == 1:
        translate = TC.doEncrypt(key, content)
    elif mode == 2:
        translate = TC.doDecrypt(key, content)

    totaltime = round(time.time() - startTime, 2)

    f = open(outputFileName, 'w')
    f.write(translate)
    f.close()

    #    finish
    print("> Done \"{}\" with {} characters".format(inputFileName, len(content)))
    print("> Using time: {} seconds".format(totaltime))
    print("> Save as \"{}\"".format(outputFileName))

if __name__ == "__main__":
    fileEncryption()

    

