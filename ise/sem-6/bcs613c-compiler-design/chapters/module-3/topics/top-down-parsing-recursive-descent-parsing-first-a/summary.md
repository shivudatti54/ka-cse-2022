# **Top-Down Parsing: Recursive Descent Parsing, First and Follow, LL(1) Grammars**

### Overview

- Top-down parsing is a parsing technique that starts with the overall structure of the input and breaks it down into smaller components.

### Key Points

- **Recursive Descent Parsing (RDP)**:
  - A top-down parsing technique that uses recursive function calls to parse the input.
  - Each function corresponds to a production rule in the grammar.
- **First and Follow Sets**:
  - First set: set of terminal symbols that can be derived from the start symbol in one step.
  - Follow set: set of terminal symbols that can be derived from a non-terminal symbol in one or more steps.
- **LL(1) Grammars**:
  - A type of LL parser that can only recognize grammars with a single production rule for each non-terminal symbol.
  - LL(1) parser can always make a correct prediction.

### Important Formulas and Definitions

- ** productions**: A rule of the form A -> α, where A is a non-terminal symbol and α is a string of terminal symbols.
- ** parsing table**: A table used to store the parsing information for each non-terminal symbol.
- **leftmost derivation**: A sequence of productions that starts with the leftmost symbol and ends with the start symbol.

### Theorems

- **Chomsky's Theorem**: If a grammar is LL(1), then it can be parsed by an LL(1) parser.

### Bottom-Up Parsing: Reductions, Handle Pruning, Shift Reduce Parsing

### Key Points

- **Reductions**:
  - A reduction is a sequence of productions that transforms a non-terminal symbol into another non-terminal symbol.
- **Handle Pruning**:
  - A technique used to reduce the number of productions in the parsing table.
  - It works by removing redundant productions.
- **Shift Reduce Parsing**:
  - A top-down parsing technique that uses shift and reduce operations to parse the input.

### Important Formulas and Definitions

- **shift**: A shift operation that moves the input head to the next symbol.
- **reduce**: A reduce operation that replaces a non-terminal symbol with a string of terminal symbols.

### Theorems

- **Parsing Algorithm**: If a grammar is LL(1), then it can be parsed by an LL(1) parser using the shift-reduce parsing algorithm.
