# **Add a Column Commission with Domain to the Employeetable**

### Key Points

- Add a new column `commission` to the `Employeetable` table.
- Define the `commission` column with a domain to restrict valid values.
- Update the column data type to accommodate the new values.
- Modify existing triggers and indexes as necessary.

### Important Formulas and Definitions

- **Domain**: A set of values that a column can take.
- **Trigger**: A stored procedure that runs automatically in response to a specific event.
- **Index**: A data structure that improves query performance.

### Important Theorems and Concepts

- **SQL syntax**: Use the `ALTER TABLE` statement to modify the column.
- **Domain constraints**: Use the `CHECK` constraint to define the domain.

### Revision Notes

- **ALTER TABLE statement**: `ALTER TABLE table_name ADD COLUMN column_name data_type;`
- **CHECK constraint**: `ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK (column_name IN (value1, value2, ...));`
- **Trigger example**: `CREATE TRIGGER trigger_name BEFORE INSERT ON table_name FOR EACH ROW SET NEW.commission = NEW.salary * 0.1;`

### Quick Revision Before Exams

- Make sure to update the `ALTER TABLE` statement with the correct column name and data type.
- Define the domain constraints using the `CHECK` constraint.
- Test the triggers and indexes after making changes to the column.
