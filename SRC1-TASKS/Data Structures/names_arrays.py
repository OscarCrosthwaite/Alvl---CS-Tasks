#when something is in all caps, it is a constant, although python doesn't have constants.
#variables
MAX = 10
found = False
index = 0

#creates list
pupilnames = ["" for _ in range(MAX)]
pupilnames[0] = "Brian"
pupilnames[1] = "Barry"
pupilnames[2] = "Bob"
pupilnames[3] = "Ben"

#asks for user input
user_Input = input("Please choose a name that you want to search for: ")
#while loop that searches through entire list to find the user input. will send message in console if user input is found
while found == False and index < MAX:
    if user_Input == pupilnames[index]:
        print(f"{user_Input} is present in the pupil names index.")
        found = True
    else:
        print(f"{user_Input} is not present in the pupil names index.")
        found = False
    index += 1