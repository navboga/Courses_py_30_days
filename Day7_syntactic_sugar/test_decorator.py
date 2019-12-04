def war_decorator(func):
    def all_weapon(text):
        print('Best weapon has name :')
        func(text)
    return all_weapon



@war_decorator
def blade(name):
    print('{} !!!'.format(name.upper()))

@war_decorator
def gun(name):
    print('{} Hahaha'.format(name.upper()))


def genre(name):
    print('{} :-)'.format(name.upper()))

test=war_decorator(genre)

if __name__ == '__main__':
    blade('Excalibur')
    print('*'*10)
    gun('Kalashnikov')
    print('*'*10)
    genre('Theater')
    print('*'*10)

    test('enjoy')



def return_min():
    return min

s=return_min()

print(s(5,9,11,2,16))