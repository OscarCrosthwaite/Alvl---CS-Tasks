outlet1Sales = [10, 12, 15, 10]
outlet2Sales = [5, 8, 3, 6]
outlet3Sales = [10, 12, 15, 10]

print("Sales for Quarter 1: ", outlet1Sales[0] + outlet2Sales[0] + outlet3Sales[0])
print("Sales for Quarter 2: ", outlet1Sales[1] + outlet2Sales[1] + outlet3Sales[1])
print("Sales for Quarter 3: ", outlet1Sales[2] + outlet2Sales[2] + outlet3Sales[2])
print("Sales for Quarter 4: ", outlet1Sales[3] + outlet2Sales[3] + outlet3Sales[3])

for i in range(0, 3):
    quarterI = outlet1Sales[i] + outlet2Sales[i] + outlet3Sales[i]
    print(quarterI)