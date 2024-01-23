#iterative fibonacci
def fibo(n):
    temp1 = 0
    temp2 = 0
    temp3 = 1
    print(0)
    print(1)
    for i in range(n):
        temp1 = temp3 + temp2
        print(temp1)
        temp2 = temp1 + temp3
        print(temp2)
        temp3 = temp2 + temp1
        print(temp3)
#fibo(5)

#recursive fibonacci
def fib(n):
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        else: 
            return fib(n - 1) + fib(n - 2)
list1 = []
def printFib(n, list):
    list.append(0)
    for i in range(n):
         list.append(fib(i))
    print(list)
#printFib(10, list1)

#recursive fibonacci and dictionary
dict = {0:0, 1:1}
def fibdict(n):
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        else: 
            return fibdict(n - 1) + fibdict(n - 2)
def printFibdict(n, dict):
    for i in range(n):
        dict[i] = fibdict(i)
    print(dict)

printFibdict(14, dict)