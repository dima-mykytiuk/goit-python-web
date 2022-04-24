from sqlalchemy import Column, Integer, String, Date
from db.db import Base, engine, db_session


class Matches(Base):
    __tablename__ = "matches_epl"
    id = Column(Integer, primary_key=True)
    football_match = Column(String(50), nullable=False)
    score = Column(String(15), nullable=False)
    match_date = Column(Date, nullable=False)


class Matches_NHL_Tribuna(Base):
    __tablename__ = "matches_nhl_tribuna"
    id = Column(Integer, primary_key=True)
    nhl_match = Column(String(50), nullable=False)
    score = Column(String(15), nullable=True)
    match_date = Column(Date, nullable=False)


class Matches_Italian_Football(Base):
    __tablename__ = "matches_italian_football"
    id = Column(Integer, primary_key=True)
    match = Column(String(50), nullable=False)
    score = Column(String(15), nullable=True)


if __name__ == "__main__":
    Base.metadata.create_all(engine)