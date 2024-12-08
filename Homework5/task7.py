# 7. Декоратор для ограничения числа вызовов: Реализуйте декоратор, который ограничивает
# количество вызовов функции определенным числом.

def decarator_limit(func):
    counter = 0
    def wrapper(x, y):
        nonlocal counter
        if counter < 2:
            counter += 1
            solution = x * y
            return solution
        else:
            return "Количество вызовов функции ограничено"
    return wrapper

@decarator_limit
def multiplication(x, y):
    return x, y

res1 = multiplication(2, 5)
res2 = multiplication(4, 9)
res3 = multiplication(7, 7)


print(res1)
print(res2)
print(res3)