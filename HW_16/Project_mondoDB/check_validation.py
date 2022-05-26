"""Imports for check_validation"""
import re
from datetime import date
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/address_book")

db = client.address_book


def check_name_in_database(name: str) -> bool:
    """Check name in database"""
    result = db.contacts.find_one({"name": name})
    return bool(result)


def check_name(value: str) -> bool:
    """Name validation"""
    result = bool(value) if len(value) > 3 else False
    return result


def check_phone(value: str) -> bool:
    """Phone validation"""
    result = (
        bool(value)
        if len(value) == 13 and value[0] == "+" and value[1:].isdigit()
        else False
    )
    return result


def check_birthday(value: str) -> bool:
    """Birthday validation"""
    try:
        value = date.fromisoformat(value)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def check_email(value: str) -> bool:
    """Email validation"""
    match = re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", value, re.IGNORECASE)
    result = bool(value) if match is not None else False
    return result


def check_address(value: str) -> bool:
    """Address validation"""
    result = bool(value) if len(value) > 5 else False
    return result


def check_note(name: str) -> bool:
    """Check if note name in database"""
    result = db.note.find_one({"name": name})
    return bool(result)


def check_note_validation(name: str) -> bool:
    """Note validation"""
    result = bool(name) if len(name) > 3 else False
    return result
