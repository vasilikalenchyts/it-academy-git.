# 1.	FizzBuzz
# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz

my_list = []
new_list = []

for x in range(1, 101):

    if x % 3 == 0 and x % 5 == 0:
        new_list.append("FizzBuzz")

    elif x % 3 == 0:
        new_list.append("Fizz")

    elif x % 5 == 0:
        new_list.append("Buzz")

    else:
        new_list.append(x)

print(new_list)



def Fizzbuzz(my_list):
    new_list = [
        ("FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x)
    for x in my_list]

    print(new_list)

new_list = range(1, 101)
Fizzbuzz(new_list)