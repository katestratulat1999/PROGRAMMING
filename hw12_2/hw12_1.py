#вариант7
#эта программа подсчитывает количество папок, название которых содержит и кириллические, и латинские символы

import os
import re

def checkDir(list):
    num = 0;
    for item in list:
        match = re.search(r'(\b\w*\W*[a-zA-Z]+\w*\W*[а-яА-яЁё]\w*)|(\b\w*\W*[а-яА-яЁё]+\w*\W*[a-zA-Z]+\w*)', item)
        if match:
            num +=1
    return num

def main():
    l = os.listdir();
    res = checkDir(l)
    if res:
        print("Количество папок, название которых содержит и кириллические, и латинские символы: ")
        print(res)

if __name__ == '__main__':
   main()

#P.S. программа hw12_2 тоже работает, но она немного другая
