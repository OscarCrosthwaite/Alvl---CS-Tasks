num1 = 1000000
print(num1)
num2 = 1000000
print(num2)

if num1 is num2:
    print("Only one object")
else:
    print("There are two objects")

a = 0
b = 0
while a is b:
    a += 1
    b += 1
print(a)
