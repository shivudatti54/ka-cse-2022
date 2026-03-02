# **Decimal Adder Design in Verilog HDL**

## **Introduction**

In digital electronics, a decimal adder is a digital circuit that performs binary addition on two decimal numbers. In this study material, we will design a decimal adder using Verilog HDL (Hardware Description Language). Verilog is a popular language used to design digital circuits.

## **Decimal Addition**

Decimal addition is a binary operation that performs addition on two decimal numbers. The result is also a decimal number. The process of decimal addition can be broken down into the following steps:

- Convert the decimal numbers to binary
- Perform binary addition
- Convert the result back to decimal

## **Verilog Design**

In this design, we will use the following 4-bit binary decimal adder as the building block. The adder takes two 4-bit binary numbers as input and produces a 5-bit binary result.

## **Binary Decimal Adder**

The binary decimal adder can be designed using the following equation:

```
A  B  C  D  Sum
-------------------
0  0  0  0  0
0  0  0  1  1
0  0  1  0  1
0  0  1  1  0
0  1  0  0  1
0  1  0  1  0
0  1  1  0  0
0  1  1  1  0
1  0  0  0  1
1  0  0  1  0
1  0  1  0  0
1  0  1  1  0
1  1  0  0  1
1  1  0  1  0
1  1  1  0  0
1  1  1  1  0
```

## **Verilog Code**

Here is the Verilog code for the 4-bit binary decimal adder:

```verilog
module decimal_adder(
    input [3:0] A,
    input [3:0] B,
    output [3:0] Sum
);

    assign Sum = A + B;

endmodule
```

## **5-Bit Decimal Adder**

To design a 5-bit decimal adder, we can use the 4-bit binary decimal adder as the building block. We will create a 5-bit binary decimal adder using 4-bit binary decimal adders in parallel.

## **Verilog Code**

Here is the Verilog code for the 5-bit decimal adder:

```verilog
module decimal_adder_5bit(
    input [6:0] A,
    input [6:0] B,
    output [7:0] Sum
);

    reg [3:0] A_4bit;
    reg [3:0] B_4bit;
    reg [3:0] Sum_4bit;

    assign A_4bit = A[3:0];
    assign B_4bit = B[3:0];

    decimal_adder U1(
        .A(A_4bit),
        .B(B_4bit),
        .Sum(Sum_4bit)
    );

    assign Sum = A + B;

endmodule
```

## **Example Use Cases**

Here are some example use cases for the 5-bit decimal adder:

- Adding two decimal numbers, 12 and 25, using the 5-bit decimal adder.
- Adding two decimal numbers, 45 and 67, using the 5-bit decimal adder.

## **Conclusion**

In this study material, we designed a 5-bit decimal adder using Verilog HDL. The decimal adder takes two 5-bit decimal numbers as input and produces a 6-bit decimal result. The design uses a 4-bit binary decimal adder as the building block. The example use cases demonstrate the application of the 5-bit decimal adder in real-world scenarios.
