# **Relational Algebra: Revision Notes**

## **Unary and Binary Relational Operations**

- Unary Relational Operations:
  - Selection (σ): Selects rows that satisfy a condition
  - Projection (π): Selects a subset of attributes
  - Renaming (ρ): Renames attributes
  - Quantification (∀/∃): Expresses universal and existential quantification
  - Union (∪): Combines two relations
- Binary Relational Operations:
  - Cartesian Product (∗): Combines two relations
  - Join (∧): Combines two relations based on a common attribute
  - Difference (∖): Removes rows from one relation that exist in another
  - Intersection (∩): Selects rows that exist in both relations

## **Additional Relational Operations**

- Aggregate Operations:
  - Sum (∑): Calculates the sum of values
  - Average (avg): Calculates the average of values
  - Count (count): Counts the number of rows
- Grouping Operations:
  - Group By (GB): Groups rows based on one or more attributes
- Set Operations:
  - Union (∪): Combines two sets
  - Intersection (∩): Selects common elements from two sets

## **Formulas and Definitions**

- Relational schema: A set of tables that define the structure of a relational database
- Relational algebra: A formal language for specifying relational queries
- Query: A request to retrieve data from a relational database

## **Theorems**

- **De Morgan's Law**: ∼(A ∩ B) = ∼A ∪ ∼B
- **Distributive Law**: (A ∪ B) ∩ (C ∪ D) = (A ∩ C) ∪ (A ∩ D)

## **Examples of Queries**

- `σ name = 'John' (employees)`
- `π age (employees)`
- `ρ surname (customers)`
- `∀ x ∈ customers ∃ y ∈ orders y.total_amount > x.total_amount`

Note: This summary is a concise revision guide and is not intended to be a comprehensive treatment of the topic.
