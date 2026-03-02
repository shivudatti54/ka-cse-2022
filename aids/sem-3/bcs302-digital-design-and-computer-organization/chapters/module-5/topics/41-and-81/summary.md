# 4:1 and 8:1

## Digital Design and Computer Organization

### Key Points

- **4:1 and 8:1 Multiplexers**
  - 4:1 multiplexer: Selects one of 4 input lines and routes it to 1 output line.
  - 8:1 multiplexer: Selects one of 8 input lines and routes it to 1 output line.
- **Number of Select Lines (nS)**
  - Number of select lines needed for a 4:1 multiplexer: 2
  - Number of select lines needed for an 8:1 multiplexer: 3
- **Logic Formula**
  - 4:1 multiplexer: A = (S1 \* B1) + (S1 \* B2) + (S1 \* B3) + (S2 \* B4)
  - 8:1 multiplexer: A = (S1 \* B1) + (S1 \* B2) + (S1 \* B3) + (S1 \* B4) + (S2 \* B5) + (S2 \* B6) + (S2 \* B7) + (S3 \* B8)
- **Karnaugh Map (K-Map)**
  - Used to simplify Boolean expressions and minimize the number of logic gates required.
- **Harrington Diagram**
  - Used to simplify Boolean expressions and minimize the number of logic gates required.

### Important Formulas and Theorems

- **De Morgan's Theorem**
  - (A + B)' = A' \* B'
  - (A \* B)' = A' + B'
- **Boolean Algebra Identities**
  - A + A' = 1
  - A \* A' = 0
