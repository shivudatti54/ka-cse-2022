# **Mapping Conceptual Design into a Logical Design: Relational Database Design using ER-to-Relational Mapping**

## **Introduction**

Relational database design is a critical step in developing a database management system (DBMS). It involves mapping a conceptual design into a logical design, which is then converted into a physical design. In this module, we will delve into the details of relational database design using ER-to-Relational mapping, a widely used technique for transforming conceptual designs into logical designs.

## **Historical Context**

The concept of ER-to-Relational mapping dates back to the 1970s, when Edgar F. Codd introduced the relational model for database management. The relational model was a significant departure from traditional database management systems, which were based on hierarchical or network structures. ER-to-Relational mapping was later developed as a way to transform conceptual designs into logical designs.

## **ER-to-Relational Mapping**

ER-to-Relational mapping involves transforming an entity-relationship (ER) diagram into a relational database schema. The ER diagram represents the conceptual structure of the database, while the relational schema represents the logical structure.

The transformation process involves the following steps:

1. **Identify the entities and attributes**: The first step is to identify the entities and attributes in the ER diagram.
2. **Determine the relationships**: The next step is to determine the relationships between the entities in the ER diagram.
3. **Convert relationships to foreign keys**: The relationships between entities are converted into foreign keys in the relational schema.
4. **Map attributes to columns**: The attributes of each entity are mapped to columns in the relational schema.
5. **Create tables and relationships**: The final step is to create tables and relationships in the relational schema based on the ER diagram.

## **Example: University Database**

Suppose we want to design a database for a university. We can use an ER diagram to represent the conceptual structure of the database.

ER Diagram:

```
+---------------+
|  Student    |
+---------------+
|  Student ID (PK) |
|  Name          |
|  Age           |
+---------------+
+---------------+
|  Course      |
+---------------+
|  Course ID (PK) |
|  Name          |
+---------------+
+---------------+
|  Enrollments  |
+---------------+
|  Student ID (FK) |
|  Course ID (FK) |
+---------------+
```

In this ER diagram, we have three entities: `Student`, `Course`, and `Enrollments`. The `Student` entity has three attributes: `Student ID`, `Name`, and `Age`. The `Course` entity has two attributes: `Course ID` and `Name`. The `Enrollments` entity has two attributes: `Student ID` and `Course ID`.

## **ER-to-Relational Mapping**

To transform the ER diagram into a relational schema, we need to follow the steps outlined above.

1. **Identify the entities and attributes**: The entities and attributes in the ER diagram are:

- `Student` entity: `Student ID`, `Name`, `Age`
- `Course` entity: `Course ID`, `Name`
- `Enrollments` entity: `Student ID`, `Course ID`

2. **Determine the relationships**: The relationships between entities in the ER diagram are:

- A student can enroll in many courses (one-to-many).
- A course can be enrolled in by many students (many-to-many).

3. **Convert relationships to foreign keys**: The relationships between entities are converted into foreign keys in the relational schema:

- `Student` entity: `Student ID` (PK)
- `Course` entity: `Course ID` (PK)
- `Enrollments` entity: `Student ID` (FK), `Course ID` (FK)

4. **Map attributes to columns**: The attributes of each entity are mapped to columns in the relational schema:

- `Student` entity: `Student ID`, `Name`, `Age`
- `Course` entity: `Course ID`, `Name`
- `Enrollments` entity: `Student ID`, `Course ID`

5. **Create tables and relationships**: The final step is to create tables and relationships in the relational schema based on the ER diagram:

```
CREATE TABLE Students (
  Student_ID INT PRIMARY KEY,
  Name VARCHAR(255),
  Age INT
);

CREATE TABLE Courses (
  Course_ID INT PRIMARY KEY,
  Name VARCHAR(255)
);

CREATE TABLE Enrollments (
  Student_ID INT,
  Course_ID INT,
  PRIMARY KEY (Student_ID, Course_ID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);
```

## **Case Study: Online Shopping Database**

Suppose we want to design a database for an online shopping system. We can use an ER diagram to represent the conceptual structure of the database.

ER Diagram:

```
+---------------+
|  Customer    |
+---------------+
|  Customer ID (PK) |
|  Name          |
|  Email         |
+---------------+
+---------------+
|  Products    |
+---------------+
|  Product ID (PK) |
|  Name          |
|  Price         |
+---------------+
+---------------+
|  Orders     |
+---------------+
|  Order ID (PK) |
|  Customer ID (FK) |
|  Product ID (FK) |
+---------------+
```

In this ER diagram, we have four entities: `Customer`, `Products`, `Orders`, and `Order Details`. The `Customer` entity has three attributes: `Customer ID`, `Name`, and `Email`. The `Products` entity has three attributes: `Product ID`, `Name`, and `Price`. The `Orders` entity has three attributes: `Order ID`, `Customer ID`, and `Product ID`. The `Order Details` entity has three attributes: `Order ID`, `Product ID`, and `Quantity`.

## **ER-to-Relational Mapping**

To transform the ER diagram into a relational schema, we need to follow the steps outlined above.

1. **Identify the entities and attributes**: The entities and attributes in the ER diagram are:

- `Customer` entity: `Customer ID`, `Name`, `Email`
- `Products` entity: `Product ID`, `Name`, `Price`
- `Orders` entity: `Order ID`, `Customer ID`, `Product ID`
- `Order Details` entity: `Order ID`, `Product ID`, `Quantity`

2. **Determine the relationships**: The relationships between entities in the ER diagram are:

- A customer can place many orders (one-to-many).
- A product can be ordered by many customers (many-to-many).
- An order can have many order details (one-to-many).

3. **Convert relationships to foreign keys**: The relationships between entities are converted into foreign keys in the relational schema:

- `Customer` entity: `Customer ID` (PK)
- `Products` entity: `Product ID` (PK)
- `Orders` entity: `Order ID` (PK), `Customer ID` (FK), `Product ID` (FK)
- `Order Details` entity: `Order ID` (FK), `Product ID` (FK)

4. **Map attributes to columns**: The attributes of each entity are mapped to columns in the relational schema:

- `Customer` entity: `Customer ID`, `Name`, `Email`
- `Products` entity: `Product ID`, `Name`, `Price`
- `Orders` entity: `Order ID`, `Customer ID`, `Product ID`
- `Order Details` entity: `Order ID`, `Product ID`, `Quantity`

5. **Create tables and relationships**: The final step is to create tables and relationships in the relational schema based on the ER diagram:

```
CREATE TABLE Customers (
  Customer_ID INT PRIMARY KEY,
  Name VARCHAR(255),
  Email VARCHAR(255)
);

CREATE TABLE Products (
  Product_ID INT PRIMARY KEY,
  Name VARCHAR(255),
  Price DECIMAL(10,2)
);

CREATE TABLE Orders (
  Order_ID INT PRIMARY KEY,
  Customer_ID INT,
  Product_ID INT,
  FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
  FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

CREATE TABLE Order_Details (
  Order_ID INT,
  Product_ID INT,
  Quantity INT,
  PRIMARY KEY (Order_ID, Product_ID),
  FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
  FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);
```

## **Applications and Advantages**

ER-to-Relational mapping has several applications and advantages in database design:

- **Efficient data storage**: ER-to-Relational mapping ensures that data is stored efficiently in the database, reducing the need for redundant data.
- **Improved data integrity**: ER-to-Relational mapping ensures that data is consistent and accurate, reducing the risk of data errors.
- **Flexibility and scalability**: ER-to-Relational mapping allows for flexibility and scalability in database design, making it easier to add new data and relationships.
- **Easy maintenance and updates**: ER-to-Relational mapping makes it easy to maintain and update the database, reducing the need for complex and time-consuming maintenance tasks.

## **Conclusion**

ER-to-Relational mapping is a widely used technique for transforming conceptual designs into logical designs. It has several applications and advantages in database design, including efficient data storage, improved data integrity, flexibility and scalability, and easy maintenance and updates. In this module, we have covered the concepts and techniques of ER-to-Relational mapping, including the steps involved in transforming an ER diagram into a relational schema.

## **Further Reading**

- **"Database Systems: The Complete Book"** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **"Database Systems: A Practical Approach"** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **"Database Systems: A Managerial Perspective"** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **"Relational Database Design"** by Edgar F. Codd
- **"Entity-Relationship Modeling"** by Edgar F. Codd
- **"Database Design"** by [Your Name]
