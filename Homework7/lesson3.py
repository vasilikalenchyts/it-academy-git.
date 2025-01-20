# Учитывая массив целых чисел nums и целое число target, верните индексы
# этих двух чисел так, чтобы их сумма равнялась target.


# Решение №1
def sum_numbers(nums, target):
    my_dict = {}
    for i, number in enumerate(nums):
        if number in my_dict:
            return my_dict[number], i
        difference = target - number
        my_dict[difference] = i

result = sum_numbers([2, 12, 11, 7], 14)
print(result)


# Решение №2
def sum_numbers(nums, target):
    my_dict = {}

    for i, number in enumerate(nums):
        value = target - number
        if value in my_dict:
            return i, my_dict[value]

        my_dict[number] = i


result = sum_numbers([2, 12, 11, 7], 14)
print(result)


# Решение №3
def sum_numbers(nums, target):
    for i, number in enumerate(nums):
        for x in range(i + 1, len(nums)):
            if number + nums[x] == target:
                return i, x


result = sum_numbers([2, 12, 11, 7], 14)
print(result)