import sqlite3

db = sqlite3.connect('mydatabase.db')

students = db.cursor()

#students.execute('CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, age INT, grade TEXT);')
#students.execute('INSERT INTO students (Id, name, age, grade) VALUES (990633088, "Rustam", 17, "Litsey")')

#students.execute('CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, age INT, grade TEXT);')
#students.execute('INSERT INTO students (Id, name, age, grade) VALUES (990633045, "Dima", 18, "Cool")')




db.commit()


def get_students_by_name():
    a = input('введите имя студента: ')
    if a == 'Rustam':
        t1 = students.execute('SELECT * FROM students WHERE name = "Rustam";')
        db.commit()
        print(t1.fetchone())
    elif a == 'Dima':
        t2 = students.execute('SELECT * FROM students WHERE name = "Dima";')
        db.commit()
        print(t2.fetchone())
    else:
        print('ERROR')


def update_student_grade():
    g = input('введите имя студенту которому хотите поставить оценку: ')
    if g.lower == 'Rustam':
        t3 = students.execute('UPDATE students SET grade = "Litsey" WHERE grade = "Good"')
        db.commit()
        print(t3.fetchone())
    elif g.lower == 'Dima':
        t6 = students.execute('UPDATE students SET grade "Cool" WHERE grade = "Bad"')
        db.commit()
        print(t6.fetchone())


    def delete_student():
        c = input('введите имя студента для удаления: ')
        if c.lower() == 'Rustam':
            t4 = students.execute('DELETE FROM students WHERE name = "Rustam";')
            db.commit()
            print(t4.fetchone())
        elif c.lower() == 'Dima':
            t5 = students.execute('DELETE FROM students WHERE name = "Dima";')
            db.commit()
            print(t5.fetchone())
        else:
            print('ERROR')


while True:
    b = input('введите name, grade, delete для запуска: ')
    if b.lower() == 'name':
        get_students_by_name()
    elif b.lower() == 'grade':
        update_student_grade()
    elif b.lower() == 'delete':
        delete_student()
    else:
        print('повторите попытку')




