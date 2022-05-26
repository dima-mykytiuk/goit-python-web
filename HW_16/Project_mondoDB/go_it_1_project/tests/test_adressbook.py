"""Imports for test adressbook"""
import unittest

from go_it_1_project.src.adressbook import RecordContacts, save_in_database
from db_queries import del_contact_from_db

record_to_test = RecordContacts(
    name="Dima", phones=None, birthday=None, email=None, address=None
)


class TestAddressBook(unittest.TestCase):
    """Class to test adressbook module"""

    @classmethod
    def tearDownClass(cls) -> None:
        del_contact_from_db(contact_name="Vlad")

    def test_save_in_database(self):
        """Testing save in database"""
        record = RecordContacts(
            name="Vlad",
            phones="+380956074864",
            birthday="1992-10-15",
            email="smisfs@gmail.com",
            address="Balza 4",
        )
        self.assertEqual(save_in_database(contact=record), "Saved in database")
        self.assertEqual(save_in_database(contact="Petya"), "Error illegal parameter")
        self.assertEqual(save_in_database(contact="141241"), "Error illegal parameter")
        self.assertEqual(save_in_database(contact=41455152), "Error illegal parameter")

    def test_add_phone(self):
        """Testing adding phone to RecordContacts object"""
        self.assertEqual(
            record_to_test.add_phone("+380506074864"), "Successfully set phone"
        )
        self.assertEqual(record_to_test.add_phone("+3805060"), "Invalid phone format")
        self.assertEqual(
            record_to_test.add_phone("380506074864"), "Invalid phone format"
        )
        self.assertEqual(record_to_test.add_phone("fhdhfddsgg"), "Invalid phone format")

    def test_add_birthday(self):
        """Testing adding birthday to RecordContacts object"""
        self.assertEqual(
            record_to_test.add_birthday("1998-10-12"), "Successfully set birthday"
        )
        self.assertEqual(
            record_to_test.add_birthday("10-12-1998"), "Invalid birthday format"
        )
        self.assertEqual(
            record_to_test.add_birthday("gdsgsdgsdgs"), "Invalid birthday format"
        )
        self.assertEqual(
            record_to_test.add_birthday(54353453), "Invalid birthday format"
        )

    def test_add_email(self):
        """Testing adding email to RecordContacts object"""
        self.assertEqual(
            record_to_test.add_email("Smilecool2012@gmail.com"),
            "Successfully set email",
        )
        self.assertEqual(record_to_test.add_email("Smilecool"), "Invalid email format")
        self.assertEqual(
            record_to_test.add_email("Smilecool@gmail.comhtffg"), "Invalid email format"
        )

    def test_add_address(self):
        """Testing adding address to RecordContacts object"""
        self.assertEqual(
            record_to_test.add_address("Drayzera 2a"), "Successfully set address"
        )
        self.assertEqual(record_to_test.add_address("Dray"), "Invalid address format")
        self.assertEqual(record_to_test.add_address("w"), "Invalid address format")
