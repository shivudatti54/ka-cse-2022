# **Create a User and Grant All Permissions**

## **Key Points**

- **GRANT Statement**: Used to assign privileges to a user or role.
- **Privileges**: Define the actions that can be performed on a database object.
- **Functions**: Can be used to grant permissions to perform specific database operations.
- **GRANT ALL PRIVILEGES**: Grants all privileges to a user or role.

## **Important Formulas/Definitions/Theorems**

- **GRANT Statement Syntax**: `GRANT [function] [privileges] ON [table_name] TO [user_or_role];`
- **Privilege Levels**:
  - `SELECT`: Allows the user to select data.
  - `INSERT`: Allows the user to insert data.
  - `UPDATE`: Allows the user to update data.
  - `DELETE`: Allows the user to delete data.
  - `CREATE`: Allows the user to create database objects.
  - `ALTER`: Allows the user to modify database objects.
  - `DROP`: Allows the user to drop database objects.

## **Revision Tips**

- Practice writing GRANT statements to grant specific privileges.
- Understand the difference between GRANT and REVOKE statements.
- Review the various privilege levels and their corresponding actions.

## **Example**

```sql
GRANT ALL PRIVILEGES ON database_name.* TO user_name;
```

This statement grants all privileges to the user with the name `user_name` on the `database_name` database.
