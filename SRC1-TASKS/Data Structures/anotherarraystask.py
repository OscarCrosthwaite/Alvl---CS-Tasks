school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4, 7, 1, 3]

valid = False

while True:
    uInput = int(input("Input school number: "))
    uArray = uInput - 1
    if uInput > 1 and uInput < 5:
        break
    else:
        print("Please enter valid message. ")
        break

addedMedals = int(input(f"How many medals did school {school[uArray]} earn?: "))
medal[uArray] = medal[uArray] + addedMedals

print("School Number: ", uInput)
print("School Name: ", school[uArray])
print("Number of Medals: ", medal[uArray])