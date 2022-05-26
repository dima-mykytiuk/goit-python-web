"""Imports for test notebook"""
import unittest

from go_it_1_project.src.notebook import Notes, save_note_in_database
from db_queries import del_note_from_db


class TestNoteBook(unittest.TestCase):
    """Class to test notebook module"""

    @classmethod
    def tearDownClass(cls) -> None:
        del_note_from_db(note_name="Сходить в кино")

    def test_save_in_database(self):
        """Testing save in database"""
        record = Notes(
            text="Сходить в кино",
            desc="Посмотреть человека паука",
            tags=["Марвел", "Человек паук"],
        )
        self.assertEqual(save_note_in_database(note=record), "Saved in database")
        self.assertEqual(save_note_in_database(note="Petya"), "Error illegal parameter")
        self.assertEqual(
            save_note_in_database(note="141241"), "Error illegal parameter"
        )
        self.assertEqual(
            save_note_in_database(note=41455152), "Error illegal parameter"
        )
