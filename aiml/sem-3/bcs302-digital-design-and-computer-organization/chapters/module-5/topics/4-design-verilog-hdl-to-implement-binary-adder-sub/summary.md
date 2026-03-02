# **Designing Verilog HDL for Binary Adder-Subtractor**

## **Half Adder**

- **Definition:** A digital circuit that adds two binary digits (0 or 1) and produces a sum and a carry.
- **Truth Table:**
  - A=0, B=0 -> S=0, C=0
  - A=0, B=1 -> S=1, C=0
  - A=1, B=0 -> S=0, C=1
  - A=1, B=1 -> S=1, C=1
- **Verilog Code:**

```verilog
module half_adder(A, B, sum, carry);
    input A, B;
    output sum, carry;

    assign sum = A XOR B;
    assign carry = A AND B;
endmodule
```

- **Full Adder**

---

- **Definition:** A digital circuit that adds three binary digits (0 or 1) and produces a sum and a carry.
- **Truth Table:**
  - A=0, B=0, C=0 -> S=0, C=0
  - A=0, B=0, C=1 -> S=0, C=0
  - A=0, B=1, C=0 -> S=1, C=0
  - A=0, B=1, C=1 -> S=1, C=0
  - A=1, B=0, C=0 -> S=1, C=1
  - A=1, B=0, C=1 -> S=0, C=1
  - A=1, B=1, C=0 -> S=0, C=1
  - A=1, B=1, C=1 -> S=0, C=1
- **Verilog Code:**

```verilog
module full_adder(A, B, C, sum, carry);
    input A, B, C;
    output sum, carry;

    assign sum = ((A XOR B) XOR C);
    assign carry = ((A AND B) OR (A AND C) OR (B AND C));
endmodule
```

- **Half and Full Adder Subtraction**

---

- **Subtraction Method:** Subtracting the least significant bit of the second operand from the most significant bit of the first operand.
- **Verilog Code:**

```verilog
module half_subtractor(A, B, sum, borrow);
    input A, B;
    output sum, borrow;

    assign sum = ~A;
    assign borrow = A AND B;
endmodule

module full_subtractor(A, B, C, sum, borrow);
    input A, B, C;
    output sum, borrow;

    assign sum = ~(A XOR B);
    assign borrow = (A AND B) OR (A AND C) OR (B AND C);
endmodule
```

- **Important Formulas and Theorems:**
  - Boolean Algebra: `A XOR B = (A AND !B) OR (A AND B)`
  - Boolean Algebra: `A AND B = A AND B`
  - Boolean Algebra: `A OR B = A OR B`
