#finds all factors of an integer
number = int(input("Please input a number: "))
#finds number
thirdNumber = number
#divides by two to avoid showing duplicate factors
for i in range(1, thirdNumber):
    if number % i == 0:
        #checks if number is a factor
        secondNumber = number // i
        print(f"Two factors are {i} and {secondNumber}")
        #finds both factors and prints
        continue
    else:
        continue
    #endif
#endfor