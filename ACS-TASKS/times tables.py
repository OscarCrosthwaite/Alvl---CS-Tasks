while True:
    userInput = int(input("Please input a number between one to ten: "))
    if userInput > 0 and userInput < 11:
        break
    else:
        print("Number too big or too small!")
        continue
for i in range(1,11):
    multiple = userInput * i
    print(multiple)
