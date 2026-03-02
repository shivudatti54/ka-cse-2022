# **Data Preparation: Datasets, Importing and Exporting Files, Accessing Databases, Data Cleaning and Transformation**

**Chapter 3: Data Preparation**

### 3.1: Understanding Datasets

- **Definition:** A dataset is a collection of data points, variables, and observations that are used to train, test, and validate machine learning models.
- **Types of Datasets:**
  - **Tabular data:** Categorical and numerical data in a table format.
  - **Temporal data:** Data that varies over time, such as time series data.
  - **Spatial data:** Data that varies across space, such as geospatial data.
- **Importance of Datasets:**
  - **Data quality:** A high-quality dataset is essential for building accurate models.
  - **Data variety:** Datasets should be diverse to account for different scenarios and distributions.

**3.2: Importing and Exporting Files**

- **Importing Files:**
  - **CSV (Comma Separated Values):** A common file format for tabular data.
  - **Excel:** A popular file format for tabular data, but may require additional processing.
  - **JSON (JavaScript Object Notation):** A lightweight file format for structured data.
- **Exporting Files:**
  - **Saving datasets:** Use the `saveRDS()` function in R to save datasets to a file.
  - **Exporting data visualization:** Use the `ggsave()` function in R to save data visualizations to a file.

**Example: Importing a CSV File**

```r
# Load the necessary libraries
library(readr)

# Import the CSV file
dataset <- read_csv("path/to/dataset.csv")

# View the first few rows of the dataset
head(dataset)
```

**3.3: Accessing Databases**

- **Definition:** A database is a collection of organized data that is stored in a way that allows for efficient querying and retrieval.
- **Types of Databases:**
  - **Relational databases:** Organize data into tables with defined relationships.
  - **NoSQL databases:** Store data in a variety of formats, such as key-value or document stores.
- **Accessing Databases in R:**
  - **DBI (Database Interface):** A set of functions for interacting with different databases.
    **Example: Accessing a Relational Database**

```r
# Load the necessary libraries
library(DBI)

# Connect to the database
conn <- dbConnect(RSQLite::SQLite(), "path/to/database.db")

# Query the database
query <- "SELECT * FROM table_name"
result <- dbGetQuery(conn, query)

# Close the database connection
dbDisconnect(conn)
```

**3.4: Data Cleaning and Transformation**

- **Definition:** Data cleaning and transformation involve preprocessing data to prepare it for analysis and modeling.
- **Types of Data Cleaning:**
  - **Handling missing values:** Deciding what to do with missing data, such as imputation or deletion.
  - **Data normalization:** Scaling data to a common range to prevent feature dominance.
- **Types of Data Transformation:**
  - **Data aggregation:** Combining data from multiple sources or variables into a single value.
  - **Data conversion:** Converting data from one format to another, such as converting categorical data to numerical data.

**Example: Handling Missing Values**

```r
# Load the necessary libraries
library(dplyr)

# Create a sample dataset with missing values
dataset <- data.frame(
    column1 = c(1, 2, NA, 4),
    column2 = c(NA, 2, 3, 4)
)

# Handle missing values using imputation
dataset <- dataset %>%
    fill_missing_values()

# View the dataset
head(dataset)
```
