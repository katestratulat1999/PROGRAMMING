print('Welocme to Pig Latin!')
var = 'ay'
word = input('Enter a word: ')
if len(word) > 0 and word.isalpha():
    wordL = word.lower()
    firstL = wordL[0]
    new_word = wordL + firstL + var
    new_word = new_word[1:]
    print(new_word)
else:
    print('Sorry, enter a word: ')
