from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

books_db = [
    Book(id=1, title="1984", author="George Orwell"),
    Book(id=2, title="Brave New World", author="Aldous Huxley")
]

@app.get("/books", response_model=List[Book])
def list_books():
    return books_db

@app.post("/books", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
