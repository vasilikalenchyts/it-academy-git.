# 2. Декоратор времени: Напишите декоратор, который выводит время выполнения любой функции и ее аргументы.
# Так же сам декоратор может принимать аргумент seconds (если True то выводит время в секундах, если False
# то в минутах)2.

import time

def dec_time(func):
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        end_time = time.time()
        difference = end_time - initial_time
        resultat = func(*args, **kwargs)
        print(f'Время выполнения функции: {difference}')
        return resultat
    return wrapper

@dec_time
def euclid(a, b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
            return a

resultat = euclid(24, 48)
print(resultat)