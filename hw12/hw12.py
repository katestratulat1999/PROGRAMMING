#вариант 4
#Сколько найдено файлов, название которых состоит только из латинских символов
#выводить на экран названия всех файлов/папок, которые она нашла, без повторов

import os
import re


def poisk():
    file_list = os.listdir()
    w = []
    for i,c in enumerate(file_list):
        res = re.match('[^а-яА-Я0-9]+[.][^а-яА-Я]*', c)
        if res:
            a = res.group()
            w.append(a)
        else:
            continue
    return w

def nineten(w):
    d = []
    for i,c in enumerate(w):
        if c in d[:i]:
            continue
        else:
            d.append(c)
    return d

def main():
    w = poisk()
    d = nineten(w)
    for i in d:
        print(i)
        
main()
