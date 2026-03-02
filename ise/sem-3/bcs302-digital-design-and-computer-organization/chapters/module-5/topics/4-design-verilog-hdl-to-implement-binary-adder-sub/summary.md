# 4 Design Verilog HDL to implement Binary Adder-Subtractor – Half and Full Adder

===========================================================

### Module Overview

This module covers the design of Binary Adder-Subtractor circuits using Verilog HDL, focusing on Half and Full Adders.

### Key Concepts

- **Half Adder**: A binary circuit that adds two bits and produces a sum and carry bit.
- **Full Adder**: A binary circuit that adds three bits (two input bits and a carry bit) and produces a sum and carry bit.
- **Verilog HDL**: A hardware description language used to design and verify digital circuits.

### Important Formulas, Definitions, and Theorems

- **Half Adder**:
  - Sum = A ⊕ B
  - Carry = A \* B
- **Full Adder**:
  - Sum = A ⊕ B ⊕ C
  - Carry = (A \* B) ⊕ (A \* C) ⊕ (B \* C)
- **Verilog Code Structure**:
  - Module declaration (e.g., `module adder_subtractor(...`)
  - Port declarations (e.g., `input A, B, C`)
  - Assignment statements (e.g., `output sum = A ^ B`)
  - Endmodule statement (e.g., `endmodule`)
- **Verilog Operators**:
  - `^` (XOR)
  - `&` (AND)
  - `|` (OR)
  - `~` (NOT)

### Design Implementation

- **Half Adder**:
  - Use XOR and AND gates to implement the sum and carry bits.
  - Example Verilog code:

```verilog
module half_adder(A, B, sum, carry);
    input A, B;
    output sum, carry;

    assign sum = A ^ B;
    assign carry = A & B;

endmodule
```

- **Full Adder**:
  - Use XOR, AND, and OR gates to implement the sum and carry bits.
  - Example Verilog code:

```verilog
module full_adder(A, B, C, sum, carry);
    input A, B, C;
    output sum, carry;

    assign sum = A ^ B ^ C;
    assign carry = (A & B) | (A & C) | (B & C);

endmodule
```

### Revision Tips

- Focus on understanding the Verilog code structure and operators.
- Practice implementing Half and Full Adder circuits using Verilog HDL.
- Review important formulas, definitions, and theorems related to Binary Adder-Subtractor circuits.
