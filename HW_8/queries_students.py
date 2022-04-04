import sqlite3


def db_connect(sql):
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


""""
5 students with the highest AVG mark in all subjects.
"""


def get_five_students_by_mark() -> list:
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


""""
1 student with the highest AVG mark in one subject.
"""


def get_one_student_by_mark() -> list:
    sql = """
    SELECT sb.subject_name, s.student, AVG(m.mark)
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


""""
AVG mark in the group in one subject.
"""


def get_group_avg_mark_by_subject() -> list:
    sql = """
    SELECT sb.subject_name, AVG(m.mark), g.group_name
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


""""
AVG mark in all groups.
"""


def get_all_groups_avg_mark() -> list:
    sql = """
    SELECT AVG(m.mark) AS average_mark_for_all_groups
    FROM marks m
    """
    return db_connect(sql)


"""
What courses does the teacher teach.
"""


def get_courses_by_teachers() -> list:
    sql = """
    SELECT sb.subject_name, sb.teacher_name
    FROM subjects sb
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


"""
List of students in the group.
"""


def get_students_by_group() -> list:
    sql = """
    SELECT s.student, g.group_name
    FROM students s
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    GROUP BY s.student
    """
    return db_connect(sql)


"""
Grades of students in the group on the subject.
"""


def get_students_marks_by_subject() -> list:
    sql = """
    SELECT s.student, sb.subject_name, m.mark, g.group_name
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    ORDER BY s.student
    """
    return db_connect(sql)


"""
Grades of students in the group on the subject at the last lesson.
"""


def get_last_student_mark() -> list:
    sql = """
    SELECT sb.subject_name, s.student, m.mark, MAX(m.created_at) AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	GROUP BY s.student
	ORDER BY m.created_at desc
	"""
    return db_connect(sql)


"""
List of courses the student is attending.
"""


def get_courses_attendance_by_students() -> list:
    sql = """
    SELECT s.student, sb.subject_name, m.created_at AS Visited
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	ORDER BY sb.id, -m.created_at
	"""
    return db_connect(sql)


"""
List of courses that the teacher reads to the student.
"""


def get_courses_teacher_reads_by_students() -> list:
    sql = """
    SELECT sb.subject_name, s.student, sb.teacher_name, m.created_at AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id  = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	LEFT JOIN groupss g ON g.id = s.group_id
	ORDER BY s.student, m.created_at DESC
	"""
    return db_connect(sql)


"""
AVG mark given by the teacher to the student.
"""


def get_avg_mark_for_student_by_teacher() -> list:
    sql = """
    SELECT s.student, sb.teacher_name, sb.subject_name, AVG(m.mark)
    FROM marks m
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    LEFT JOIN students s ON s.id = m.student_id
    WHERE m.subject_id = 2
    GROUP BY m.student_id
    """
    return db_connect(sql)


"""
AVG mark given by the teacher.
"""


def get_avg_mark_by_teacher() -> list:
    sql = """
    SELECT AVG(m.mark), sb.subject_name, sb.teacher_name
    FROM marks m
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


if __name__ == '__main__':
    print(get_five_students_by_mark())
    print(get_one_student_by_mark())
    print(get_group_avg_mark_by_subject())
    print(get_all_groups_avg_mark())
    print(get_courses_by_teachers())
    print(get_students_by_group())
    print(get_students_marks_by_subject())
    print(get_last_student_mark())
    print(get_courses_attendance_by_students())
    print(get_courses_teacher_reads_by_students())
    print(get_avg_mark_for_student_by_teacher())
    print(get_avg_mark_by_teacher())
