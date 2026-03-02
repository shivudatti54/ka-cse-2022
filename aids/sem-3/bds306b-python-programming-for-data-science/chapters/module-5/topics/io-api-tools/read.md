# Module 5: I/O API Tools in Python for Data Science

## Introduction

In Data Science, the ability to read data from various sources (like CSV files, databases, web APIs) and write processed results back is a fundamental and often the first step in any workflow. Python's I/O (Input/Output) API tools, primarily within the `pandas` library, provide a powerful, flexible, and efficient suite of functions to handle this data exchange. This module focuses on these essential tools for serialization—converting data structures into a storable or transmittable format—and deserialization—reconstructing the data from that format.

## Core Concepts and Functions

The `pandas` library is the workhorse for data I/O in Python data science. Its functions are designed to be intuitive, handling the intricacies of parsing and data type conversion automatically.

### 1. Reading and Writing Text Files

**a) CSV (Comma-Separated Values):**
The most common format for tabular data.

*   **Reading:** `pd.read_csv()`
    *   This function reads a CSV file into a `pandas DataFrame`, the primary data structure for data manipulation.
    *   **Key parameters:**
        *   `filepath_or_buffer`: Path to the file or a URL.
        *   `sep`: Delimiter to use (e.g., `','`, `'\t'` for tab).
        *   `header`: Row number to use as column names (default `0`). Use `None` if no header.
        *   `index_col`: Column to use as the row labels.
        *   `dtype`: Specify data types for columns.
        *   `usecols`: Which columns to read.

*   **Writing:** `df.to_csv()`
    *   Writes the DataFrame to a CSV file.
    *   **Key parameters:**
        *   `path_or_buf`: Output file path.
        *   `index`: Whether to write row indices (default `True`). Often set to `False` when saving processed data.

**Example:**