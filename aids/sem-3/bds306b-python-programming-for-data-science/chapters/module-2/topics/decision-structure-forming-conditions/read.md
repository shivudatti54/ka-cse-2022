# Module 2: Decision Structures - Forming Conditions

## Introduction

In programming, the flow of execution is rarely a straight line. We often need our programs to make decisions and execute different blocks of code based on specific criteria. This is where **decision structures** come into play. At the heart of every decision structure is a **condition**—a logical statement that evaluates to either `True` or `False`. Mastering the formation of these conditions is fundamental to writing dynamic and intelligent Python code for data science, allowing you to filter data, handle edge cases, and direct your program's logic based on the data it encounters.

## Core Concepts: Forming Conditions

A condition is formed using **comparison** and **logical** operators. These operators allow you to compare values and combine multiple logical statements.

### 1. Comparison Operators

These operators are used to compare two values. The result of a comparison is always a Boolean value (`True` or `False`).

| Operator | Description              | Example          | Result |
| :------- | :----------------------- | :--------------- | :----- |
| `==`     | Equal to                 | `5 == 5`         | `True` |
| `!=`     | Not equal to             | `5 != 3`         | `True` |
| `>`      | Greater than             | `7 > 5`          | `True` |
| `<`      | Less than                | `7 < 5`          | `False`|
| `>=`     | Greater than or equal to | `10 >= 10`       | `True` |
| `<=`     | Less than or equal to    | `8 <= 10`        | `True` |

**Example in a Data Science Context:**
Imagine you have a dataset of student scores. You want to find all students who scored above a passing grade (let's say 40).