# HDL Models of Combinational Circuits – Adder

=====================================================

## Overview

---

An adder is a fundamental digital circuit used to perform binary addition. It takes two binary numbers as inputs and produces the sum and carry-out as outputs. In this study material, we will explore the HDL (Hardware Description Language) models of combinational circuits, specifically focusing on the adder circuit.

## What is an Adder?

---

An adder is a digital circuit that performs binary addition. It takes two binary numbers as inputs, A and B, and produces the sum, S, and carry-out, C. The adder circuit consists of a series of AND gates, OR gates, and NOT gates.

### Example:

Suppose we want to add the binary numbers 101 (5 in decimal) and 110 (6 in decimal). The adder circuit would produce a sum of 1001 (13 in decimal) and a carry-out of 1.

## HDL Models of Combinational Circuits

---

### Basic Concepts

- **Combinational Circuits:** These circuits produce an output based on a combination of inputs and do not have any memory storage.
- **HDL (Hardware Description Language):** A language used to describe the behavior of digital circuits.
- **Verilog and VHDL:** Two popular HDLs used for designing digital circuits.

### HDL Models of Adder Circuit

#### Verilog Code:

```verilog
module adder(A, B, S, C);
    input A, B;
    output S, C;

    assign S = ~(A & ~B) | (A & B);
    assign C = (A & ~B) | (~A & B);
endmodule
```

#### VHDL Code:

```vhdl
entity adder is
    Port ( A : in  STD_LOGIC;
           B : in  STD_LOGIC;
           S : out  STD_LOGIC;
           C : out  STD_LOGIC);
end adder;

architecture Behavioral of adder is
begin
    S <= ~(A and not B) or (A and B);
    C <= (A and not B) or (not A and B);
end Behavioral;
```

### How the HDL Models Work

The Verilog and VHDL models of the adder circuit work by using a combination of AND, OR, and NOT gates to perform the binary addition.

- The `S` output is calculated using the expression `~(A & ~B) | (A & B)`, which is equivalent to performing a bitwise OR operation between the two inputs.
- The `C` output is calculated using the expression `(A & ~B) | (~A & B)`, which is equivalent to performing a bitwise OR operation between the two inputs and also determining the carry-out.

### Key Concepts

- **Bitwise Operations:** These operations are used to perform binary operations between bits.
- **AND, OR, and NOT Gates:** These gates are used to implement the HDL models of the adder circuit.
- **Binary Addition:** This is the fundamental operation performed by the adder circuit.

### Conclusion

---

In conclusion, the HDL models of combinational circuits, specifically the adder circuit, are an essential part of digital design and computer organization. Understanding the concepts of combinational circuits, HDLs, and binary addition is crucial for designing and implementing digital circuits.

### Study Tips

- Practice creating HDL models of the adder circuit using Verilog and VHDL.
- Study binary addition and bitwise operations.
- Review the concepts of combinational circuits and HDLs.

### References

---

- "Digital Design and Computer Organization" by Morris Mano
- "Verilog HDL: A Guide to Hardwired Digital Systems" by Rakesh V. Kulkarni
- "VHDL: A Guide to Hardware Description Language" by Rakesh V. Kulkarni
