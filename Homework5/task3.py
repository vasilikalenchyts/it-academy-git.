# 3 Декоратор для проверки типов аргументов: Создайте декоратор, который проверяет,
# что переданные функции аргументы соответствуют указанным типам.

def dec_check(arg):
    def wrapper(x):
            if type(x) == int:
                return 'Аргумент является числом'
            else:
                return 'Аргумент не является числом'
    return wrapper

@dec_check
def decarator(x):
    return x

my_int = decarator('BMW')
print(my_int)