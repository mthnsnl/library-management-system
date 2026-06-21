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
from loan import (
    borrow_book,
    return_book,
    list_active_loans,
    list_loan_history
)

"""
CLI Utility Functions

These functions improve user interaction.
"""

def print_header():
    """
    Prints application header.
    """

    print("\n" + "=" * 50)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)


def pause():
    """
    Waits for user input before continuing.
    """

    input("\nPress ENTER to continue...")


def get_integer(message):
    """
    Safely receives integer input.

    Returns:
        int
    """

    while True:

        try:

            value = int(input(message))

            return value

        except ValueError:

            print("Please enter a valid number.")

def display_menu():
    """
    Displays main menu.
    """

    print_header()

    print("\nBOOK OPERATIONS")
    print("1  - Add Book")
    print("2  - List Books")
    print("3  - Update Book")
    print("4  - Delete Book")
    print("5  - Search Book")

    print("\nMEMBER OPERATIONS")
    print("6  - Add Member")
    print("7  - List Members")
    print("8  - Update Member")
    print("9  - Delete Member")
    print("10 - Search Member")

    print("\nLOAN OPERATIONS")
    print("11 - Borrow Book")
    print("12 - Return Book")
    print("13 - Active Loans")
    print("14 - Loan History")

    print("\nSYSTEM")
    print("0  - Exit")

def main():

    initialize_database()

    while True:

        display_menu()
        
        choice = get_integer("\nSelect option: ")

        # CREATE

        if choice == 1:

            print("\nADD BOOK")

            title = input("Title: ")
            author = input("Author: ")
            year = get_integer("Year: ")

            add_book(title, author, year)

            pause()

        # READ

        elif choice == 2:

            print("\nLIST BOOKS")

            list_books()

            pause()

        # UPDATE

        elif choice == 3:

            print("\nUPDATE BOOK")

            book_id = get_integer("Book ID: ")
            title = input("New Title: ")
            author = input("New Author: ")
            year = get_integer("New Year: ")

            update_book(
                book_id,
                title,
                author,
                year
            )

            pause()

        # DELETE

        elif choice == 4:

            print("\nDELETE BOOK")

            book_id = get_integer("Book ID: ")

            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == "y":

                delete_book(book_id)

            pause()

        # SEARCH

        elif choice == 5:

            print("\nSEARCH BOOK")

            book_id = get_integer("Book ID: ")

            search_book(book_id)

            pause()

        elif choice == 6:

            print("\nADD MEMBER")

            name = input("Member Name: ")
            email = input("Email: ")

            add_member(name, email)

            pause()

        elif choice == 7:

            print("\nLIST MEMBERS")

            list_members()

            pause()

        elif choice == 8:

            print("\nUPDATE MEMBER")

            member_id = get_integer("Member ID: ")

            new_name = input("New Name: ")

            new_email = input("New Email: ")

            update_member(
                member_id,
                new_name,
                new_email
            )

            pause()

        elif choice == 9:

            print("\nDELETE MEMBER")

            member_id = get_integer("Member ID: ")

            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == "y":

                delete_member(member_id)

            pause()

        elif choice == 10:

            print("\nSEARCH MEMBER")

            member_id = get_integer("Member ID: ")

            search_member(member_id)

            pause()

        elif choice == 11:

            print("\nBORROW BOOK")

            book_id = get_integer("Book ID: ")

            member_id = get_integer("Member ID: ")

            borrow_book(
                book_id,
                member_id
            )

            pause()

        elif choice == 12:

            print("\nRETURN BOOK")

            loan_id = get_integer("Loan ID: ")

            return_book(
                loan_id
            )

            pause()

        elif choice == 13:

            print("\nLIST ACTIVE LOANS")

            list_active_loans()

            pause()

        elif choice == 14:

            print("\nLIST LOAN HISTORY")

            list_loan_history()

            pause()
        
        elif choice == 0:

            print("Program terminated.")

            break

        else:

            print("Invalid menu option.")

            pause()


if __name__ == "__main__":
    main()