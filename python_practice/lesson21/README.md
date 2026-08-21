# Lesson 21 — Система управління студентами (SQLAlchemy ORM)

## Задача

Модель даних: студенти, курси та їх відношення (багато до багатьох).
5 курсів, 20 студентів, розподілених рандомно.

1. Додавання нового студента та запис його на курс
2. Запити: студенти певного курсу / курси певного студента
3. Оновлення та видалення даних

## Файли

- `models.py` — моделі `Student`, `Course`, проміжна таблиця `student_course`, engine та Session
- `seed.py` — створює таблиці, 5 курсів і 20 студентів з рандомним розподілом
- `homework_21.py` — пункти 1–3 задачі

## Підготовка

```bash
pip install SQLAlchemy psycopg2-binary
createdb university
```

## Запуск

```bash
python seed.py          # заповнити базу
python homework_21.py   # виконати пункти 1-3
```

`seed.py` можна запускати повторно — він спочатку видаляє таблиці (`drop_all`).

## Структура

```
students            student_course           courses
--------            --------------           -------
id (PK)      <----  student_id (FK, PK)
name                course_id  (FK, PK)  ---->  id (PK)
email (UNIQUE)                                  title (UNIQUE)
age                                             teacher
```

Відношення "багато до багатьох" реалізовано через `relationship(secondary=...)`
з `back_populates`, тому `student.courses` і `course.students` працюють в обидва боки.
