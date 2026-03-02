# Exploratory Data Analysis (EDA) - Module 1: Structured Data

## Introduction

Exploratory Data Analysis (EDA) is the critical first step in any data science or analytics workflow. Before applying complex machine learning models or sophisticated statistical tests, you must **understand your data**. EDA involves investigating datasets to summarize their main characteristics, often using visual methods. The goal is to "explore" the data to find patterns, spot anomalies, test hypotheses, and check assumptions. This module focuses on the foundation of all data analysis: **Structured Data**.

## Core Concepts of Structured Data

### 1. What is Structured Data?

Structured data is data that is highly organized and formatted in a way that it is easily searchable in relational databases and data warehouses. It adheres to a predefined **schema** or data model, meaning it is arranged in a rigid, tabular format with rows and columns.

*   **Rows (Observations/Records):** Each row represents a single entity, instance, or observation in the dataset. For example, a single student's record.
*   **Columns (Features/Variables):** Each column represents a specific attribute, characteristic, or measurement about the entities. For example, `Student_ID`, `Name`, `Marks`, `Grade`.

This tabular structure makes it exceptionally efficient for computers to process and analyze.

### 2. Key Characteristics

*   **Tabular Format:** Exists in rows and columns, like a spreadsheet or a database table.
*   **Predefined Schema:** The data types (integer, float, string, date) and relationships between tables are defined upfront.
*   **High Accessibility:** Easily queried using languages like **SQL** (Structured Query Language).
*   **Quantifiable:** Well-suited for mathematical operations and statistical analysis.

### 3. Common Sources and File Formats

As an engineer, you will frequently encounter structured data from various sources:

*   **Relational Databases:** The most common source. Data is stored in tables linked by keys (e.g., MySQL, PostgreSQL, Oracle).
    *   *Example:* A university's student management system database.
*   **Spreadsheets:** Files like Microsoft Excel (`.xlsx`) or Google Sheets.
*   **Comma-Separated Values (CSV):** A simple, plain-text format where each line is a row and values are separated by commas. This is a universal format for data exchange.
*   **JSON/XML (Semi-structured):** While often categorized as semi-structured, they can represent structured data when they enforce a strict schema. JSON is increasingly common for web APIs.

### 4. Types of Structured Data

Understanding the type of each variable (column) is crucial for correct analysis. The two primary types are:

#### A. Numerical Data
Represent quantities that can be measured and counted. They are always numbers.
*   **Continuous:** Can take any value within a given range. They are often measurements.
    *   *Example:* `Temperature`, `Height`, `Voltage`, `Marks (0 to 100)`.
*   **Discrete:** Countable and often integer-based. They represent the number of occurrences.
    *   *Example:* `Number of students in a class`, `Number of components on a PCB`.

#### B. Categorical Data
Represent characteristics or qualities that can be used to group data. They are often labels.
*   **Nominal:** Categories with no inherent order or rank.
    *   *Example:* `Gender (Male/Female/Other)`, `City (Bengaluru/Mysuru/Mangaluru)`, `Component Type (Resistor/Capacitor/Transistor)`.
*   **Ordinal:** Categories with a logical, ordered sequence, but the intervals between categories are not known.
    *   *Example:* `Grade (A/B/C/D/F)`, `Satisfaction Level (Low/Medium/High)`, `Severity (Low/Medium/Critical)`.

### 5. Why is this Important for EDA?

The structure and type of your data directly dictate the techniques you will use during exploration:
*   **Summary Statistics:** You will calculate measures of central tendency (mean, median, mode) and dispersion (standard deviation, range) primarily for **numerical data**.
*   **Visualization:**
    *   **Histograms** and **Box plots** are ideal for visualizing the distribution of numerical data.
    *   **Bar charts** and **Pie charts** are used to show the frequency of categories in categorical data.
*   **Data Cleaning:** Identifying missing values (`NaN`, `NULL`), and outliers is straightforward in a structured format. You can easily filter, sort, and impute values based on the column's data type.
*   **Analysis:** The relationship between variables (e.g., how `Study Hours` affects `Exam Score`) can be analyzed using correlation and regression techniques, which require structured, numerical data.

## Example: A Simple Engineering Dataset

Consider a CSV file `sensor_readings.csv` from a lab experiment:

| Timestamp           | Sensor_ID | Temperature (°C) | Pressure (kPa) | Status       |
| :------------------ | :-------- | :--------------- | :------------- | :----------- |
| 2023-10-27 10:00:00 | S01       | 25.4             | 101.3          | Normal       |
| 2023-10-27 10:01:00 | S01       | 26.1             | 101.5          | Normal       |
| 2023-10-27 10:02:00 | S02       | 120.5            | 202.8          | **Overheat** |
| 2023-10-27 10:03:00 | S01       | 25.8             | 101.2          | Normal       |

*   **Structured?** Yes, it's in a clear tabular format.
*   **Rows:** Each row is a reading from a sensor at a specific time.
*   **Columns:** These are the variables/features.
    *   `Timestamp`: DateTime (Can be treated as numerical or categorical).
    *   `Sensor_ID`: Categorical (Nominal).
    *   `Temperature`: Numerical (Continuous).
    *   `Pressure`: Numerical (Continuous).
    *   `Status`: Categorical (Nominal).

An EDA on this data would involve calculating the average temperature, checking for anomalous readings (like the overheat event for S02), and perhaps plotting pressure vs. temperature to see if a relationship exists.

## Key Points / Summary

*   **Foundation of EDA:** Structured data is the organized, tabular data (rows and columns) that serves as the primary input for EDA.
*   **Characteristics:** It is defined by a strict schema, is easily queryable (e.g., with SQL), and is highly efficient for computation.
*   **Data Types:** Correctly identifying whether data is **Numerical** (Continuous/Discrete) or **Categorical** (Nominal/Ordinal) is the first step in choosing the right analytical and visualization techniques.
*   **Ubiquitous Formats:** Commonly found in relational databases, CSV files, and spreadsheets.
*   **Prerequisite for Analysis:** Understanding your data's structure is non-negotiable. It enables effective data cleaning, summarization, visualization, and hypothesis testing—the core pillars of EDA.

Mastering the handling of structured data is an essential skill for any engineer venturing into data analytics, machine learning, or the broader field of data science.