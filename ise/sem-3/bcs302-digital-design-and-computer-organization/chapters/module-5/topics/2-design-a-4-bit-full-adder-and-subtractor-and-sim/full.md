# **Designing a 4-bit Full Adder and Subtractor using Basic Gates**

## **Introduction**

In digital design, a full adder and subtractor are fundamental building blocks for more complex arithmetic and logic circuits. A full adder is used to perform binary addition, while a subtractor is used to perform binary subtraction. In this module, we will design and simulate a 4-bit full adder and subtractor using basic gates.

## **Historical Context**

The concept of full adders and subtractors dates back to the early days of digital computing. In the 1950s and 1960s, full adders and subtractors were implemented using CMOS (Complementary Metal-Oxide-Semiconductor) technology. With the advent of advanced CMOS designs and the development of Field-Programmable Gate Arrays (FPGAs), full adders and subtractors are now widely used in digital systems.

## **Designing a 4-bit Full Adder**

A full adder is a digital circuit that performs binary addition of two bits and a carry-in bit. The 4-bit full adder will take two 4-bit inputs (A and B) and a carry-in bit (C_in). The output of the full adder will be a 4-bit result (A_out, B_out, C_out, and Sum_out).

## **Block Diagram**

Here is the block diagram of a 4-bit full adder:

```
          +---------------+
          |  Carry-In    |
          +---------------+
                  |
                  |  C_in
                  v
+---------------+---------------+
|  Bit 3        |  Bit 2        |
|  A3           |  A2           |
+---------------+---------------+
|  XOR        |       XOR      |
|  (A3, A2 and C_in) | (A3, A2 and C_in) |
+---------------+---------------+
|  Bit 2        |  Bit 1        |
|  B3           |  B2           |
+---------------+---------------+
|  XOR        |       XOR      |
|  (B3, B2 and C_in) | (B3, B2 and C_in) |
+---------------+---------------+
|  Bit 1        |  Bit 0        |
|  C2           |  C1           |
+---------------+---------------+
|  XOR        |       XOR      |
|  (C2, C1 and C_in) | (C2, C1 and C_in) |
+---------------+---------------+
|  Sum Out    |
+---------------+
```

## **Truth Table**

Here is the truth table for the 4-bit full adder:

| A3  | A2  | A1  | A0  | B3  | B2  | B1  | B0  | C_in | C_out | Sum_out |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ------- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 0    | 0     | 1       |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 0    | 0     | 0       |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 0    | 0     | 1       |
| 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 1    | 1     | 0       |
| 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 0   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 0   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 1   | 1   | 0   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 1   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 0   | 1   | 0   | 1   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 0   | 1   | 0   | 1   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1    | 1     | 0       |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1    | 1     | 0       |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 1    | 1     | 0       |
| 1   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 1    | 1     | 1       |
| 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1    | 1     | 0       |
| 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1    | 1     | 1       |
| 1   | 1   | 1   | 1   | 0   | 1   | 0   | 0   | 1    | 1     | 0       |
| 1   |
