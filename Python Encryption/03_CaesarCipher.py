# Caesar Cipher

print("\n> Caesar Cipher, input your message:")
message = input("<<< ")
translate = ""

#    input mode
mode = 0
while mode == 0:
    print("> lock(1) or unlock(2)?")
    mode_str = input("<<< ")
    try:
        mode = int(mode_str)
    except ValueError:
        print("> You should input a number, not letter...")

#    input key
key = 0
while key == 0:
    print("> input your cipher code:")
    key_str = input("<<< ")
    try:
        key = int(key_str)
    except ValueError:
        print("> You should input a number, not letter...")
while key >= 26:
    key = key - 26
    
#    letter form
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"
SYMBOLS = "1234567890!@#$%^&*()[],.?:"

"""
# More general
LETTERS = "1!2@3#4$5%6^7&8*9(0)-_=+\\|~`QAZWSXEDCRFVTGBYHNUJMIK,OL.P;/[\']qazwsxedcrfvtgbyhnujmik<ol>p:?{\"}"
    
key = 0
while key == 0:
    print "> input your cipher code:"
    key_str = raw_input("<<< ")
    try:
        key = int(key_str)
    except ValueError:
        print "> You should input a number, not letter..."
while key >= len(LETTERS):
    key = key - len(LETTERS)   
    
 """

#    start
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 1:
            num = num + key
        elif mode == 2:
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translate = translate + LETTERS[num]

    elif symbol in letters:
        num = letters.find(symbol)
        if mode == 1:
            num = num + key
        elif mode == 2:
            num = num - key

        if num >= len(letters):
            num = num - len(letters)
        elif num < 0:
            num = num + len(letters)

        translate = translate + letters[num]
        
    elif symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 1:
            num = num + key
        elif mode == 2:
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translate = translate + SYMBOLS[num]
        
    else:
        translate = translate + symbol

#    finish
print("> Finish! Answer is this:\n  " + translate)