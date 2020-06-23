#Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, 
#или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
#одним ходом.

import math

print('You have chess Board like:')
print('  1 2 3 4 5 6 7 8')
i = ord('A')

let=list()

while i < (ord('A')+8):
    print(chr(i))
    let.append(i)
    i +=1

A = input("Input first point! F.Ex. A2\n")

error = 1

while error == 1:
    if (str.isalpha(A[0]) and str.isdigit(A[1])):
        if ord(str.upper(A[0])) in let:
            x1 = str.upper(A[0])
            error = 0
        else:
            A = input("Sorry, you've writen wrong point\nInput first point again! F.Ex. A2\n")
            error = 1
        if int(A[1]) in range(1,9):
            y1 = A[1]
            error = 0
        else:
            A = input("Sorry, you've writen wrong point\nInput first point again! F.Ex. A2\n")
            error = 1
    else:
        A = input("Sorry, you've writen wrong point\nInput first point again! F.Ex. A2\n")

B = input("Input second point! F.Ex. B4\n")

error = 1

while error == 1:
    if (str.isalpha(B[0]) and str.isdigit(B[1])):
        if ord(str.upper(B[0])) in let:
            x2 = str.upper(B[0])
            error = 0
        else:
            B = input("Sorry, you've writen wrong point\nInput second point again! F.Ex. B4\n")
            error = 1
        if int(B[1]) in range(1,9):
            y2 = B[1]
            error = 0
        else:
            B = input("Sorry, you've writen wrong point\nInput second point again! F.Ex. B4\n")
            error = 1
    else:
        B = input("Sorry, you've writen wrong point\nInput second point again! F.Ex. B4\n")

summa = math.fabs(ord(x2) - ord(x1)) + math.fabs(ord(y2) - ord(y1))

if summa == 3:
    print("It's OK. Hourse can move so!")
else:
    print("Sorry, Hourse can't  move so!")

input("\nPress anything to close the programm")