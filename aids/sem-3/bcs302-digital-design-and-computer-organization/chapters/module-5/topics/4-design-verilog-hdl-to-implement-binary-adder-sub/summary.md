# **4 Design Verilog HDL to implement Binary Adder-Subtractor – Half and Full Adder**

### Overview

- Binary Adder-Subtractor is a digital circuit that performs binary addition or subtraction.
- Half Adder and Full Adder are basic binary adder-subtractors.

### Half Adder

---

- **Definition:** A Half Adder is a 2-bit binary adder that adds two bits and produces a sum and carry-out.
- **Truth Table:**

| A   | B   | Sum | Carry-out |
| --- | --- | --- | --------- |
| 0   | 0   | 0   | 0         |
| 0   | 1   | 1   | 0         |
| 1   | 0   | 1   | 0         |
| 1   | 1   | 0   | 1         |

- **Verilog Implementation:**

```verilog
module half_adder(A, B, sum, carry_out);
    input A, B;
    output sum, carry_out;

    assign sum = (A & B);
    assign carry_out = A | B;
endmodule
```

### Full Adder

---

- **Definition:** A Full Adder is a 3-bit binary adder that adds three bits and produces a sum and carry-out.
- **Truth Table:**

| A   | B   | C   | Sum | Carry-out |
| --- | --- | --- | --- | --------- |
| 0   | 0   | 0   | 0   | 0         |
| 0   | 0   | 1   | 1   | 0         |
| 0   | 1   | 0   | 1   | 0         |
| 0   | 1   | 1   | 0   | 1         |
| 1   | 0   | 0   | 1   | 0         |
| 1   | 0   | 1   | 0   | 1         |
| 1   | 1   | 0   | 0   | 1         |
| 1   | 1   | 1   | 1   | 1         |

- **Verilog Implementation:**

```verilog
module full_adder(A, B, C, sum, carry_out);
    input A, B, C;
    output sum, carry_out;

    wire temp;
    wire sum_out;

    assign sum_out = (A & B & C) | ((~A & ~B & C) | (~A & B & ~C) | (A & ~B & ~C));
    assign carry_out = (A & ~B & ~C) | (~A & B & C) | (A & B & ~C) | (~A & ~B & C);

endmodule
```

### Important Formulas and Theorems

- **Carry-In and Carry-Out:** The carry-in is the input that is passed to the adder to produce a carry-out.
- **Boolean Algebra:** Boolean algebra is used to simplify the Verilog implementation of the adder-subtractor.

Note: This summary provides key points for quick revision before exams. It is not a comprehensive guide to designing binary adder-subtractors in Verilog.
