# Задав римскую цифру, преобразуйте ее в целое число.
# s = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

# Решение №1
def converting_numbers(s):

    my_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    result = 0
    for i in range(len(s)):
        if i < len(s) - 1 and my_dict[s[i]] < my_dict[s[i + 1]]:
            result -= my_dict[s[i]]
        else:
            result += my_dict[s[i]]

    return result

s = converting_numbers("MCMLXXX")
print(s)


# Решение №2
def converting_numbers(s):

    my_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and my_dict[s[i]] < my_dict[s[i + 1]]:
            result -= my_dict[s[i]]
        else:
            result += my_dict[s[i]]

    return result

s = converting_numbers("MCMLXXX")
print(s)
