# Caeeasar Chpher Hacker

print(" ---* Caeeasar Chpher Hacker *---")
print("\n> Input the message:")
message = input("<<< ")

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = "abcdefghijklmnopqrstuvwxyz"

print("------start------")

for key in range(26):
    translate = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(LETTERS)
            
            translate = translate + LETTERS[num]

        elif symbol in letters:
            num = letters.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(letters)
            
            translate = translate + letters[num]

        else:
            translate = translate + symbol

    print("   Key {0:2d}: {1}".format(key, translate))

print("------finish-------")