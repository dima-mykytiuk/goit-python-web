import sqlite3
from datetime import date, datetime, timedelta


def change_name_in_db(old_name: str, new_name: str) -> str:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE contacts
        SET name= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_name, old_name])
    return f'Successfully changed {old_name} to {new_name}'


def change_phone_in_db(new_phone: str, phone_name: str) -> str:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE contacts
        SET phone= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_phone, phone_name])
    return f"Successfully changed phone for contact {phone_name}"


def change_birthday_in_db(new_birthday: date, birthday_name: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE contacts
        SET birthday= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_birthday, birthday_name])
    return f"Successfully changed birthday for contact {birthday_name}"


def change_email_in_db(new_email: str, email_name: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE contacts
        SET email= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_email, email_name])
    return f"Successfully changed email for contact {email_name}"


def change_address_in_db(new_address: str, address_name: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE contacts
        SET address= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_address, address_name])
    return f"Successfully changed address for contact {address_name}"


def del_contact_from_db(contact_name: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        DELETE
        FROM contacts
        WHERE name= ?
        """
        cur.execute(sql, [contact_name])
    return f"Successfully deleted contact {contact_name}"


def get_contact_from_db(contact_name: str) -> list:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        SELECT c.name, c.phone, c.birthday, c.email, c.address
        FROM contacts c
        WHERE name= ?
        """
        cur.execute(sql, [contact_name])
        return cur.fetchall()


def get_all_contacts_from_db():
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        SELECT c.name, c.phone, c.birthday, c.email, c.address
        FROM contacts c
        """
        cur.execute(sql)
        return cur.fetchall()


def get_all_notes():
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        SELECT n.name
        FROM notes n
        ORDER BY created
        """
        cur.execute(sql)
        return cur.fetchall()


def get_note_by_name(note_name: str) -> list:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        SELECT n2.name, n2.created
        FROM notes n2
        WHERE name = ?
        """
        cur.execute(sql, [note_name])
        return cur.fetchall()


def change_note_in_db(new_note: str, old_note: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        UPDATE notes
        SET name= ?
        WHERE name= ?
        """
        cur.execute(sql, [new_note, old_note])
    return f'Successfully changed {old_note} to {new_note}'


def del_note_from_db(note_name: str) -> str:
    with sqlite3.connect(
            '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        sql = """
        DELETE
        FROM notes
        WHERE name= ?
        """
        cur.execute(sql, [note_name])
    return f"Successfully deleted note {note_name}"


# get note id
def get_note_id_from_db(name: str) -> int:
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


# get tag id
def get_tag_id_from_db(tag_name: str) -> int:
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


# insert data into many 2 many table
def insert_into_m2m_table(tag: id, id: id) -> None:
    with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
        cur = con.cursor()
        get_names = """
        INSERT INTO note_m2m_tag (note, tag)
        VALUES (?, ?)
        """
        cur.execute(get_names, [id, tag])
        
        
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
            birthdays_current_year = valid_bthd.replace(datetime.now().year)
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
            valid_days = datetime.now() + timedelta(days=delta_days)
            if value.month == valid_days.month and value.day == valid_days.day:
                valid_birthdays.append((key, value.strftime(("%d %B"))))
        delta_days += 1
    return valid_birthdays
