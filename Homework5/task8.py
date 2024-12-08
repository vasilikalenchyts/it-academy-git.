# 8. Рекурсия для подсчета глубины списка: Напишите рекурсивную функцию, которая
# считает максимальную глубину вложенности вложенных списков.

def recursion_list(lst, depth = 1):
    max_depth = depth
    for x in lst:
        if type(x) is list:
            max_depth = max(max_depth, recursion_list(x, depth + 1))

    return max_depth

new_list = ['BMW', ['Opel', ['Nissan', ['123'], 'Mersedes'], 'Audi'], 'Susuki']
y = recursion_list(new_list)
print(y)