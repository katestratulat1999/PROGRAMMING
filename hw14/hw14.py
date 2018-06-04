#вариант4

import re


def readtext(filename):
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def del_empty(words):
    while '' in words:
        words.remove('')
    return words


def punct(text):
    words = re.split(r'[\s.,()—:`;"-*&!?\'“”]+', text)
    del_empty(words)
    return words


def main():
    sentences = [lst for lst in [(punct(sentence), sentence)
                    for sentence in re.split(r'(\.+|[?!])', readtext("text.txt"))] if len(lst[0]) > 0]
    result_dict = {sentence : {word : len(word) for word in punct_sentence} for punct_sentence, sentence in sentences}
    print('Результат:\n%s' % result_dict)


if __name__ == "__main__":
    main()
