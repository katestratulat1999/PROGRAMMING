#вариант4
w = []
word = input('Введите латинское слово: ')
if word == '':
    print('Нет, надо ввести слово: ')
else:
    while word != '':
        if word.endswith('re') or word.endswith('ri'):
            w.append(word + '\n')
        word = input()
with open('hw5text.txt', 'w', encoding='utf-8') as f:
    f.writelines(w)
