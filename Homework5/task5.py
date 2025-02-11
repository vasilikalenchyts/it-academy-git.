#  5. Замыкание для счетчика: Создайте функцию, которая возвращает другую функцию (счетчик),
#  увеличивающуюся при каждом вызове.

def counter(start = 0):
    def step():
        nonlocal start
        start += 1
        return start
    return step

count1 = counter(100)
count2 = counter(200)

print(count1(), count2())
print(count1(), count2())
print(count1(), count2())
print(count1(), count2())