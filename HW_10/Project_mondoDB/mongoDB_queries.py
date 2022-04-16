import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/address_book")

db = client.address_book


def change_name_in_db(old_name: str, new_name: str) -> str:
    db.contacts.update_one({"name": old_name}, {"$set": {"name": new_name}})
    return f'Successfully changed {old_name} to {new_name}'


def change_phone_in_db(new_phone: str, phone_name: str) -> str:
    db.contacts.update_one({"name": phone_name}, {"$set": {"phone": new_phone}})
    return f"Successfully changed phone for contact {phone_name}"


def change_birthday_in_db(new_birthday: datetime.date, birthday_name: str) -> str:
    db.contacts.update_one({"name": birthday_name}, {"$set": {"birthday": new_birthday}})
    return f"Successfully changed birthday for contact {birthday_name}"


def change_email_in_db(new_email: str, email_name: str) -> str:
    db.contacts.update_one({"name": email_name}, {"$set": {"email": new_email}})
    return f"Successfully changed email for contact {email_name}"


def change_address_in_db(new_address: str, address_name: str) -> str:
    db.contacts.update_one({"name": address_name}, {"$set": {"address": new_address}})
    return f"Successfully changed address for contact {address_name}"


def del_contact_from_db(contact_name: str) -> str:
    db.contacts.delete_one({"name": contact_name})
    return f"Successfully deleted contact {contact_name}"


def get_contact_from_db(contact_name: str) -> dict:
    result = db.contacts.find_one({"name": contact_name})
    return result


def get_all_contacts_from_db() -> list:
    contacts_list = []
    result = db.contacts.find({}, { "_id": 0})
    for el in result:
        contacts_list.append(el)
    return contacts_list


def get_all_notes() -> list:
    notes_list = []
    result = db.note.find({}, {"_id": 0})
    for el in result:
        notes_list.append(el)
    return notes_list


def get_note_by_name(note_name: str) -> dict:
    result = db.note.find_one({"name": note_name})
    return result


def change_note_in_db(new_note: str, old_note: str) -> str:
    db.note.update_one({"name": old_note}, {"$set": {"name": new_note}})
    return f'Successfully changed {old_note} to {new_note}'


def del_note_from_db(note_name: str) -> str:
    db.note.delete_one({"name": note_name})
    return f"Successfully deleted note {note_name}"
        
        
def insert_tag(note_name: str, tag: str) -> str:
    db.note.update_one({"name": note_name}, {"$push": {"tags": {"name": tag}}})
    return f'"Successfully added tag to note {note_name}'


# 1. Get all contact_name + birthdays to list_of_contacts
# 2. Choose only valid contacts where birthday in days
# 3. Change year to current to get valid day
def get_birthday_in_database(days: int) -> list:
    list_of_contacts = []
    delta_days = 0
    valid_contacts = []
    result = db.contacts.find({}, {"_id": 0, 'address': 0, 'phone': 0, 'email': 0})
    for contact in result:
        list_of_contacts.append(contact)
    while delta_days != days:
        for item in list_of_contacts:
            valid_days = datetime.datetime.now() + datetime.timedelta(days=delta_days)
            for value in item.values():
                if type(value) != str:
                    if value.month == valid_days.month and value.day == valid_days.day:
                        valid_contacts.append(item)
        delta_days += 1
    for item in valid_contacts:
        date = item.get('birthday')
        valid_year = date.replace(year=datetime.datetime.now().year)
        item.update({'birthday': valid_year.strftime("%d %B")})
    return valid_contacts
