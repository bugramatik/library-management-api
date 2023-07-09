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
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print("An error occurred during table creation:", str(e))


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
