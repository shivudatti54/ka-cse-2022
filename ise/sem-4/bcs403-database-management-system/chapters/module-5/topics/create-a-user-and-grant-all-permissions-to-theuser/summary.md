# **Create a User and Grant All Permissions to the User**

**Key Points:**

- **CREATE USER Statement:**
  - `CREATE USER [user_name]@[host];`
    - `user_name`: The name of the user to be created.
    - `[host]`: The host on which the user will be created. (Optional)
- **GRANT Privileges:**
  - `GRANT [privilege] ON [database_name].*[table_object_name] TO [user_name];`
    - `privilege`: The privileges to be granted (e.g., `ALL PRIVILEGES`, `SELECT`, `INSERT`, etc.).
    - `[database_name]`: The name of the database on which the privileges will be granted.
    - `*[table_object_name]*`: The name of the table or other database objects to which privileges will be granted.
    - `TO [user_name]`: The user to whom the privileges will be granted.

**Important Formulas and Definitions:**

- **GRANT Statement Syntax:** `GRANT [privilege] ON [database_name].*[table_object_name] TO [user_name];`
- **Privileges:** `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `GRANT`, `REVOKE`
- **Database Object Names:** `table`, `view`, `procedure`, `function`, `index`
- **User Table:** `mysql.users`

**Theorem:** The `GRANT` statement can be used to assign privileges to a user, while the `REVOKE` statement can be used to revoke privileges from a user.

**Quick Revision Points:**

- Use `CREATE USER` to create a new user.
- Use `GRANT` to assign privileges to a user.
- Use `REVOKE` to revoke privileges from a user.
- Use the `ALL PRIVILEGES` privilege to grant all privileges to a user.
