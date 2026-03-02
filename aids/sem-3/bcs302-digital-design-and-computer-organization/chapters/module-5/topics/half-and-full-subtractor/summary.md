# Half and Full Subtractor

### Definitions

- **Half Subtractor**: A digital circuit that subtracts two binary numbers by borrowing from the least significant bit.
- **Full Subtractor**: A digital circuit that subtracts three binary numbers and can borrow from multiple bits.

### Key Formulas

- **Half Subtractor Formula**:
  ```
  A = B
  B = C
  P = (B ⊕ C)  ( Borrow Flag )
  ```

```
  Where:
  * `A` is the result of the subtraction
  * `B` is the least significant bit of the minuend
  * `C` is the least significant bit of the subtrahend
  * `P` is the borrow flag (1 if a borrow is needed, 0 otherwise)
* **Full Subtractor Formula**:
```

A = (B ⊕ C) ( Borrow Flag )
D = (B ⊕ C ⊕ B ⊕ D) ( Borrow Flag )
E = B ⊕ D

```
  Where:
  * `A` is the result of the subtraction
  * `B` is the least significant bit of the minuend
  * `C` is the least significant bit of the subtrahend
  * `D` is the second least significant bit of the minuend
  * `E` is the second least significant bit of the subtrahend
  * `P` and `Q` are the borrow flags for the first and second bits respectively

### Theorems

* **Borrowing Theorem**: If `B = 1` and `C = 0`, then `P = 1` and `B = 0`.
* **Latching Theorem**: If `P = 1` and `B = 0`, then `B = 0` and `B' = 1` (next cycle).

### Important Concepts

* **Borrow Flag**: A flag that indicates whether a borrow is needed.
* **Latching**: The process of setting the carry to 1 based on the borrow flag.
* **Full Subtraction**: The process of subtracting three binary numbers with multiple borrow flags.
```
