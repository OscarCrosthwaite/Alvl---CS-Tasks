num = [0 for _ in range(6)]
for i in range(0,6):
    num[i] = int(input("Enter number: "))
print(num)
for i in range(5, -1, -1):
    print(num[i])

total = 0
for i in range(0,6):
    total = total + num[i]
print(total)

average = total / len(num)
print(average)