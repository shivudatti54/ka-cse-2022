# **Digital Design and Computer Organization**

## **Module 8: 8 Hours**

## **Topic: Design Verilog HDL to implement Binary Adder-Subtractor – Half and Full Adder**

## **Introduction**

Binary adders and subtractors are fundamental building blocks in digital design. They are used to perform arithmetic operations on binary numbers. In this topic, we will learn how to design and implement binary adders and subtractors using Verilog HDL.

## **Half Adder**

A half adder is a digital circuit that adds two binary digits (bits) and produces a sum and a carry output.

**Definition:** A half adder consists of two XOR gates and one AND gate.

**Truth Table:**

| A   | B   | Sum | Carry |
| --- | --- | --- | ----- |
| 0   | 0   | 0   | 0     |
| 0   | 1   | 1   | 0     |
| 1   | 0   | 1   | 0     |
| 1   | 1   | 0   | 1     |

**Verilog Implementation:**

```verilog
module half_adder(A, B, sum, carry);
    input A, B;
    output sum, carry;

    assign sum = A ^ B;
    assign carry = A & B;

endmodule
```

## **Full Adder**

A full adder is a digital circuit that adds three binary digits (bits) and produces a sum and a carry output.

**Definition:** A full adder consists of two half adders and an OR gate.

**Truth Table:**

| A   | B   | C   | Sum | Carry |
| --- | --- | --- | --- | ----- |
| 0   | 0   | 0   | 0   | 0     |
| 0   | 0   | 1   | 1   | 0     |
| 0   | 1   | 0   | 1   | 0     |
| 0   | 1   | 1   | 0   | 1     |
| 1   | 0   | 0   | 1   | 0     |
| 1   | 0   | 1   | 0   | 1     |
| 1   | 1   | 0   | 0   | 1     |
| 1   | 1   | 1   | 1   | 1     |

**Verilog Implementation:**

```verilog
module full_adder(A, B, C, sum, carry);
    input A, B, C;
    output sum, carry;

    half_adder HA(A, B, HA.sum, HA.carry);
    half_adder HA1(A, C, HA1.sum, HA1.carry);

    assign sum = HA.sum ^ HA1.sum;
    assign carry = HA.carry | HA1.carry;

endmodule
```

## **Binary Adder**

A binary adder is a digital circuit that adds two binary numbers of equal length.

**Definition:** A binary adder consists of multiple full adders.

**Example:**

Suppose we want to add the binary numbers 101 and 110.

|     | 0   | 1   | 0   |
| --- | --- | --- | --- |
| 101 | 1   | 0   | 1   |
| 110 | 1   | 1   | 0   |

We can use two full adders to add the two binary numbers.

| Full Adder 1 | Full Adder 2 |
| ------------ | ------------ |
| 101          | 110          |
|              |              |
| 0            | 0            |
|              |              |
| 1            | 1            |

The sum of the two binary numbers is 011, and the carry is 1.

**Verilog Implementation:**

```verilog
module binary_adder(A, B, sum, carry);
    input [2:0] A, B;
    output [2:0] sum, carry;

    full_adder FA(A[2], B[2], A[1], sum[2], carry[2]);
    full_adder FA1(A[1], B[1], sum[1], carry[1]);
    full_adder FA2(A[0], B[0], sum[0], carry[0]);

    assign sum = {sum[2], sum[1], sum[0]};
    assign carry = {carry[2], carry[1], carry[0]};

endmodule
```

## **Binary Subtractor**

A binary subtractor is a digital circuit that subtracts one binary number from another.

**Definition:** A binary subtractor consists of a binary adder and a complement generator.

**Verilog Implementation:**

```verilog
module binary_subtractor(A, B, sum, carry);
    input [2:0] A, B;
    output [2:0] sum, carry;

    binary_adder AB(A, B, sum, carry);
    assign sum = ~B;
    assign carry = carry;

endmodule
```

In this study material, we have learned the basics of binary adders and subtractors, including half adders, full adders, binary adders, and binary subtractors. We have also seen how to implement these circuits using Verilog HDL. The next topic will cover more advanced digital design concepts.
