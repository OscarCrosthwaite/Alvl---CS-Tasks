def calc(n):
    if n == 1:
        factorial = 1
    else: 
        factorial = n * calc(n - 1)
    print(factorial)
    return factorial

#calc(300)

def listCalc(list):
    temp = 0
    sum = 0 
    while temp < len(list):
        sum = sum + list[temp]
        temp += 1
        print(sum)
    return sum


list1 = [5, 2, 3, 5, 4, 1]
#listCalc(list1)


def listCalc2(list, temp):

    if temp < 0:
        return 0
    else: 
        print(list[temp] + listCalc2(list, temp - 1))
        return list[temp] + listCalc2(list, temp - 1)



listCalc2(list1, len(list1) - 1)



