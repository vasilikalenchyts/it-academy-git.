# 3 Tuple practice

# 3.1 Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.

def form_a_tuple(my_list):

    new_tuple = tuple(my_list)
    return new_tuple

my_list = ["a", "b", "c"]
print(form_a_tuple(my_list))

#3.2 Создайте кортеж ('a', 'b', 'c') и сделайте из него список.

def form_a_list(my_tuple):

    new_list = list(my_tuple)
    return new_list

my_tuple = ("a", "b", "c")
print(form_a_list(my_tuple))

#3.3 Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.

def change_list(my_list):

    my_list[0:3] = ["a", 2, "pyhton"]
    return my_list

my_list = ["a", "b", "c"]
print(change_list(my_list))

# 3.4 Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно
# выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.