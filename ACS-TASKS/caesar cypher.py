word = input("Input your word: ")
for i in range(0,len(word)):
    letter = word[i]
    if letter == "x" or letter == "y" or letter == "z":
        letter = ord(letter) - 23
    else:
        letter = ord(letter) + 3
    print(chr(letter))