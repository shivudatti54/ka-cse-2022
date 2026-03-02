# **3.1 to 3.10 RBT: L1 - Database Management System**

## **Introduction**

Database Management System (DBMS) is a software system that allows you to define, create, maintain, and manipulate databases. It provides a way to store, manage, and retrieve data in a structured and controlled manner. In this module, we will cover the fundamental concepts of DBMS, including Relational Database Management System (RDBMS), NoSQL databases, and modern developments in the field.

## **Historical Context**

The concept of DBMS dates back to the 1960s, when the first relational database management systems were developed. The relational model, introduced by Edgar F. Codd in 1970, revolutionized the way data was stored and managed. The relational model emphasized the use of tables, rows, and columns to store and retrieve data.

In the 1980s, the development of transaction processing and query languages such as SQL (Structured Query Language) further enhanced the capabilities of DBMS. The introduction of object-oriented databases in the 1990s and the rise of NoSQL databases in the 2000s marked significant milestones in the evolution of DBMS.

## **Relational Database Management System (RDBMS)**

RDBMS is a type of DBMS that uses a relational model to store and manage data. The relational model consists of:

- **Tables**: These are the basic storage units in an RDBMS. Each table has a unique name and contains rows and columns.
- **Rows**: Each row represents a single record or entry in the table.
- **Columns**: Each column represents a field or attribute in the table.

## **Key Features of RDBMS**

- **ACID Compliance**: RDBMS ensures that database transactions are processed in a consistent and reliable manner.
- **Data Integrity**: RDBMS provides features such as primary keys, foreign keys, and referential integrity to ensure data consistency and accuracy.
- **Data Security**: RDBMS provides features such as access control, encryption, and authentication to ensure data security.

## **Examples of RDBMS**

- **MySQL**: A popular open-source RDBMS.
- **PostgreSQL**: A powerful and feature-rich open-source RDBMS.
- **Microsoft SQL Server**: A commercial RDBMS developed by Microsoft.

## **Case Study: Online Shopping Platform**

Suppose we want to develop an online shopping platform that allows users to browse and purchase products. We can use an RDBMS to store and manage the data.

- **Database Schema**: We can create a database schema with tables for products, customers, orders, and payment information.
- **Data Storage**: We can store product information, customer details, order information, and payment information in the respective tables.
- **Querying**: We can use SQL queries to retrieve data from the database, such as retrieving a list of all products or retrieving the total cost of an order.

## **NoSQL Databases**

NoSQL databases are designed to handle large amounts of unstructured or semi-structured data. They are often used in big data applications.

## **Key Features of NoSQL Databases**

- **Schema-less**: NoSQL databases do not require a predefined schema.
- **Scalability**: NoSQL databases are designed to handle large amounts of data and scale horizontally.
- **High performance**: NoSQL databases are optimized for high-performance applications.

## **Examples of NoSQL Databases**

- **MongoDB**: A popular NoSQL database.
- **Cassandra**: A distributed NoSQL database.
- **Redis**: An in-memory NoSQL database.

## **Modern Developments**

- **Cloud-based DBMS**: Cloud-based DBMS allow users to deploy and manage databases in the cloud.
- **Big data analytics**: Big data analytics involve processing and analyzing large amounts of data to gain insights.
- **Artificial intelligence and machine learning**: AI and ML involve using database management systems to train and deploy models.

## **Diagrams**

### RDBMS Diagram

```markdown
+---------------+
| Table |
+---------------+
| | |
| | |
| | |
| | |
+---------------+
| Row |
+---------------+
| | | |
| | | |
| | | |
| | | |
+---------------+
| Column |
+---------------+
```

### NoSQL Database Diagram

```markdown
+---------------+
| Collection |
+---------------+
| | |
| | |
| | |
| | |
+---------------+
| Document |
+---------------+
| | | |
| | | |
| | | |
| | | |
+---------------+
| Field |
+---------------+
```

## **Further Reading**

- **Database Systems: The Complete Book** by Hector Garcia-Molina
- **Database Management Systems** by Raghu Ramakrishnan and Johannes Gehrke
- **NoSQL Distilled** by Pramod J. Sadalage and Martin Fowler

I hope this detailed content helps you understand the concepts of RDBMS and NoSQL databases, including their historical context, key features, examples, and modern developments.
