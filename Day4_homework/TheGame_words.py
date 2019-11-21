import string
import random

print( "Let's play word games")
words = []
USER_LEN_WORDS= int(input('Whot length word are you want?, \n'))
for letter in range(USER_LEN_WORDS):
    words.append(random.choice(string.ascii_lowercase))

LEN=len(words)
words_ask = ['_']*LEN
MAX_TRY=LEN+3
print('-'*LEN)
print('You have {} try'.format(MAX_TRY))

INDEX_TRY=0
INDEX_CHAR=0
def FIND_CHAR(wrd_comp,position=0):
    for num in range(wc):
        IDX = wrd_comp.index(CHARACTER, position)
        words_ask[IDX] = CHARACTER
        position = IDX+1
    return  words_ask

while INDEX_TRY < MAX_TRY:
    CHARACTER = input()
    wc = words.count(CHARACTER)

    if CHARACTER in words:
        words_ask=FIND_CHAR(words)
        INDEX_TRY += 1
        print(*words_ask)
        print('TRY number :{}'.format(INDEX_TRY))
        if words == words_ask:
            print('Congratulations you guessed the word!!!')
            break
        if INDEX_TRY ==MAX_TRY:
            print('YOU LOSE, whe word is: ',*words, sep='')
            break
    else:
        INDEX_TRY += 1
        print('Not this time, letter in absence in this word')
        print('TRY number :{}'.format(INDEX_TRY))

        if INDEX_TRY ==MAX_TRY:
            print('YOU LOSE, whe word is: ',*words, sep='')
            break








