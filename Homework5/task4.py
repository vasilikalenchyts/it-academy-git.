# 4. Рекурсивное вычисление факториала: Реализуйте рекурсивную функцию для вычисления факториала числа.

def faktorial(n):
    if n <= 0:
        return 1
    else:
        return n * faktorial(n - 1)

f = faktorial(3)
print(f)