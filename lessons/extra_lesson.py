import sqlite3
from pprint import pprint


def create_tables(conn):
    conn.execute("""DROP TABLE IF EXISTS students""")
    conn.execute("""DROP TABLE IF EXISTS courses""")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )""")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT,
        course_id INTEGER,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )""")



def add_courses(conn, courses):
    for course in courses:
        conn.execute("""INSERT INTO courses (name) VALUES (?)""", course)
    conn.commit()


def add_students(conn, students):
    for student in students:
        conn.execute(
            """INSERT INTO students (name, age, city, course_id) VALUES (?, ?, ?, ?)""",
            student,
        )
    conn.commit()

def get_student_by_courseid(conn, course_id):
    result = conn.execute("""
    SELECT * FROM students WHERE course_id = ?
    """,
    (course_id,)
    )
    return result.fetchall()


def get_students_by_course_name(conn, course_name):
    result = conn.execute("""
    SELECT s.id, s.name, c.name FROM students AS s
    JOIN courses AS c ON s.course_id = c.id
    WHERE c.name = ?
    """,
    (course_name,)
    )
    return result.fetchall()


if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    # Создание таблиц
    create_tables(connection)

    # Добавление курсов
    courses_ = [("фронтенд",), ("бекенд",), ("мобильная разработка",)]
    add_courses(connection, courses_)

    # Добавление студентов
    students_ = [
        # Студенты на курсе "фронтенд" (course_id = 1)
        ("Айгуль", 22, "Бишкек", 1),
        ("Бекзат", 20, "Ош", 1),
        ("Гульмира", 24, "Каракол", 1),
        # Студенты на курсе "бекенд" (course_id = 2)
        ("Данияр", 25, "Бишкек", 2),
        ("Эльмира", 23, "Нарын", 2),
        # Студенты на курсе "мобильная разработка" (course_id = 3)
        ("Жанар", 21, "Бишкек", 3),
        ("Канат", 26, "Ош", 3),
        ("Нурай", 22, "Талас", 3),
    ]
    add_students(connection, students_)

    # pprint(get_student_by_courseid(connection,1))

    students_2 = get_students_by_course_name(connection, "бекенд")
    pprint(students_2)