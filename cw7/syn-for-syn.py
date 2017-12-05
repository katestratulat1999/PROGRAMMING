#чтоб вводилось слово Бездомный и выводились его синонимы
def get_synonims(target):
    with open('syn.txt',encoding='utf-8')as f:
        for line in f:
            splitted_line = line.split('#')
            word = splitted_line[0]
            syns = splitted_line[1]
            if word == target:
                return(syns)
print(get_synonims('Бездомный'))
