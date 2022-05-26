""""Import for assistant"""
from datetime import date

from adressbook import save_in_database, RecordContacts
from notebook import Notes, save_note_in_database
from check_validation import (
    check_note_validation,
    check_name_in_database,
    check_name,
    check_phone,
    check_email,
    check_note,
    check_birthday,
    check_address,
)

from db_queries import (
    change_name_in_db,
    change_phone_in_db,
    change_birthday_in_db,
    change_email_in_db,
    change_address_in_db,
    del_contact_from_db,
    get_note_by_name,
    change_note_in_db,
    del_note_from_db,
    insert_tag,
    get_contact_from_db,
    get_birthday_in_database,
)


def add_contact() -> str:
    """ "add_contact"""
    name = input("Write name: ")
    while len(name) < 3:
        name = input("Name must be at least 3 symbols, Try again: ")
    new_contact = RecordContacts(
        name=name, phones=None, birthday=None, email=None, address=None
    )
    phone = input("Write phone: ")
    new_contact.add_phone(phone)
    while new_contact.phones.value is None:
        phone = input(
            "Invalid format for phone, please enter phone in format +380123456789: "
        )
        new_contact.add_phone(phone)
    birthday = input("Write birthday: ")
    new_contact.add_birthday(birthday)
    while new_contact.birthday.value is None:
        birthday = input("Incorrect format date was given, Try again: ")
        new_contact.add_birthday(birthday)
    email = input(
        "[OPTIONAL] You can skip this info, just press enter or write email: "
    )
    new_contact.add_email(email)
    if len(email) > 0:
        while new_contact.email.value is None:
            email = input(
                '["Invalid email!"][OPTIONAL] You can skip this info,'
                "just press enter or try again: "
            )
            new_contact.add_email(email)
            if len(email) == 0:
                break
    address = input(
        "[OPTIONAL] You can skip this info, " "just press enter or write address: "
    )
    new_contact.add_address(address)
    if len(address) > 0:
        while new_contact.address.value is None:
            address = input(
                '["Invalid address!"][OPTIONAL] '
                "You can skip this info, just press enter or try again: "
            )
            new_contact.add_address(address)
            if len(address) == 0:
                break
    save_in_database(new_contact)
    return f"Successfully add contact {name} to contact book"


def change_name() -> str:
    """Func to change name in database with validation"""
    old_name = input("Write the name you want to change: ")
    check_name_database = check_name_in_database(old_name)
    while check_name_database is not True:
        old_name = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(old_name)
    new_name = input("Write new name: ").capitalize()
    name_validation = check_name(new_name)
    while name_validation is not True:
        new_name = input("Name must be at least 3 symbols, Try again: ")
        name_validation = check_name(new_name)
    return change_name_in_db(old_name, new_name)


def change_phone() -> str:
    """ "Func to change phone in database with validation"""
    phone_name = input("Write the name of whom you want to change the phone: ")
    check_name_database = check_name_in_database(phone_name)
    while check_name_database is not True:
        phone_name = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(phone_name)
    new_phone = input("Write new phone: ")
    phone_validation = check_phone(new_phone)
    while phone_validation is not True:
        new_phone = input(
            "Invalid format for phone, please enter phone in format +380123456789: "
        )
        phone_validation = check_phone(new_phone)
    return change_phone_in_db(new_phone, phone_name)


def change_birthday() -> str:
    """ "Func to change birthday in database with validation"""
    birthday_name = input("Write the name of whom you want to change birthday: ")
    check_name_database = check_name_in_database(birthday_name)
    while check_name_database is not True:
        birthday_name = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(birthday_name)
    new_birthday = input("Write new birthday: ")
    birthday_validation = check_birthday(new_birthday)
    while birthday_validation is not True:
        new_birthday = input("Incorrect format date was given, Try again: ")
        birthday_validation = check_birthday(new_birthday)
    new_birthday = date.fromisoformat(new_birthday)
    return change_birthday_in_db(new_birthday, birthday_name)


def change_email() -> str:
    """ "Func to change email in database with validation"""
    email_name = input("Write the name of whom you want to change email: ")
    check_name_database = check_name_in_database(email_name)
    while check_name_database is not True:
        email_name = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(email_name)
    new_email = input("Write new email: ")
    email_validation = check_email(new_email)
    while email_validation is not True:
        new_email = input("Invalid email, Try again: ")
        email_validation = check_email(new_email)
    return change_email_in_db(new_email, email_name)


def change_address() -> str:
    """ "Func to change address in database with validation"""
    address_name = input("Write the name of whom you want to change address: ")
    check_name_database = check_name_in_database(address_name)
    while check_name_database is not True:
        address_name = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(address_name)
    new_address = input("Write new address: ")
    address_validation = check_address(new_address)
    while address_validation is not True:
        new_address = input("Invalid address, Try again: ")
        address_validation = check_address(new_address)
    return change_address_in_db(new_address, address_name)


def change_contact() -> str:
    """ "Func to start function depends on what user want to change"""
    user_commands = {
        "phone": change_phone,
        "name": change_name,
        "birthday": change_birthday,
        "email": change_email,
        "address": change_address,
    }
    what_change = input("What you want to change?\n")
    while what_change not in user_commands:
        print("I can change only phone, name, birthday, email, address")
        what_change = input("What you want to change?\n")
    return user_commands[what_change]()


def del_contact() -> str:
    """ "Func to delete contact from database with validation"""
    name_to_delete = input("What name do you want to remove from contacts?: ")
    check_name_database = check_name_in_database(name_to_delete)
    while check_name_database is not True:
        name_to_delete = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(name_to_delete)
    return del_contact_from_db(name_to_delete)


def find_contact() -> dict:
    """ "Func to find contact from database with validation"""
    name_to_find = input("What name do you want to find in contacts?: ")
    check_name_database = check_name_in_database(name_to_find)
    while check_name_database is not True:
        name_to_find = input("This name is not in the database, try again: ")
        check_name_database = check_name_in_database(name_to_find)
    return get_contact_from_db(name_to_find)


def get_birthdays() -> list:
    """ "Func to get birthdays in days from database"""
    days = input("Please write for how many days do you want to know the birthdays?: ")
    while days.isdigit() is False:
        days = input(
            '"Error please enter digits"\nFor how many days do you want to know the birthdays?\n'
        )
    days = int(days)
    return get_birthday_in_database(days)


def add_note() -> str:
    """ "Func to add note in database"""
    note_to_add = None
    note_name = input("Write down your note: ")
    while len(note_name) < 3:
        note_name = input("Note must be at least 3 symbols, try again: ")
    text_tags = input(
        "[OPTIONAL] You can skip this info, just press enter or write tags: "
    )
    note_desc = input("Write description to this note: ")
    while len(note_desc) < 3:
        note_desc = input("Description must be at least 3 symbols, try again: ")
    if len(text_tags) > 0:
        tags = text_tags.split(",")
        tags = [tag.strip() for tag in tags]
        note_to_add = Notes(text=note_name, desc=note_desc, tags=tags)
        save_note_in_database(note_to_add)
    else:
        note_to_add = Notes(text=note_name, desc=note_desc, tags=[])
        save_note_in_database(note_to_add)
    return f"Successfully add note {note_name} to notebook"


def find_note_by_name() -> dict:
    """ "Func to find 1 note by name"""
    note_name = input("Write down note name: ")
    check_note_database = check_note(note_name)
    while check_note_database is not True:
        note_name = input("This note is not in the database, try again: ")
        check_note_database = check_note(note_name)
    return get_note_by_name(note_name)


def change_note() -> str:
    """ "Func to change note"""
    note_to_change = input("Write down note which you want to change: ")
    check_note_database = check_note(note_to_change)
    while check_note_database is not True:
        note_to_change = input("This note is not in the database, try again: ")
        check_note_database = check_note(note_to_change)
    new_note = input("Write new note: ")
    note_validation = check_note_validation(new_note)
    while note_validation is not True:
        new_note = input("Name must be at least 3 symbols, Try again: ")
        note_validation = check_note_validation(new_note)
    return change_note_in_db(new_note, note_to_change)


def delete_note() -> str:
    """ "Func to delete note"""
    note_to_delete = input("Write down note which you want to delete: ")
    check_note_database = check_note(note_to_delete)
    while check_note_database is not True:
        note_to_delete = input("This note is not in the database, try again: ")
        check_note_database = check_note(note_to_delete)
    return del_note_from_db(note_to_delete)


def add_tags() -> str:
    """ "Func to add tags to note"""
    note_to_add_tags = input("Write down a note to which you want to add tags: ")
    check_note_database = check_note(note_to_add_tags)
    while check_note_database is not True:
        note_to_add_tags = input("This note is not in the database, try again: ")
        check_note_database = check_note(note_to_add_tags)
    tag_to_add = input("Write down a tag: ")
    check_tag_database = check_note_validation(tag_to_add)
    while check_tag_database is not True:
        tag_to_add = input("Tag must be at least 3 symbols, try again: ")
        check_tag_database = check_note_validation(tag_to_add)
    return insert_tag(note_to_add_tags, tag_to_add)
