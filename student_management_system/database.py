import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        course TEXT NOT NULL,
        year INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_student(name, email, course, year):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email, course, year) VALUES (?, ?, ?, ?)",
        (name, email, course, year)
    )

    conn.commit()
    conn.close()


def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students  

def update_student(student_id, name, email, course, year):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, email = ?, course = ?, year = ?
    WHERE id = ?
    """, (name, email, course, year, student_id))

    conn.commit()
    conn.close() 

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close() 

def get_student_by_id(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    conn.close()
    return student 
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close() 

