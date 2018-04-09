#вариант4
#статьи об учёных (напр., Эйнштейн, Альберт) — научная сфера

import re
import os


#считывает файл
def read_text(filename):
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


#проверяет существование файла с заданным именем
def check_file(filename):
    return os.path.exists(filename)



#возвращает первую научную сферу учёного, указанную в карточке
def search(text):
        match = re.search('Научная сфера</th><td>\n(.*?)title="(.*?)"', text)
        if match:
            return match.group(2)
        return False


#создаёт файл, в который записывает ответ
def write_ans(res):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(res)


#главная функция
def main():
    filename = input('Введите имя файла c расширением: ')
    while not check_file(filename):
        filename = input('Нет файла с таким названием. Повторите попытку: ')
    text = read_text(filename)
    res = search(text)
    if not res:
        res = 'Статья не соответсвует нужному формату.'
    write_ans(res)

if __name__ == '__main__':
   main()
