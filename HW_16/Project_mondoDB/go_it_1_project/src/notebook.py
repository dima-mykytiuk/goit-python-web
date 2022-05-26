# pylint: disable=too-few-public-methods
"""Imports for notebook"""
from mongoengine import connect
from contact_book_models import Note, Record, Tag


class Tags:
    """Init tags"""

    def __init__(self, value: str) -> None:
        self.value = value

    @property
    def values(self):
        """Getter"""
        return self.__value

    @values.setter
    def values(self, value: str) -> None:
        self.__value = value


class Notes:
    """Init class Notes"""

    def __init__(self, text: str, desc: str, tags: list) -> None:
        self.text = text
        self.tag_id = id
        self.desc = desc
        if len(tags) != 0:
            self.tags = [Tags(tag) for tag in tags]
        else:
            self.tags = []


def save_note_in_database(note: Notes):
    """Save note in database"""
    if isinstance(note, Notes):
        connect(host="mongodb://localhost:27017/address_book")
        Note(
            name=note.text,
            records=[
                Record(description=note.desc),
            ],
            tags=[Tag(name=tag.value) for tag in note.tags],
        ).save()
    else:
        return "Error illegal parameter"
    return "Saved in database"
