# **Database Management Systems**

## **Chapter 9.1 to 9.2 Textbook 2: 3.5 RBT: L1**

## **Introduction**

Database Management Systems (DBMS) have revolutionized the way we store, manage, and retrieve data. In this chapter, we will delve into the world of DBMS, exploring its historical context, modern developments, and key concepts.

## **Historical Context**

The concept of DBMS dates back to the 1960s, when the first relational database management system, IBM's Information Management System (IMS), was developed. However, it wasn't until the 1970s that the first commercial relational database management system, IBM's System R, was released. The introduction of SQL (Structured Query Language) in the 1980s further popularized the use of DBMS.

## **Modern Developments**

In recent years, there has been a significant shift towards NoSQL databases, which are designed to handle large amounts of unstructured or semi-structured data. Some popular NoSQL databases include:

- **MongoDB**: A document-based database that stores data in JSON-like documents.
- **Redis**: An in-memory data store that can be used as a database, message broker, or cache.
- **Cassandra**: A distributed database that is designed to handle large amounts of data across many commodity servers.

## **Key Concepts**

### 1. Relational Database Management Systems

Relational DBMS are based on the concept of relational algebra, which involves defining relationships between data entities using tables and queries.

**Example**

Suppose we have two tables: `Employees` and `Departments`.

| Employee ID | Name        | Department ID | Department Name |
| ----------- | ----------- | ------------- | --------------- |
| 1           | John Smith  | 10            | Sales           |
| 2           | Jane Doe    | 20            | Marketing       |
| 3           | Bob Johnson | 30            | IT              |

We can define a relationship between the two tables using a foreign key, `Department ID`, which references the `Department ID` column in the `Departments` table.

| Department ID | Department Name |
| ------------- | --------------- |
| 10            | Sales           |
| 20            | Marketing       |
| 30            | IT              |

### 2. NoSQL Database Management Systems

NoSQL databases are designed to handle large amounts of unstructured or semi-structured data.

**Example**

Suppose we have a document-based database that stores data in JSON-like documents.

| Document ID | Name      | Description                    |
| ----------- | --------- | ------------------------------ |
| 1           | Product 1 | This is a sample product       |
| 2           | Product 2 | This is another sample product |
| 3           | Product 3 | This is a third sample product |

### 3. Data Modeling

Data modeling is the process of designing and representing data entities and relationships using entities, attributes, and relationships.

**Example**

Suppose we want to model a database for a university's student information system.

| Entity  | Attributes                                    |
| ------- | --------------------------------------------- |
| Student | Student ID, Name, Age, Course ID, Course Name |
| Course  | Course ID, Course Name, Credits               |

## **Data Flow Diagrams**

Data flow diagrams (DFDs) are a graphical representation of the flow of data through an application or system.

**Example**

Suppose we want to model a database for a simple online shopping system.

```
                                +-----------------+
                                |  Customer     |
                                |  Information  |
                                +-----------------+
                                |  |             |
                                |  |  Place Order  |
                                |  |             |
                                v             v
                                +-----------------+
                                |  Order Details  |
                                |  (Order ID,   |
                                |   Product ID,  |
                                |   Quantity)    |
                                +-----------------+
                                |  |             |
                                |  |  Update Order |
                                |  |             |
                                v             v
                                +-----------------+
                                |  Product       |
                                |  Information   |
                                +-----------------+
```

## **Case Study: University Student Information System**

Suppose we want to design a database for a university's student information system. We need to define the entities, attributes, and relationships between them.

| Entity     | Attributes                                         |
| ---------- | -------------------------------------------------- |
| Student    | Student ID, Name, Age, Course ID, Course Name      |
| Course     | Course ID, Course Name, Credits                    |
| Professor  | Professor ID, Name, Department ID, Department Name |
| Department | Department ID, Department Name                     |

**Relationships**

- A student is enrolled in one or more courses (one-to-many).
- A course is taught by one or more professors (one-to-many).
- A professor teaches one or more courses (many-to-many).

## **SQL Implementation**

We can implement this database using SQL. Here is an example:

```sql
CREATE TABLE Students (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(255),
  Age INT,
  CourseID INT,
  CourseName VARCHAR(255)
);

CREATE TABLE Courses (
  CourseID INT PRIMARY KEY,
  CourseName VARCHAR(255),
  Credits INT
);

CREATE TABLE Professors (
  ProfessorID INT PRIMARY KEY,
  Name VARCHAR(255),
  DepartmentID INT,
  DepartmentName VARCHAR(255)
);

CREATE TABLE Departments (
  DepartmentID INT PRIMARY KEY,
  DepartmentName VARCHAR(255)
);

CREATE TABLE Course_Professors (
  CourseID INT,
  ProfessorID INT,
  PRIMARY KEY (CourseID, ProfessorID),
  FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
  FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
);

CREATE TABLE Student_Courses (
  StudentID INT,
  CourseID INT,
  PRIMARY KEY (StudentID, CourseID),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```

## **Further Reading**

- **Database Systems: The Complete Book** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Systems: A Practical Approach to Design, Implementation, and Management** by Hector Garcia-Molina, Ivan Martinez, and Jose Valenza
- **Database Systems: A Review of the Literature** by Kilpelainen and Saarinen

In this chapter, we have explored the world of Database Management Systems, including their historical context, modern developments, and key concepts. We have also examined relational, NoSQL, and data modeling, as well as data flow diagrams and case studies. Finally, we have implemented a university student information system using SQL.
