# **DATABASE MANAGEMENT SYSTEM**

## **Module: Ch 9.1 to 9.2 Textbook 2: 3.5 RBT: L1**

## **Introduction**

Database management systems (DBMS) are software applications that enable us to store, manage, and retrieve data efficiently. A DBMS acts as an intermediary between the user and the database, providing a layer of abstraction to hide the underlying complexity of data storage and retrieval. In this module, we will delve into the historical context, modern developments, and key concepts of database management systems.

## **Historical Context**

The concept of database management systems dates back to the 1960s, when the first relational database management systems (RDBMS) were introduced. The first RDBMS, called System R, was developed in 1969 at IBM. However, it wasn't until the 1970s that the first commercial RDBMS, called Ingres, was released.

In the 1980s, the development of object-oriented programming (OOP) led to the introduction of object-oriented database management systems (OODBMS). The first OODBMS, called Extended Entity-Relational Model (EER), was developed in 1981.

The 1990s saw the rise of client-server architecture, which enabled multiple users to access a centralized database over a network. This led to the development of modern DBMS, such as Oracle and Microsoft SQL Server.

## **Modern Developments**

Today, database management systems continue to evolve with advancements in technology. Some of the key developments include:

- **Cloud-based DBMS**: Cloud-based DBMS, such as Amazon RDS and Google Cloud SQL, provide a scalable and on-demand infrastructure for database management.
- **NoSQL DBMS**: NoSQL DBMS, such as MongoDB and Cassandra, offer an alternative to traditional RDBMS, providing flexible schema designs and high scalability.
- **Big Data Analytics**: The increasing availability of big data has led to the development of DBMS that can handle large amounts of data, such as Hadoop and Spark.
- **Artificial Intelligence (AI) and Machine Learning (ML)**: The integration of AI and ML into DBMS enables personalized recommendations, predictive analytics, and automated data processing.

## **Key Concepts**

### 1. Database Architecture

A database architecture refers to the design of a database, including the physical and logical structure, data models, and data relationships.

### 2. Data Models

There are several data models, including:

- **Relational Model**: A relational model stores data in tables with well-defined relationships between them.
- **Object-Oriented Model**: An object-oriented model stores data in objects that encapsulate data and behavior.
- **Graph Model**: A graph model stores data as a network of nodes and edges.

### 3. Data Normalization

Data normalization is the process of organizing data in a database to minimize data redundancy and dependency.

### 4. Data Denormalization

Data denormalization is the process of organizing data in a database to improve performance and reduce complexity.

## **Case Study: Online Shopping Platform**

Suppose we are building an online shopping platform that requires a database to store customer information, product details, and order history. We will use a relational model to store the data.

## **Database Design**

We will create a database with the following tables:

| Table Name | Attributes                                                                              |
| ---------- | --------------------------------------------------------------------------------------- |
| Customers  | customer_id (primary key), name, email, password                                        |
| Products   | product_id (primary key), name, description, price                                      |
| Orders     | order_id (primary key), customer_id (foreign key), product_id (foreign key), order_date |

## **SQL Code**

```sql
CREATE TABLE Customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  price DECIMAL(10, 2)
);

CREATE TABLE Orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```

## **Example Use Cases**

- **Inserting a new customer**: `INSERT INTO Customers (customer_id, name, email, password) VALUES (1, 'John Doe', 'john.doe@example.com', 'password123');`
- **Inserting a new product**: `INSERT INTO Products (product_id, name, description, price) VALUES (1, 'Product 1', 'This is product 1', 19.99);`
- **Placing an order**: `INSERT INTO Orders (order_id, customer_id, product_id, order_date) VALUES (1, 1, 1, '2022-01-01');`

## **Further Reading**

- **Database Systems: The Complete Book** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Systems: The Complete Book, 2nd Edition** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Management Systems, 4th Edition** by Raghu Ramakrishnan and Johannes Gehrke

## **Diagram Descriptions**

The following diagrams illustrate the different components of a database management system:

- **Database Architecture Diagram**
  ```
  +---------------+
  |  Database   |
  +---------------+
         |
         |  Physical
         |  Structure
         |  ------
         |
         |  Logical
         |  Structure
         |  ------
         |
         |  Data
         |  Models
         |  ------
         |
         +---------------+
              |  Data
              |  Normalization
              +---------------+
  ```

````

*   **Relational Model Diagram**
    ```
  +---------------+
  |  Relations  |
  +---------------+
           |
           |  Tables
           |  ------
           |
           |  Attributes
           |  ------
           |
           +---------------+
                |  Relations
                |  ------
                |
                +---------------+
````

- **Object-Oriented Model Diagram**
  ```
  +---------------+
  |  Objects    |
  +---------------+
         |
         |  Encapsulation
         |  ------
         |
         |  Inheritance
         |  ------
         |
         |  Polymorphism
         |  ------
         |
         +---------------+
              |  Objects
              |  ------
              |
              +---------------+
  ```

```

```
