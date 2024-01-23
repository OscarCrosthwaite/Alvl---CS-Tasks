arr = [7, 4, 6, 8, 1, 5]

def swap(a, b, arr):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp

def swap2(a, b, arr):
    arr[b], arr[a] = arr[a], arr[b]
#end procedure
    

first, *middle, last = "hello"
    
print(arr)
swap2(0, 1, arr)
print(arr)

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1, arr)
            #endif
        #next i
    #next i
#end procedure