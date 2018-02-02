vowels= 'АаЕеЁёИиОоУуЫыЭэЮюЯя'
a = input('Введите слово или фразу: ')
end = ''
for i in a:
    if i in vowels:
        i = i + 'c' + i
        print(i, end = '')
    else:
        print(i, end = '')
        
        
