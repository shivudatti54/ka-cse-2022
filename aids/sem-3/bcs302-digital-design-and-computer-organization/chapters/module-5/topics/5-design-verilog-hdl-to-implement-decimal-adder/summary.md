# 5 Design Verilog HDL to implement Decimal adder

=============================================

### Overview

---

- Decimal adder is a digital circuit that adds two decimal numbers.
- Verilog HDL is used to design and implement digital circuits.

### Key Points

---

- **Decimal Representation**
  - Decimal numbers are represented using a base-10 system.
  - Each digit in a decimal number is multiplied by a power of 10.
- **Adder Architecture**
  - Half adder: adds two single-digit numbers.
  - Full adder: adds three single-digit numbers.
  - Carry generation and propagation.
- **Verilog Implementation**
  - Use of binary counters and arithmetic logic units (ALUs).
  - Example: decimal adder implementation using a 4-bit binary counter.

### Important Formulas and Definitions

---

- **Binary Counter**: a counter that counts binary numbers.
- **Arithmetic Logic Unit (ALU)**: performs arithmetic and logical operations.
- **Carry Generation**: the process of generating a carry bit for a full adder.
- **Propagated Carry**: the process of propagating a carry bit through an adder.

### Theorems

---

- **Karnaugh Map (K-Map)**: a method for simplifying Boolean expressions.
- **Boolean Algebra**: a set of mathematical operations used to manipulate Boolean expressions.

### Example Verilog Code

---

- `decimal_adder.v`:

```verilog
module decimal_adder(
    input [3:0] a,
    input [3:0] b,
    output [4:0] sum
);

    // Half adder logic
    assign sum[0] = a[0] ^ b[0];

    // Full adder logic
    assign sum[1] = (a[0] & b[0]) ^ (a[1] & b[1]) ^ (a[0] & b[1]) ^ (a[1] & b[0]);

    assign sum[2] = (a[0] & b[0]) & (a[1] & b[1]) ^ (a[0] & b[1]) | (a[1] & b[0] & a[2] & b[2]) ^ (a[0] & b[2] & a[1] & b[1]) | (a[1] & b[2] & a[2] & b[0]);

    assign sum[3] = (a[0] & b[0] & b[2] & a[2]) | (a[0] & b[2] & b[1] & a[1]) | (a[1] & b[0] & b[2] & a[2]) | (a[2] & b[1] & b[0] & a[0]);

    assign sum[4] = (a[0] & b[0] & b[2] & b[1]) | (a[0] & b[1] & b[2] & a[1]) | (a[1] & b[0] & b[1] & b[2]) | (a[2] & b[0] & b[2] & b[1]) | (a[2] & b[1] & b[0] & b[2]);

endmodule
```

Note: This is a simplified example and may not be optimal for a real-world implementation.
