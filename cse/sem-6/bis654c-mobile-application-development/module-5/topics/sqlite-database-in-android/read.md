# SQLite Database in Android

## 1. Introduction to SQLite

**SQLite** is a lightweight, embedded relational database management system that is built into Android. It provides local data storage for Android applications without requiring a separate database server.

### Key Features of SQLite

- **Serverless**: No separate server process required
- **Zero-configuration**: No setup or administration needed
- **Cross-platform**: Works on all Android devices
- **ACID compliant**: Ensures data integrity
- **Lightweight**: Small memory footprint
- **Self-contained**: Single database file

## 2. When to Use SQLite

SQLite is ideal for:

- Storing structured data
- Complex queries with relationships
- Large amounts of data
- Offline data persistence
- Data that needs to be searchable

**Not suitable for**:

- Small key-value pairs (use SharedPreferences instead)
- Real-time multi-user access
- Extremely large databases (> 100 GB)

## 3. SQLite Database Architecture in Android

```
Application Layer
 ↓
SQLiteOpenHelper (Database Helper Class)
 ↓
SQLiteDatabase (Database Instance)
 ↓
SQL Queries (Create, Read, Update, Delete)
 ↓
SQLite Engine
 ↓
Database File (.db)
```

## 4. Creating Database Contract

A **contract class** defines the schema of your database in a structured way.

```java
public final class NotesContract {
 // To prevent someone from accidentally instantiating the contract class
 private NotesContract() {}

 public static class NotesEntry implements BaseColumns {
 public static final String TABLE_NAME = "notes";
 public static final String COLUMN_NAME_TITLE = "title";
 public static final String COLUMN_NAME_DESCRIPTION = "description";
 public static final String COLUMN_NAME_TIMESTAMP = "timestamp";
 }
}
```

**BaseColumns Interface**:

- Provides `_ID` column (primary key)
- Provides `_COUNT` column (for cursor operations)

## 5. Creating SQLiteOpenHelper Class

The **SQLiteOpenHelper** class manages database creation and version management.

```java
public class NotesDatabaseHelper extends SQLiteOpenHelper {
 // Database Info
 private static final String DATABASE_NAME = "notesDatabase.db";
 private static final int DATABASE_VERSION = 1;

 // Table and column names
 private static final String TABLE_NOTES = NotesContract.NotesEntry.TABLE_NAME;
 private static final String COLUMN_ID = NotesContract.NotesEntry._ID;
 private static final String COLUMN_TITLE = NotesContract.NotesEntry.COLUMN_NAME_TITLE;
 private static final String COLUMN_DESCRIPTION = NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION;
 private static final String COLUMN_TIMESTAMP = NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP;

 // Constructor
 public NotesDatabaseHelper(Context context) {
 super(context, DATABASE_NAME, null, DATABASE_VERSION);
 }

 // Called when database is created for the first time
 @Override
 public void onCreate(SQLiteDatabase db) {
 String CREATE_NOTES_TABLE = "CREATE TABLE " + TABLE_NOTES +
 "(" +
 COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT," +
 COLUMN_TITLE + " TEXT NOT NULL," +
 COLUMN_DESCRIPTION + " TEXT," +
 COLUMN_TIMESTAMP + " DATETIME DEFAULT CURRENT_TIMESTAMP" +
 ")";
 db.execSQL(CREATE_NOTES_TABLE);
 }

 // Called when database version is upgraded
 @Override
 public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
 if (oldVersion != newVersion) {
 // Simplest implementation: Drop old table and create new one
 db.execSQL("DROP TABLE IF EXISTS " + TABLE_NOTES);
 onCreate(db);
 }
 }
}
```

### Key Methods

| Method          | Description                                |
| --------------- | ------------------------------------------ |
| `onCreate()`    | Called when database is created first time |
| `onUpgrade()`   | Called when database version changes       |
| `onDowngrade()` | Called when database version is downgraded |
| `onOpen()`      | Called when database is opened             |

## 6. CRUD Operations

### 6.1 Create (Insert) Operation

```java
public class NotesDao {
 private SQLiteDatabase database;
 private NotesDatabaseHelper dbHelper;

 public NotesDao(Context context) {
 dbHelper = new NotesDatabaseHelper(context);
 }

 // Insert a new note
 public long insertNote(String title, String description) {
 database = dbHelper.getWritableDatabase();

 ContentValues values = new ContentValues();
 values.put(NotesContract.NotesEntry.COLUMN_NAME_TITLE, title);
 values.put(NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION, description);

 // Insert row and return new row ID
 long newRowId = database.insert(
 NotesContract.NotesEntry.TABLE_NAME,
 null,
 values
 );

 database.close();
 return newRowId;
 }
}
```

**Using SQL Insert**:

```java
public void insertNoteSQL(String title, String description) {
 database = dbHelper.getWritableDatabase();

 String sql = "INSERT INTO " + NotesContract.NotesEntry.TABLE_NAME +
 " (title, description) VALUES (?, ?)";

 database.execSQL(sql, new String[]{title, description});
 database.close();
}
```

### 6.2 Read (Query) Operation

**Query All Notes**:

```java
public List<Note> getAllNotes() {
 List<Note> notes = new ArrayList<>();
 database = dbHelper.getReadableDatabase();

 // Define columns to retrieve
 String[] projection = {
 NotesContract.NotesEntry._ID,
 NotesContract.NotesEntry.COLUMN_NAME_TITLE,
 NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION,
 NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP
 };

 // Query the database
 Cursor cursor = database.query(
 NotesContract.NotesEntry.TABLE_NAME, // Table name
 projection, // Columns to return
 null, // WHERE clause
 null, // WHERE values
 null, // GROUP BY
 null, // HAVING
 NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP + " DESC" // ORDER BY
 );

 // Iterate through results
 while (cursor.moveToNext()) {
 int id = cursor.getInt(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry._ID));
 String title = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_TITLE));
 String description = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION));
 String timestamp = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP));

 Note note = new Note(id, title, description, timestamp);
 notes.add(note);
 }

 cursor.close();
 database.close();
 return notes;
}
```

**Query with Selection (WHERE clause)**:

```java
public Note getNoteById(int noteId) {
 database = dbHelper.getReadableDatabase();

 String selection = NotesContract.NotesEntry._ID + " = ?";
 String[] selectionArgs = { String.valueOf(noteId) };

 Cursor cursor = database.query(
 NotesContract.NotesEntry.TABLE_NAME,
 null,
 selection,
 selectionArgs,
 null,
 null,
 null
 );

 Note note = null;
 if (cursor.moveToFirst()) {
 int id = cursor.getInt(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry._ID));
 String title = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_TITLE));
 String description = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION));
 String timestamp = cursor.getString(cursor.getColumnIndexOrThrow(NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP));

 note = new Note(id, title, description, timestamp);
 }

 cursor.close();
 database.close();
 return note;
}
```

**Using Raw SQL Query**:

```java
public List<Note> getNotesRawSQL() {
 List<Note> notes = new ArrayList<>();
 database = dbHelper.getReadableDatabase();

 String query = "SELECT * FROM " + NotesContract.NotesEntry.TABLE_NAME +
 " ORDER BY " + NotesContract.NotesEntry.COLUMN_NAME_TIMESTAMP + " DESC";

 Cursor cursor = database.rawQuery(query, null);

 while (cursor.moveToNext()) {
 // Extract data...
 }

 cursor.close();
 database.close();
 return notes;
}
```

### 6.3 Update Operation

```java
public int updateNote(int noteId, String newTitle, String newDescription) {
 database = dbHelper.getWritableDatabase();

 ContentValues values = new ContentValues();
 values.put(NotesContract.NotesEntry.COLUMN_NAME_TITLE, newTitle);
 values.put(NotesContract.NotesEntry.COLUMN_NAME_DESCRIPTION, newDescription);

 String selection = NotesContract.NotesEntry._ID + " = ?";
 String[] selectionArgs = { String.valueOf(noteId) };

 int count = database.update(
 NotesContract.NotesEntry.TABLE_NAME,
 values,
 selection,
 selectionArgs
 );

 database.close();
 return count; // Number of rows updated
}
```

### 6.4 Delete Operation

```java
public int deleteNote(int noteId) {
 database = dbHelper.getWritableDatabase();

 String selection = NotesContract.NotesEntry._ID + " = ?";
 String[] selectionArgs = { String.valueOf(noteId) };

 int deletedRows = database.delete(
 NotesContract.NotesEntry.TABLE_NAME,
 selection,
 selectionArgs
 );

 database.close();
 return deletedRows;
}

// Delete all notes
public void deleteAllNotes() {
 database = dbHelper.getWritableDatabase();
 database.delete(NotesContract.NotesEntry.TABLE_NAME, null, null);
 database.close();
}
```

## 7. Understanding Cursor

A **Cursor** represents the result set of a database query.

```java
Cursor cursor = database.query(...);

// Important Cursor methods
cursor.moveToFirst(); // Move to first row
cursor.moveToNext(); // Move to next row
cursor.moveToLast(); // Move to last row
cursor.moveToPrevious(); // Move to previous row
cursor.moveToPosition(5); // Move to specific position

cursor.getCount(); // Get total number of rows
cursor.isAfterLast(); // Check if past last row
cursor.isBeforeFirst(); // Check if before first row

cursor.getInt(columnIndex);
cursor.getString(columnIndex);
cursor.getDouble(columnIndex);

cursor.close(); // Always close cursor to free resources
```

## 8. Data Model Class

```java
public class Note {
 private int id;
 private String title;
 private String description;
 private String timestamp;

 public Note(int id, String title, String description, String timestamp) {
 this.id = id;
 this.title = title;
 this.description = description;
 this.timestamp = timestamp;
 }

 // Getters and Setters
 public int getId() { return id; }
 public void setId(int id) { this.id = id; }

 public String getTitle() { return title; }
 public void setTitle(String title) { this.title = title; }

 public String getDescription() { return description; }
 public void setDescription(String description) { this.description = description; }

 public String getTimestamp() { return timestamp; }
 public void setTimestamp(String timestamp) { this.timestamp = timestamp; }
}
```

## 9. Using SQLite in Activity

```java
public class MainActivity extends AppCompatActivity {
 private NotesDao notesDao;

 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);

 notesDao = new NotesDao(this);

 // Insert a note
 long id = notesDao.insertNote("My First Note", "This is the description");

 // Get all notes
 List<Note> allNotes = notesDao.getAllNotes();

 // Update a note
 notesDao.updateNote(1, "Updated Title", "Updated Description");

 // Delete a note
 notesDao.deleteNote(1);
 }
}
```

## 10. Database Best Practices

### 10.1 Use Singleton Pattern

```java
public class DatabaseManager {
 private static DatabaseManager instance;
 private NotesDatabaseHelper dbHelper;

 private DatabaseManager(Context context) {
 dbHelper = new NotesDatabaseHelper(context.getApplicationContext());
 }

 public static synchronized DatabaseManager getInstance(Context context) {
 if (instance == null) {
 instance = new DatabaseManager(context);
 }
 return instance;
 }

 public SQLiteDatabase getDatabase() {
 return dbHelper.getWritableDatabase();
 }
}
```

### 10.2 Close Database Properly

Always close database connections to prevent memory leaks:

```java
database.close();
cursor.close();
```

### 10.3 Use Transactions for Multiple Operations

```java
database.beginTransaction();
try {
 // Perform multiple operations
 database.insert(...);
 database.update(...);
 database.delete(...);

 database.setTransactionSuccessful();
} finally {
 database.endTransaction();
}
```

### 10.4 Perform Database Operations on Background Thread

```java
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.execute(() -> {
 // Perform database operations
 List<Note> notes = notesDao.getAllNotes();

 // Update UI on main thread
 runOnUiThread(() -> {
 // Update RecyclerView or UI components
 });
});
```

## 11. Database Debugging

### View Database in Device Explorer

1. Open Android Studio Device Explorer
2. Navigate to: `/data/data/your.package.name/databases/`
3. Download `.db` file
4. Open with SQLite browser

### Log Database Queries

```java
SQLiteDatabase.enableWriteAheadLogging();
```

## 12. Modern Alternatives: Room Database

While SQLite is powerful, Google recommends using **Room Persistence Library** for new projects:

```java
@Entity(tableName = "notes")
public class Note {
 @PrimaryKey(autoGenerate = true)
 private int id;

 @ColumnInfo(name = "title")
 private String title;

 // Getters and setters
}

@Dao
public interface NoteDao {
 @Insert
 void insert(Note note);

 @Query("SELECT * FROM notes")
 List<Note> getAllNotes();

 @Update
 void update(Note note);

 @Delete
 void delete(Note note);
}
```

**Room Benefits**:

- Compile-time verification of SQL queries
- Less boilerplate code
- LiveData and coroutines support
- Migration management

## 13. Summary

SQLite in Android provides:

- Local relational database storage
- CRUD operations for data management
- Structured data organization
- Offline data persistence
- Query capabilities with SQL

**Key Components**:

- **Contract Class**: Defines database schema
- **SQLiteOpenHelper**: Manages database creation and versioning
- **SQLiteDatabase**: Provides database operations
- **Cursor**: Represents query results

## Further Reading

1. **"Android Programming: The Big Nerd Ranch Guide"** by Bill Phillips
2. **"Professional Android"** by Reto Meier and Ian Lake
3. Official Android documentation on Data Storage: developer.android.com/training/data-storage/sqlite
