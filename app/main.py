from fastapi import FastAPI
from app.api import books, students, borrows
from app.database import setup_database

setup_database()

app = FastAPI()

app.include_router(books.router)
app.include_router(students.router)
app.include_router(borrows.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
