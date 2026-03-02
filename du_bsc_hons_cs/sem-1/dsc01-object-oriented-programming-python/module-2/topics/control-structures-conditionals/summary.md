# Control Structures: Conditionals

## Introduction

Control structures in Python determine the flow of program execution. **Conditionals** allow the program to make decisions based on certain conditions, enabling dynamic and flexible code execution. This is a fundamental topic in Object Oriented Programming and is included in the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus.

---

## Key Concepts

### 1. What are Control Structures?
- Statements that control the order of execution of other statements
- Three main types: **Sequence**, **Selection (Conditionals)**, and **Iteration**
- Conditionals implement **selection/branching** logic

### 2. Types of Conditional Statements in Python

#### **if Statement**
- Simplest conditional; executes block only when condition is `True`
- Syntax:
  ```python
  if condition:
      # statements
  ```

#### **if-else Statement**
- Provides alternative execution path
- Syntax:
  ```python
  if condition:
      # if true
  else:
      # if false
  ```

#### **if-elif-else Statement**
- Handles multiple conditions sequentially
- Syntax:
  ```python
  if condition1:
      # block1
  elif condition2:
      # block2
  else:
      # block3
  ```

### 3. Comparison Operators
- `==` (equal), `!=` (not equal)
- `>` (greater than), `<` (less than)
- `>=` (greater or equal), `<=` (less or equal)

### 4. Logical Operators
- `and` — returns `True` if both conditions are true
- `or` — returns `True` if at least one condition is true
- `not` — inverts the boolean value

### 5. Nested Conditionals
- Conditionals inside other conditionals
- Used for complex decision-making scenarios
- Example: `if` inside another `if` block

### 6. Key Points for Exam Revision

- **Condition evaluates to boolean**: Python treats non-zero numbers and non-empty objects as `True`
- **Indentation matters**: Python uses indentation to define code blocks
- **elif vs else-if**: Python uses `elif`, not `else if`
- **Ternary operator**: Compact form — `value_if_true if condition else value_if_false`
- **No switch-case**: Python 3.10+ has `match-case`; earlier versions use `if-elif` chains

---

## Conclusion

Conditional statements are essential for implementing decision-making logic in Python programs. Mastery of `if`, `elif`, and `else` statements, along with comparison and logical operators, is crucial for both written exams and practical programming. Understand syntax, indentation rules, and common patterns to excel in this topic.