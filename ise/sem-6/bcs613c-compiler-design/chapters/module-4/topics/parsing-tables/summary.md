# **Parsing Tables**

**Definitions and Notations**

- A parsing table is a table used to store the parse table for an LR parser.
- It is used to determine the next production to apply during the parsing process.
- The table is typically stored in a 2D table with states on one axis and terminals on the other.

**Key Points**

- **Elements of a Parsing Table:**
  - `gij`: the production to apply when in state `i` and reading terminal `j`.
  - `gi`: the next state when in state `i` and reading terminal `j`.
  - `ij`: the current state when in state `i` and reading terminal `j`.
- **Parsing Table Construction:**
  - The table is constructed by filling in the values for each `gij` and `gi` based on the production rules and the LR parsing algorithm.
  - The table is typically divided into three parts:
    - `gij`: the production table.
    - `gi`: the next state table.
    - `ij`: the table showing the current state.
- **Parsing Table Theorems:**
  - **Closure Property**: if `gij = gik`, then `gi = gik`.
  - **Transition Property**: if `gij = 1`, then `gi = i'` for some state `i'`.
- **Parsing Algorithm:**
  - The algorithm works by starting in an initial state and reading the input one symbol at a time.
  - At each step, the algorithm looks up the value of `gi` in the parsing table to determine the next state and production to apply.

**Important Formulas and Equations**

- **LR(1) Parsing Algorithm:**
  - `gij = 1` if `gik = 1` and `k = i'` for some state `i'`
  - `gi = i'` if `gij = 1` and `k = i'`
- **SLR(1) Parsing Algorithm:**
  - `gij = gik` if `gij = 1` and `k = i'` for some state `i'`

**Revision Tips**

- Make sure to understand the definitions and notations used in the parsing table.
- Practice constructing a parsing table for a given grammar.
- Review the theorems and formulas used in the parsing algorithm.
- Familiarize yourself with the LR and SLR parsing algorithms.
