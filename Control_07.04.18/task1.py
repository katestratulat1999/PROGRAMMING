#вариант1
#задание1

import re

# эта функция считывает файл
def read_file():
    with open('mystem.xml', encoding = 'utf-8') as f:
        file = f.read()
    return file

#считает число строк внутри тега se
def count_se(file):
    i = 0
    with open('result.txt', 'w', encoding = 'utf-8') as f:
        count_se = re.findall(r'<se>.*</se>?', file)
        for se in count_se:
            se = se.split('<se>\n')
            for line in element:
                i += 1
        f.write(str(i))
    return

#эта функция главная 
def main():
    file = read_file()
    count_se(file)
    return

main()


