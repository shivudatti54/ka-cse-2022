# **SQLite Database in Android: Creation and Connection of the Database**

**Chapter 8: SQLite Database in Android**

## **Introduction**

In this chapter, we will learn about SQLite database in Android. SQLite is a lightweight, self-contained, zero-configuration database that is well-suited for use in mobile applications.

## **What is SQLite?**

SQLite is a SQL database that is designed to be used in embedded systems, such as smartphones, tablets, and other mobile devices. It is a self-contained database that does not require a separate server process to operate.

## **Key Features of SQLite**

- **Self-contained**: SQLite is a single file database that contains all the necessary data and code to operate.
- **Zero-configuration**: SQLite does not require any configuration or setup before it can be used.
- **Embedded**: SQLite can be embedded directly into an application, making it a good choice for mobile applications.
- **ACID compliant**: SQLite is ACID (Atomicity, Consistency, Isolation, Durability) compliant, which means that it ensures the reliability and integrity of database transactions.

## **Creating a SQLite Database**

To create a SQLite database in Android, we need to use the `SQLiteOpenHelper` class. This class provides a way to create and manage a SQLite database.

**Example Code**

```java
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "mydatabase.db";

    public DatabaseHelper(Context context) {
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

## **Connecting to a SQLite Database**

To connect to a SQLite database, we need to use the `SQLiteDatabase` class. This class provides a way to execute SQL queries on the database.

**Example Code**

```java
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseManager {
    private static final String DATABASE_NAME = "mydatabase.db";
    private static final String TABLE_NAME = "users";

    public DatabaseManager(Context context) {
        DatabaseHelper dbHelper = new DatabaseHelper(context);
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        // Execute SQL queries on the database
    }
}
```

## **SQL Queries**

SQL queries are used to manage data in a database. There are several types of SQL queries, including:

- **SELECT**: Retrieves data from a database.
- **INSERT**: Inserts data into a database.
- **UPDATE**: Updates data in a database.
- **DELETE**: Deletes data from a database.

**Example Code**

```java
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseManager {
    private static final String DATABASE_NAME = "mydatabase.db";
    private static final String TABLE_NAME = "users";

    public DatabaseManager(Context context) {
        DatabaseHelper dbHelper = new DatabaseHelper(context);
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        // Execute a SELECT query to retrieve data from the database
        String query = "SELECT * FROM users";
        Cursor cursor = db.rawQuery(query, null);
        // Process the retrieved data
    }
}
```

## **Best Practices for SQLite Database Development**

- **Use transactions**: Use transactions to ensure that multiple database operations are executed as a single, atomic unit.
- **Use parameterized queries**: Use parameterized queries to prevent SQL injection attacks.
- **Use indexes**: Use indexes to improve the performance of database queries.
- **Use caching**: Use caching to improve the performance of database queries.

## **Conclusion**

In this chapter, we learned about SQLite database in Android. We covered the basics of SQLite, including its features, creation, and connection. We also learned about SQL queries and best practices for SQLite database development. By following the examples and best practices outlined in this chapter, you can develop efficient and reliable SQLite databases for your Android applications.
