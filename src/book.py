"""
Book Management Module

This module handles all CRUD operations
for books in the library database.

CRUD:
Create  -> Add Book
Read    -> List Books
Update  -> Update Book
Delete  -> Delete Book
"""

from database import get_connection


def add_book(title, author, year):
    """
    Adds a new book to database.

    Parameters:
        title (str)
        author (str)
        year (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO books(title, author, year)
        VALUES (?, ?, ?)
        """,
        (title, author, year)
    )

    connection.commit()
    connection.close()

    print("Book added successfully.")


def list_books():
    """
    Lists all books in database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\n===== BOOK LIST =====")

    if not books:
        print("No books found.")

    else:
        for book in books:
            print(
                f"ID: {book[0]} | "
                f"Title: {book[1]} | "
                f"Author: {book[2]} | "
                f"Year: {book[3]}"
            )

    connection.close()


def update_book(book_id, new_title, new_author, new_year):
    """
    Updates a book record.

    Parameters:
        book_id (int)
        new_title (str)
        new_author (str)
        new_year (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE books
        SET title = ?,
            author = ?,
            year = ?
        WHERE id = ?
        """,
        (
            new_title,
            new_author,
            new_year,
            book_id
        )
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Book updated successfully.")
    else:
        print("Book not found.")

    connection.close()


def delete_book(book_id):
    """
    Deletes a book from database.

    Parameters:
        book_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Book deleted successfully.")
    else:
        print("Book not found.")

    connection.close()


def search_book(book_id):
    """
    Searches a book by id.

    Parameters:
        book_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    book = cursor.fetchone()

    if book:
        print(
            f"\nID: {book[0]}"
            f"\nTitle: {book[1]}"
            f"\nAuthor: {book[2]}"
            f"\nYear: {book[3]}"
        )
    else:
        print("Book not found.")

    connection.close()