# SQLite Database in Android: Creation and Connection of the Database

===========================================================

## Table of Contents

---

1. [Introduction](#introduction)
2. [What is SQLite?](#what-is-sqlite)
3. [Creating a SQLite Database in Android](#creating-a-sqlite-database-in-android)
4. [Connecting to a SQLite Database in Android](#connecting-to-a-sqlite-database-in-android)
5. [Key Concepts](#key-concepts)

## Introduction

---

In this chapter, we will explore the basics of SQLite database in Android. SQLite is a self-contained, file-based relational database that can be used to store and manage data in an Android application. It is a powerful tool for storing and retrieving data, and is widely used in Android development.

## What is SQLite?

---

SQLite is a lightweight, server-less relational database that can be embedded in an application. It is a zero-configuration database, meaning that no additional setup or configuration is required to use it. SQLite databases are stored on the device as a single file, and can be easily accessed and manipulated using SQL (Structured Query Language) commands.

### Key Features of SQLite:

- **Self-contained**: SQLite databases are stored as a single file, making them easy to manage and transport.
- **Relational**: SQLite databases are based on a relational model, allowing for easy creation of tables, relationships, and complex queries.
- **Zero-configuration**: SQLite databases do not require any additional setup or configuration to use.
- **Powerful**: SQLite supports a wide range of SQL commands and features, making it a powerful tool for storing and retrieving data.

## Creating a SQLite Database in Android

---

To create a SQLite database in Android, you can use the `SQLiteDatabase` class. This class provides methods for creating, opening, and closing a database connection.

### Creating a Database Instance

To create a database instance, you can use the following code:

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create the tables
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the tables
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }
}
```

### Creating a Database File

You can also create a database file manually and store it in the application's `assets` directory. This can be useful if you want to distribute your application with a pre-populated database.

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create the tables
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the tables
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }
}
```

## Connecting to a SQLite Database in Android

---

To connect to a SQLite database in Android, you can use the `SQLiteDatabase` class. This class provides methods for opening, closing, and executing SQL commands.

### Opening a Database Connection

To open a database connection, you can use the following code:

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create the tables
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the tables
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }

    public SQLiteDatabase openDatabase() {
        return getReadableDatabase();
    }
}
```

### Executing SQL Commands

To execute SQL commands, you can use the `executeSQL()` method of the `SQLiteDatabase` class.

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create the tables
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the tables
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }

    public void insertUser(String name, String email) {
        SQLiteDatabase db = openDatabase();
        db.execSQL("INSERT INTO users (name, email) VALUES ('" + name + "', '" + email + "')");
        db.close();
    }

    public void deleteUser(int id) {
        SQLiteDatabase db = openDatabase();
        db.execSQL("DELETE FROM users WHERE _id = " + id);
        db.close();
    }
}
```

## Key Concepts

---

- **Database Creation**: A SQLite database can be created using the `SQLiteDatabase` class.
- **Database Connection**: A database connection can be established using the `openDatabase()` method of the `SQLiteOpenHelper` class.
- **SQL Commands**: SQL commands can be executed using the `executeSQL()` method of the `SQLiteDatabase` class.
- **Table Creation**: Tables can be created using the `CREATE TABLE` SQL command.
- **Table Insertion**: Data can be inserted into tables using the `INSERT INTO` SQL command.
- **Table Deletion**: Data can be deleted from tables using the `DELETE FROM` SQL command.

### Best Practices:

- **Use Prepared Statements**: Prepared statements can be used to prevent SQL injection attacks.
- **Close Database Connections**: Database connections should be closed after use to conserve resources.
- **Use Transactions**: Transactions can be used to ensure data consistency and integrity.
