# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников

N = int(input("Введите количество школьников: "))
language_all_studens = set()
language_one_student = set()

for x in range(N):
    Mi = int(input("Введите количество языков, которые знает " + str(x + 1) + " школьник: "))

languages = set()
for y in range(Mi):
    language = input("Введите название " + str(y + 1) + "-го языка: ")
    languages.add(language)
    language_one_student.update(languages)
    if x == 0:
        language_all_studens.update(languages)
    else:
        language_all_studens.intersection_update(languages)

print("Языки, которые знают все школьники:", language_all_studens)
print("Языки, которые знает хотя бы один школьник:", language_one_student)