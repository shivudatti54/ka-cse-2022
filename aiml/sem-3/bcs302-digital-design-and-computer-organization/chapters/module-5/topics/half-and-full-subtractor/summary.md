# Half and Full Subtractor

### Definitions and Theorems

- **Half Subtractor**: performs subtraction with two single-bit inputs, producing a 4-bit result.
- **Full Subtractor**: performs subtraction with three single-bit inputs, producing a 4-bit result.
- **Borrow**: a bit that is "borrowed" from the most significant bit to aid in subtraction.
- **Complement**: the bit that is the opposite of the most significant bit.

### Formulas

- **Half Subtractor Formula**:
  - A (input 1) = 0, B (input 2) = 0, C (result) = 0
  - A = 0, B = 1, C = 1: C = 0, B' + A = 1
  - A = 1, B = 0, C = 1: C = 0, B + A' = 1
  - A = 1, B = 1, C = 0: C = 1, A' + B' = 1
- **Full Subtractor Formula**:
  - A (input 1) = 0, B (input 2) = 0, C (input 3) = 0: C = 0, B + A = 0
  - A = 0, B = 0, C = 1: C = 0, B + A = 1
  - A = 1, B = 0, C = 1: C = 1, B + A = 0
  - A = 1, B = 1, C = 0: C = 0, B' + A = 1
  - A = 1, B = 1, C = 1: C = 0, B + A = 1

### Key Points

- Half Subtractor uses two single-bit inputs and produces a 4-bit result.
- Full Subtractor uses three single-bit inputs and produces a 4-bit result.
- Borrow and complement are used to aid in subtraction.
- The formulas for Half and Full Subtraction are essential for digital design and computer organization.
