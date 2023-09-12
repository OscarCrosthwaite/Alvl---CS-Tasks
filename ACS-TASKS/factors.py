number = int(input("Please input a number: "))
thirdNumber = number // 2
for i in range(1, thirdNumber):
    if number % i == 0:
        secondNumber = number // i
        print(f"Two factors are {i} and {secondNumber}")
        continue
    else:
        continue