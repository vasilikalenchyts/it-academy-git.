# Оглянемся назад. Числа
# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида.

def alg_euclid(x, y):
    if x == 0:
        return y
    return alg_euclid(y % x, x)

result = alg_euclid(30, 18)

print(result)