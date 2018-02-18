import random

def create_dict(fname):
    dict = {}
    with open(fname, encoding="utf-8") as f:
        a = f.readlines()
    for line in a:
        if line.endswith('\n'):
            line = line[:-1]
        word = line.split(',')
        dict[word[1]] = word[0]
    return dict

def rand_choice(fname):
    a = create_dict(fname)
    keys = list(a.keys())
    return random.choice(keys)

def enigma():
    k = ''
    c = ''
    dict = create_dict('file.csv')
    a = rand_choice('file.csv')
    for keys,value in dict.items():
        if keys == a:
            k = keys
            for i in range(len(a)):
                c += '.'
            print(value,' ',c)
        else:
            continue
    return k

def answ():
    a = riddle()
    b = input('Угадай слово. Сколько точек, столько и букв в слове: ')
    while True:
        if b == a:
            print('Ты угадал!')
            break
        else:
            print('Ты не угадал! Попробуй ещё раз.')
            b = input('Ты думаешь, что это: ')


a = answ()
