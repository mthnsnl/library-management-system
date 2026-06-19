"""
Library Management System
Main Application Entry Point
"""

from database import initialize_database


def main():

    initialize_database()

    print("Library Management System Started")


if __name__ == "__main__":
    main()