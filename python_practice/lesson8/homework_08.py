''''Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.'''


class Student:

    def __init__(self, name, second_name, age):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gpa = 0

    def change_gpa(self, value):
        self.gpa = value


student = Student('Oleksandr', 'QA', 34)
student.change_gpa(3)
print(f"Student name: {student.name}")
print(f"Student second name: {student.second_name}")
print(f"Student age: {student.age}")
print(f"Student Grade point average: {student.gpa}")
