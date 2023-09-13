word = input("input a word: ")
list1 = []
for i in range(0,len(word)):
    letter = word[i]
    list1.append(letter)
list1.reverse()
print(list1)