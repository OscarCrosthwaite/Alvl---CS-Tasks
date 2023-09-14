#program that intakes a word or sentence and outputs every letter as three letters to right (in the alphabet).
word = input("Input your word: ")
for i in range(0,len(word)):
    letter = word[i]
    #finds individual letters
    if letter == "x" or letter == "y" or letter == "z":
        letter = ord(letter) - 23
        #turns letter into ASCII code and decreases value by twenty-three
    else:
        letter = ord(letter) + 3
        #turn letter into ASCII code and increases value by three
    #endif
    print(chr(letter))
    #turns ASCII code into regular letters
#endfor