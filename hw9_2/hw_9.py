import os
import re


def read_text(filename):
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text

def check(word):
    raw = re.findall(r'(\bси[дж][ияу]\w*)|(\bсиде[^н]\w*)', word) 
    match = []
    res = []
    if raw:
        for tup in raw:
            match.append(''.join(tup))
        for i in range(len(match)):
            if match.count(match[i]) == 1 or match.index(match[i]) == i:
                res.append(match[i])
        return res
    return False

def main():
    filename = input('Введите имя файла с расширением: ')
    while not os.path.exists(filename):
        filename = input('Нет файла с таким названием. Введите заново: ')
    text = read_text(filename).lower()
    res = check(text)
    print('Формы глагола "сидеть", найденные в тексте: ')
    print(', '.join(res))


if __name__ == '__main__':
   main()
