import sqlite3


def db_connect(sql):
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# 5 студентов с наибольшим средним баллом по всем предметам.
def five_students_greatest_avg() -> list:
    sql = """
    SELECT s.student, AVG(m.mark), g.group_name
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN groupss g ON g.id = s.group_id
    GROUP BY s.student
    ORDER BY -AVG(m.mark)
    LIMIT 5
    """
    return db_connect(sql)


# 1 студент с наивысшим средним баллом по одному предмету.
def one_student_greatest_mark_one_subj() -> list:
    sql = """
    SELECT a.subject_name, s.student, AVG(m.mark)
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects a ON a.id = m.subject_id
    GROUP BY a.subject_name """
    return db_connect(sql)


# средний балл в группе по одному предмету.
def group_avg_marks_one_subj() -> list:
    sql = """
    SELECT a.subject_name, AVG(m.mark), g.group_name
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects a ON a.id = m.subject_id
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    GROUP BY a.subject_name
    """
    return db_connect(sql)


# Средний балл в потоке.
def avg_marks_thread() -> list:
    sql = """
    SELECT AVG(m.mark) AS average_mark_for_all_groups
    FROM marks m
    """
    return db_connect(sql)


# Какие курсы читает преподаватель.
def teachers_subject() -> list:
    sql = """
    SELECT s.subject_name, s.teacher_name
    FROM subjects s
    GROUP BY s.subject_name
    """
    return db_connect(sql)


# Список студентов в группе.
def students_group() -> list:
    sql = """
    SELECT s.student, g.group_name
    FROM students s
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    GROUP BY s.student
    """
    return db_connect(sql)


# Оценки студентов в группе по предмету.
def students_marks_subjects() -> list:
    sql = """
    SELECT s.student, a.subject_name, m.mark, g.group_name
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects a ON a.id = m.subject_id
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    ORDER BY s.student
    """
    return db_connect(sql)


# Оценки студентов в группе по предмету на последнем занятии..
def last_lesson_marks() -> list:
    sql = """
    SELECT s2.subject_name, s.student, m.mark, MAX(m.created_at) AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects s2 ON s2.id = m.subject_id
	GROUP BY s.student
	ORDER BY m.created_at desc
	"""
    return db_connect(sql)


# Список курсов, которые посещает студент.
def students_courses() -> list:
    sql = """
    SELECT s.student, s2.subject_name, m.created_at AS Visited
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects s2 ON s2.id = m.subject_id
	ORDER BY s2.id, -m.created_at
	"""
    return db_connect(sql)


# Список курсов, которые студенту читает преподаватель.
def courses_student_teachers() -> list:
    sql = """
    SELECT s2.subject_name, s.student, s2.teacher_name, m.created_at AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id  = s.id
	LEFT JOIN subjects s2 ON s2.id = m.subject_id
	LEFT JOIN groupss g ON g.id = s.group_id
	ORDER BY s.student, m.created_at DESC
	"""
    return db_connect(sql)


# Средний балл, который преподаватель ставит студенту.
def avg_mark_student_by_teacher() -> list:
    sql = """
    SELECT s2.student, s.teacher_name, s.subject_name, AVG(m.mark)
    FROM marks m
    LEFT JOIN subjects s ON s.id = m.subject_id
    LEFT JOIN students s2 ON s2.id = m.student_id
    WHERE m.subject_id = 2
    GROUP BY m.student_id
    """
    return db_connect(sql)


# Средний балл, который ставит преподаватель.
def avg_mark_by_teacher() -> list:
    sql = """
    SELECT AVG(m.mark), s.subject_name, s.teacher_name
    FROM marks m
    LEFT JOIN subjects s ON s.id = m.subject_id
    GROUP BY s.subject_name
    """
    return db_connect(sql)


if __name__ == '__main__':
    # print(five_students_greatest_avg())  # +++
    # print(one_student_greatest_mark_one_subj())  # +++++++++
    # print(group_avg_marks_one_subj())  # +++++
    # print(avg_marks_thread())  # +++++++++++++
    # print(teachers_subject())  # +++++++++++++
    # print(students_group())    # +++++++++++++
    # print(students_marks_subjects())  # ++++++
    # print(last_lesson_marks())  # ++++++++++++
    # print(students_courses())  # +++++++++++++
    # print(courses_student_teachers())  # +++++
    # print(avg_mark_student_by_teacher())  # ++
    # print(avg_mark_by_teacher())  # ++++++++++
