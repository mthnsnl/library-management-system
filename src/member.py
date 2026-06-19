"""
Member Management Module

This module handles all CRUD operations
for library members.

CRUD:
Create -> Add Member
Read   -> List Members
Update -> Update Member
Delete -> Delete Member
"""

from database import get_connection


def add_member(name, email):
    """
    Adds a new member to the database.

    Parameters:
        name (str)
        email (str)
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO members(name, email)
            VALUES (?, ?)
            """,
            (name, email)
        )

        connection.commit()

        print("Member added successfully.")

    except Exception as error:

        print("Error:", error)

    finally:

        connection.close()


def list_members():
    """
    Lists all members.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM members
        """
    )

    members = cursor.fetchall()

    print("\n===== MEMBER LIST =====")

    if not members:
        print("No members found.")

    else:

        for member in members:

            print(
                f"ID: {member[0]} | "
                f"Name: {member[1]} | "
                f"Email: {member[2]}"
            )

    connection.close()


def update_member(member_id, new_name, new_email):
    """
    Updates member information.

    Parameters:
        member_id (int)
        new_name (str)
        new_email (str)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE members
        SET name = ?,
            email = ?
        WHERE id = ?
        """,
        (
            new_name,
            new_email,
            member_id
        )
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Member updated successfully.")
    else:
        print("Member not found.")

    connection.close()


def delete_member(member_id):
    """
    Deletes a member.

    Parameters:
        member_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM members
        WHERE id = ?
        """,
        (member_id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Member deleted successfully.")
    else:
        print("Member not found.")

    connection.close()


def search_member(member_id):
    """
    Searches a member by ID.

    Parameters:
        member_id (int)
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM members
        WHERE id = ?
        """,
        (member_id,)
    )

    member = cursor.fetchone()

    if member:

        print(
            f"\nID: {member[0]}"
            f"\nName: {member[1]}"
            f"\nEmail: {member[2]}"
        )

    else:

        print("Member not found.")

    connection.close()