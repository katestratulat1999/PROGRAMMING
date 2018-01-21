volwes= 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
a = input('Введите английское слово или фразу: ')
for i in a:
    if i in volwes:
        i = i + 'aig'
        print(i, end = '')
    else:
        print(i, end = '')
