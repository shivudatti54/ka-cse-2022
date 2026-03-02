# **Design Verilog HDL for Binary Adder-Subtractor**

## **Introduction**

Binary adders and subtractors are fundamental digital circuit components used in computer arithmetic. In this study material, we will design and implement half and full adders using Verilog HDL.

## **Binary Adder/Subtractor Basics**

### Definition

A binary adder/subtractor is a digital circuit that performs binary addition or subtraction of two binary numbers.

### Types

- **Half Adder:** A half adder is a digital circuit that adds two binary digits (bits) and produces a sum and carry output.
- **Full Adder:** A full adder is a digital circuit that adds three binary digits (bits) and produces a sum and carry output.

### Truth Tables

| A   | B   | Sum | Carry |
| --- | --- | --- | ----- |
| 0   | 0   | 0   | 0     |
| 0   | 1   | 1   | 0     |
| 1   | 0   | 1   | 0     |
| 1   | 1   | 0   | 1     |

## **Half Adder Design**

### Half Adder Circuit

A half adder consists of two XOR gates and one AND gate.

| A   | B   | Sum | Carry |
| --- | --- | --- | ----- |
| 0   | 0   | 0   | 0     |
| 0   | 1   | 1   | 0     |
| 1   | 0   | 1   | 0     |
| 1   | 1   | 0   | 1     |

### Verilog Code for Half Adder

```verilog
module half_adder(A, B, sum, carry);
    input A, B;
    output sum, carry;

    sum = A XOR B;
    carry = A AND B;

endmodule
```

## **Full Adder Design**

### Full Adder Circuit

A full adder consists of three XOR gates and one AND gate.

| A   | B   | C   | Sum | Carry |
| --- | --- | --- | --- | ----- |
| 0   | 0   | 0   | 0   | 0     |
| 0   | 0   | 1   | 1   | 0     |
| 0   | 1   | 0   | 1   | 0     |
| 0   | 1   | 1   | 0   | 1     |
| 1   | 0   | 0   | 1   | 0     |
| 1   | 0   | 1   | 0   | 1     |
| 1   | 1   | 0   | 0   | 1     |
| 1   | 1   | 1   | 1   | 0     |

### Verilog Code for Full Adder

```verilog
module full_adder(A, B, C, sum, carry);
    input A, B, C;
    output sum, carry;

    sum = ((A XOR B) XOR C);
    carry = ((A AND B) OR (B AND C) OR (A AND C));

endmodule
```

## **Example Use Cases**

- Binary adder/subtractor circuits are used in digital calculators, computers, and other electronic devices.
- Binary adder/subtractor circuits are also used in cryptographic algorithms, such as encryption and decryption.

## **Conclusion**

In this study material, we have designed and implemented half and full adders using Verilog HDL. We have also explained the truth tables, circuit diagrams, and Verilog code for both half and full adders. This knowledge is essential for understanding digital design and computer organization.
