# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа
# от 1 до 20, а значениями кубы этих чисел.

numbers = range(1, 21)
new_dict = {}

for n in numbers:
    new_dict[n] = n ** 3

print(new_dict)

numbers = range(1, 21)
new_dict = {n : n ** 3 for n in numbers}
print(new_dict)