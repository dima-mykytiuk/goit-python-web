"""Imports for test sorter"""
import unittest

from go_it_1_project.src.sorter import sort, normalize


class TestSorter(unittest.TestCase):
    """Class to test sorter module"""

    def test_sort(self):
        """Testing if directory for sort is valid"""
        self.assertEqual(
            sort(_dir="/Users/dimamykytiuk/Desktop/Новая папка"), "Successfully sorted"
        )
        self.assertEqual(sort(_dir="Petya"), "No such directory.")
        self.assertEqual(sort(_dir="141241"), "No such directory.")

    def test_normalize(self):
        """Testing name normalize"""
        self.assertEqual(normalize("Новая папка"), "Novaya_papka")
        self.assertEqual(normalize("Звіт з практики"), "Zvit_z_praktyky")
