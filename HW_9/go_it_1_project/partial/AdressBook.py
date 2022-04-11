from typing import Optional
from datetime import date
import re
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from contact_book_models import Note, Record, Tag, Contact


class Field:
    """Fields of records in contact book : name , phone/phones , etc."""

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Name(Field):
    """Name class field of class Record"""


class Adress(Field):
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
    """Birthday field of cls Record"""

    def __init__(self, value):
        try:
            value = date.fromisoformat(value)
            super().__init__(value)
        except ValueError:
            self.value = None
        except TypeError:
            self.value = None


class Email(Field):
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
    def __init__(self, value):
        if value is not None:
            if value is not None and len(value) > 5:
                super().__init__(value)
            else:
                self.value = None
        else:
            self.value = None


class RecordContacts:
    """Records(contacts) in users contact book.
    Only one name , but it can be more than one phone"""

    def __init__(
        self,
        name: str,
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

    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        self.phones = phone

    def add_birthday(self, birthday_date):
        """
        Add 'Birthday' object
        """
        self.birthday = Birthday(birthday_date)

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)


class AddressBook:
    def save_in_database(self, contact: RecordContacts):
        engine = create_engine("sqlite:////Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        contacts = []
        contacts.append(Contact(name=contact.name.value,
                                phone=contact.phones.value,
                                birthday=contact.birthday.value,
                                email=contact.email.value,
                                address=contact.address.value
                                )
                        )
        session.add_all(contacts)
        session.commit()