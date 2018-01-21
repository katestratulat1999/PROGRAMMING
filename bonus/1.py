list = []
while True:
    a = input()
    if not a:
        break
    a = float(a)
    list.append(a)
print('Арифметическое среднее:', sum(list)/len(list))
print('Самое большое число:', min(list))
print('Самое маленькое число:', max(list))
