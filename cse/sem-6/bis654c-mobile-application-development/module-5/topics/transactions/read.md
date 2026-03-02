# Android SQLite Transactions

## Introduction

A **transaction** in Android SQLite is a group of database operations that are executed as a single atomic unit. Either all operations succeed and are committed, or all fail and are rolled back. Transactions are essential for maintaining data integrity in Android applications.

## Why Use Transactions?

### Data Integrity

When inserting related data across multiple tables (such as an order and its items), transactions ensure that either all records are saved or none are, preventing partial or inconsistent data.

### Performance Improvement

By default, SQLite wraps each individual INSERT, UPDATE, or DELETE in its own transaction. Grouping multiple operations in a single explicit transaction drastically reduces disk I/O.

```
Without Transaction: 1000 inserts = ~5000ms (each has its own transaction)
With Transaction: 1000 inserts = ~200ms (one transaction for all)
Performance gain: ~25x faster
```

### Error Recovery

If any operation within a transaction fails, the entire transaction is rolled back, leaving the database in its previous consistent state.

## Transaction Methods in Android SQLite

Android provides three key methods on the `SQLiteDatabase` class for transaction management:

| Method                           | Description                                            |
| -------------------------------- | ------------------------------------------------------ |
| `beginTransaction()`             | Starts a new transaction in EXCLUSIVE mode             |
| `setTransactionSuccessful()`     | Marks the transaction for commit                       |
| `endTransaction()`               | Commits if successful was called, otherwise rolls back |
| `beginTransactionNonExclusive()` | Starts a transaction in IMMEDIATE mode                 |
| `inTransaction()`                | Returns true if currently inside a transaction         |

## Basic Transaction Pattern

The standard pattern for using transactions in Android:

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();

db.beginTransaction();
try {
 // Perform database operations
 db.insert("notes", null, values1);
 db.update("categories", values2, "id=?", args);
 db.delete("temp_data", null, null);

 // Mark transaction as successful (commit)
 db.setTransactionSuccessful();
} catch (Exception e) {
 // Transaction will be rolled back automatically
 Log.e("DB", "Transaction failed: " + e.getMessage());
} finally {
 // Always call endTransaction() in finally block
 db.endTransaction();
}
```

### How It Works

1. `beginTransaction()` - Opens a new transaction and acquires a database lock
2. Database operations are performed within the try block
3. `setTransactionSuccessful()` - Flags the transaction for commit (must be called before endTransaction)
4. `endTransaction()` - If `setTransactionSuccessful()` was called, the transaction is committed; otherwise it is rolled back
5. The finally block ensures `endTransaction()` is always called, even if an exception occurs

## Practical Examples

### Example 1: Inserting a Note with Tags

```java
public boolean insertNoteWithTags(String title, String body, List<String> tags) {
 SQLiteDatabase db = dbHelper.getWritableDatabase();
 boolean success = false;

 db.beginTransaction();
 try {
 // Insert the note
 ContentValues noteValues = new ContentValues();
 noteValues.put("title", title);
 noteValues.put("body", body);
 long noteId = db.insert("notes", null, noteValues);

 if (noteId == -1) {
 throw new SQLException("Failed to insert note");
 }

 // Insert each tag linked to the note
 for (String tag : tags) {
 ContentValues tagValues = new ContentValues();
 tagValues.put("note_id", noteId);
 tagValues.put("tag_name", tag);
 long tagId = db.insert("note_tags", null, tagValues);
 if (tagId == -1) {
 throw new SQLException("Failed to insert tag: " + tag);
 }
 }

 db.setTransactionSuccessful();
 success = true;
 } catch (Exception e) {
 Log.e("NoteDB", "Error: " + e.getMessage());
 } finally {
 db.endTransaction();
 }

 return success;
}
```

### Example 2: Batch Insert for Performance

```java
public void bulkInsertContacts(List<Contact> contacts) {
 SQLiteDatabase db = dbHelper.getWritableDatabase();

 db.beginTransaction();
 try {
 for (Contact contact : contacts) {
 ContentValues values = new ContentValues();
 values.put("name", contact.getName());
 values.put("phone", contact.getPhone());
 values.put("email", contact.getEmail());
 db.insert("contacts", null, values);
 }
 db.setTransactionSuccessful();
 } finally {
 db.endTransaction();
 }
}
```

### Example 3: Transfer Between Accounts

```java
public boolean transferAmount(int fromId, int toId, double amount) {
 SQLiteDatabase db = dbHelper.getWritableDatabase();

 db.beginTransaction();
 try {
 // Debit from source
 db.execSQL("UPDATE accounts SET balance = balance - ? WHERE _id = ?",
 new Object[]{amount, fromId});

 // Credit to destination
 db.execSQL("UPDATE accounts SET balance = balance + ? WHERE _id = ?",
 new Object[]{amount, toId});

 // Log the transfer
 ContentValues logValues = new ContentValues();
 logValues.put("from_account", fromId);
 logValues.put("to_account", toId);
 logValues.put("amount", amount);
 logValues.put("timestamp", System.currentTimeMillis());
 db.insert("transfer_log", null, logValues);

 db.setTransactionSuccessful();
 return true;
 } catch (Exception e) {
 Log.e("Transfer", "Failed: " + e.getMessage());
 return false;
 } finally {
 db.endTransaction();
 }
}
```

## Room Database Transactions

Modern Android development uses Room, which provides built-in transaction support.

### Using @Transaction Annotation

```java
@Dao
public interface OrderDao {

 @Transaction
 @Query("SELECT * FROM orders WHERE id = :orderId")
 OrderWithItems getOrderWithItems(int orderId);

 @Insert
 long insertOrder(Order order);

 @Insert
 void insertOrderItems(List<OrderItem> items);

 @Transaction
 default void createOrderWithItems(Order order, List<OrderItem> items) {
 long orderId = insertOrder(order);
 for (OrderItem item : items) {
 item.setOrderId(orderId);
 }
 insertOrderItems(items);
 }
}
```

### Programmatic Room Transactions

```java
// Using runInTransaction
appDatabase.runInTransaction(() -> {
 orderDao.insertOrder(order);
 itemDao.insertItems(items);
 inventoryDao.updateStock(stockUpdates);
});
```

## Transaction Best Practices

### 1. Always Use try-finally

```java
db.beginTransaction();
try {
 // operations
 db.setTransactionSuccessful();
} finally {
 db.endTransaction(); // Always executed
}
```

### 2. Keep Transactions Short

Do not include network calls, file I/O, or other slow operations inside a transaction. Perform those outside, then use a transaction only for the database operations.

### 3. Run on Background Thread

Database transactions should never run on the main UI thread to avoid blocking the user interface.

### 4. Check Operation Results

Always verify that insert/update/delete operations succeeded before marking the transaction as successful.

### 5. Batch Large Operations in Chunks

For very large datasets, split into smaller batch transactions to avoid holding the database lock for too long.

## Common Pitfalls

| Pitfall                                | Solution                                         |
| -------------------------------------- | ------------------------------------------------ |
| Forgetting endTransaction()            | Always use finally block                         |
| Not calling setTransactionSuccessful() | Transaction rolls back silently                  |
| Long-running transactions              | Keep transactions short, no network calls inside |
| Running on main thread                 | Use AsyncTask, Executor, or coroutines           |
| Not checking insert/update results     | Verify return values before marking successful   |

## Summary

- Transactions group multiple SQLite operations into a single atomic unit
- Use beginTransaction(), setTransactionSuccessful(), and endTransaction() pattern
- Transactions improve performance by 10-25x for batch operations
- Always use try-finally to ensure endTransaction() is called
- Room provides @Transaction annotation for simpler transaction management
- Keep transactions short and run them on background threads
