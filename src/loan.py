"""
Loan Management Module

Handles all loan operations.

Features:
- Borrow book
- Return book
- List active loans
- List loan history
"""

from database import get_connection
from datetime import datetime


def borrow_book(book_id, member_id):
    """
    Creates a new loan record.

    Parameters:
        book_id (int)
        member_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    # Check if book exists

    cursor.execute(
        """
        SELECT *
        FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    book = cursor.fetchone()

    if not book:

        print("Book not found.")

        connection.close()

        return

    # Check if member exists

    cursor.execute(
        """
        SELECT *
        FROM members
        WHERE id = ?
        """,
        (member_id,)
    )

    member = cursor.fetchone()

    if not member:

        print("Member not found.")

        connection.close()

        return

    # Check if book is already borrowed

    cursor.execute(
        """
        SELECT *
        FROM loans
        WHERE book_id = ?
        AND return_date IS NULL
        """,
        (book_id,)
    )

    active_loan = cursor.fetchone()

    if active_loan:

        print("This book is already borrowed.")

        connection.close()

        return

    # Create loan

    loan_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        INSERT INTO loans
        (
            book_id,
            member_id,
            loan_date
        )
        VALUES (?, ?, ?)
        """,
        (
            book_id,
            member_id,
            loan_date
        )
    )

    connection.commit()

    print("Book borrowed successfully.")

    connection.close()


def return_book(loan_id):
    """
    Returns a borrowed book.

    Parameters:
        loan_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    return_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        UPDATE loans
        SET return_date = ?
        WHERE id = ?
        AND return_date IS NULL
        """,
        (
            return_date,
            loan_id
        )
    )

    connection.commit()

    if cursor.rowcount > 0:

        print("Book returned successfully.")

    else:

        print("Loan not found or already returned.")

    connection.close()


def list_active_loans():
    """
    Lists all active loans.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            loans.id,
            books.title,
            members.name,
            loans.loan_date

        FROM loans

        JOIN books
        ON loans.book_id = books.id

        JOIN members
        ON loans.member_id = members.id

        WHERE loans.return_date IS NULL
        """
    )

    loans = cursor.fetchall()

    print("\n===== ACTIVE LOANS =====")

    if not loans:

        print("No active loans.")

    else:

        for loan in loans:

            print(
                f"Loan ID: {loan[0]} | "
                f"Book: {loan[1]} | "
                f"Member: {loan[2]} | "
                f"Loan Date: {loan[3]}"
            )

    connection.close()


def list_loan_history():
    """
    Lists all loan records.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            loans.id,
            books.title,
            members.name,
            loans.loan_date,
            loans.return_date

        FROM loans

        JOIN books
        ON loans.book_id = books.id

        JOIN members
        ON loans.member_id = members.id

        ORDER BY loans.id DESC
        """
    )

    loans = cursor.fetchall()

    print("\n===== LOAN HISTORY =====")

    if not loans:

        print("No loan records found.")

    else:

        for loan in loans:

            print(
                f"Loan ID: {loan[0]} | "
                f"Book: {loan[1]} | "
                f"Member: {loan[2]} | "
                f"Loan Date: {loan[3]} | "
                f"Return Date: {loan[4]}"
            )

    connection.close()