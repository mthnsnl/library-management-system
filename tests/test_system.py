"""
Library Management System Tests

This module tests:

1. Database connection
2. Book CRUD operations
3. Member CRUD operations
4. Loan operations
"""

import unittest
import os
import sys

# src klasörünü Python path'ine ekle
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from database import (
    initialize_database,
    get_connection
)

from book import (
    add_book
)

from member import (
    add_member
)

from loan import (
    borrow_book
)


class LibrarySystemTests(unittest.TestCase):

    """
    Main test class
    """

    @classmethod
    def setUpClass(cls):
        """
        Runs once before all tests.
        """

        initialize_database()

    def test_database_connection(self):
        """
        Tests database connection.
        """

        connection = get_connection()

        self.assertIsNotNone(
            connection
        )

        connection.close()

    def test_add_book(self):
        """
        Tests adding a book.
        """

        add_book(
            "Test Book",
            "Test Author",
            2025
        )

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM books
            WHERE title = ?
            """,
            ("Test Book",)
        )

        result = cursor.fetchone()

        connection.close()

        self.assertIsNotNone(
            result
        )

    def test_add_member(self):
        """
        Tests adding a member.
        """

        add_member(
            "Test Member",
            "testmember@email.com"
        )

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM members
            WHERE email = ?
            """,
            (
                "testmember@email.com",
            )
        )

        result = cursor.fetchone()

        connection.close()

        self.assertIsNotNone(
            result
        )

    def test_borrow_book(self):
        """
        Tests loan creation.
        """

        connection = get_connection()
        cursor = connection.cursor()

        # Test book

        cursor.execute(
            """
            INSERT INTO books
            (
                title,
                author,
                year
            )
            VALUES
            (
                'Loan Test Book',
                'Author',
                2025
            )
            """
        )

        book_id = cursor.lastrowid

        # Test member

        cursor.execute(
            """
            INSERT INTO members
            (
                name,
                email
            )
            VALUES
            (
                'Loan User',
                'loanuser@test.com'
            )
            """
        )

        member_id = cursor.lastrowid

        connection.commit()

        connection.close()

        borrow_book(
            book_id,
            member_id
        )

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM loans
            WHERE book_id = ?
            """,
            (book_id,)
        )

        result = cursor.fetchone()

        connection.close()

        self.assertIsNotNone(
            result
        )


if __name__ == "__main__":

    unittest.main()