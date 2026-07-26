# task 01 == Виправте синтаксичні помилки
print("Hello", end="\n")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(apples)
print(banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05 та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

"""
    Задачі 07 -10:
    Переведіть задачі з книги "Математика, 2 клас"
    на мову пітон і виведіть відповідь, так, щоб було
    зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
    У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
    Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plum = apples - 2
sum_trees = apples + pears + plum
print("Яблук:", apples, end="\n")
print("Груш:", pears, end="\n")
print("Слив:", plum, end="\n")
print("Всього дерев:", sum_trees, end="\n")

# task 08
"""
    До обіда температура повітря була на 5 градусів вище нуля.
    Після обіду температура опустилася на 10 градусів.
    Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
zero_temperature = 0
temperature_before_lunch = zero_temperature + 5
temperature_after_lunch = temperature_before_lunch - 10
temperature_evening = temperature_after_lunch + 4
print("Температура повітря до обіду:", temperature_before_lunch, end="\n")
print("Температура повітря після обіду:", temperature_after_lunch, end="\n")
print("Температура повітря надвечір:", temperature_evening, end="\n")

# task 09
"""
    Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
    1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
    Скількі сьогодні дітей у театральному гуртку?
"""
boys_in_theater_group = 24
girls_in_theater_group = boys_in_theater_group / 2
boys_in_theater_group_today = boys_in_theater_group - 1
girls_in_theater_group_today = girls_in_theater_group - 2
sum_boys_and_girls_today = boys_in_theater_group_today + girls_in_theater_group_today
print("Кількість дітей у театральному гуртку сьогодні:", int(sum_boys_and_girls_today))

# task 10
"""
    Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
    а третя - як половина вартості першої та другої разом.
    Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
sum_book = first_book + second_book + third_book
print("Перша книга", first_book)
print("Друга книга", second_book)
print("Третя книга", int(third_book))
print("Вартість всіх книг:", int(sum_book))
