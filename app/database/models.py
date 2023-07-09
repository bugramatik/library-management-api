from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    borrowed_books = relationship("Borrow", back_populates="student")


class BookType(Base):
    __tablename__ = "book_types"

    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String)
    books = relationship("Book", back_populates="book_type")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    copy_number = Column(Integer)
    book_type_id = Column(Integer, ForeignKey("book_types.id", ondelete="SET NULL", onupdate="CASCADE"))
    book_type = relationship("BookType", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE", onupdate="CASCADE"))
    student = relationship("Student", back_populates="borrowed_books")
    book = relationship("Book", back_populates="borrows")


