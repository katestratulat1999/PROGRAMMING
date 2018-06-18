#вариант7
#эта программа выдаёт список названий папок и файлов, которые содержат латинские и кириллические символы

import os
import re

def checkDir(list):
    listToStr = ' '.join(list)
    match = re.findall(r'(\b\d*[a-zA-Z]+\d*[а-яА-яЁё]\w*)|(\b\d*[а-яА-яЁё]+\d*[a-zA-Z]+\w*)', listToStr)
    res = []
    if match:
        for tup in match:
            res.append(''.join(tup))
        return res
    return False

def main():
    l = os.listdir();
    res = checkDir(l)
    if res:
        print("Папки и файлы, которые содержат латинские и кириллические символы: ")
        print(", ".join(res))

if __name__ == '__main__':
   main()

#P.S. программа hw12_1 тоже работает, но она немного другая
