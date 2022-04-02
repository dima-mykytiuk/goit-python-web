from datetime import datetime

import faker
from random import randint
import sqlite3

NUMBER_TEACHERS = 3
NUMBER_STUDENTS = 30
MARKS = 20
GROUPS = [('KN-1-1',), ('KN-1-2',), ('KN-4-2',)]
SUBJECTS = ['Mathematics','Physics','Biology','History','Geography']
for_marks = []
fake_data = faker.Faker('ru-RU')
for _ in range(1000):
    for_marks.append(
        (randint(1, 30), randint(1, 5), randint(1, 5), fake_data.date_between_dates(date_start=datetime(2015, 1, 1))))


def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_students = []
    fake_teachers = []
    
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
    
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    return fake_students, fake_teachers


def prepare_data(students, teachers) -> tuple():
    for_students = []
    for_subjects = []
    for company in students:
        for_students.append((company, randint(1, 3)))
    
    tick = 0
    tock = 0
    for _ in range(len(SUBJECTS) + 1):
        if tick > len(SUBJECTS) + 1:
            break
        if tock == len(teachers):
            tock = 0
        else:
            for_subjects.append((SUBJECTS[tick], teachers[tock]))
            tick += 1
            tock += 1
    print(for_subjects)
    return for_students, for_subjects


def insert_data_to_db(students, groups, subject, marks) -> None:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        
        sql_to_groups = """INSERT INTO groupss(group_name)
                               VALUES (?)"""
        
        cur.executemany(sql_to_groups, groups)
        
        sql_to_students = """INSERT INTO students(student, group_id)
                               VALUES (?, ?)"""
        
        cur.executemany(sql_to_students, students)
        
        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_name)
                               VALUES (?, ?)"""
        
        cur.executemany(sql_to_subjects, subject)
        
        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, created_at)
                                       VALUES (?, ?, ?, ?)"""
        
        cur.executemany(sql_to_marks, marks)
        
        con.commit()


if __name__ == "__main__":
    students, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)
    students, subjects = prepare_data(students, subjects)
    insert_data_to_db(students, GROUPS, subjects, for_marks)
