from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# table for many-to-many relationship between notes and tags tables
note_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("note", Integer, ForeignKey("notes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)


# The contacts table, where the contacts will be stored
class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=True)
    birthday = Column(DateTime, nullable=False)
    email = Column(String(15), nullable=True)
    address = Column(String(15), nullable=True)


# The notes table, where the names of the to-do list will be stored
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.now())
    records = relationship("Record", cascade="all, delete", backref="note")
    tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")


# The records table, where records for a specific case from the notes table will be stored - one-to-one relationship, note_id field
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)
    note_id = Column(Integer, ForeignKey(Note.id, ondelete="CASCADE"))


# The tags table, where the set of tags for the to-do list is stored
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)