"""
Library Management System

Main menu for book operations.
"""

from database import initialize_database
from book import (
    add_book,
    list_books,
    update_book,
    delete_book,
    search_book
)
from member import (
    add_member,
    list_members,
    update_member,
    delete_member,
    search_member
)


def main():

    initialize_database()

    while True:

        print("\n==========================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("==========================")

        print("BOOK OPERATIONS")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")

        print("\nMEMBER OPERATIONS")
        print("6. Add Member")
        print("7. List Members")
        print("8. Update Member")
        print("9. Delete Member")
        print("10. Search Member")

        print("\n0. Exit")

        choice = input("\nSelect an option: ")

        # CREATE

        if choice == "1":

            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))

            add_book(title, author, year)

        # READ

        elif choice == "2":

            list_books()

        # UPDATE

        elif choice == "3":

            book_id = int(input("Book ID: "))

            title = input("New Title: ")
            author = input("New Author: ")
            year = int(input("New Year: "))

            update_book(
                book_id,
                title,
                author,
                year
            )

        # DELETE

        elif choice == "4":

            book_id = int(input("Book ID: "))

            delete_book(book_id)

        # SEARCH

        elif choice == "5":

            book_id = int(input("Book ID: "))

            search_book(book_id)

        elif choice == "6":

            name = input("Member Name: ")
            email = input("Email: ")

            add_member(name, email)

        elif choice == "7":

            list_members()

        elif choice == "8":

            member_id = int(
                input("Member ID: ")
            )

            new_name = input(
                "New Name: "
            )

            new_email = input(
                "New Email: "
            )

            update_member(
                member_id,
                new_name,
                new_email
            )

        elif choice == "9":

            member_id = int(
                input("Member ID: ")
            )

            delete_member(member_id)

        elif choice == "10":

            member_id = int(
                input("Member ID: ")
            )

            search_member(member_id)
        
        elif choice == "0":

            print("Program terminated.")
            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()