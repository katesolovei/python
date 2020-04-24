#Треугольник Паскаля

import math

row = int(input("Input the number of the row\n"))
b = list() #список чисел в строке
n = 0 # номер строки треугольника
while n<row:
    n += 1
    m = 0 #номер числа в строке
    while m < n:
        b.append(math.factorial(n-1)/(math.factorial(m)*math.factorial(n-1-m)))
        m +=1
    print(b, end = '\n')
    b.clear()