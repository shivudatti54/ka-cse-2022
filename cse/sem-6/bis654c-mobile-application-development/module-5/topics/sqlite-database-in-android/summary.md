# SQLite Database in Android

## Overview

SQLite is Android's built-in relational database for local data storage. SQLiteOpenHelper simplifies database creation, version management, and operations, enabling structured data persistence.

## Key Points

- **SQLiteOpenHelper**: Abstract class managing database creation and version upgrades
- **onCreate()**: Creates tables when database first accessed
- **onUpgrade()**: Handles database schema changes during version updates
- **CRUD Operations**: Create (insert), Read (query), Update, Delete via SQLiteDatabase
- **Cursor**: Result set iterator for query results
- **ContentValues**: Key-value pairs for insert/update operations
- **Transactions**: Begin, commit, rollback for atomic operations

## Important Concepts

- Database stored in /data/data/package/databases/
- Primary keys with AUTOINCREMENT for unique IDs
- Raw SQL vs SQLiteDatabase helper methods
- Close Cursor and Database to prevent memory leaks
- Database version increments trigger onUpgrade()

## Notes

- Always close cursors after use
- Use transactions for multiple related operations
- Practice writing CREATE TABLE statements
- Understand when to use Room (modern alternative) vs raw SQLite
