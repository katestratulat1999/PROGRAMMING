#4 вариант
N = int(input('Введите число:'))
if N > 0:
    for i in range(N):
        a = input('Введите слово:')
        if a == 'Программирование' or a == 'программирование':
            break
        else:
            print(a)
else:
    N = int(input('Введите положительное число:'))
    for i in range(N):
        a = input('Введите слово:')
        if a == 'Программирование' or a == 'программирование':
            break
        else:
            print(a)
print('End')
