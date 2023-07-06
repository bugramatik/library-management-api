from fastapi import FastAPI
from app.api import books
from app.database import setup_database

setup_database()

app = FastAPI()

app.include_router(books.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
