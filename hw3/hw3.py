#Вариант 4
x = input('Введите слово: ')
for y in x:
    print (x)
    x = x[-1] + x[:-1]
if x == "":
    print ('Но это же пустая строка... ')
    x = input('Введите слово: ')
for y in x:
    print (x)
    x = x[-1] + x[:-1] 
