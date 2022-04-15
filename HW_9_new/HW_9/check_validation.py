import re
import sqlite3
from datetime import date


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
    