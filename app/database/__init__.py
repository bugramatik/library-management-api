from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .models import Student, BookType, Book, Borrow

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="lmsdb",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


def setup_database():
    Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
