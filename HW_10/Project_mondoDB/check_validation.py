import re
from datetime import date
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/address_book")

db = client.address_book


def check_name_in_database(name: str) -> bool:
    result = db.contacts.find_one({"name": name})
    if result:
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
    result = db.note.find_one({"name": name})
    if result:
        return True
    else:
        return False
    
    
# note validation
def check_note_validation(name: str) -> bool:
    if len(name) > 3:
        return True
    else:
        return False