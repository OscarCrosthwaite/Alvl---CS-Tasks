#compares the size of two numbers and prints them in size order
input1 = int(input("Please input a number: "))
input2 = int(input("Please input a second number: "))
#takes two numbers
if input1 > input2:
    print(input2,input1)
elif input2 > input1:
    print(input1, input2)
elif input2 == input1:
    print(input1,input2)
else:
    print("Please use numbers")
#endif
#compares number size and prints