import sqlite3
from pprint import pprint


def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students (city, name, age)
    VALUES (?, ?, ?)
    """,
    (city, name, age)
    )
    conn.commit()


def get_students(conn):
    # result = conn.execute("""
    # SELECT name, city FROM students LIMIT 1
    # """)
    result = conn.execute("""
    SELECT * FROM students 
    """)
    # return result.fetchone()
    return result.fetchall()


def get_student_by_id(conn, id, city):
    result = conn.execute("""
    SELECT * FROM students WHERE id = ? OR city = ?
    """,
    (id, city)
    )
    # "SELECT * FROM students WHERE city IN ('Bishkek', 'Karakol')"
    # "SELECT * FROM students WHERE age >= 18 AND age <= 20"
    return result.fetchall()

def delete_student_by_id(conn, id):
    conn.execute("""
    DELETE FROM students WHERE id = ?
    """,
    (id,))
    conn.commit()

def update_student(conn, id, name, age, city):
    conn.execute("""
    UPDATE students SET 
    name = ?, 
    age = ?,
    city = ? WHERE id = ?
    """,
    (name, age, city, id)
    )
    conn.commit()

if __name__ == '__main__':
    connection = sqlite3.connect('database.db')
    create_tables(connection)
    # insert
    add_student(connection, 'Igor', 30, 'Bishkek')
    add_student(connection, 'Kurmanbek', 20, 'Bishkek')

    # select
    pprint(get_students(connection))

    # select one
    student = get_student_by_id(connection, 2, 'Bishkek')
    print(student)

    # delete
    delete_student_by_id(connection, 1)
    pprint(get_students(connection))

    # update
    update_student(connection, 2, 'Ilgiz', 20, 'Bishkek')
    pprint(get_students(connection))

    connection.close()