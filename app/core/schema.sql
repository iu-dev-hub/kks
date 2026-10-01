-- Kampüs Kütüphane Sistemi: initial schema
--
-- Bu şema bir BAŞLANGIÇ noktasıdır. Ekipler Sprint 2'de arayüz sözleşmesini
-- (docs/interface-contract.md) yaparken tabloları birlikte genişletecektir.
-- Bir tabloya sütun eklemek diğer ekipleri etkileyebilir: önce konuşun!

DROP TABLE IF EXISTS fines;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;

-- Owner: Team Membership
CREATE TABLE users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    email         TEXT    NOT NULL UNIQUE,
    password_hash TEXT    NOT NULL,
    full_name     TEXT    NOT NULL,
    role          TEXT    NOT NULL CHECK (role IN ('student', 'academic', 'librarian'))
);

-- Owner: Team Catalog
CREATE TABLE books (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn    TEXT    NOT NULL UNIQUE,
    title   TEXT    NOT NULL,
    author  TEXT    NOT NULL,
    status  TEXT    NOT NULL DEFAULT 'on_shelf'
            CHECK (status IN ('on_shelf', 'on_loan', 'overdue', 'reserved'))
);

-- Owner: Team Loans
CREATE TABLE loans (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      INTEGER NOT NULL REFERENCES users (id),
    book_id      INTEGER NOT NULL REFERENCES books (id),
    borrowed_at  TEXT    NOT NULL,
    due_date     TEXT    NOT NULL,
    returned_at  TEXT
);

-- Owner: Team Fines-Reports
CREATE TABLE fines (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id  INTEGER NOT NULL REFERENCES loans (id),
    amount   INTEGER NOT NULL,
    paid     INTEGER NOT NULL DEFAULT 0
);
