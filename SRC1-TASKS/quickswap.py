
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
#end procedure
    
def quickPass(arr):
    pivot = len(arr) - 1
    ptr = 0
    right = True
    direction = 1
    while ptr != pivot:
        if arr[ptr] < arr[pivot]:
            ptr += direction
        else:
            swap(arr, ptr, pivot)
            pivot, ptr = ptr, pivot
            direction = direction * -1
        #end if
    #end while
    print(arr)
#end procedure
            
list1 = ["A", "F", "G", "B", "E", "C", "H", "D"]

quickPass(list1)

def quickSplit(arr, ptr, pivot): 
    direction = 1 
    while ptr != pivot: 
        if ((direction == 1 and arr[ptr] > arr[pivot]) or  
            (direction == -1 and arr[ptr] < arr[pivot])): 
            swap(arr, ptr, pivot) 
            ptr, pivot = pivot, ptr 
            direction = direction * -1 
        #endif 
        ptr += direction 
    #endwhile 
    return pivot 

def quickSort(arr, left, right): 
    if left >= right: 
        pass 
    else: 
        pivotPos = quickSplit(arr, left, right) 
        quickSort(arr, left, pivotPos - 1) 
        quickSort(arr, pivotPos + 1, right) 
    