# **Decimal Adder Implementation using Verilog HDL**

## **Introduction**

A decimal adder is a digital circuit that performs the basic arithmetic operation of addition of two decimal numbers. In this module, we will explore five different design approaches to implement a decimal adder using Verilog HDL (Hardware Description Language). Verilog is a popular hardware description language used to design and implement digital circuits.

## **Historical Context**

The concept of decimal addition dates back to the early days of computing. In the 1950s and 1960s, digital computers used binary arithmetic, which is based on the binary number system. However, as computers became more advanced, the need for decimal arithmetic arose. In the 1970s and 1980s, digital designers developed decimal adders using various techniques, including bitwise addition, carry-lookahead addition, and binary-carry decimal addition.

## **Modern Developments**

In recent years, there has been a significant increase in the use of digital design automation tools, such as Verilog and VHDL (VHSIC Hardware Description Language). These tools have made it easier to design and implement digital circuits, including decimal adders. Additionally, the development of field-programmable gate arrays (FPGAs) and application-specific integrated circuits (ASICs) has enabled the creation of complex digital systems, including decimal adders.

## **Design Approaches**

In this section, we will explore five different design approaches to implement a decimal adder using Verilog HDL:

### 1. Bitwise Addition

Bitwise addition is a straightforward approach to implementing a decimal adder. This approach involves performing bitwise addition on the decimal digits, starting from the least significant digit (LSD) to the most significant digit (MSD). The result of the addition is then propagated through the circuit.

**Verilog Code**

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = a + b;
assign carry = temp[9];

result <= temp;

endmodule
```

### 2. Carry-Lookahead Addition

Carry-lookahead addition is a more efficient approach to implementing a decimal adder. This approach involves computing the carry values for each bit position, rather than propagating a single carry value through the circuit. The result of the addition is then computed using the carry values.

**Verilog Code**

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry[9:0];
reg  [9:0]  temp;

assign temp = a + b;
assign carry[0] = temp[0];
assign carry[1] = temp[1];
assign carry[2] = temp[2];
assign carry[3] = temp[3];
assign carry[4] = temp[4];
assign carry[5] = temp[5];
assign carry[6] = temp[6];
assign carry[7] = temp[7];
assign carry[8] = temp[8];

result <= temp;

endmodule
```

### 3. Binary-Carry Decimal Addition

Binary-carry decimal addition is a technique used to implement decimal addition using binary arithmetic. This approach involves converting the decimal digits to binary and performing binary addition. The result of the addition is then converted back to decimal.

**Verilog Code**

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = bin_to_dec(a[0:7]) + bin_to_dec(b[0:7]);
assign carry = temp[8];

result <= dec_to_bin(temp);

endmodule

// Helper modules

module bin_to_dec(
  input  [7:0]  bin,
  output [9:0]  dec
);

reg  [9:0]  temp;

assign temp = bin * 2 + dec_to_bin(bin[1:0]);

dec <= temp;

endmodule

module dec_to_bin(
  input  [9:0]  dec,
  output [7:0]  bin
);

reg  [7:0]  temp;

assign temp = dec / 2;

bin <= temp;

endmodule
```

### 4. Gray Code Decimal Addition

Gray code decimal addition is a technique used to implement decimal addition using Gray code arithmetic. This approach involves converting the decimal digits to Gray code and performing Gray code addition. The result of the addition is then converted back to decimal.

**Verilog Code**

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = gray_to_dec(a[0:7]) + gray_to_dec(b[0:7]);
assign carry = temp[8];

result <= dec_to_gray(temp);

endmodule

// Helper modules

module gray_to_dec(
  input  [7:0]  gray,
  output [9:0]  dec
);

reg  [9:0]  temp;

assign temp = gray << 1;

dec <= temp;

endmodule

module dec_to_gray(
  input  [9:0]  dec,
  output [7:0]  gray
);

reg  [7:0]  temp;

assign temp = dec >> 1;

gray <= temp;

endmodule
```

### 5. Binary-Carry-Addition with Carry Propagation

Binary-carry-addition with carry propagation is a technique used to implement decimal addition using binary arithmetic. This approach involves performing binary addition and propagating the carry values through the circuit. The result of the addition is then converted back to decimal.

**Verilog Code**

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = a + b;
assign carry = temp[9];

result <= temp;

endmodule
```

## **Case Studies**

1. **Simple Decimal Adder**: Implement a simple decimal adder using bitwise addition.

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = a + b;
assign carry = temp[9];

result <= temp;

endmodule
```

2. **Decimal Adder with Carry Propagation**: Implement a decimal adder using binary-carry-addition with carry propagation.

```verilog
module decimal_adder(
  input  [9:0]  a,
  input  [9:0]  b,
  output [9:0]  result
);

reg  [9:0]  carry;
reg  [9:0]  temp;

assign temp = a + b;
assign carry = temp[9];

result <= temp;

endmodule
```

## **Applications**

1. **Digital Calculators**: Decimal adders are widely used in digital calculators to perform arithmetic operations.
2. **Digital Financial Systems**: Decimal adders are used in digital financial systems to perform transactions and calculations.
3. **Digital Communication Systems**: Decimal adders are used in digital communication systems to perform data transmission and reception.

## **Further Reading**

1. **"Digital Design and Computer Organization" by Manfred Glesner**: This book provides a comprehensive introduction to digital design and computer organization.
2. **"Verilog HDL: A Guide to Designing Digital Systems" by David A. Patterson and John L. Hennessy**: This book provides a detailed introduction to Verilog HDL and its applications.
3. **"Digital Arithmetic" by Thomas L. Farris and Peter E. Black**: This book provides a comprehensive introduction to digital arithmetic and its applications.
