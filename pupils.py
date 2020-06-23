#В школе решили набрать три новых математических класса. 
#Так как занятия по математике у них проходят в одно и то же время, 
#было решено выделить кабинет для каждого класса и купить в них новые парты. 
#За каждой партой может сидеть не больше двух учеников. 
#Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? 
#Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

import math

first_class = int(input("Input number of pupils in the first class\n"))
second_class = int(input("Input number of pupils in the second class\n"))
third_class = int(input("Input number of pupils in the third class\n"))

desks = list()

if first_class % 2 == 1:
    desks.append(first_class//2 + 1)
else:
    desks.append(first_class//2)

if second_class % 2 == 1:
    desks.append(second_class//2 + 1)
else:
    desks.append(second_class//2)

if third_class % 2 == 1:
    desks.append(third_class//2 + 1)
else:
    desks.append(third_class//2)

print('The school needs',sum(desks), 'desks.')