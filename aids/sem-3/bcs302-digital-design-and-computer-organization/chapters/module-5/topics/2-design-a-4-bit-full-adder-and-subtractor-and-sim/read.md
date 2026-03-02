# **2 Design a 4-bit Full Adder and Subtractor and Simulate the Same using Basic Gates**

## **Introduction**

In this topic, we will design and simulate a 4-bit full adder and subtractor using basic gates. A full adder is a digital circuit that performs the operation of adding two bits and a carry bit, while a subtractor is a digital circuit that performs the operation of subtracting one bit from another.

## **Basic Gates**

Before designing the full adder and subtractor, we need to understand the basic gates that can be used to build them. The basic gates are:

- **AND Gate**: Produces an output of 1 only if all inputs are 1.
- **OR Gate**: Produces an output of 1 if any input is 1.
- **NOT Gate**: Produces an output that is the opposite of the input.
- **NAND Gate**: Produces an output of 0 only if all inputs are 1.
- **NOR Gate**: Produces an output of 1 only if all inputs are 0.

## **4-bit Full Adder**

A 4-bit full adder is a digital circuit that performs the operation of adding two 4-bit numbers and a carry bit. The inputs to the full adder are:

- **A0, A1, A2, A3**: The two 4-bit numbers being added.
- **C**: The carry bit.

The output of the full adder is:

- **S0, S1, S2, S3**: The sum bits.

## **Truth Table**

| A0  | A1  | A2  | A3  | C   | S0  | S1  | S2  | S3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   |
| 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 0   |
| 0   | 0   | 1   | 0   | 0   | 1   | 1   | 0   | 0   |
| 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 1   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   |
| 0   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | 1   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 1   | 1   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 1   |
| 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   |
| 1   | 0   | 0   | 1   | 0   | 0   | 1   | 1   | 1   |
| 1   | 0   | 1   | 0   | 0   | 1   | 0   | 1   | 1   |
| 1   | 0   | 1   | 1   | 0   | 0   | 1   | 0   | 0   |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   |
| 1   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 0   |
| 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   |

## **Design**

The 4-bit full adder can be designed using the following logic equations:

- **S0**: A0 + A1 + C
- **S1**: A1 + A2 + C
- **S2**: A2 + A3 + C
- **S3**: A3 + C

The corresponding logic circuit is:

```markdown
+---------------+
| A0 A1 A2 |
+---------------+
|
|
v
+---------------+
| C S0 S1 |
+---------------+
|
|
v
+---------------+
| S2 S3 |
+---------------+
```

## **4-bit Subtractor**

A 4-bit subtractor is a digital circuit that performs the operation of subtracting one 4-bit number from another. The inputs to the subtractor are:

- **B0, B1, B2, B3**: The 4-bit number being subtracted.
- **A0, A1, A2, A3**: The 4-bit number from which to subtract.

The output of the subtractor is:

- **S0, S1, S2, S3**: The difference bits.

## **Truth Table**

| B0  | B1  | B2  | B3  | A0  | A1  | A2  | A3  | S0  | S1  | S2  | S3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   |
| 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 0   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 0   |
| 0   | 1   | 0   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | 1   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 1   | 1   | 0   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   |
| 1   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 1   | 1   |
| 1   | 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   |
| 1   | 0   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0   |
| 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 0   |
| 1   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 1   | 0   | 1   | 1   |
| 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 0   |
| 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |

## **Design**

The 4-bit subtractor can be designed using the following logic equations:

- **S0**: B0 + ~A0
- **S1**: B1 + ~A1
- **S2**: B2 + ~A2
- **S3**: B3 + ~A3

The corresponding logic circuit is:

```markdown
+---------------+
| B0 B1 B2 |
+---------------+
|
|
v
+---------------+
| A0 A1 A2 |
+---------------+
|
|
v
+---------------+
| ~A0 ~A1 |
+---------------+
|
|
v
+---------------+
| S0 S1 S2 |
+---------------+
|
|
v
+---------------+
| S3 |
+---------------+
```

## **Simulation**

The 4-bit full adder and subtractor can be simulated using a digital circuit simulator such as Verilog or VHDL.

```markdown
// Full Adder
module full_adder(A0, A1, A2, A3, C, S0, S1, S2, S3) {
input [3:0] A0, A1, A2, A3;
input C;
output [3:0] S0, S1, S2, S3;

S0 = A0 + A1 + C;
S1 = A1 + A2 + C;
S2 = A2 + A3 + C;
S3 = A3 + C;

assign S0 = S0;
assign S1 = S1;
assign S2 = S2;
assign S3 = S3;
}

// Subtractor
module subtractor(B0, B1, B2, B3, A0, A1, A2, A3, S0, S1, S2, S3) {
input [3:0] B0, B1, B2, B3;
input [3:0] A0, A1, A2, A3;
output [3:0] S0, S1, S2, S3;

S0 = B0 + ~A0;
S1 = B1 + ~A1;
S2 = B2 + ~A2;
S3 = B3 + ~A3;

assign S0 = S0;
assign S1 = S1;
assign S2 = S2;
assign S3 = S3;
}
```

This study material provides a comprehensive overview of designing and simulating 4-bit full adders and subtractors using basic gates. The truth tables, logic equations, and logic circuits are provided to illustrate the design process. The simulation using Verilog or VHDL is also discussed to verify the correctness of the designs.
