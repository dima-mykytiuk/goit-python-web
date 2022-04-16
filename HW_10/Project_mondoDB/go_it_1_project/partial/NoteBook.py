from mongoengine import connect
from HW_10.Project_mondoDB.contact_book_models import *


class Tags:
    def __init__(self, value: str) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value


class Notes:
    def __init__(self, text: str, desc: str, tags=[]) -> None:
        self.text = text
        self.id = id
        self.desc = desc
        if len(tags) != 0:
            self.tags = [Tags(tag) for tag in tags]
        else:
            self.tags = []


class NoteBook:
    """
    Desrcibes object fo personal book with notes
    """

    def save_note_in_database(self, note: Notes):
        connect(host=f"mongodb://localhost:27017/address_book")
        Note(name=note.text,
             records=[Record(description=note.desc), ],
             tags=[Tag(name=tag.value) for tag in note.tags],).save()

