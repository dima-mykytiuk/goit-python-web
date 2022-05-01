from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from test_spyder.db.db import Base, engine, db_session

# table for many-to-many relationship between notes and tags tables
quote_m2m_tag = Table(
    "quote_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("quote", Integer, ForeignKey("quotes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)


# The notes table, where the names of the to-do list will be stored
class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    quote = Column(String(400), nullable=False)
    link = Column(String(100), nullable=False)
    tags = relationship("Tag", secondary=quote_m2m_tag, backref="quotes")


class Biography(Base):
    __tablename__ = "biography"
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    birthday = Column(String(400), nullable=False)
    born_location = Column(String(100), nullable=False)
    biography = Column(String(5000), nullable=False)

# The records table, where records for a specific case from the notes table will be stored - one-to-one relationship, note_id field


# The tags table, where the set of tags for the to-do list is stored
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=False)
    
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)