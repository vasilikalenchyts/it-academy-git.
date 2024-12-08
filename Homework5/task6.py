# 6. Замыкание для создания функций умножения:Создайте функцию, которая принимает
#  число и возвращает новую функцию, которая умножает свой аргумент на это число.

def multiplication(a):
    def new_func():
        nonlocal a
        b = 32
        res = a * b
        return res
    return new_func

x = multiplication(10)
print(x())