 # Reverse Cipher

print("\n> Reverse Cipher, input your message:")
message = input("<<< ")
translate = ""

i = len(message) - 1
while i >= 0:
    translate = translate + message[i]
    i = i - 1

print("> Finish! Ciphertext is this:\n  " + translate)