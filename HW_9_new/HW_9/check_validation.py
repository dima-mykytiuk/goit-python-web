import re
import sqlite3
from datetime import date
import datetime


# Check if name in database
def check_name_in_database(name: str) -> bool:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        names = []
        get_names = """
        SELECT c.name
        FROM contacts c
        """
        check = cur.execute(get_names)
        for item in check.fetchall():
            for i in item:
                names.append(i)
    if name in names:
        return True
    else:
        return False


# name validation
def check_name(value: str) -> bool:
    if len(value) > 3:
        return True
    else:
        return False


# phone validation
def check_phone(value: str) -> bool:
    if len(value) == 13 and value[0] == "+" and value[1:].isdigit():
        return True
    else:
        return False
    
    
# birthday validation
def check_birthday(value: str) -> bool:
    try:
        value = date.fromisoformat(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
    

# email validation
def check_email(value: str) -> bool:
    if (
        re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", value, re.IGNORECASE)
        is not None
    ):
        return True
    else:
        return False
    
    
# Address validation
def check_address(value: str) -> bool:
    if len(value) > 5:
        return True
    else:
        return False
    

# get birthdays in days
def get_birthday_in_database(days: int) -> list:
    names = []
    birthdays = []
    res = {}
    valid_birthdays = []
    delta_days = 0
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_birthdays = """
        SELECT c.birthday
        FROM contacts c
        """
        check = cur.execute(get_birthdays)
    for item in check.fetchall():
        for i in item:
            valid_bthd = date.fromisoformat(i)
            birthdays_current_year = valid_bthd.replace(datetime.datetime.now().year)
            birthdays.append(birthdays_current_year)
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_names = """
        SELECT c.name
        FROM contacts c
        """
        check = cur.execute(get_names)
        for item in check.fetchall():
            for i in item:
                names.append(i)
    for key in names:
        for value in birthdays:
            res[key] = value
            birthdays.remove(value)
            break
    while delta_days != days:
        for key, value in res.items():
            valid_days = datetime.datetime.now() + datetime.timedelta(days=delta_days)
            if value.month == valid_days.month and value.day == valid_days.day:
                valid_birthdays.append((key, value.strftime(("%d %B"))))
        delta_days += 1
    return valid_birthdays


# Check if note name in database
def check_note(name: str) -> bool:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        notes = []
        get_names = """
        SELECT n.name
        FROM notes n
        """
        check = cur.execute(get_names)
        for item in check.fetchall():
            for i in item:
                notes.append(i)
    if name in notes:
        return True
    else:
        return False
    
    
# note validation
def check_note_validation(name: str) -> bool:
    if len(name) > 3:
        return True
    else:
        return False
 
    
# get note id
def find_note_id(name: str) -> int:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        notes = None
        get_names = """
        SELECT n.id
        FROM notes n
        WHERE name = ?
        """
        check = cur.execute(get_names, [name])
        for item in check.fetchall():
            for i in item:
                notes = i
    return notes


# insert data into table records
def insert_into_records(id: int, tag: str) -> None:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_names = """
        INSERT INTO records (description, done, note_id)
        VALUES (?, 0, ?)
        """
        cur.execute(get_names, [tag, id])


# insert data into table tags
def insert_into_tags(tag: str) -> None:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_names = """
        INSERT INTO tags (name)
        VALUES (?)
        """
        cur.execute(get_names, [tag])


# get tag id
def find_tag_id(tag_name: str) -> int:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        tag_id = None
        get_names = """
        SELECT t.id
        FROM tags t
        WHERE name = ?
        """
        check = cur.execute(get_names, [tag_name])
        for item in check.fetchall():
            for i in item:
                tag_id = i
    return tag_id


# insert data into many 2 many table
def insert_into_m2m_table(tag: id, id: id) -> None:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_names = """
        INSERT INTO note_m2m_tag (note, tag)
        VALUES (?, ?)
        """
        cur.execute(get_names, [id, tag])