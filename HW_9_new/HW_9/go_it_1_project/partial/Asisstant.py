from AdressBook import *
from NoteBook import *
from check_validation import *


class Asisstant:
    def __init__(self) -> None:
        self.address_book = AddressBook()
        self.note_book = NoteBook()
    
    # add new contact to database step-by-step with validation
    def add_contact(self) -> str:
        name = input('Write name: ')
        while len(name) < 3:
            name = input('Name must be at least 3 symbols, Try again: ')
        new_contact = RecordContacts(name=name, phones=None, birthday=None, email=None, address=None)
        phone = input('Write phone: ')
        new_contact.add_phone(phone)
        while new_contact.phones.value is None:
            phone = input('Invalid format for phone, please enter phone in format +380123456789: ')
            new_contact.add_phone(phone)
        birthday = input('Write birthday: ')
        new_contact.add_birthday(birthday)
        while new_contact.birthday.value is None:
            birthday = input('Incorrect format date was given, Try again: ')
            new_contact.add_birthday(birthday)
        email = input('[OPTIONAL] You can skip this info, just press enter or write email: ')
        new_contact.add_email(email)
        if len(email) > 0:
            while new_contact.email.value is None:
                email = input(f'["Invalid email!"][OPTIONAL] You can skip this info, just press enter or try again: ')
                new_contact.add_email(email)
                if len(email) == 0:
                    break
        address = input('[OPTIONAL] You can skip this info, just press enter or write address: ')
        new_contact.add_address(address)
        if len(address) > 0:
            while new_contact.address.value is None:
                address = input(f'["Invalid address!"][OPTIONAL] You can skip this info, just press enter or try again: ')
                new_contact.add_address(address)
                if len(address) == 0:
                    break
        self.address_book.save_in_database(new_contact)
        return f'Successfully add contact {name} to contact book'
    
    # func to change name in database with validation
    def __change_name(self) -> str:
        old_name = input('Write the name you want to change: ')
        check_name_database = check_name_in_database(old_name)
        while check_name_database is not True:
            old_name = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(old_name)
        new_name = input("Write new name: ").capitalize()
        name_validation = check_name(new_name)
        while name_validation is not True:
            new_name = input('Name must be at least 3 symbols, Try again: ')
            name_validation = check_name(new_name)
        with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE contacts
            SET name= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_name, old_name])
        return f'Successfully changed {old_name} to {new_name}'

    # func to change phone in database with validation
    def __change_phone(self) -> str:
        name_phone = input('Write the name of whom you want to change the phone: ')
        check_name_database = check_name_in_database(name_phone)
        while check_name_database is not True:
            name_phone = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_phone)
        new_phone = input("Write new phone: ")
        phone_validation = check_phone(new_phone)
        while phone_validation is not True:
            new_phone = input('Invalid format for phone, please enter phone in format +380123456789: ')
            phone_validation = check_phone(new_phone)
        with sqlite3.connect('/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE contacts
            SET phone= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_phone, name_phone])
        return f"Successfully changed phone for contact {name_phone}"

    # func to change birthday in database with validation
    def __change_birthday(self) -> str:
        name_birthday = input('Write the name of whom you want to change birthday: ')
        check_name_database = check_name_in_database(name_birthday)
        while check_name_database is not True:
            name_birthday = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_birthday)
        new_birthday = input("Write new birthday: ")
        birthday_validation = check_birthday(new_birthday)
        while birthday_validation is not True:
            new_birthday = input('Incorrect format date was given, Try again: ')
            birthday_validation = check_birthday(new_birthday)
        new_birthday = date.fromisoformat(new_birthday)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE contacts
            SET birthday= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_birthday, name_birthday])
        return f"Successfully changed birthday for contact {name_birthday}"

    # func to change email in database with validation
    def __change_email(self) -> str:
        name_email = input('Write the name of whom you want to change email: ')
        check_name_database = check_name_in_database(name_email)
        while check_name_database is not True:
            name_email = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_email)
        new_email = input("Write new email: ")
        email_validation = check_email(new_email)
        while email_validation is not True:
            new_email = input('Invalid email, Try again: ')
            email_validation = check_email(new_email)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE contacts
            SET email= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_email, name_email])
        return f"Successfully changed email for contact {name_email}"

    # func to change address in database with validation
    def __change_address(self) -> str:
        name_address = input('Write the name of whom you want to change address: ')
        check_name_database = check_name_in_database(name_address)
        while check_name_database is not True:
            name_address = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_address)
        new_address = input("Write new address: ")
        address_validation = check_address(new_address)
        while address_validation is not True:
            new_address = input('Invalid address, Try again: ')
            address_validation = check_address(new_address)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE contacts
            SET address= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_address, name_address])
        return f"Successfully changed address for contact {name_address}"

    # func to start function depends on what user want to change
    def change_contact(self) -> str:
        user_commands = {
            "phone": Asisstant().__change_phone,
            "name": Asisstant().__change_name,
            "birthday": Asisstant().__change_birthday,
            "email": Asisstant().__change_email,
            "address": Asisstant().__change_address,
        }
        what_change = input("What you want to change?\n")
        while what_change not in user_commands.keys():
            print("I can change only phone, name, birthday, email, address")
            what_change = input("What you want to change?\n")
        print(user_commands[what_change]())
        return 'Done'

    # func to delete contact from database with validation
    def del_contact(self) -> str:
        name_to_delete = input("What name do you want to remove from contacts?: ")
        check_name_database = check_name_in_database(name_to_delete)
        while check_name_database is not True:
            name_to_delete = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_to_delete)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            DELETE
            FROM contacts
            WHERE name= ?
            """
            cur.execute(sql, [name_to_delete])
        return f"Successfully deleted contact {name_to_delete}"

    # func to find contact from database with validation
    def find_contact(self) -> list:
        name_to_find = input("What name do you want to find in contacts?: ")
        check_name_database = check_name_in_database(name_to_find)
        while check_name_database is not True:
            name_to_find = input('This name is not in the database, try again: ')
            check_name_database = check_name_in_database(name_to_find)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            SELECT c.name, c.phone, c.birthday, c.email, c.address
            FROM contacts c
            WHERE name= ?
            """
            cur.execute(sql, [name_to_find])
            return cur.fetchall()

    # func to get birthdays in days from database
    def get_birthdays(self) -> list:
        days = input('Please write for how many days do you want to know the birthdays?: ')
        while days.isdigit() is False:
            days = input(
                '"Error please enter digits"\nFor how many days do you want to know the birthdays?\n'
            )
        days = int(days)
        return get_birthday_in_database(days)
    
    # func to display all contacts from database
    def show_all_contacts(self) -> list:
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            SELECT c.name, c.phone, c.birthday, c.email, c.address
            FROM contacts c
            """
            cur.execute(sql)
            return cur.fetchall()
    
    # func to add note in database
    def add_note(self) -> str:
        note_name = input("Write down your note: ")
        while len(note_name) < 3:
            note_name = input("Note must be at least 3 symbols, try again: ")
        text_tags = input('[OPTIONAL] You can skip this info, just press enter or write tags: ')
        note_desc = input("Write description to this note: ")
        while len(note_desc) < 3:
            note_desc = input("Description must be at least 3 symbols, try again: ")
        if len(text_tags) > 0:
            tags = text_tags.split(",")
            tags = [tag.strip() for tag in tags]
            add_note = Notes(text=note_name, desc=note_desc, tags=tags)
            self.note_book.save_note_in_database(add_note)
            return f'Successfully add note {note_name} to notebook'
        else:
            add_note = Notes(text=note_name, desc=note_desc)
            self.note_book.save_note_in_database(add_note)
            return f'Successfully add note {note_name} to notebook'
    
    # func to display all notes
    def show_notes(self) -> list:
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
    
    # func to find 1 note by name
    def find_note_by_name(self) -> list:
        note_name = input("Write down note name: ")
        check_note_database = check_note(note_name)
        while check_note_database is not True:
            note_name = input('This note is not in the database, try again: ')
            check_note_database = check_note(note_name)
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
    
    # func to change note
    def change_note(self) -> str:
        note_to_change = input("Write down note which you want to change: ")
        check_note_database = check_note(note_to_change)
        while check_note_database is not True:
            note_to_change = input('This note is not in the database, try again: ')
            check_note_database = check_note(note_to_change)
        new_note = input("Write new note: ")
        note_validation = check_note_validation(new_note)
        while note_validation is not True:
            new_note = input('Name must be at least 3 symbols, Try again: ')
            note_validation = check_note_validation(new_note)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            UPDATE notes
            SET name= ?
            WHERE name= ?
            """
            cur.execute(sql, [new_note, note_to_change])
        return f'Successfully changed {note_to_change} to {new_note}'
    
    # func to delete note
    def delete_note(self) -> str:
        note_to_delete = input("Write down note which you want to delete: ")
        check_note_database = check_note(note_to_delete)
        while check_note_database is not True:
            note_to_delete = input('This note is not in the database, try again: ')
            check_note_database = check_note(note_to_delete)
        with sqlite3.connect(
                '/Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db') as con:
            cur = con.cursor()
            sql = """
            DELETE
            FROM notes
            WHERE name= ?
            """
            cur.execute(sql, [note_to_delete])
        return f"Successfully deleted note {note_to_delete}"

    # func to add tags to note
    def add_tags(self) -> str:
        note_to_add_tags = input("Write down a note to which you want to add tags: ")
        check_note_database = check_note(note_to_add_tags)
        while check_note_database is not True:
            note_to_add_tags = input('This note is not in the database, try again: ')
            check_note_database = check_note(note_to_add_tags)
        note_id = find_note_id(note_to_add_tags)
        tag_to_add = input('Write down a tag: ')
        check_tag_database = check_note(tag_to_add)
        while check_tag_database is not True:
            tag_to_add = input('Tag must be at least 3 symbols, try again: ')
            check_tag_database = check_note(tag_to_add)
        insert_into_records(id=note_id, tag=tag_to_add)
        insert_into_tags(tag=tag_to_add)
        tag_id = find_tag_id(tag_to_add)
        insert_into_m2m_table(id=note_id, tag=tag_id)
        return f"Successfully add tags"
    