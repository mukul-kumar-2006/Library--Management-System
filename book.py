import sqlite3

class Book:
    @staticmethod
    def add_book(title, author):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        conn.close()

    @staticmethod
    def view_books():
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        conn.close()
        return books
