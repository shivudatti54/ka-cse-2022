# Module 4: Reading and Writing Array Data on Files in Python

## Introduction

In data science, the data you work with is rarely generated on the fly; it is almost always stored in files. For numerical and array-based data, which is the foundation of data science, efficient methods for saving and loading this data are crucial. Python's NumPy library provides highly optimized and simple-to-use functions to read from and write to files, making the process of persisting your data (and your results) seamless and efficient.

## Core Concepts and Methods

NumPy offers two primary file formats for array data: plain text files (e.g., `.txt`, `.csv`) and binary files (e.g., `.npy`, `.npz`). Each has its advantages and use cases.

### 1. Working with Text Files

Text files are human-readable and can be easily opened in text editors or spreadsheet applications like Excel. However, they are less efficient in terms of file size and read/write speed, especially for large arrays.

*   **`np.savetxt(fname, array, delimiter=' ')`**: Saves a 1D or 2D array to a text file.
    *   `fname`: Filename or file handle.
    *   `array`: The NumPy array to be saved.
    *   `delimiter`: The string used to separate values (e.g., `','` for CSV).

*   **`np.loadtxt(fname, delimiter=' ')`**: Loads data from a text file into an array. The file must have a consistent number of values in each row.

**Example: Saving and Loading a CSV File**