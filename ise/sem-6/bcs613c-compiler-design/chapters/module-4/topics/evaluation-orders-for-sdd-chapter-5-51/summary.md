# **Evaluation Orders for SDD Chapter 5: 5.1**

## **Key Points**

- Evaluation Orders (EO) define the sequence of parses to apply when parsing a string
- EO is used in SLR parsing to construct the parse table
- EO is a crucial concept in parser design
- The EO is determined by the SDD (State Determinization Diagram)
- EO is calculated using the following formula:
  - EO = (A × S) + I
    - A: set of non-terminal symbols
    - S: set of start symbols
    - I: set of terminal symbols

## **Important Formulas and Definitions**

- **Evaluation Order**: the sequence of parses to apply when parsing a string
- **SDD (State Determinization Diagram)**: a diagram used to determine the evaluation order
- **SLR (Simple LR) Parsing Algorithm**: an algorithm used to construct the parse table using the evaluation order

## **Theorems**

- **Theorem 5.1.1**: The evaluation order is determined by the SDD and can be calculated using the formula EO = (A × S) + I

## **Notes**

- EO is used to construct the parse table for SLR parsing
- EO is a crucial concept in parser design and is used in various parsing algorithms
- EO can be used to analyze the complexity of a parser and determine its efficiency
