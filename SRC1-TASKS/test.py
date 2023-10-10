rows, cols = (6, 4)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 'O'

for row in arr:
    for x in row:
        print(x, end="")
    print("")




#my_row = int(input("Enter column to move to"))
#my_row = my_row - 1
#my_column = int(input("Enter column to move to"))
#my_column = my_column - 1

#arr[0][0] = "X"
#earr[my_row][my_column] = "O"
