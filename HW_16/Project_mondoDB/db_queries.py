"""Imports for db_queries"""
import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/address_book")

db = client.address_book


def change_name_in_db(old_name: str, new_name: str) -> str:
    """Func to change name in database"""
    result = db.contacts.find_one({"name": old_name})
    if result:
        db.contacts.update_one({"name": old_name}, {"$set": {"name": new_name}})
    else:
        return "That name not in db"
    return "Successfully changed"


def change_phone_in_db(new_phone: str, phone_name: str) -> str:
    """Func to change user phone in database"""
    result = db.contacts.find_one({"name": phone_name})
    if result:
        db.contacts.update_one({"name": phone_name}, {"$set": {"phone": new_phone}})
    else:
        return "That name not in db"
    return "Successfully changed phone"


def change_birthday_in_db(new_birthday: datetime.date, birthday_name: str) -> str:
    """Func to change user birthday in database"""
    result = db.contacts.find_one({"name": birthday_name})
    if result:
        db.contacts.update_one(
            {"name": birthday_name}, {"$set": {"birthday": new_birthday}}
        )
    else:
        return "That name not in db"
    return "Successfully changed birthday"


def change_email_in_db(new_email: str, email_name: str) -> str:
    """Func to change user email in database"""
    result = db.contacts.find_one({"name": email_name})
    if result:
        db.contacts.update_one({"name": email_name}, {"$set": {"email": new_email}})
    else:
        return "That name not in db"
    return "Successfully changed email"


def change_address_in_db(new_address: str, address_name: str) -> str:
    """Func to change user address in database"""
    result = db.contacts.find_one({"name": address_name})
    if result:
        db.contacts.update_one(
            {"name": address_name}, {"$set": {"address": new_address}}
        )
    else:
        return "That name not in db"
    return "Successfully changed address"


def del_contact_from_db(contact_name: str) -> str:
    """Func to delete user from database"""
    result = db.contacts.find_one({"name": contact_name})
    if result:
        db.contacts.delete_one({"name": contact_name})
    else:
        return "That name not in db"
    return "Successfully deleted contact"


def get_contact_from_db(contact_name: str) -> dict:
    """Func to get user from database"""
    result = db.contacts.find_one({"name": contact_name})
    if result is None:
        return "That name not in db"
    return result


def get_all_contacts_from_db() -> list:
    """Func to get all users from database"""
    contacts_list = []
    results = db.contacts.find({}, {"_id": 0})
    for result in results:
        contacts_list.append(result)
    return contacts_list


def get_all_notes() -> list:
    """Func to get all notes from database"""
    notes_list = []
    results = db.note.find({}, {"_id": 0})
    for result in results:
        notes_list.append(result)
    return notes_list


def get_note_by_name(note_name: str) -> dict:
    """Func to get note from database"""
    result = db.note.find_one({"name": note_name})
    if result is None:
        return "That note name not in db"
    return result


def change_note_in_db(new_note: str, old_note: str) -> str:
    """Func to change note in database"""
    result = db.note.find_one({"name": old_note})
    if result:
        db.note.update_one({"name": old_note}, {"$set": {"name": new_note}})
    else:
        return "That note name not in db"
    return "Successfully changed note"


def del_note_from_db(note_name: str) -> str:
    """Func to delete note from database"""
    result = db.note.find_one({"name": note_name})
    if result:
        db.note.delete_one({"name": note_name})
    else:
        return "That note not in db"
    return "Successfully deleted note"


def insert_tag(note_name: str, tag: str) -> str:
    """Func to insert tag to note"""
    result = db.note.find_one({"name": note_name})
    if result:
        db.note.update_one({"name": note_name}, {"$push": {"tags": {"name": tag}}})
    else:
        return "That note not in db"
    return "Successfully added tags"


def get_birthday_in_database(days: int) -> list:
    """
    1. Get all contact_name + birthdays to list_of_contacts
    2. Choose only valid contacts where birthday in days
    3. Change year to current to get valid day
    """
    list_of_contacts = []
    delta_days = 0
    valid_contacts = []
    result = db.contacts.find({}, {"_id": 0, "address": 0, "phone": 0, "email": 0})
    for contact in result:
        list_of_contacts.append(contact)
    while delta_days != days:
        for item in list_of_contacts:
            valid_days = datetime.datetime.now() + datetime.timedelta(days=delta_days)
            for value in item.values():
                if not isinstance(value, str):
                    if value.month == valid_days.month and value.day == valid_days.day:
                        valid_contacts.append(item)
        delta_days += 1
    for item in valid_contacts:
        date = item.get("birthday")
        valid_year = date.replace(year=datetime.datetime.now().year)
        item.update({"birthday": valid_year.strftime("%d %B")})
    return valid_contacts
