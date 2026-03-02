# Python Built-in Functions for Looping (Module 2)

## Introduction

In data science, we constantly work with collections of data—lists of numbers, rows in a DataFrame, or sequences of text. Manually iterating over each element using traditional `for` or `while` loops can sometimes be verbose and inefficient. Python's built-in functions for looping provide powerful, concise, and optimized tools to process these collections. Mastering `enumerate()`, `zip()`, `map()`, and `filter()` is essential for writing clean, readable, and performant data science code.

## Core Concepts & Examples

### 1. `enumerate(iterable, start=0)`

This function adds a counter to any iterable object (like a list or tuple) and returns it as an `enumerate` object. This is crucial when you need access to both the index and the value of each item during iteration.

*   **Use Case:** Iterating over a dataset where the position/index of the data point is meaningful (e.g., tracking row numbers in a log file).
*   **Syntax:** `for index, value in enumerate(iterable, start=0):`

**Example:**