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


def main():

    initialize_database()

    while True:

        print("\n==========================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("==========================")

        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Exit")

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

            print("Program terminated.")
            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()