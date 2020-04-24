#Полиндром
word = list(input("Input the word\n"))
index_list = list() #список индексов
word_len = len(word) #длина введенного слова
for i in word:
    index_list.append(word.index(i))
check = 0 #переменная для проверки 
for j in range(0, word_len):
    if index_list[j] == index_list[word_len-1-j]:
        check += 1
if check == word_len:
    print("Polindrom")
else:
    print("Not Polindrom") 