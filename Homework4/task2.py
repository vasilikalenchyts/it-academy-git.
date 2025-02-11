# Города
# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
# в какой стране он находится.

my_dict = {}

for x in range(int(input())):
    country, *cities = input().split()
    my_dict[country] = cities

for y in range(int(input())):
    city = input()
    for country, cities in my_dict.items():
        if city in cities:
         print(country)