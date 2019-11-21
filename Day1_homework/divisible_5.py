
numbers = list(int(i) for i in (input('выведу все числа кратные 5 из указанного (через пробел) диапазона \n').split(' ')))


for i in range(numbers[0],numbers[1]+1):
    if i % 5 == 0:
        print(i)
