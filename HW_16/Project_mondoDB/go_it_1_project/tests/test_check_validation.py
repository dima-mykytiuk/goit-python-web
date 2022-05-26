"""Imports for check validation"""
import unittest

from check_validation import (
    check_name_in_database,
    check_name,
    check_phone,
    check_birthday,
    check_email,
    check_address,
    check_note,
    check_note_validation,
)


class TestValidation(unittest.TestCase):
    """Class to test check_validation module"""

    def test_1_check_name_in_database(self):
        """Testing if name in database"""
        self.assertEqual(check_name_in_database(name="Zhenya"), True)
        self.assertEqual(check_name_in_database(name="Petya"), False)

    def test_2_check_name(self):
        """Testing name validation"""
        self.assertEqual(check_name(value="Sanya"), True)
        self.assertEqual(check_name(value="San"), False)

    def test_1_check_phone(self):
        """Testing phone validation"""
        self.assertEqual(check_phone(value="+380506074864"), True)
        self.assertEqual(check_phone(value="+3805"), False)
        self.assertEqual(check_phone(value="380506074864"), False)
        self.assertEqual(check_phone(value="hgdfhdfhdf"), False)

    def test_1_check_birthday(self):
        """Testing birthday validation"""
        self.assertEqual(check_birthday(value="1998-10-15"), True)
        self.assertEqual(check_birthday(value="gsdhshds"), False)
        self.assertEqual(check_birthday(value="10-1998-15"), False)
        self.assertEqual(check_birthday(value="1998-15-10"), False)

    def test_1_check_email(self):
        """Testing email validation"""
        self.assertEqual(check_email(value="smilecool2012@gmail.com"), True)
        self.assertEqual(check_email(value="Smilecool"), False)
        self.assertEqual(check_email(value="Smilecool@gmail.comhtfdjfgj"), False)

    def test_1_check_address(self):
        """Testing address validation"""
        self.assertEqual(check_address(value="Drayzera 2a"), True)
        self.assertEqual(check_address(value="Dray"), False)

    def test_1_check_note(self):
        """Testing if note in database"""
        self.assertEqual(check_note(name="Сходить купить тачку"), True)
        self.assertEqual(check_note(name="gsdgsdgs"), False)
        self.assertEqual(check_note(name="525235235"), False)

    def test_1_check_note_validation(self):
        """Testing note validation"""
        self.assertEqual(check_note_validation(name="qwerty"), True)
        self.assertEqual(check_note_validation(name="qwe"), False)
