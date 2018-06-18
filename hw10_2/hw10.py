#вариант4

import os
import re

def readFile(fname):
    rfile = open(fname, 'r', encoding='utf-8')
    txt = rfile.read()
    rfile.close()
    return txt

def search(txt):
    pattern = re.compile(r'Научная сфера</th><td>\n(.*?)title="(.*?)"')    
    match = pattern.search(txt)
    if match:
        return match.group(2)
    return False

#запись результата в файл
def resToFile(txt):
    wfile = open("searchResult.txt", "w", encoding="utf-8")
    wfile.write(txt)

def main():
    fileName = input('Введите имя файла для обработки: ')
    fileName += ".html"
    while not os.path.exists(fileName):
        f = input('Нет файла с таким названием. Повторите попытку: ')
    text = readFile(fileName)
    result = search(text)
    if not result:
        result = 'Совпадений не найдено. Проверьте формат статьи.'
    resToFile(result)

if __name__ == '__main__':
   main()
