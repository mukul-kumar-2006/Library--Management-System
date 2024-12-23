import sqlite3
from datetime import datetime

class IssueReturn:
    @staticmethod
    def issue_book(book_id, member_id):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        
        # Check if book is available
        c.execute("SELECT available FROM books WHERE id = ?", (book_id,))
        book = c.fetchone()
        
        if book and book[0] == 1:
            issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO issued_books (book_id, member_id, issue_date) VALUES (?, ?, ?)", 
                      (book_id, member_id, issue_date))
            c.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
            conn.commit()
            print(f"✅ Book {book_id} issued to Member {member_id} on {issue_date}")
        else:
            print(f"❌ Book {book_id} is not available for issue.")

        conn.close()

    @staticmethod
    def return_book(issue_id):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()

        # Check if issue record exists
        c.execute("SELECT book_id FROM issued_books WHERE id = ?", (issue_id,))
        issue_record = c.fetchone()
        
        if issue_record:
            book_id = issue_record[0]
            return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("UPDATE issued_books SET return_date = ? WHERE id = ?", (return_date, issue_id))
            c.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
            conn.commit()
            print(f"✅ Book {book_id} returned successfully on {return_date}")
        else:
            print(f"❌ Issue record {issue_id} not found!")

        conn.close()