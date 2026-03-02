# **Syntactic Analysis: Revision Notes**

### Context-Free Grammar (CFG)

- A set of production rules for generating strings in a specific language
- Strings can be broken down into non-terminal symbols and terminal symbols
- Examples:
  - S -> NP VP
  - NP -> Det N
  - VP -> V NP

### Constituency

- A hierarchical representation of a sentence into a tree-like structure
- Constituents are identified by a set of rules, such as:
  - Phrase structure grammar (PSG)
  - Constituent-constituent (CC) analysis

### Top-Down Parsing

- A parsing algorithm that starts with the overall sentence and breaks it down into constituent parts
- Uses a stack data structure to keep track of the current parse tree
- Examples:
  - Recursive descent parsing
  - LR parsing

### Bottom-Up Parsing

- A parsing algorithm that starts with individual words and builds up the overall sentence
- Uses a table or matrix to keep track of the parse tree
- Examples:
  - Earley parsing
  - CYK parsing

### CYK Parsing

- A bottom-up parsing algorithm that uses a table to keep track of the parse tree
- Works by filling in a table where each cell represents a possible parse for a substring
- Formula:
  - CYK(n, m) = max{CYK(i, j) | i + j = n} for n = m
- Theorem:
  - A sentence can be parsed if and only if the table is filled in correctly

### Important Formulas and Definitions

- **Context-free grammar**: A set of production rules for generating strings in a specific language
- **Constituent**: A hierarchical representation of a sentence into a tree-like structure
- **CYK table**: A table used in CYK parsing to keep track of the parse tree
- **Earley parsing**: A bottom-up parsing algorithm that uses a table to keep track of the parse tree
- **Top-down parsing**: A parsing algorithm that starts with the overall sentence and breaks it down into constituent parts
