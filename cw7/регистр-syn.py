#чтоб преобр. в нижний регистр
def get_synonims(target):
    target = target.capitalize()
    with open('syn.txt',encoding='utf-8')as f:
        for line in f:
            splitted_line = line.split('#')
            word = splitted_line[0]
            syns = splitted_line[1]
            if word == target:
                return(syns)
target = input()
print(get_synonims(target))
