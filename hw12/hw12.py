#вариант 4
#Сколько найдено файлов, название которых состоит только из латинских символов
#выводить на экран названия всех файлов/папок, которые она нашла, без повторов

import os
import re


# эта функция возвращает именно название файла, без расширения
def name(filename):
    match = re.search('(.+)\.', filename)
    filename = match.group(1)
    return filename


# эта функция подсчитывает количество файлов, название которых состоит только из латинских символов
def count():
    c = 0
    file_list = os.listdir()
    for filename in file_list:
        if os.path.isfile(filename):
            filename = name(filename)
            if not re.search('[^A-Za-z]', filename):
                c += 1
    return c


# эта функция выводит название всех функций или папок
def all_names():
    file_list = os.listdir()
    for filename in file_list:
        print(filename, end = '\n')


# эта функция главная
def main():
    print('Количество файлов, название которых состоит только из латинских символов, равно', count())
    all_names()


if __name__ == '__main__':
   main()
