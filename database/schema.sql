-- ==========================================
-- Library Management System Database Schema
-- ==========================================

-- Books table
-- Stores information about books

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
);

-- Members table
-- Stores library member information

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- Loans table
-- Stores book borrowing records

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,

    loan_date TEXT NOT NULL,
    return_date TEXT,

    FOREIGN KEY (book_id)
        REFERENCES books(id),

    FOREIGN KEY (member_id)
        REFERENCES members(id)
);