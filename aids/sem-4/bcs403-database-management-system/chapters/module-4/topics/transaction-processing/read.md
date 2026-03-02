# Transaction Processing in JDBC

## Introduction to Transactions

A **transaction** is a logical unit of work that consists of one or more database operations that should be executed as a single atomic unit. In database terms, transactions follow the **ACID properties**:

- **Atomicity**: All operations in a transaction succeed or all fail
- **Consistency**: Database remains consistent before and after transaction
- **Isolation**: Transactions don't interfere with each other
- **Durability**: Once committed, changes persist even after system failure

In JDBC, transaction processing allows you to group multiple SQL statements into a single transaction that can be committed or rolled back as a unit.

## JDBC Transaction Management

### Auto-Commit Mode

By default, JDBC operates in **auto-commit mode**, where each SQL statement is treated as an individual transaction that is automatically committed after execution.

```java
Connection conn = DriverManager.getConnection(url, user, password);
// conn.getAutoCommit() returns true by default
```

### Manual Transaction Control

To manage transactions manually, you need to:

1. Disable auto-commit mode
2. Execute your SQL statements
3. Commit or rollback the transaction

```java
Connection conn = DriverManager.getConnection(url, user, password);
conn.setAutoCommit(false); // Start transaction

try {
    Statement stmt = conn.createStatement();
    stmt.executeUpdate("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    stmt.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    
    conn.commit(); // Commit transaction if all operations succeed
} catch (SQLException e) {
    conn.rollback(); // Rollback if any operation fails
    throw e;
} finally {
    conn.setAutoCommit(true); // Restore auto-commit mode
    conn.close();
}
```

## Transaction Isolation Levels

JDBC supports different isolation levels that control how transactions interact with each other:

| Isolation Level | Description | Problems Prevented |
|-----------------|-------------|-------------------|
| TRANSACTION_NONE | Not supported | - |
| TRANSACTION_READ_UNCOMMITTED | Lowest isolation level | None |
| TRANSACTION_READ_COMMITTED | Prevents dirty reads | Dirty Reads |
| TRANSACTION_REPEATABLE_READ | Prevents non-repeatable reads | Dirty Reads, Non-repeatable Reads |
| TRANSACTION_SERIALIZABLE | Highest isolation level | Dirty Reads, Non-repeatable Reads, Phantom Reads |

### Setting Isolation Level

```java
Connection conn = DriverManager.getConnection(url, user, password);
conn.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
```

## Savepoints

**Savepoints** allow you to create intermediate points within a transaction that you can roll back to without affecting the entire transaction.

```java
Connection conn = DriverManager.getConnection(url, user, password);
conn.setAutoCommit(false);

Savepoint savepoint1 = conn.setSavepoint("SAVEPOINT_1");

try {
    // Execute some SQL
    Statement stmt = conn.createStatement();
    stmt.executeUpdate("INSERT INTO orders (product_id, quantity) VALUES (1, 5)");
    
    // Set another savepoint
    Savepoint savepoint2 = conn.setSavepoint("SAVEPOINT_2");
    
    // More SQL operations
    stmt.executeUpdate("UPDATE inventory SET stock = stock - 5 WHERE product_id = 1");
    
    conn.commit();
} catch (SQLException e) {
    // Rollback to the second savepoint
    conn.rollback(savepoint2);
    // Or rollback entire transaction: conn.rollback();
}
```

## Distributed Transactions

JDBC supports **distributed transactions** that span multiple databases using the Java Transaction API (JTA) and XA interfaces.

```java
// Example using XADataSource (simplified)
XADataSource xaDataSource = getXADataSource();
XAResource xaResource = xaDataSource.getXAConnection().getXAResource();

Xid xid = createXid(); // Transaction identifier

try {
    xaResource.start(xid, XAResource.TMNOFLAGS);
    // Execute operations across multiple databases
    xaResource.end(xid, XAResource.TMSUCCESS);
    
    int result = xaResource.prepare(xid);
    if (result == XAResource.XA_OK) {
        xaResource.commit(xid, false);
    }
} catch (Exception e) {
    xaResource.rollback(xid);
}
```

## Transaction Best Practices

### 1. Use Try-with-Resources

Java 7+ introduced try-with-resources for automatic resource management:

```java
try (Connection conn = DriverManager.getConnection(url, user, password);
     Statement stmt = conn.createStatement()) {
    
    conn.setAutoCommit(false);
    // Transaction operations
    conn.commit();
    
} catch (SQLException e) {
    // Auto-rollback occurs if connection is closed without commit
}
```

### 2. Handle Exceptions Properly

Always ensure transactions are properly committed or rolled back in exception handling:

```java
Connection conn = null;
try {
    conn = DriverManager.getConnection(url, user, password);
    conn.setAutoCommit(false);
    
    // Business logic
    conn.commit();
} catch (SQLException e) {
    if (conn != null) {
        try {
            conn.rollback();
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
    throw e;
} finally {
    if (conn != null) {
        try {
            conn.setAutoCommit(true);
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. Set Appropriate Timeouts

```java
// Set transaction timeout (seconds)
conn.setNetworkTimeout(executor, 30000); // 30 seconds

// Set query timeout
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(10); // 10 seconds
```

## Real-World Example: Bank Transfer

```java
public boolean transferFunds(int fromAccount, int toAccount, double amount) {
    String sqlDebit = "UPDATE accounts SET balance = balance - ? WHERE id = ?";
    String sqlCredit = "UPDATE accounts SET balance = balance + ? WHERE id = ?";
    String sqlCheckBalance = "SELECT balance FROM accounts WHERE id = ?";
    
    try (Connection conn = DataSource.getConnection();
         PreparedStatement debitStmt = conn.prepareStatement(sqlDebit);
         PreparedStatement creditStmt = conn.prepareStatement(sqlCredit);
         PreparedStatement checkStmt = conn.prepareStatement(sqlCheckBalance)) {
        
        conn.setAutoCommit(false);
        conn.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
        
        // Check sufficient funds
        checkStmt.setInt(1, fromAccount);
        ResultSet rs = checkStmt.executeQuery();
        if (rs.next() && rs.getDouble("balance") < amount) {
            conn.rollback();
            return false;
        }
        
        // Perform debit
        debitStmt.setDouble(1, amount);
        debitStmt.setInt(2, fromAccount);
        debitStmt.executeUpdate();
        
        // Perform credit
        creditStmt.setDouble(1, amount);
        creditStmt.setInt(2, toAccount);
        creditStmt.executeUpdate();
        
        conn.commit();
        return true;
        
    } catch (SQLException e) {
        // Log error and return false
        return false;
    }
}
```

## Transaction Patterns

### 1. Optimistic Locking

```java
// Using version column for optimistic locking
String updateSQL = "UPDATE products SET price = ?, version = version + 1 " +
                   "WHERE id = ? AND version = ?";
```

### 2. Pessimistic Locking

```java
// Using SELECT FOR UPDATE for pessimistic locking
String selectSQL = "SELECT * FROM accounts WHERE id = ? FOR UPDATE";
```

## ASCII Diagram: Transaction Flow

```
+----------------+     +-----------------+     +-----------------+
| Begin Transaction |→| Execute SQL Operations |→| Check for Errors |
+----------------+     +-----------------+     +-----------------+
        ↑                      |                      |
        |                      ↓                      ↓
        |               +-----------------+     +-----------------+
        +---------------|   Rollback     |←-----|   Error Found   |
                        +-----------------+     +-----------------+
                                |
                                ↓
                        +-----------------+
                        |   End Transaction |
                        +-----------------+
                                |
                                ↓
                        +-----------------+
                        |   Release Locks |
                        +-----------------+
```

## Exam Tips

1. **Remember ACID properties** and be able to explain each one
2. **Understand isolation levels** and what concurrency problems they prevent
3. **Practice writing transaction code** with proper try-catch-finally blocks
4. **Know the difference** between savepoints and full rollbacks
5. **Be familiar with** both optimistic and pessimistic locking strategies
6. **Understand when to use** distributed transactions vs regular transactions
7. **Remember that** setAutoCommit(false) starts a transaction in JDBC