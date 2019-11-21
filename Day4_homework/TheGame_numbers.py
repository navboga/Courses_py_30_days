import random
print('I want you to guess a number between one and ten')
NUMB=random.randint(1,11)
SEQ_TRY=0
MAX_TRY =5
USER_INPUT=None
SEQ_TRY =0

while SEQ_TRY < MAX_TRY:
    SEQ_TRY += 1
    GOOD_TRY=True
    try:
         USER_INPUT =int(input('try to guess number which thinking computer, input the number: \n'))
    except ValueError:
        SEQ_TRY -= 1
        GOOD_TRY=False
        print('Wrong input!!!Please input the number')
    if USER_INPUT==NUMB:
        print('CONGRATULATIONS you guessed the number')
        SEQ_TRY =6
        break
    else:
        #SEQ_TRY +=1
        if GOOD_TRY:
            print('try number {}, Max try count: {}'.format(SEQ_TRY,MAX_TRY))
        else:
            print('Last try was wrong,please try again. Max try count: {}'.format(MAX_TRY))
        if SEQ_TRY==5:
            print('YOU LOSE')

print('The hidden number was {}'.format(NUMB))