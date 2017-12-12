with open('Ozhegov.txt', encoding='utf-8') as f:
    #text = f.read()
    #text = text.split('\n')  
    for line in f:#text:
        word = line.split('|')
        #leng = word[0]#.split(' ')
        if len(word[0]) >= 20:
            print(line)
