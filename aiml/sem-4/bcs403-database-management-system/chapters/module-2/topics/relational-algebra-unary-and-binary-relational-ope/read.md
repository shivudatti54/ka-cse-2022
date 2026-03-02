# **Relational Algebra: Unary and Binary Relational Operations, Additional Relational Operations**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Unary Relational Operations](#unary-relational-operations)
   - [Definition](#definition)
   - [Examples](#examples)
3. [Binary Relational Operations](#binary-relational-operations)
   - [Definition](#definition)
   - [Examples](#examples)
4. [Additional Relational Operations](#additional-relational-operations)
   - [Aggregate Operations](#aggregate-operations)
   - [Grouping Operations](#grouping-operations)
5. [Examples of Queries in Relational Algebra](#examples-of-queries-in-relational-algebra)

## **Introduction**

Relational algebra is a formal language used to manipulate relational databases. It provides a way to specify queries and operations on relational databases using logical operators and functions. In this topic, we will learn about unary and binary relational operations, additional relational operations, and examples of queries in relational algebra.

## **Unary Relational Operations**

### Definition

Unary relational operations are operations that take a single relation as input and produce another relation as output. They are used to perform operations such as selecting, projecting, and renaming attributes.

### Examples

- **Selection**: Selects a subset of tuples from a relation based on a condition.
  - _σ (condition)_ R: Selects tuples from relation R where the condition is true.
  - Example: Let R = {1, 2, 3, 4, 5} and condition x > 3. Then σ(x > 3) R = {4, 5}.
- **Projection**: Selects a subset of attributes from a relation.
  - π (attribute list)\* R: Selects attributes from relation R.
  - Example: Let R = {id, name, age} and attribute list {id, age}. Then π(id, age) R = {1, 2, 3, 4, 5}.
- **Renaming**: Renames attributes in a relation.
  - ρ (attribute list)\* R: Renames attributes in relation R.
  - Example: Let R = {id, name, age} and attribute list {name, age} -> {new_name, new_age}. Then ρ(new_name, new_age) R = {1, Jane, 25, 2, Bob, 30, 3, Alice, 35, 4, Mike, 40, 5, Emma, 45}.

## **Binary Relational Operations**

### Definition

Binary relational operations are operations that take two relations as input and produce another relation as output. They are used to perform operations such as joining, dividing, and intersecting relations.

### Examples

- **Joining**: Combines two relations based on a common attribute.
  - _ρ (relation list)_: Joins relations based on a common attribute.
  - Example: Let R1 = {id, name, age} and R2 = {id, city, country}. Then ρ(R1, R2, id) = {1, Jane, 25, New York, USA, 2, Bob, 30, London, UK}.
- **Division**: Divides one relation into two relations based on a common attribute.
  - _π (attribute list)_: Divides relation into two relations based on a common attribute.
  - Example: Let R = {id, name, age, salary} and attribute list {age}. Then π(age) R = {25, 30, 35, 40}.
- **Intersection**: Finds common tuples between two relations.
  - _σ (condition)_: Finds common tuples between two relations based on a condition.
  - Example: Let R1 = {id, name, age} and R2 = {id, name, age, city}. Then σ(id = 1, name = 'Jane') (R1 ∩ R2) = {1, Jane, 25}.

## **Additional Relational Operations**

### Aggregate Operations

Aggregate operations are used to perform calculations on a relation.

- **SUM**: Calculates the sum of a set of values.
  - _σ (condition)_ SUM (attribute list): Calculates the sum of a set of values.
  - Example: Let R = {id, salary} and attribute list {salary}. Then σ(sum(salary) = 1000) R = {1, 1000}.
- **AVG**: Calculates the average of a set of values.
  - _σ (condition)_ AVG (attribute list): Calculates the average of a set of values.
  - Example: Let R = {id, salary} and attribute list {salary}. Then σ(avg(salary) = 500) R = {1, 500}.
- **MAX**: Finds the maximum value of a set of values.
  - _σ (condition)_ MAX (attribute list): Finds the maximum value of a set of values.
  - Example: Let R = {id, salary} and attribute list {salary}. Then σ(max(salary) = 1000) R = {1, 1000}.
- **MIN**: Finds the minimum value of a set of values.
  - _σ (condition)_ MIN (attribute list): Finds the minimum value of a set of values.
  - Example: Let R = {id, salary} and attribute list {salary}. Then σ(min(salary) = 500) R = {1, 500}.

### Grouping Operations

Grouping operations are used to group a relation by one or more attributes.

- **GROUP BY**: Groups a relation by one or more attributes.
  - _σ (condition)_ GROUP BY (attribute list): Groups a relation by one or more attributes.
  - Example: Let R = {id, name, age} and attribute list {age}. Then σ(age = 25) GROUP BY (age) R = {1, Jane, 25, 2, Bob, 25, 3, Alice, 25}.

## **Examples of Queries in Relational Algebra**

- **Example 1**: Find the names of students with age greater than 18.
  - Let R = {id, name, age} and condition x > 18.
  - Then σ(x > 18) R = {1, John, 20, 2, Alice, 22, 3, Bob, 25}.
- **Example 2**: Find the total salary for each department.
  - Let R = {id, name, age, salary, department} and attribute list {salary, department}.
  - Then σ(sum(salary) = 1000) GROUP BY (department) R = {1, 1000, 2, 500, 3, 750}.
- **Example 3**: Find the names of students who are between 18 and 25 years old and from New York.
  - Let R = {id, name, age, city, country} and conditions x between 18 and 25 and city = 'New York'.
  - Then σ(x between 18 and 25) AND (city = 'New York') R = {1, John, 20, 2, Alice, 22}.
