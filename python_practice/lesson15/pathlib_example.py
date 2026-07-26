import pathlib
from constants import BASE_PROJECT_PATH
import os

base_path = pathlib.Path(BASE_PROJECT_PATH)

current_dir = pathlib.Path().absolute()
print(type(current_dir))  # <class 'pathlib.PosixPath'>
print(
    current_dir)  # поевртає абсолютний шлях до фолдеру "/Users/demianvyrozub/PycharmProjects/hillel2026/python_practice/automation_course_2026/lesson15"
print(current_dir.name)  # lesson15
print(current_dir.parent)  # /Users/demianvyrozub/PycharmProjects/hillel2026/python_practice/automation_course_2026

parents = current_dir.parents

# Виводить багатьох паретнів: automation_course_2026 python_practice hillel2026 PycharmProjects demianvyrozub Users
for par in current_dir.parents:
    print(par.name)

# Повертає файли всередині папки якої ми знаходимось
for path_ in current_dir.iterdir():
    if path_.is_file:
        print(path_.name)

    # Перевірка чи це директорія
for path_ in current_dir.iterdir():
    if path_.is_dir:
        print(path_.name)

for path_ in base_path.iterdir():
    if path_.is_file:
        print(path_.name)

    # Перевірка чи це директорія
for path_ in base_path.iterdir():
    if path_.is_dir:
        print(path_.name)

# Шукаємо файл
lesson4_full_path = os.path.join(BASE_PROJECT_PATH, "lesson4")
print(lesson4_full_path)

# Full path до файлу
lesson4_full_path = os.path.join(str(current_dir.parent), "lesson4")
print(lesson4_full_path)

# Всередині lesson4
for path_ in pathlib.Path(lesson4_full_path).iterdir():
    if path_.is_file:
        print(path_.name)

    # Перевірка чи це директорія у середині вже lesson4
for path_ in pathlib.Path(lesson4_full_path).iterdir():
    if path_.is_dir:
        print(path_.name)

# Метод який дозволяє пройтись по всім елементам проекту в корневій папці: повертає список туплів
file_to_find = "join_example.py"

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    if file_to_find in files:
        print(os.path.join(current_path, file_to_find))
