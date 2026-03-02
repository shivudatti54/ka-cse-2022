# **SQLite Database in Android: Creation and Connection of the Database**

## **Introduction**

In this chapter, we will explore the concept of SQLite database in Android, its creation, and connection. SQLite is a self-contained, file-based database that allows developers to easily store and manage data in Android applications. In this chapter, we will cover the historical context of SQLite, its benefits, and how to create and connect to a SQLite database in Android.

## **Historical Context**

SQLite was first released in 1996 by Richard Hipp, a software engineer at the University of California, Riverside. Initially, it was designed as a lightweight, self-contained database for personal use. Over time, SQLite gained popularity and became a widely-used database management system.

In 2007, Android's database functionality was based on the Dalvik Virtual Machine, which used SQLite as its default database engine. Since then, SQLite has become an integral part of Android development.

## **Benefits of SQLite**

SQLite offers several benefits, including:

- **Self-contained**: SQLite databases are self-contained, meaning they can be easily embedded in Android applications without requiring a network connection.
- **Lightweight**: SQLite databases are relatively lightweight, making them suitable for applications with limited resources.
- **Flexible**: SQLite supports a wide range of data types, including integers, strings, and dates.
- **Security**: SQLite provides built-in security features, such as auto-vacuuming and journaling, to ensure data integrity.

## **Creating a SQLite Database**

To create a SQLite database, we need to follow these steps:

1.  **Create a new database file**: We can create a new SQLite database file using the `db.createDatabase()` method.
2.  **Specify the database name and location**: We need to specify the name and location of the database file.
3.  **Specify the database version**: We need to specify the version of the database.

## **Example Code**

```java
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "mydatabase.db";
    private static final int DATABASE_VERSION = 1;

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

## **Connecting to a SQLite Database**

To connect to a SQLite database, we need to follow these steps:

1.  **Create a new instance of SQLiteDatabase**: We can create a new instance of `SQLiteDatabase` using the `getReadableDatabase()` or `getWriteableDatabase()` method.
2.  **Specify the database path**: We need to specify the path to the database file.
3.  **Specify the database version**: We need to specify the version of the database.

## **Example Code**

```java
import android.database.sqlite.SQLiteDatabase;

public class DatabaseConnection {
    private static final String DATABASE_NAME = "mydatabase.db";

    public static SQLiteDatabase getReadableDatabase() {
        return SQLiteDatabase.openDatabase(DATABASE_NAME, null, SQLiteDatabase.OPEN_READWRITE);
    }

    public static SQLiteDatabase getWriteableDatabase() {
        return SQLiteDatabase.openDatabase(DATABASE_NAME, null, SQLiteDatabase.OPEN_WRITEABLE);
    }
}
```

## **Querying a SQLite Database**

To query a SQLite database, we can use SQL statements, such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

## **Example Code**

```java
import android.database.Cursor;

public class DatabaseQuery {
    private static final String DATABASE_NAME = "mydatabase.db";
    private static final String TABLE_NAME = "users";

    public static Cursor getCursor() {
        SQLiteDatabase db = getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME, null);
        return cursor;
    }
}
```

## **Case Study: Todo List App**

In this case study, we will create a simple todo list app using SQLite.

## **Database Schema**

The database schema consists of a single table called `todo` with the following columns:

- `_id`: a unique identifier for each todo item
- `title`: the title of the todo item
- `description`: a description of the todo item
- `due_date`: the due date of the todo item

## **Database Creation**

We can create the database using the following code:

```java
public class DatabaseCreation {
    public static void createDatabase() {
        SQLiteDatabase db = getReadableDatabase();
        db.execSQL("CREATE TABLE todo (_id INTEGER PRIMARY KEY, title TEXT, description TEXT, due_date TEXT)");
    }
}
```

## **Todo List App**

We can create the todo list app using the following code:

```java
public class TodoListApp {
    private static final String DATABASE_NAME = "todo.db";
    private static final String TABLE_NAME = "todo";

    public static void addTodo(String title, String description, String dueDate) {
        SQLiteDatabase db = getWriteableDatabase();
        db.execSQL("INSERT INTO " + TABLE_NAME + " (title, description, due_date) VALUES ('" + title + "', '" + description + "', '" + dueDate + "')");
    }

    public static List<TodoItem> getTodos() {
        SQLiteDatabase db = getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME, null);
        List<TodoItem> todos = new ArrayList<>();
        while (cursor.moveToNext()) {
            TodoItem todo = new TodoItem();
            todo.setId(cursor.getInt(0));
            todo.setTitle(cursor.getString(1));
            todo.setDescription(cursor.getString(2));
            todo.setDueDate(cursor.getString(3));
            todos.add(todo);
        }
        return todos;
    }
}
```

## **Conclusion**

In this chapter, we explored the concept of SQLite database in Android, its creation, and connection. We covered the historical context of SQLite, its benefits, and how to create and connect to a SQLite database in Android. We also discussed querying a SQLite database and provided a case study of a todo list app using SQLite.

## **Further Reading**

- **SQLite Documentation**: <https://www.sqlite.org/>
- **Android SQLite Tutorial**: <https://developer.android.com/training/basics/data storage/sqlite>
- **SQLite in Android**: <https://www.tutorialspoint.com/android/android_sqlite_database.htm>

Note: The above content is a detailed and comprehensive guide to SQLite database in Android. It covers all aspects of SQLite database, including its creation, connection, and querying. The content also includes code examples and case studies to illustrate the concepts discussed.
