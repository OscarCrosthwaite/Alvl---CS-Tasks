import time

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    #endif
#endfunction

#this algorithm is very inefficient - O(2^n)

def fibonacci2(n):
    fibNumbers = [0, 1]
    for i in range(2, n - 1):
        fibNumbers.append(fibNumbers[i - 1] + fibNumbers[i - 2])
    temp = 1
    for index in range(len(fibNumbers)):
        temp += fibNumbers[index]
    return temp


print(fibonacci2(10))

startTime1 = time.time()
fibonacci(10)
endTime1 = time.time()

startTime2 = time.time()
fibonacci2(10)
endTime2 = time.time()

if endTime1 > endTime2:
    print("Iterative is faster")
elif endTime2 > endTime1:
    print("Recursive is faster")
elif endTime2 == endTime1:
    print("Equal Speed")
else:
    print("")
