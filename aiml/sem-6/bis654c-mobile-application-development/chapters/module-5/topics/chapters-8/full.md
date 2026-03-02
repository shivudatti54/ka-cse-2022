# SQLite Database in Android: SQLite Database – Creation and Connection of the database

=====================================================

# Introduction

---

SQLite is a self-contained, file-based relational database that can be used with Android applications. It is a popular choice for Android app development due to its ease of use, flexibility, and performance. In this chapter, we will explore the creation and connection of a SQLite database in Android, including its historical context, modern developments, and applications.

## Historical Context

---

SQLite was first developed in 1996 by David V. Hyatt and is now maintained by the SQLite Association. It was designed to be a lightweight, self-contained database that could be used in embedded systems and other applications where a full-fledged database management system was not necessary.

SQLite was first released as an open-source project in 1999 and has since become one of the most popular database systems used in Android app development.

## Modern Developments

---

SQLite has undergone significant developments over the years, including:

- **SQL Support**: SQLite now supports a wide range of SQL commands, including SELECT, INSERT, UPDATE, and DELETE.
- **ACID Compliance**: SQLite now complies with the Atomicity, Consistency, Isolation, and Durability (ACID) principles, ensuring that database transactions are processed reliably and securely.
- **Security**: SQLite now includes built-in support for encryption and access control, ensuring that sensitive data is protected from unauthorized access.

## Applications

---

SQLite is widely used in Android app development for a variety of applications, including:

- **Data Storage**: SQLite is often used to store application data, such as user preferences, settings, and other metadata.
- **Caching**: SQLite is often used to cache data retrieved from external sources, such as web services or APIs.
- **Offline Data Access**: SQLite is often used to provide offline data access for Android apps, allowing users to access data even when internet connectivity is unavailable.

## Android SQLite Database Basics

---

Before we dive into the details of creating and connecting to a SQLite database in Android, let's cover some basic concepts:

- **Database File**: SQLite stores its database in a file with a `.db` extension. The default database file name is `databases.sqlite`.
- **Database Schema**: The database schema defines the structure of the database, including the tables, columns, and relationships between them.
- **Database Transactions**: Database transactions ensure that multiple operations are processed reliably and securely.

## Creating a SQLite Database in Android

---

To create a SQLite database in Android, we need to:

1.  Create a new SQLiteOpenHelper class that extends the `SQLiteOpenHelper` class.
2.  Override the `onCreate()` method to create the database schema.
3.  Override the `onUpgrade()` method to handle database upgrades.

Here's an example of creating a SQLite database in Android:

```java
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDatabaseHelper extends SQLiteOpenHelper {

    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public MyDatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }
}
```

## Connecting to a SQLite Database in Android

---

To connect to a SQLite database in Android, we need to:

1.  Create a new SQLiteDatabase object that extends the `SQLiteDatabase` class.
2.  Use the `open()` method to connect to the database file.
3.  Use the `execSQL()` method to execute SQL commands.

Here's an example of connecting to a SQLite database in Android:

```java
import android.database.sqlite.SQLiteDatabase;

public class MyDatabase {
    private static final String DATABASE_NAME = "mydatabase.db";

    public static SQLiteDatabase getDatabase(Context context) {
        SQLiteDatabase db = context.openOrCreateDatabase(DATABASE_NAME, context.MODE_READ_WRITE, null);

        return db;
    }
}
```

## Inserting Data into a SQLite Database

---

To insert data into a SQLite database, we need to:

1.  Create a new SQLiteDatabase object that extends the `SQLiteDatabase` class.
2.  Use the `execSQL()` method to execute an INSERT command.

Here's an example of inserting data into a SQLite database:

```java
import android.database.sqlite.SQLiteDatabase;

public class MyDatabase {
    public static void insertData(SQLiteDatabase db, String name, String email) {
        String insertQuery = "INSERT INTO users (name, email) VALUES ('" + name + "', '" + email + "')";
        db.execSQL(insertQuery);
    }
}
```

## Retrieving Data from a SQLite Database

---

To retrieve data from a SQLite database, we need to:

1.  Create a new SQLiteDatabase object that extends the `SQLiteDatabase` class.
2.  Use the `execSQL()` method to execute a SELECT command.
3.  Use a Cursor to retrieve the data.

Here's an example of retrieving data from a SQLite database:

```java
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.Cursor;

public class MyDatabase {
    public static void retrieveData(SQLiteDatabase db) {
        String selectQuery = "SELECT * FROM users";
        Cursor cursor = db.rawQuery(selectQuery, null);

        while (cursor.moveToNext()) {
            int id = cursor.getInt(0);
            String name = cursor.getString(1);
            String email = cursor.getString(2);

            System.out.println("ID: " + id + ", Name: " + name + ", Email: " + email);
        }

        cursor.close();
    }
}
```

## Conclusion

---

In this chapter, we explored the creation and connection of a SQLite database in Android, including its historical context, modern developments, and applications. We also covered the basics of creating and connecting to a SQLite database, inserting data, retrieving data, and handling database transactions.

## Further Reading

---

- [SQLite Documentation](https://www.sqlite.org/)
- [Android SQLite Database Tutorial](https://developer.android.com/training/basics/data storage/sqlite)
- [SQLite in Android - BBVA](https://www.bbc.es/ciberseguridad/banco-de-pruebas/jsonData/SQLiteAndroid.pdf)
