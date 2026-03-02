# Database Administration Commands - Summary

## Key Definitions and Concepts

- **Database Administration Commands:** SQL statements and utilities used to manage users, security, backups, and maintenance of database systems.

- **Privileges:** Permissions granted to users that determine what operations they can perform (SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, etc.).

- **mysqldump:** A MySQL utility used for logical backups, creating SQL dump files containing table definitions and data.

- **Transaction:** A sequence of database operations treated as a single unit of work with ACID properties.

- **Index:** A data structure that improves the speed of data retrieval operations on database tables.

## Important Formulas and Theorems

- **User Creation:** `CREATE USER 'username'@'host' IDENTIFIED BY 'password';`

- **Granting Privileges:** `GRANT privilege_type ON database.table TO 'user'@'host';`

- **Backup Command:** `mysqldump -u user -p database > file.sql`

- **Restore Command:** `mysql -u user -p database < file.sql`

- **Transaction Control:** `START TRANSACTION; ... COMMIT/ROLLBACK;`

## Key Points

- MySQL supports privilege assignment at four levels: Global, Database, Table, and Column.

- The `%` wildcard in host allows connections from any host, while `localhost` restricts to local connections.

- FLUSH PRIVILEGES is required after manually modifying the mysql.user table, but not after GRANT/REVOKE.

- OPTIMIZE TABLE reclaims space after bulk deletions and improves performance.

- Indexes improve SELECT performance but slow down DML operations (INSERT, UPDATE, DELETE).

- SHOW GRANTS displays the exact privileges assigned to a user.

- mysqldump creates logical backups (SQL statements), while MySQL Enterprise Backup creates physical backups.

## Common Mistakes to Avoid

1. **Arrow Direction Confusion:** Remember backup uses `>` (output direction), restore uses `<` (input direction).

2. **Forgetting FLUSH PRIVILEGES:** After direct table modifications, forgetting FLUSH causes privilege changes not to take effect.

3. **Granting ALL PRIVILEGES unnecessarily:** Follow the principle of least privilege—grant only required privileges.

4. **Not using transactions:** Performing multiple related operations without transactions can leave data inconsistent if one operation fails.

5. **Dropping tables accidentally:** Always backup before DROP operations; DROP is permanent and cannot be rolled back without backup.

## Revision Tips

1. Practice user creation and privilege assignment in a local MySQL installation to reinforce concepts.

2. Memorize the mysqldump syntax with proper direction of arrows for backup/restore.

3. Create a quick reference sheet for SHOW commands—they're essential for debugging.

4. Understand when to use OPTIMIZE vs ANALYZE vs CHECK TABLE for different maintenance scenarios.

5. Review transaction examples to clearly understand COMMIT vs ROLLBACK behavior.