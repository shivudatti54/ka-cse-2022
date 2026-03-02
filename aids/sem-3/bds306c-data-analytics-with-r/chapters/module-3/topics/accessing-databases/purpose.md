# Learning Purpose: Accessing Databases

**1. Why is this topic important?**
In the real world, valuable data is rarely stored in simple spreadsheet files; it resides in organized, scalable databases. The ability to efficiently access and retrieve data directly from these databases is a foundational skill for any data analyst. It prevents the error-prone process of manual export/import and ensures you can work with the most current, large, and complex datasets available.

**2. What will students learn?**
Students will learn the core techniques for connecting R to relational databases. This includes establishing connections using `DBI` and `odbc`, securely managing credentials, and writing `SQL` queries directly within R to pull specific data subsets into a data frame for subsequent analysis.

**3. How does it connect to other concepts?**
This module directly builds upon prior knowledge of R data structures (e.g., data frames from Module 1) and data manipulation with `dplyr` (from Module 2). It provides the crucial data acquisition step that feeds into the entire analytical workflow, enabling more advanced cleaning, visualization, and modeling with live database data.

**4. Real-world applications**
This skill is essential for creating reproducible analytical pipelines that automatically pull data from corporate data warehouses (e.g., SQL Server, PostgreSQL), customer relationship management (CRM) systems like Salesforce, or any other application that uses a database backend, ensuring analyses are both efficient and based on a single source of truth.