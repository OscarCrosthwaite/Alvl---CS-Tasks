#program that divides one number chosen by the user by another, giving a full integer and the remainder
numberOne = int(input("Please choose a number to be divided: "))
numberTwo = int(input("Please choose a number to be the divider: "))
valueOne = numberOne//numberTwo
#divides numbers
valueTwo = numberOne % numberTwo
#finds remainder
print(f"The number is {valueOne} and the remainder is {valueTwo}.")
#prints numbers