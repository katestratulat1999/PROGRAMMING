#убираем символы
def txt(fname):
    with open (fname + '.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        symbols_to_remove = ',:;.!?"()'
        for s in symbols_to_remove:
            txt = txt.replace(s, '')
        words = txt.split()
        return words

#находим формы на -ed, а также сколько из них образованы от глаголов на -y  или -e 
def c(txt):
    c = [0,0]
    for word in txt:
        if word[-2:] == 'ed':
            c[0] += 1
            if word[-3] == 'i':
                c[1] += 1
    return c

#запрашиваем имя файла 
file = input('Введите имя файла: ')
txt = txt(file)
c = c(txt)

#выводим результат
print('Форм на -ed: ',c[0])
print('Форм на -ied: ',c[1])
                
                
        
