from random import randint

num = randint(100000, 1000000)
list = [int(x) for x in str(num)]

total = list[1] * 1 + list[2] * 3 + list[3] * 1 + list[4] * 3 + list[5]  * 1
remainder = total % 10

