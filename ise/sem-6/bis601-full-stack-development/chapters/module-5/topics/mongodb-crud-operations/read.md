# SQLite CRUD Operations in Android

## Introduction to SQLite in Android

SQLite is a lightweight, serverless, self-contained, transactional SQL database engine that is widely used in mobile applications, including Android. It provides a local storage solution for structured data within an app. Unlike client-server database systems, SQLite doesn't require a separate server process and stores the entire database as a single file on the device.

**Why SQLite for Android?**

- Zero-configuration: No setup or administration needed
- Serverless: No separate server process required
- Compact: Entire database is a single cross-platform file
- ACID-compliant: Atomic, Consistent, Isolated, Durable transactions
- Standard SQL syntax with some limitations

## SQLite Architecture in Android

```
+-----------------------+
|   Android Application |
+-----------------------+
|  Content Provider     |  ← Optional abstraction layer
+-----------------------+
|  SQLiteOpenHelper     |  ← Database helper class
+-----------------------+
|   SQLiteDatabase      |  ← Core database class
+-----------------------+
|   SQLite Database File|
+-----------------------+
```

The Android SDK provides the `android.database.sqlite` package which contains all the necessary classes for working with SQLite databases.

## Core Components for SQLite Operations

### 1. SQLiteOpenHelper Class

This helper class manages database creation and version management. You extend this class to implement your database operations.

```java
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME = "my_database.db";
    private static final int DATABASE_VERSION = 1;

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create tables
        db.execSQL("CREATE TABLE users (_id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade database schema
        db.execSQL("DROP TABLE IF EXISTS users");
        onCreate(db);
    }
}
```

### 2. SQLiteDatabase Class

This class provides the main interface for database operations including:

- Executing SQL statements
- Performing CRUD operations
- Managing transactions

## CRUD Operations Explained

CRUD stands for Create, Read, Update, Delete - the four basic operations of persistent storage.

### CREATE Operations

**1. Using execSQL() for Raw SQL:**

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();
db.execSQL("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')");
```

**2. Using insert() with ContentValues:**

```java
ContentValues values = new ContentValues();
values.put("name", "Jane Smith");
values.put("email", "jane@example.com");

long newRowId = db.insert("users", null, values);
```

**Comparison of INSERT Methods:**

| Method    | Pros                               | Cons                                  | Use Case                         |
| --------- | ---------------------------------- | ------------------------------------- | -------------------------------- |
| execSQL() | Full SQL control, complex queries  | Prone to SQL injection if not careful | Complex inserts, bulk operations |
| insert()  | Safe from SQL injection, type-safe | Limited to simple inserts             | Simple single-row inserts        |

### READ Operations

**1. Using rawQuery() for Raw SQL:**

```java
Cursor cursor = db.rawQuery("SELECT * FROM users WHERE name = ?",
                           new String[]{"John Doe"});
```

**2. Using query() method:**

```java
Cursor cursor = db.query(
    "users",                     // Table name
    new String[]{"_id", "name", "email"}, // Columns
    "name = ?",                  // WHERE clause
    new String[]{"John Doe"},    // WHERE args
    null,                        // GROUP BY
    null,                        // HAVING
    null                         // ORDER BY
);
```

**Processing Cursor Results:**

```java
if (cursor.moveToFirst()) {
    do {
        int id = cursor.getInt(cursor.getColumnIndex("_id"));
        String name = cursor.getString(cursor.getColumnIndex("name"));
        String email = cursor.getString(cursor.getColumnIndex("email"));
        // Process the data
    } while (cursor.moveToNext());
}
cursor.close(); // Always close the cursor!
```

### UPDATE Operations

**1. Using execSQL():**

```java
db.execSQL("UPDATE users SET email = ? WHERE name = ?",
           new String[]{"newemail@example.com", "John Doe"});
```

**2. Using update() with ContentValues:**

```java
ContentValues values = new ContentValues();
values.put("email", "updated@example.com");

int rowsAffected = db.update(
    "users",                    // Table name
    values,                     // New values
    "name = ?",                 // WHERE clause
    new String[]{"John Doe"}    // WHERE args
);
```

### DELETE Operations

**1. Using execSQL():**

```java
db.execSQL("DELETE FROM users WHERE name = ?",
           new String[]{"John Doe"});
```

**2. Using delete() method:**

```java
int rowsDeleted = db.delete(
    "users",                    // Table name
    "name = ?",                 // WHERE clause
    new String[]{"John Doe"}    // WHERE args
);
```

## Transactions in SQLite

Transactions ensure that a set of database operations either complete entirely or not at all, maintaining data integrity.

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();

db.beginTransaction();
try {
    // Multiple database operations
    db.insert("users", null, values1);
    db.insert("users", null, values2);
    db.update("users", values3, "name = ?", new String[]{"John"});

    db.setTransactionSuccessful(); // Mark transaction as successful
} finally {
    db.endTransaction(); // This will commit if successful, rollback otherwise
}
```

## Best Practices for SQLite CRUD Operations

1. **Always close databases and cursors:**

   ```java
   cursor.close();
   db.close();
   ```

2. **Use parameterized queries to prevent SQL injection:**

   ```java
   // GOOD: Parameterized query
   db.rawQuery("SELECT * FROM users WHERE name = ?", new String[]{userInput});

   // BAD: String concatenation (vulnerable to SQL injection)
   db.rawQuery("SELECT * FROM users WHERE name = '" + userInput + "'", null);
   ```

3. **Perform database operations on background threads:**

   ```java
   new AsyncTask<Void, Void, Void>() {
       protected Void doInBackground(Void... params) {
           // Database operations here
           return null;
       }
   }.execute();
   ```

4. **Use indexes for frequently queried columns:**
   ```java
   db.execSQL("CREATE INDEX idx_users_name ON users(name)");
   ```

## Integration with Location Services

SQLite is often used with location services to store location data:

```java
// Storing location data
public void saveLocation(Location location) {
    SQLiteDatabase db = dbHelper.getWritableDatabase();
    ContentValues values = new ContentValues();
    values.put("latitude", location.getLatitude());
    values.put("longitude", location.getLongitude());
    values.put("timestamp", System.currentTimeMillis());
    db.insert("locations", null, values);
}

// Retrieving nearby locations
public Cursor getNearbyLocations(double lat, double lng, double radius) {
    SQLiteDatabase db = dbHelper.getReadableDatabase();
    String query = "SELECT * FROM locations WHERE " +
                   "(latitude BETWEEN ? AND ?) AND " +
                   "(longitude BETWEEN ? AND ?)";
    double latRange = radius / 111000; // Approximate conversion
    double lngRange = radius / (111000 * Math.cos(Math.toRadians(lat)));

    return db.rawQuery(query, new String[]{
        String.valueOf(lat - latRange),
        String.valueOf(lat + latRange),
        String.valueOf(lng - lngRange),
        String.valueOf(lng + lngRange)
    });
}
```

## Common Patterns and Anti-patterns

**Good Pattern: Using try-with-resources (API level 16+)**

```java
try (SQLiteDatabase db = dbHelper.getWritableDatabase();
     Cursor cursor = db.query(...)) {
    // Use database and cursor
} // Automatically closed
```

**Anti-pattern: Database operations on UI thread**

```java
// DON'T DO THIS - causes Application Not Responding (ANR)
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // Database operations here - BAD!
}
```

## Exam Tips

1. **Remember the method signatures:** Know the parameters for insert(), query(), update(), and delete() methods.

2. **Understand cursor management:** Always close cursors to avoid memory leaks and know how to navigate through cursor results.

3. **Transaction importance:** Remember that without db.setTransactionSuccessful(), all operations in the transaction will be rolled back.

4. **Security considerations:** Always use parameterized queries to prevent SQL injection attacks.

5. **Performance aspects:** Database operations should be performed on background threads to avoid blocking the UI thread.

6. **Lifecycle awareness:** Manage database connections appropriately in activity/fragment lifecycle methods.
