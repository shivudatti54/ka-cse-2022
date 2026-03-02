# Database Administration Commands

## Introduction

Database Administration Commands form the backbone of effective database management in any enterprise environment. For Computer Science students at the University of Delhi, understanding these commands is essential as organizations increasingly rely on database administrators (DBAs) to maintain data integrity, security, and optimal performance. MySQL, being one of the most widely used open-source relational database management systems (RDBMS), provides a comprehensive set of administrative commands that every database professional must master.

In the context of modern applications, databases store critical business data ranging from customer information to financial records. The ability to properly administer these databases—creating users, managing permissions, performing backups, and optimizing queries—separates a competent developer from a skilled database administrator. This topic covers the essential MySQL administrative commands that DU students must know for both academic success and professional competence.

## Key Concepts

### 1. User Management Commands

User management is fundamental to database security. MySQL provides several commands to create, modify, and delete database users.

**Creating Users:**
```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

The `CREATE USER` command creates a new MySQL account. The `username` specifies the user name, while `host` determines which hosts the user can connect from. Common host values include:
- `'localhost'` - Only from the local machine
- `'%'` - From any host
- Specific IP addresses like `'192.168.1.100'`

**Granting Privileges:**
```sql
GRANT privilege_type ON database_name.table_name TO 'username'@'host';
```

Privileges can be granted at different levels:
- **Global level:** `ON *.*` - applies to all databases and tables
- **Database level:** `ON database_name.*` - applies to all tables in a specific database
- **Table level:** `ON database_name.table_name` - applies to a specific table
- **Column level:** Specific columns within a table

Common privilege types include `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `ALTER`, `INDEX`, and `ALL PRIVILEGES`.

**Revoking Privileges:**
```sql
REVOKE privilege_type ON database_name.table_name FROM 'username'@'host';
```

**Deleting Users:**
```sql
DROP USER 'username'@'host';
```

### 2. Backup and Recovery Commands

Data backup is critical for disaster recovery and business continuity.

**Logical Backups using mysqldump:**
```bash
mysqldump -u username -p database_name > backup_file.sql
```

For backing up multiple databases:
```bash
mysqldump -u username -p --databases db1 db2 > backup_file.sql
```

For complete server backup:
```bash
mysqldump -u username -p --all-databases > full_backup.sql
```

**Restoring from Backup:**
```bash
mysql -u username -p database_name < backup_file.sql
```

**Physical Backup (MySQL Enterprise):**
MySQL Enterprise Backup command:
```bash
mysqlbackup --user=root --password --backup-dir=/backup hot backup
```

### 3. Table Maintenance Commands

Regular table maintenance ensures optimal database performance.

**ANALYZE TABLE:**
```sql
ANALYZE TABLE table_name;
```

Updates key distribution for more accurate query execution plans. Should be run after significant changes to table data.

**OPTIMIZE TABLE:**
```sql
OPTIMIZE TABLE table_name;
```

Reclaims unused space and defragments the table. Particularly useful after bulk deletes or updates.

**CHECK TABLE:**
```sql
CHECK TABLE table_name;
```

Checks tables for errors. Useful for diagnosing corruption.

**REPAIR TABLE:**
```sql
REPAIR TABLE table_name;
```

Repairs corrupted MyISAM tables.

### 4. Index Management Commands

Indexes significantly improve query performance.

**Creating Indexes:**
```sql
CREATE INDEX index_name ON table_name (column1, column2);
```

or

```sql
ALTER TABLE table_name ADD INDEX index_name (column_name);
```

**Creating Unique Index:**
```sql
CREATE UNIQUE INDEX unique_index ON table_name (column_name);
```

**Dropping Indexes:**
```sql
DROP INDEX index_name ON table_name;
```

or

```sql
ALTER TABLE table_name DROP INDEX index_name;
```

### 5. Transaction Control Commands

Transactions ensure data integrity in multi-step operations.

```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
```

For rolling back:
```sql
ROLLBACK;
```

**Setting Savepoints:**
```sql
SAVEPOINT savepoint_name;
ROLLBACK TO SAVEPOINT savepoint_name;
```

### 6. Show Commands for Database Inspection

MySQL provides numerous SHOW commands for database introspection:

```sql
SHOW DATABASES;
SHOW TABLES;
SHOW COLUMNS FROM table_name;
SHOW INDEX FROM table_name;
SHOW GRANTS FOR 'username'@'host';
SHOW PROCESSLIST;
SHOW STATUS;
SHOW VARIABLES;
```

### 7. Database and Table Management

```sql
-- Create database
CREATE DATABASE database_name;

-- Select database
USE database_name;

-- Show current database
SELECT DATABASE();

-- Create table
CREATE TABLE table_name (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Describe table structure
DESCRIBE table_name;
```

### 8. Server Administration Commands

**MySQL Service Management (Linux):**
```bash
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl status mysql
```

## Examples

### Example 1: Complete User Creation and Privilege Assignment

**Scenario:** Create a user `student_user` who can connect from localhost and has SELECT and INSERT privileges on the `university` database.

**Solution:**
```sql
-- Step 1: Create the user with password
CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'Student@123';

-- Step 2: Grant specific privileges
GRANT SELECT, INSERT ON university.* TO 'student_user'@'localhost';

-- Step 3: Reload privileges to apply changes
FLUSH PRIVILEGES;

-- Step 4: Verify the grants
SHOW GRANTS FOR 'student_user'@'localhost';
```

**Output:**
```
+----------------------------------------------------------+
| Grants for student_user@localhost                        |
+----------------------------------------------------------+
| GRANT USAGE ON *.* TO 'student_user'@'localhost'         |
| GRANT SELECT, INSERT ON `university`.* TO 'student_user'@'localhost' |
+----------------------------------------------------------+
```

### Example 2: Database Backup and Restore Workflow

**Scenario:** The college administration needs to backup the `student_records` database before making bulk updates and restore it if issues occur.

**Solution:**

**Backup Command:**
```bash
mysqldump -u root -p student_records > student_records_backup_$(date +%Y%m%d).sql
```

This creates a timestamped backup file like `student_records_backup_20240115.sql`.

**After performing updates, if issues arise:**
```bash
mysql -u root -p student_records < student_records_backup_20240115.sql
```

**Verification after restore:**
```sql
USE student_records;
SELECT COUNT(*) FROM students;
```

### Example 3: Table Optimization After Bulk Delete

**Scenario:** After deleting 10,000 inactive student records from the `alumni` table, the table size remains large and queries are slow.

**Solution:**
```sql
-- Check table status before optimization
SHOW TABLE STATUS LIKE 'alumni';

-- Analyze table to update statistics
ANALYZE TABLE alumni;

-- Optimize table to reclaim space
OPTIMIZE TABLE alumni;

-- Verify improvement
SHOW TABLE STATUS LIKE 'alumni';
```

The `OPTIMIZE TABLE` command rebuilds the table and index, reclaiming unused space and improving performance.

## Exam Tips

1. **Understand Privilege Levels:** Remember the hierarchy of privileges—Global (ON *.*), Database (ON database.*), Table (ON database.table), and Column level. This is frequently tested in DU exams.

2. **mysqldump is Essential:** Always remember the syntax for logical backup using mysqldump. The direction of arrows (`>` for backup, `<` for restore) is crucial and commonly confused.

3. **FLUSH PRIVILEGES:** After modifying user privileges directly in the mysql.user table, you must run `FLUSH PRIVILEGES` for changes to take effect. However, GRANT and REVOKE commands automatically flush privileges.

4. **Difference between DROP, DELETE, and TRUNCATE:** DROP removes the entire table structure, DELETE removes rows one by one (can be rolled back with transaction), TRUNCATE removes all rows quickly (cannot be rolled back).

5. **Transaction Properties (ACID):** Understand Atomicity, Consistency, Isolation, and Durability. Know how COMMIT and ROLLBACK work in transaction management.

6. **Index Trade-offs:** While indexes speed up SELECT queries, they slow down INSERT, UPDATE, and DELETE operations and consume additional storage space.

7. **SHOW Commands are Your Friends:** For debugging and inspection, SHOW commands are invaluable. Know how to check grants, processlist, and table status.

8. **Practical Application:** DU exams often include scenario-based questions. Practice creating users with specific privileges and performing complete backup/restore cycles.