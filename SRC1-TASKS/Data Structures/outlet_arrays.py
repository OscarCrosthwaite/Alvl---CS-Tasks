outlet1Sales = [10, 12, 15, 10]
outlet2Sales = [5, 8, 3, 6]
outlet3Sales = [10, 12, 15, 10]

averageOutletSales = [7, 12, 13, 9]

for i in range(0, 4):
    total = outlet1Sales[i] + outlet2Sales[i] + outlet3Sales[i] + (averageOutletSales[i] * 47)
    print(f"Sales for quarter {i + 1} are {total}.")

