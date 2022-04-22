
from datetime import datetime

import faker
from sqlalchemy import Column, Integer, String, Boolean, create_engine, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table, MetaData
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import sessionmaker
from HW_11.config.db import Base, engine, db_session

# таблица для связи many2many

note_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("note", Integer, ForeignKey("notes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=True)
    birthday = Column(Date, nullable=False)
    email = Column(String(15), nullable=True)
    address = Column(String(15), nullable=True)
    
    
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(Date, default=datetime.now())
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)
    tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)

    def __repr__(self) -> str:
        return self.name
    
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)