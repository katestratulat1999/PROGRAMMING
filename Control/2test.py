with open('Ozhegov.txt', encoding='utf-8') as f:
    #text = f.read()
    #text = text.split('\n')
    a = 0
    for line in f:#text:
        word = line.split('|')
        #leng = word[0].split(' ')
        if len(word) >= 3:
            if word [2]!='':
                a+=1
    print('Кол-во антонимов:',a)
        
