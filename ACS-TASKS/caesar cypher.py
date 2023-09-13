word = input("Input your word: ")

for i in range(1,len(word) + 1):
    letter = word[i]
    if letter == "x" or "y" or "z":
        letter = chr(ord(word[i]) - 23 )
    else:
        letter = chr(ord(word[i]) + 3)
    print(letter)
