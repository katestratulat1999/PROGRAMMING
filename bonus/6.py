h = int(input('Введите свой рост (в см): '))
m = int(input('Введите свой вес (в кг): '))
if h == 0 or m == 0:
    print('Введите достоверные данные')
else:
    i = m/((h/100)**2)
if i <= 16:
    print('Выраженный дефицит массы тела')
elif i <= 18.5:
    print('Недостаточная масса тела')
elif i <= 24.99:
    print('Норма')
elif i <= 30:
    print('Избыточная масса тела')
elif i <= 35:
    print('Ожирение первой степени')
elif i <= 40:
    print('Ожирение второй степени')
else:
   print('Ожирение третьей степени')
