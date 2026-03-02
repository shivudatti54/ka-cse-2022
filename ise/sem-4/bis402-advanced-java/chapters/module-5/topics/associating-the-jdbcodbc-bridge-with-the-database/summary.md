# Associating JDBC/ODBC Bridge with Database

### Key Points

- **JDBC/ODBC Bridge**: Acts as a bridge between JDBC and the database.
- **Database Driver**: A piece of software that enables JDBC to communicate with the database.
- **Types of Database Drivers**:
  - **Type 1**: Converts JDBC requests to ODBC requests and sends them to the database.
  - **Type 2**: Converts JDBC requests to SQL statements and sends them to the database.
  - **Type 4**: Native driver, converts JDBC requests to the native language of the database.
- **JDBC Driver Manager**: Manages the loading of JDBC drivers.
- **JDBC Driver URL**: Points to the database driver and the database.

### Formulas/Definitions/Theorems

- ** JDBC Driver URL**: `jdbc:driver://host:port/database`
- **Database Driver Class**: `java.sql.drivers.Driver`

### Important Concepts

- **Registering JDBC Drivers**: Registering the JDBC drivers with the DriverManager.
- **Getting the DriverManager**: Getting the DriverManager from the java.sql package.
- **Loading the Driver**: Loading the driver using the `Class.forName()` method.

### Quick Revision Tips

- Understand the different types of database drivers.
- Know how to register JDBC drivers with the DriverManager.
- Understand the JDBC Driver URL and how to use it.
