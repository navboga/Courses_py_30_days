#задаем пользователю вопросы, проверяем ответы выводим результат и общие данные

all_user_response_list = ('Назовите столицу Рф?','Назовите не летающую птицу','Назовите страну которой правит Король','На каком языке разговаривают в Финляндии','Как называется подземный транспорт')
all_right_answer=('Москва','курица','Испания','Финский','Метро')
# # print(user_response)
cnt_ask=0
wrong_answer=0
correct_answer=0

while len(all_user_response_list) > cnt_ask:
    user_response = input('{} \n'.format(all_user_response_list[cnt_ask])).lower()
    if (all_right_answer[cnt_ask]).lower() == user_response:
        correct_answer+=1
        print('Поздравляю Ответ {} верный!'.format(user_response))
    else:
        wrong_answer +=1
        print('Очень жаль ответ {} не верный!'.format(user_response.capitalize()))
    cnt_ask += 1


print('верных ответов: {} \nне верных ответов: {}'.format(correct_answer,wrong_answer))