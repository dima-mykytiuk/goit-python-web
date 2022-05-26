"""Imports to test db queries"""
import unittest
from datetime import datetime
from go_it_1_project.src.adressbook import RecordContacts, save_in_database
from go_it_1_project.src.notebook import Notes, save_note_in_database

from db_queries import (
    change_phone_in_db,
    change_birthday_in_db,
    change_name_in_db,
    change_email_in_db,
    change_address_in_db,
    del_contact_from_db,
    get_contact_from_db,
    get_all_contacts_from_db,
    get_all_notes,
    get_note_by_name,
    change_note_in_db,
    del_note_from_db,
    insert_tag,
    get_birthday_in_database,
)


class TestDbQueries(unittest.TestCase):
    """Class to test database queries"""

    @classmethod
    def setUpClass(cls) -> None:
        change_name_in_db(old_name="Vasya", new_name="Sanya")
        record = RecordContacts(
            name="Dima",
            phones="+380346074864",
            birthday="1992-10-11",
            email="smik@gmail.com",
            address="Balzaka 4",
        )
        note_record = Notes(
            text="Сходил за пивком",
            desc="Бухнул",
            tags=["Пивко", "Водка"],
        )
        save_note_in_database(note=note_record)
        save_in_database(contact=record)

    def test_1_change_name_in_db(self):
        """Testing to changing name in database"""
        self.assertEqual(
            change_name_in_db(old_name="Sanya", new_name="Vasya"),
            "Successfully changed",
        )
        self.assertEqual(
            change_name_in_db(old_name="Euge", new_name="Petya"), "That name not in db"
        )

    def test_2_change_phone_in_db(self):
        """Testing to changing user phone in database"""
        self.assertEqual(
            change_phone_in_db(new_phone="+380506074821", phone_name="Zhenya"),
            "Successfully changed phone",
        )
        self.assertEqual(
            change_phone_in_db(new_phone="+380506074855", phone_name="Petya"),
            "That name not in db",
        )

    def test_3_change_birthday_in_db(self):
        """Testing to changing user birthday in database"""
        self.assertEqual(
            change_birthday_in_db(
                new_birthday=datetime.fromisoformat("1998-11-05"),
                birthday_name="Zhenya",
            ),
            "Successfully changed birthday",
        )
        self.assertEqual(
            change_birthday_in_db(
                new_birthday=datetime.fromisoformat("1998-11-10"), birthday_name="Petya"
            ),
            "That name not in db",
        )

    def test_4_change_email_in_db(self):
        """Testing to changing user email in database"""
        self.assertEqual(
            change_email_in_db(new_email="vendetta2012@gmail.com", email_name="Zhenya"),
            "Successfully changed email",
        )
        self.assertEqual(
            change_email_in_db(new_email="vendetta2012@gmail.com", email_name="Petya"),
            "That name not in db",
        )

    def test_5_change_address_in_db(self):
        """Testing to changing user address in database"""
        self.assertEqual(
            change_address_in_db(new_address="Radunskaya 2", address_name="Zhenya"),
            "Successfully changed address",
        )
        self.assertEqual(
            change_address_in_db(new_address="Radunskaya 2", address_name="Petya"),
            "That name not in db",
        )

    def test_6_del_contact_from_db(self):
        """Testing to deleting contact from database"""
        self.assertEqual(
            del_contact_from_db(contact_name="Dima"), "Successfully deleted contact"
        )
        self.assertEqual(
            del_contact_from_db(contact_name="Petya"), "That name not in db"
        )

    def test_7_get_contact_from_db(self):
        """Testing to get contact from database"""
        self.assertEqual(
            get_contact_from_db(contact_name="Zhenya"),
            get_contact_from_db(contact_name="Zhenya"),
        )
        self.assertEqual(
            get_contact_from_db(contact_name="Petya"), "That name not in db"
        )

    def test_8_get_all_contacts_from_db(self):
        """Testing to get all contacts from database"""
        self.assertEqual(get_all_contacts_from_db(), get_all_contacts_from_db())

    def test_9_get_all_notes(self):
        """Testing to get all notes from database"""
        self.assertEqual(get_all_notes(), get_all_notes())

    def test_10_get_note_by_name(self):
        """Testing to get note from database"""
        self.assertEqual(
            get_note_by_name(note_name="Сходить купить тачку"),
            get_note_by_name(note_name="Сходить купить тачку"),
        )
        self.assertEqual(
            get_note_by_name(note_name="Сходил куда-то"), "That note name not in db"
        )

    def test_11_change_note_in_db(self):
        """Testing to change note in database"""
        self.assertEqual(
            change_note_in_db(
                new_note="Сходить купить машинку", old_note="Сходил за пивком"
            ),
            "Successfully changed note",
        )
        self.assertEqual(
            change_note_in_db(new_note="Сходить купить машину", old_note="Сходил"),
            "That note name not in db",
        )

    def test_12_del_note_from_db(self):
        """Testing to delete note from database"""
        self.assertEqual(
            del_note_from_db(note_name="Сходить купить машинку"),
            "Successfully deleted note",
        )
        self.assertEqual(del_note_from_db(note_name="Сходил"), "That note not in db")

    def test_13_insert_tag(self):
        """Testing to insert tag to note"""
        self.assertEqual(
            insert_tag(note_name="Сходить купить тачку", tag="Mazda"),
            "Successfully added tags",
        )
        self.assertEqual(
            insert_tag(note_name="Сходил", tag="Винчик"), "That note not in db"
        )

    def test_14_get_birthday_in_database(self):
        """Testing to get birthdays in some period of time"""
        self.assertEqual(
            get_birthday_in_database(days=50), get_birthday_in_database(days=50)
        )
