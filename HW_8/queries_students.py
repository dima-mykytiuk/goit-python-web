import sqlite3


def db_connect(sql):
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# 5 студентов с наибольшим средним баллом по всем предметам.
def query_one() -> list:
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
def query_two() -> list:
    sql = """
    SELECT sb.subject_name, s.student, AVG(m.mark)
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


# средний балл в группе по одному предмету.
def query_three() -> list:
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


# Средний балл в потоке.
def query_four() -> list:
    sql = """
    SELECT AVG(m.mark) AS average_mark_for_all_groups
    FROM marks m
    """
    return db_connect(sql)


# Какие курсы читает преподаватель.
def query_five() -> list:
    sql = """
    SELECT sb.subject_name, sb.teacher_name
    FROM subjects sb
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


# Список студентов в группе.
def query_six() -> list:
    sql = """
    SELECT s.student, g.group_name
    FROM students s
    LEFT JOIN groupss g ON g.id = s.group_id
    WHERE s.group_id = 1
    GROUP BY s.student
    """
    return db_connect(sql)


# Оценки студентов в группе по предмету.
def query_seven() -> list:
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


# Оценки студентов в группе по предмету на последнем занятии..
def query_eight() -> list:
    sql = """
    SELECT sb.subject_name, s.student, m.mark, MAX(m.created_at) AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	GROUP BY s.student
	ORDER BY m.created_at desc
	"""
    return db_connect(sql)


# Список курсов, которые посещает студент.
def query_nine() -> list:
    sql = """
    SELECT s.student, sb.subject_name, m.created_at AS Visited
    FROM students s
	LEFT JOIN marks m ON m.student_id = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	ORDER BY sb.id, -m.created_at
	"""
    return db_connect(sql)


# Список курсов, которые студенту читает преподаватель.
def query_ten() -> list:
    sql = """
    SELECT sb.subject_name, s.student, sb.teacher_name, m.created_at AS DateOfLection
    FROM students s
	LEFT JOIN marks m ON m.student_id  = s.id
	LEFT JOIN subjects sb ON sb.id = m.subject_id
	LEFT JOIN groupss g ON g.id = s.group_id
	ORDER BY s.student, m.created_at DESC
	"""
    return db_connect(sql)


# Средний балл, который преподаватель ставит студенту.
def query_eleven() -> list:
    sql = """
    SELECT s.student, sb.teacher_name, sb.subject_name, AVG(m.mark)
    FROM marks m
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    LEFT JOIN students s ON s.id = m.student_id
    WHERE m.subject_id = 2
    GROUP BY m.student_id
    """
    return db_connect(sql)


# Средний балл, который ставит преподаватель.
def query_twelve() -> list:
    sql = """
    SELECT AVG(m.mark), sb.subject_name, sb.teacher_name
    FROM marks m
    LEFT JOIN subjects sb ON sb.id = m.subject_id
    GROUP BY sb.subject_name
    """
    return db_connect(sql)


if __name__ == '__main__':
    print(query_one())
    print(query_two())
    print(query_three())
    print(query_four())
    print(query_five())
    print(query_six())
    print(query_seven())
    print(query_eight())
    print(query_nine())
    print(query_ten())
    print(query_eleven())
    print(query_twelve())
