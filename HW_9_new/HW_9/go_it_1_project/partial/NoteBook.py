from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from contact_book_models import Note, Record, Tag, Contact


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
        engine = create_engine("sqlite:////Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_9/contact_book.db")
        Session = sessionmaker(bind=engine)
        session = Session()
        contacts = []
        notes = Note(name=note.text)
        notes.tags = [Tag(name=tag.value) for tag in note.tags]
        contacts.append(Record(description=note.desc, note=notes))
        session.add_all(contacts)
        session.commit()

