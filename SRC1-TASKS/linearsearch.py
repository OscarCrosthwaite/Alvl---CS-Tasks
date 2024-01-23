list1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        else:
            print()
    return False

if linearSearch(list1, 5) != False:
    print("It works!")


def linearSearchWhile(arr, item):
    retindex = -1
    index = 0
    while item != arr[index] and index < len(arr):
        index = index + 1
    if index == len(arr):
        return -1
    else:
        return index
    