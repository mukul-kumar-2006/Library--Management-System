import sqlite3

class Member:
    @staticmethod
    def add_member(name, email):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

    @staticmethod
    def view_members():
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("SELECT * FROM members")
        members = c.fetchall()
        conn.close()
        return members
