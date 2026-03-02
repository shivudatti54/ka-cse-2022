# **SQLite Database in Android: Creation and Connection of the database**

## **Table of Contents**

1. [Introduction](#introduction)
2. [What is SQLite?](#what-is-sqlite)
3. [Benefits of Using SQLite in Android](#benefits-of-using-sqlite-in-android)
4. [Creating a SQLite Database in Android](#creating-a-sqlite-database-in-android)
5. [Connecting to a SQLite Database in Android](#connecting-to-a-sqlite-database-in-android)
6. [Example SQLite Database Creation and Connection](#example-sqlite-database-creation-and-connection)

## **Introduction**

In Android, SQLite is a lightweight, self-contained database that can be used to store data locally on the device. SQLite is widely used in mobile applications due to its ease of use, flexibility, and ability to support complex queries.

## **What is SQLite?**

SQLite is a relational database management system (RDBMS) that is based on the SQL (Structured Query Language) language. It is designed to be lightweight and easy to use, making it an ideal choice for mobile applications.

## **Benefits of Using SQLite in Android**

- **Easy to use**: SQLite has a simple and intuitive API that makes it easy to use in Android applications.
- **Flexible**: SQLite supports a wide range of data types, including integers, strings, and dates.
- **Relational**: SQLite supports complex queries and relationships between tables.

## **Creating a SQLite Database in Android**

To create a SQLite database in Android, you need to follow these steps:

- **Create a new SQLiteOpenHelper class**: This class is responsible for creating and managing the SQLite database.
- **Create a database object**: In the SQLiteOpenHelper class, create a database object using the `openDatabase()` method.
- **Create a table**: Use the `createTable()` method to create a new table in the database.
- **Insert data**: Use the `insert()` method to insert data into the table.

## **Connecting to a SQLite Database in Android**

To connect to a SQLite database in Android, you need to follow these steps:

- **Create a connection**: Use the `connect()` method to create a connection to the SQLite database.
- **Create a cursor**: Use the `createCursor()` method to create a cursor object that can be used to execute queries.
- **Execute queries**: Use the `executeQuery()` method to execute queries on the database.
- **Close the connection**: Use the `close()` method to close the connection to the SQLite database.

## **Example SQLite Database Creation and Connection**

Here is an example of how to create a SQLite database and connect to it in an Android application:

```java
import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDatabase extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "mydatabase.db";

    public MyDatabase(Context context) {
        super(context, DATABASE_NAME, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }
}

public class MainActivity extends AppCompatActivity {
    private MyDatabase db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        db = new MyDatabase(this);

        // Create a connection to the database
        SQLiteDatabase dbConnection = db.getWritableDatabase();

        // Create a cursor object
        Cursor cursor = dbConnection.rawQuery("SELECT * FROM users", null);

        // Execute queries
        while (cursor.moveToNext()) {
            int id = cursor.getInt(0);
            String name = cursor.getString(1);
            String email = cursor.getString(2);

            // Print the data
            Log.d("Data", "ID: " + id + ", Name: " + name + ", Email: " + email);
        }

        // Close the connection
        dbConnection.close();
    }
}
```

This example creates a SQLite database with a single table called `users`, and then connects to the database to execute a query and retrieve the data.
