# Transaction Processing in JDBC

## Introduction

Transaction processing forms the backbone of reliable database operations in enterprise applications. A transaction represents a sequence of database operations that must execute as an atomic unit to maintain data integrity. In JDBC, transactions are managed through the Connection interface, providing critical control over commit and rollback operations.

Modern applications demand ACID-compliant transactions, especially in financial systems, inventory management, and distributed systems. Consider an e-commerce platform processing orders: reducing stock quantities and creating shipment records must occur atomically. Partial updates would lead to inconsistent product availability or unfulfilled orders.

JDBC's transaction support enables developers to group multiple SQL statements into logical units. By disabling auto-commit mode, programmers gain fine-grained control over when changes become permanent. This is particularly crucial in multi-user environments where concurrent transactions might interfere through phenomena like dirty reads or lost updates.

## ACID Properties

### 1. Atomicity

Guarantees "all or nothing" execution. Either all operations complete successfully, or none take effect.

**Formula:**
T = {OP₁, OP₂, ..., OPₙ}
∀ OP ∈ T, OP succeeds → Commit
∃ OP ∈ T fails → Rollback

**Example:**
Funds transfer between bank accounts:

```java
try {
 conn.setAutoCommit(false);
 withdraw(accountA, amount);
 deposit(accountB, amount);
 conn.commit();
} catch (SQLException e) {
 conn.rollback();
}
```

### 2. Consistency

Ensures database transitions from one valid state to another, maintaining all integrity constraints.

**Example:**
Order processing system must maintain:

```sql
CHECK (order_total = SUM(line_items.price * quantity))
```

### 3. Isolation

Concurrent transactions don't interfere. Implemented through isolation levels:

| Level            | Dirty Reads | Non-Repeatable Reads | Phantom Reads |
| ---------------- | ----------- | -------------------- | ------------- |
| READ_UNCOMMITTED | Yes         | Yes                  | Yes           |
| READ_COMMITTED   | No          | Yes                  | Yes           |
| REPEATABLE_READ  | No          | No                   | Yes           |
| SERIALIZABLE     | No          | No                   | No            |

Set using:

```java
conn.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ);
```

### 4. Durability

Committed transactions survive system failures. Achieved through write-ahead logging (WAL).

## JDBC Transaction Management

### Core Methods

1. `connection.setAutoCommit(false)` - Disables auto-commit
2. `connection.commit()` - Finalizes transaction
3. `connection.rollback()` - Aborts transaction
4. `connection.setSavepoint()` - Creates intermediate rollback point

### Transaction Lifecycle

1. Begin transaction (auto-commit off)
2. Execute SQL operations
3. If successful → commit
4. If failure → rollback
5. Handle exceptions
6. Restore auto-commit state

**Code Template:**

```java
Connection conn = null;
try {
 conn = dataSource.getConnection();
 conn.setAutoCommit(false);

 // Transaction operations
 updateInventory();
 createOrder();

 conn.commit();
} catch (SQLException e) {
 if(conn != null) conn.rollback();
} finally {
 if(conn != null) {
 conn.setAutoCommit(true); // Restore default
 conn.close();
 }
}
```

## Savepoints

Enable partial rollbacks within transactions. Useful for complex operations with recoverable stages.

**Example:**

```java
Savepoint sp1 = conn.setSavepoint("SAVEPOINT_1");
try {
 processPayment();
 Savepoint sp2 = conn.setSavepoint("SAVEPOINT_2");
 updateShipping();
} catch (PaymentException e) {
 conn.rollback(sp1); // Back to before payment
} catch (ShippingException e) {
 conn.rollback(sp2); // Back to after payment
}
```

## Examples

### 1. Bank Funds Transfer

**Problem:** Transfer ₹5000 from account 101 to 102 atomically.

**Solution:**

```java
public void transferFunds(int from, int to, double amount) throws SQLException {
 Connection conn = DriverManager.getConnection(DB_URL);
 try {
 conn.setAutoCommit(false);

 PreparedStatement withdraw = conn.prepareStatement(
 "UPDATE accounts SET balance = balance - ? WHERE acc_no = ?");
 withdraw.setDouble(1, amount);
 withdraw.setInt(2, from);
 withdraw.executeUpdate();

 PreparedStatement deposit = conn.prepareStatement(
 "UPDATE accounts SET balance = balance + ? WHERE acc_no = ?");
 deposit.setDouble(1, amount);
 deposit.setInt(2, to);
 deposit.executeUpdate();

 conn.commit();
 } catch (SQLException e) {
 conn.rollback();
 throw e;
 } finally {
 conn.setAutoCommit(true);
 conn.close();
 }
}
```

### 2. E-Commerce Order Processing

**Problem:** Create order while updating inventory atomically.

**Solution:**

```java
public void createOrder(Order order) throws SQLException {
 Connection conn = dataSource.getConnection();
 try {
 conn.setAutoCommit(false);

 // 1. Update inventory
 for(Item item : order.getItems()) {
 updateStock(conn, item.getId(), item.getQty());
 }

 // 2. Create order record
 saveOrder(conn, order);

 conn.commit();
 } catch (StockException e) {
 conn.rollback();
 throw new OrderException("Insufficient stock", e);
 } finally {
 conn.close();
 }
}

private void updateStock(Connection conn, int itemId, int qty) throws SQLException {
 PreparedStatement ps = conn.prepareStatement(
 "UPDATE inventory SET stock = stock - ? WHERE item_id = ? AND stock >= ?");
 ps.setInt(1, qty);
 ps.setInt(2, itemId);
 ps.setInt(3, qty);
 int rows = ps.executeUpdate();
 if(rows == 0) {
 throw new StockException("Item "+itemId+" out of stock");
 }
}
```

## Transaction States Diagram

(Described in text)

```
 Active
 │
 ▼
Partially Committed
 │
 ├─────────▶ Failed
 │ │
 ▼ ▼
 Committed ◀───── Aborted
```

1. **Active:** Initial state where operations execute
2. **Partially Committed:** After final operation, before commit
3. **Committed:** Successful completion
4. **Failed:** Error during execution
5. **Aborted:** Rolled back to pre-transaction state

## Exam Tips

1. **ACID Mnemonic:** Always use "Atomic, Consistent, Isolated, Durable" with examples
2. **Auto-Commit Default:** Remember JDBC starts with auto-commit=true
3. **Isolation Levels:**

- READ_COMMITTED prevents dirty reads
- SERIALIZABLE prevents all anomalies but reduces concurrency

4. **Savepoint Usage:**

- Create with `Savepoint sp = conn.setSavepoint();`
- Rollback to `conn.rollback(sp);`

5. **Error Handling:**

- Always rollback in catch blocks
- Close connections in finally

6. **Concurrency Issues:**

- Dirty Read: Reading uncommitted data
- Phantom Read: New rows appear in subsequent reads

7. ** Favorite:** Prepare code snippets for fund transfer and order processing scenarios

## Real-World Applications

1. **Banking Systems:** Core banking transactions across multiple accounts
2. **Inventory Management:** Synchronized stock updates during sales
3. **Ticket Booking:** Atomic seat reservation and payment processing
4. **Healthcare Systems:** Patient record updates across multiple tables
5. **Blockchain:** Distributed transaction consensus mechanisms

## Performance Considerations

1. Keep transactions short to reduce lock contention
2. Choose appropriate isolation levels (higher isn't always better)
3. Use batch updates for bulk operations:

```java
Statement stmt = conn.createStatement();
stmt.addBatch("INSERT INTO logs VALUES (...)");
stmt.addBatch("UPDATE counters SET ...");
int[] counts = stmt.executeBatch();
```

4. Avoid long-running transactions in web applications

By mastering these transaction processing techniques, you'll be equipped to build robust, enterprise-grade Java applications that maintain data integrity under complex operational scenarios.
