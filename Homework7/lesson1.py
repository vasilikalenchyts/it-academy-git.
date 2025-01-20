# 1. Вам дано большое целое число, представленное в виде целочисленного массива digits,
# где каждая digits[i] - это i-я цифра целого числа. Цифры упорядочены от наибольшего
# значения к наименьшему в порядке слева направо. Большое целое число не содержит лидирующих 0.
# Увеличьте большое целое число на единицу и верните полученный массив цифр.


# Решение №1
def sum(digits):
    return [int(number) for number in str((int("".join([str(number) for number in digits])) + 1))]
result = sum([9])
print(result)


# Решение №2
def sum(digits):
    num_str = "".join([str(number) for number in digits])
    value = int(num_str)
    new_value = value + 1
    new_value_str = str(new_value)
    return [int(number) for number in new_value_str]

result = sum([4, 3, 2, 1])
print(result)





