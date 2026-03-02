# **Chapter 10: Data Warehousing**

### 10.1 Introduction to Data Warehousing

---

A data warehouse is a centralized repository that stores data from various sources in a structured and normalized format. It provides a single point of truth for an organization's data, enabling users to access and analyze data from different perspectives.

### 10.2 Principles of Dimensional Modelling

---

Dimensional modelling is a methodology used to design a data warehouse. It involves breaking down data into dimensions and facts, and defining relationships between them.

#### Key Concepts:

- **Fact Table**: A table that stores facts or measurements, such as sales amount or customer count.
- **Dimension Table**: A table that stores information about the facts, such as date, product, or location.
- **Star Schema**: A data warehouse design pattern that uses a fact table surrounded by dimension tables.
- **Star Operations**: Operations performed on the dimension tables to support the fact table, such as inserting, updating, and deleting data.

### 10.3 Dimensional Modelling Techniques

---

There are several techniques used in dimensional modelling, including:

#### Key Concepts:

- **Hierarchical Modelling**: Modelling relationships between dimensions using a hierarchical structure.
- **Star and Snowflake Modelling**: Modelling relationships between dimensions using a star and snowflake structure.
- **Factual Hierarchy Modelling**: Modelling relationships between facts and dimensions using a hierarchical structure.
- **Data Mart Modelling**: Modelling a subset of an organization's data using a data mart.

### 10.4 Star Schema

---

A star schema is a data warehouse design pattern that uses a fact table surrounded by dimension tables. It is a popular choice for data warehousing because it is easy to understand and implement.

#### Key Concepts:

- **Fact Table**: A table that stores facts or measurements.
- **Dimension Tables**: Tables that store information about the facts.
- **Date Dimension**: A dimension table that stores date information.
- **Geographic Dimension**: A dimension table that stores geographic information.

### 10.5 Star Operations

---

Star operations are operations performed on the dimension tables to support the fact table. They include:

#### Key Concepts:

- **Insert**: Inserting new data into the dimension tables.
- **Update**: Updating existing data in the dimension tables.
- **Delete**: Deleting data from the dimension tables.

### 10.6 Best Practices

---

Best practices for dimensional modelling include:

#### Key Concepts:

- **Use Normalization**: Normalizing data to eliminate data redundancy and improve data integrity.
- **Use Granularity**: Using granularity to provide detailed information about the data.
- **Use Summary Aggregations**: Using summary aggregations to provide aggregated values for large datasets.
- **Use Indexing**: Indexing dimension tables to improve query performance.

### 10.7 Data Warehousing Tools

---

Data warehousing tools are software applications that support data warehousing and dimensional modelling. Examples of data warehousing tools include:

#### Key Concepts:

- **ETL Tools**: Tools that extract, transform, and load data from various sources.
- **OLAP Tools**: Tools that support online analytical processing and data analysis.
- **Data warehousing Platforms**: Platforms that support data warehousing and dimensional modelling.

By following these best practices and using the techniques and tools outlined in this chapter, you can design and implement a data warehouse that meets your organization's needs.
