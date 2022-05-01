from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine(
    "sqlite:////Users/dimamykytiuk/PycharmProjects/go_it_web/goit-python-web/HW_13/test_spyder/quotes.db", connect_args={"check_same_thread": False}, echo=True
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()