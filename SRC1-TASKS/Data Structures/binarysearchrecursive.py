mylist = [1, 4, 13, 27, 32, 37, 56, 83, 102, 115]

def binarySearchRecursive(arr, item):
    if len(arr) == 1:
        if arr[0] == item:
            return 0
        else:
            return -1
    else:
        mid = len(arr) // 2 - 1
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binarySearchRecursive(arr[0:mid], item)

        else:
            return binarySearchRecursive(arr[mid+1:], item)
        #endif
    #endif
#endfunction

print(binarySearchRecursive(mylist, 32))