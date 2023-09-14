#program that organises numbers into a list depending on their size
input1 = int(input("Input number: "))
input2 = int(input("Input number: "))
input3 = int(input("Input number: "))
#takes three numbers
numbers = [input1, input2, input3]
#puts numbers into list
numbers = sorted(numbers)
#sorts numbers into size
print(numbers)
#prints list