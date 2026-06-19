"""
Database Module

Responsible for:
- Creating database connection
- Creating tables
- Initializing database schema

Library Management System
"""

import sqlite3

# SQLite database file name
DB_NAME = "library.db"


def get_connection():
    """
    Creates and returns a database connection.

    Returns:
        sqlite3.Connection
    """

    connection = sqlite3.connect(DB_NAME)

    return connection


def create_tables():
    """
    Creates all database tables if they do not exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    # --------------------------
    # Books Table
    # --------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    """)

    # --------------------------
    # Members Table
    # --------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    # --------------------------
    # Loans Table
    # --------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            book_id INTEGER NOT NULL,
            member_id INTEGER NOT NULL,

            loan_date TEXT NOT NULL,
            return_date TEXT,

            FOREIGN KEY(book_id)
                REFERENCES books(id),

            FOREIGN KEY(member_id)
                REFERENCES members(id)
        )
    """)

    connection.commit()
    connection.close()


def initialize_database():
    """
    Initializes the database.

    This function is called when the
    application starts for the first time.
    """

    create_tables()

    print("Database initialized successfully.")


# Test purpose only
if __name__ == "__main__":
    initialize_database()