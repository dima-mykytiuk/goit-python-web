# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
"""Imports for adressbook"""
from typing import Optional
from datetime import date
import re
from mongoengine import connect
from contact_book_models import Contacts


class Field:
    """Fields of records in contact book : name , phone/phones , etc."""

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        """Getter"""
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Name(Field):
    """Name class field of class Record"""


class Phone(Field):
    """Phone of the contact"""

    def __init__(self, value):
        if value is not None:
            if len(value) == 13 and value[0] == "+" and value[1:].isdigit():
                super().__init__(value)
            else:
                self.value = None
        else:
            self.value = None


class Birthday(Field):
    """Birthday of the contact"""

    def __init__(self, value):
        try:
            value = date.fromisoformat(value)
            super().__init__(value)
        except ValueError:
            self.value = None
        except TypeError:
            self.value = None


class Email(Field):
    """Email of the contact"""

    def __init__(self, value):
        if value is not None:
            if (
                re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", value, re.IGNORECASE)
                is not None
            ):
                super().__init__(value)
            else:
                self.value = None
        else:
            self.value = None


class Address(Field):
    """Address of the contact"""

    def __init__(self, value):
        if value is not None:
            if value is not None and len(value) > 5:
                super().__init__(value)
            else:
                self.value = None
        else:
            self.value = None


class RecordContacts:
    """Init RecordContacts"""

    def __init__(
        self,
        name: Optional[str] = None,
        phones: Optional[str] = None,
        birthday: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None,
    ) -> None:
        self.phones = Phone(phones)
        self.birthday = Birthday(birthday)
        self.name = Name(name)
        self.email = Email(email)
        self.address = Address(address)

    def add_phone(self, phone_number: str) -> str:
        """Add 'Phone' object"""
        phone = Phone(phone_number)
        self.phones = phone
        if self.phones.value is not None:
            return "Successfully set phone"
        return "Invalid phone format"

    def add_birthday(self, birthday_date):
        """
        Add 'Birthday' object
        """
        self.birthday = Birthday(birthday_date)
        if self.birthday.value is not None:
            return "Successfully set birthday"
        return "Invalid birthday format"

    def add_email(self, email):
        """Add 'Email' object"""
        self.email = Email(email)
        if self.email.value is not None:
            return "Successfully set email"
        return "Invalid email format"

    def add_address(self, address):
        """Add 'Address' object"""
        self.address = Address(address)
        if self.address.value is not None:
            return "Successfully set address"
        return "Invalid address format"


def save_in_database(contact: RecordContacts):
    """Save contact in database"""
    if isinstance(contact, RecordContacts):
        connect(host="mongodb://localhost:27017/address_book")
        Contacts(
            name=contact.name.value,
            phone=contact.phones.value,
            birthday=contact.birthday.value,
            email=contact.email.value,
            address=contact.address.value,
        ).save()
    else:
        return "Error illegal parameter"
    return "Saved in database"
