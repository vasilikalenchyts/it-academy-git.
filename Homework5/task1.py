# 1.1 Напишите генератор который отдает любые строки рандомным образом. (Механизм рандомайзера придумать самим)
# 1.2 Написать функцию, которая все эти слова запишет в txt файл отделяя каждое пробелом.

import random

def generator_random(x):
    str = ['Генератор', 'Рандом', 'Питон', 'Функция']

    for i in range(x):
        yield random.choice(str)

n = 3
sampling = ''.join(generator_random(3))

print(sampling)