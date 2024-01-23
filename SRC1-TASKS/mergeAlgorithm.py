arr1 = [1, 3, 4, 6, 8, 9]
arr2 = [2, 5, 12, 14, 17]
arr3 = [0 for _ in range(len(arr1) + len(arr2))]

def merge(arrA, arrB, arrC):
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    
    for i in range(len(arr1) + len(arr2)):
        if pointer1 <= len(arrA) and pointer2 <= len(arrB):
            if arrA[pointer1] <= arrB[pointer2]:
                arrC[pointer3] = arrA[pointer1]
                pointer1 += 1
                pointer3 += 1
            else:
                arrC[pointer3] = arrB[pointer2]
                pointer2 += 1
                pointer3 += 1
        elif pointer1 > len(arrA) and pointer2 <= len(arrB):
            for i in range(0, arrB):
                if pointer2 <= len(arrB):
                    arrC[pointer3] = arrB[i + pointer1]
                    pointer2 += 1
                    pointer3 += 1
        elif pointer2 > len(arrB) and pointer1 <= len(arrA):
            for i in range(0, arrA):
                if pointer1 <= len(arrA):
                    arrC[pointer3] = arrB[i + pointer2]
                    pointer1 += 1
                    pointer3 += 1
        else:
            print("Its working")
        return arrC

            


merge(arr1, arr2, arr3)
print(arr3)

	