# Learning Purpose: Accessing Databases

**1. Why is this topic important?**
Modern data analysts rarely work with isolated flat files. Data is stored in relational database management systems (RDBMS) like MySQL, PostgreSQL, and SQLite. The ability to efficiently access, query, and import this data directly into R is a fundamental and highly marketable skill, preventing error-prone manual exports and enabling reproducible analysis on live data.

**2. What will students learn?**
Students will learn to establish connections between R and various databases using appropriate packages (e.g., `DBI`, `RMySQL`, `RSQLite`). They will learn to write and execute SQL queries from within R to selectively pull data and will practice bringing result sets into R as data frames for subsequent analysis.

**3. How does it connect to other concepts?**
This module directly builds on prior knowledge of data structures (e.g., data frames from Module 1) and data manipulation (e.g., `dplyr` from Module 2). It provides the crucial data acquisition step that feeds into all subsequent processes like data cleaning, visualization, and statistical modeling.

**4. Real-world applications**
This skill is essential for building automated reporting pipelines, performing analysis on large datasets that exceed memory limits by querying only necessary parts, and creating Shiny apps that interact dynamically with a backend database, which is a standard architecture in industry.