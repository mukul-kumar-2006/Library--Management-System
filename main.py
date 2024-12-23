from book import Book
from member import Member
from issue_return import IssueReturn
from database import create_tables

print("✅ Library Management System Started!")

# Database tables create करें (सिर्फ पहली बार)
create_tables()

def main_menu():
    print("\n📚 Library Management System 📚")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

while True:
    user_choice = main_menu()
    
    if user_choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        Book.add_book(title, author)
        print(f"✅ Book '{title}' added successfully!")

    elif user_choice == "2":
        books = Book.view_books()
        for book in books:
            print(book)

    elif user_choice == "3":
        name = input("Enter member name: ")
        email = input("Enter member email: ")
        Member.add_member(name, email)
        print(f"✅ Member '{name}' added successfully!")

    elif user_choice == "4":
        members = Member.view_members()
        for member in members:
            print(member)

    elif user_choice == "5":
        book_id = int(input("Enter Book ID to issue: "))
        member_id = int(input("Enter Member ID: "))
        IssueReturn.issue_book(book_id, member_id)

    elif user_choice == "6":
        issue_id = int(input("Enter Issue ID to return: "))
        IssueReturn.return_book(issue_id)

    elif user_choice == "7":
        print("👋 Exiting the system. Goodbye!")
        break

    else:
        print(f"You selected option {user_choice}. (Feature not implemented yet)")