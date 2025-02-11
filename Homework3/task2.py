# 2	List practice

# 2.1 Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

def generator_list(my_list):

    y = [x for x in my_list]
    return y

my_list = ["ab", "ac", "ad", "bb", "bc", "bd"]
print(generator_list(my_list))

# 2.2 Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].

def sl_list(my_list):

    slice = my_list[0:5:2]
    return slice

my_list = ["ab", "ac", "ad", "bb", "bc", "bd"]
print(sl_list(my_list))

#2.3 Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].

def generator_list(my_list):

    y = [x for x in my_list]
    return y

my_list = ["1a", "2a", "3a", "4a"]
print(generator_list(my_list))

# 2.4 Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.

def delete_element(new_list):

    new_list.pop(1)
    return new_list

new_list = ["1a", "2a", "3a", "4a"]
print(delete_element(new_list))

# 2.5 Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было

def add_element(new_list):

    add = new_list.insert(1, "2a")
    add = new_list
    return add

new_list = ["1a", "3a", "4a"]
print(add_element(new_list))