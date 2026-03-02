# SQLite Database Creation and Connection

## Overview

Creating and connecting to SQLite databases in Android requires extending SQLiteOpenHelper and implementing database operations. Proper connection management ensures data integrity and prevents resource leaks.

## Key Points

- **Extend SQLiteOpenHelper**: Override onCreate() and onUpgrade() methods
- **Database Connection**: getWritableDatabase() for write, getReadableDatabase() for read
- **Table Creation**: Execute CREATE TABLE SQL in onCreate() method
- **Data Types**: INTEGER, TEXT, REAL, BLOB supported
- **Database Path**: Automatically managed in app's private storage
- **Connection Pooling**: SQLiteDatabase handles connections efficiently

## Important Concepts

- Singleton pattern for database helper prevents multiple instances
- Database opened lazily on first getDatabase() call
- Foreign keys disabled by default, enable with PRAGMA
- Database operations should run on background thread
- Use try-finally blocks to ensure database closing

## Notes

- Create database helper as singleton
- Define table schema as constants for reusability
- Test database operations with dummy data
- Consider using Room for type-safe database access
