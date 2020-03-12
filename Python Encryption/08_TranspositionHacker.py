# Transposition Cipher Hacker

import use_original.CheckEnglishUseinEight as Ceu
import use_original.TranspositionCipherUseinSix as Tc
import sys, time, os

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
    translate = hackTransposition(message)
    
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

#    hacking Process
def hackTransposition(message):
    starttime = time.time()
    print("> May use lot of time, use \'Ctrl-D\' quit at any time")
    print("> Hacking...")

    for key in range(1, len(message)):
        print("> Trying key #{}...".format(key))
        translate = Tc.doDecrypt(key, message)

        if Ceu.isEnglish(translate)[0]:
            print("> \n> possible result: key #{}".format(key))
            print(">\n{}".format(translate[:300]))
            totaltime = round(time.time() - starttime, 4)
            print("> Now use time: {} second.".format(totaltime))
            print("> Enter \'D\' to done, or continue hacking...")
            back = input("<<< ")
            if back.strip().upper().startswith('D'):
                return translate

    return None

if __name__ == "__main__":
    Processing()



 