# var4
# эта программа генерирует хайку на итальянском языке
# в итальянском кол-во слогов = кол-ву гласных
# coding=utf-8
import random
def nome_1():
# эта функция возвращает случайное сущ-е ж.р; у неё нет аргументов
    with open("nome_1.txt", encoding="utf-8") as f:
         text=f.read()
         nome1=text.split()
         return random.choice(nome1)
def aggettivo_1():
# эта функция возвращает случайное прилагательное ж.р; у неё нет аргументов
    with open("aggettivo_1.txt", encoding="utf-8") as f:
         text=f.read()
         aggettivo1=text.split()
         return random.choice(aggettivo1)
def verbo_2():
# эта функция возвращает случайный глагол 3л; у неё нет аргументов
    with open("verbo_2.txt", encoding="utf-8") as f:
         text=f.read()
         verbo2=text.split()
         return random.choice(verbo2)
def predlog_2():
# эта функция возвращает случайный предлог; у неё нет аргументов
    with open("predlog_2.txt", encoding="utf-8") as f:
         text=f.read()
         predlog2=text.split()
         return random.choice(predlog2)
def nome_2():
# эта функция возвращает случайное сущ-е м.р. и ж.р.; у неё нет аргументов
    with open("nome_2.txt", encoding="utf-8") as f:
         text=f.read()
         nome2=text.split()
         return random.choice(nome2)
def predlog_3():
# эта функция возвращает случайный предлог; у неё нет аргументов
    with open("predlog_3.txt", encoding="utf-8") as f:
         text=f.read()
         predlog3=text.split()
         return random.choice(predlog3)
def nome_3():
# эта функция возвращает случайное сущ-е м.р. и ж.р.; у неё нет аргументов
    with open("nome_3.txt", encoding="utf-8") as f:
         text=f.read()
         nome3=text.split()
         return random.choice(nome3)
def punctuation():
# эта функция возвращает случайный знак препинания из небольшого списка; у неё нет аргументов
    marks = [".", "?", "!", "..."]
    return random.choice(marks)
def verse1():
    # эта функция собирает строчку из сущ., прилаг. и знака препинания
    return nome_1() + ' ' + aggettivo_1() + punctuation()
def verse2():
    # эта функция собирает строчку из глаг., предлога, сущ. и знака препинания
    return verbo_2() + ' ' + predlog_2()+ ' ' + nome_2() + punctuation()
def verse3():
    # эта функция собирает строчку из предлога, сущ. и знака препинания
    # например "малыши пожуют камыши!"
    return predlog_3() + ' ' + nome_3() + punctuation()
print(verse1())
print(verse2())
print(verse3())










        
