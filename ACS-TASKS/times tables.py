#program the finds the first ten multiples of any integer between one and ten
while True:
    userInput = int(input("Please input a number between one to ten: "))
    #obtains user value between one and ten
    if userInput > 0 and userInput < 11:
        #confirms size of user value
        break
    else:
        print("Number too big or too small!")
        continue
    #endif
for i in range(1,11):
    multiple = userInput * i
    #finds multiples from one to ten
    print(multiple)
#endfor
#endwhile
