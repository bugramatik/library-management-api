from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

Base = declarative_base()

from database import Student, BookType, Book, Borrow

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="lmsdb",
    port=5432
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Drop all tables in the database
Base.metadata.drop_all(engine)

# Recreate all tables
Base.metadata.create_all(engine)

print("Database reset complete.")
