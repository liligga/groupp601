import sqlite3


def create_tables(conn):
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
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """,
    (name, age, city)
    )
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_tables(conn)
    add_student(conn, 'Igor', 30, 'Bishkek')
    add_student(conn, 'Kurmanbek', 20, 'Bishkek')