#takes word (or sentence) and reverses the order of all words and letters
word = input("input a word: ")
#finds word
list1 = []
#creates empty list
for i in range(0,len(word)):
    #range depends on word length
    letter = word[i]
    #finds letter
    list1.append(letter)
    #adds letter to list
list1.reverse()
#reverses list
print(list1)
#prints list