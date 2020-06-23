#Дано целое, положительное, трёхзначное число. Например: 123, 867, 374. Необходимо его перевернуть. 
#Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только с числами. 
#Строки, оператор IF и циклы использовать НЕЛЬЗЯ!

number = int(input("Input *** number\n"))

res = list()

res.append(number//100)
number = number - res[0]*100

res.append(number//10)
number = number - res[1]*10

res.append(number)

new_res = res[-1]*100 + res[-2]*10 +res[-3]
print(new_res)