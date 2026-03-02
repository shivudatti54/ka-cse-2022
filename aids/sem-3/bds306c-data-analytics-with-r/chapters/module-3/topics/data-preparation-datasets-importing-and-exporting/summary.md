# **Data Preparation Datasets, Importing and Exporting files, Accessing Databases, Data Cleaning and Transformation Chapter 3**

### 3.1 Datasets

- **Definition:** A collection of data, often in numerical or textual format, used for analysis or modeling.
- **Types of datasets:**
  - In-memory datasets (e.g., R's built-in datasets)
  - External datasets (e.g., CSV, Excel files)
  - Database datasets (e.g., SQL tables)
- **Importing datasets in R:**
  - `data <- read.csv("filename.csv")`
  - `data <- read.table("filename.txt")`
  - `data <- fread("filename.csv")`

### 3.2 Importing and Exporting Files

- **Importing files:**
  - CSV: `read.csv()`
  - Excel: `readxl::read_excel()`
  - Text: `read.table()`
  - JSON: `jsonlite::json_loads()`
- **Exporting files:**
  - CSV: `write.csv()`
  - Excel: `writexl::write_excel()`
  - Text: `write.table()`
  - JSON: `jsonlite::writeJSON()`

### 3.3 Accessing Databases

- **Definition:** A database is a collection of organized data that can be stored, managed, and retrieved electronically.
- **Types of databases:**
  - Relational databases (e.g., MySQL, PostgreSQL)
  - NoSQL databases (e.g., MongoDB, Cassandra)
- **Accessing databases in R:**
  - `db <- dbConnect(RSQLite::SQLite(), "database.db")`
  - `db <- dbConnect(RDBI::DBI(), "database.db")`
  - `db <- dbConnect(odbc::odbc(), "database.db")`

### 3.4 Data Cleaning and Transformation

- **Definition:** Data cleaning and transformation involve preparing data for analysis by removing errors, handling missing values, and transforming data into a suitable format.
- **Data cleaning techniques:**
  - Handling missing values
  - Removing duplicates
  - Data normalization
- **Data transformation techniques:**
  - Data aggregation
  - Data grouping
  - Data scaling

Note: This summary is not exhaustive and is intended to provide a brief overview of the key points.
