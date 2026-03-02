# 5 Design Verilog HDL to implement Decimal Adder

=====================================================

In this module, we will explore the design of decimal adders using Verilog HDL. A decimal adder is a digital circuit that performs addition of decimal numbers. In this module, we will discuss five different design approaches to implement a decimal adder using Verilog HDL.

## Historical Context

---

Decimal addition has been a fundamental operation in digital systems since the early days of computing. The first electronic computers used binary arithmetic, but decimal arithmetic was also used in some systems, particularly in financial and scientific applications. The development of decimal adders has been an ongoing process, with new design techniques and technologies emerging over the years.

## Modern Developments

---

In recent years, there has been a significant increase in the use of digital signal processing (DSP) and field-programmable gate arrays (FPGAs) in various applications, including decimal addition. Modern design tools and techniques, such as hardware description languages (HDLs) and simulation software, have made it easier to design and verify decimal adders.

## Design Approaches

---

In this section, we will discuss five different design approaches to implement a decimal adder using Verilog HDL:

### 1. Ripple-Carry Adder Design

A ripple-carry adder is a simple and efficient design for decimal addition. It uses a chain of full adders to perform the addition, with each full adder having a ripple-carry output.

#### Verilog Code

```verilog
module decimal_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum
);

    wire [1:0] carry;
    wire [1:0] sumbit;

    assign sumbit = a[0] ^ b[0] ^ carry;
    assign carry = a[1] & b[1] | a[0] & b[1] | a[1] & b[0];

    assign sum[0] = sumbit;
    assign sum[1] = a[2] ^ b[2] ^ carry;
    assign sum[2] = a[3] ^ b[3] ^ carry;
    assign sum[3] = carry;
endmodule
```

#### Diagram Description

The diagram below shows the block diagram of a ripple-carry adder:

```
          +---------------+
          |  Full Adder  |
          |  (A0, A1, A2, A3)|
          +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (B0, B1, B2, | |  (C0, C1, C2, |
|   B3)        | |   B3)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A2, A3,    | |  (B2, B3,    |
|   C0)        | |   C0)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A3, C1,    | |  (B3, C1,    |
|   C2)        | |   C2)        |
+---------------+ +---------------+
```

### 2. Carry-Save Adder Design

A carry-save adder is a more efficient design for decimal addition than a ripple-carry adder. It uses a chain of full adders to perform the addition, with each full adder having a carry-save output.

#### Verilog Code

```verilog
module decimal_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum
);

    wire [1:0] carry;
    wire [1:0] sumbit;

    assign sumbit = a[0] ^ b[0] ^ carry;
    assign carry = a[1] & b[1] | a[0] & b[1] | a[1] & b[0];

    assign sum[0] = sumbit;
    assign sum[1] = a[2] ^ b[2] ^ carry;
    assign sum[2] = a[3] ^ b[3] ^ carry;
    assign sum[3] = carry;

    wire [1:0] cs0, cs1;
    wire [1:0] sum0, sum1;

    assign cs0 = a[0] & b[0];
    assign cs1 = a[1] & b[1];

    assign sum0 = a[2] ^ b[2] ^ cs1;
    assign sum1 = a[3] ^ b[3] ^ cs0;
endmodule
```

#### Diagram Description

The diagram below shows the block diagram of a carry-save adder:

```
          +---------------+
          |  Full Adder  |
          |  (A0, A1, A2, A3)|
          +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (B0, B1, B2, | |  (C0, C1, C2, |
|   B3)        | |   B3)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A2, A3,    | |  (B2, B3,    |
|   C0)        | |   C0)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A3, C1,    | |  (B3, C1,    |
|   C2)        | |   C2)        |
+---------------+ +---------------+
```

### 3. Wallace Tree Design

A Wallace tree is a highly efficient design for decimal addition. It uses a tree-like structure of full adders to perform the addition.

#### Verilog Code

```verilog
module decimal_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum
);

    wire [1:0] carry;
    wire [1:0] sumbit;

    assign sumbit = a[0] ^ b[0] ^ carry;
    assign carry = a[1] & b[1] | a[0] & b[1] | a[1] & b[0];

    assign sum[0] = sumbit;
    assign sum[1] = a[2] ^ b[2] ^ carry;
    assign sum[2] = a[3] ^ b[3] ^ carry;
    assign sum[3] = carry;

    wire [1:0] wt[0], wt[1];
    wire [1:0] st[0], st[1];

    assign wt[0] = a[0] & b[0];
    assign st[0] = a[1] & b[1];

    assign wt[1] = a[0] & b[1];
    assign st[1] = a[1] & b[0];

    assign sum[2] = a[2] ^ b[2] ^ st[1];
    assign sum[3] = a[3] ^ b[3] ^ st[0];
endmodule
```

#### Diagram Description

The diagram below shows the block diagram of a Wallace tree:

```
          +---------------+
          |  Full Adder  |
          |  (A0, A1, A2, A3)|
          +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (B0, B1, B2, | |  (C0, C1, C2, |
|   B3)        | |   B3)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A2, A3,    | |  (B2, B3,    |
|   C0)        | |   C0)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A3, C1,    | |  (B3, C1,    |
|   C2)        | |   C2)        |
+---------------+ +---------------+
```

### 4. Kogge-Sarason Design

A Kogge-Sarason adder is a highly efficient design for decimal addition. It uses a tree-like structure of full adders to perform the addition.

#### Verilog Code

```verilog
module decimal_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum
);

    wire [1:0] carry;
    wire [1:0] sumbit;

    assign sumbit = a[0] ^ b[0] ^ carry;
    assign carry = a[1] & b[1] | a[0] & b[1] | a[1] & b[0];

    assign sum[0] = sumbit;
    assign sum[1] = a[2] ^ b[2] ^ carry;
    assign sum[2] = a[3] ^ b[3] ^ carry;
    assign sum[3] = carry;

    wire [1:0] ks1, ks2;
    wire [1:0] st1, st2;

    assign ks1 = a[0] & b[0];
    assign st1 = a[1] & b[1];

    assign ks2 = a[0] & b[1];
    assign st2 = a[1] & b[0];

    assign sum[2] = a[2] ^ b[2] ^ st2;
    assign sum[3] = a[3] ^ b[3] ^ st1;
endmodule
```

#### Diagram Description

The diagram below shows the block diagram of a Kogge-Sarason adder:

```
          +---------------+
          |  Full Adder  |
          |  (A0, A1, A2, A3)|
          +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (B0, B1, B2, | |  (C0, C1, C2, |
|   B3)        | |   B3)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A2, A3,    | |  (B2, B3,    |
|   C0)        | |   C0)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A3, C1,    | |  (B3, C1,    |
|   C2)        | |   C2)        |
+---------------+ +---------------+
```

### 5. Booth's Modulo Rounding Design

Booth's modulo rounding is a method for rounding numbers to the nearest multiple of a given divisor. This design uses a tree-like structure of full adders to perform the addition.

#### Verilog Code

```verilog
module decimal_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum
);

    wire [1:0] carry;
    wire [1:0] sumbit;

    assign sumbit = a[0] ^ b[0] ^ carry;
    assign carry = a[1] & b[1] | a[0] & b[1] | a[1] & b[0];

    assign sum[0] = sumbit;
    assign sum[1] = a[2] ^ b[2] ^ carry;
    assign sum[2] = a[3] ^ b[3] ^ carry;
    assign sum[3] = carry;

    wire [1:0] br0, br1;
    wire [1:0] st0, st1;

    assign br0 = a[0] & b[0];
    assign st0 = a[1] & b[1];

    assign br1 = a[0] & b[1];
    assign st1 = a[1] & b[0];

    assign sum[2] = a[2] ^ b[2] ^ st1;
    assign sum[3] = a[3] ^ b[3] ^ st0;
endmodule
```

#### Diagram Description

The diagram below shows the block diagram of Booth's modulo rounding adder:

```
          +---------------+
          |  Full Adder  |
          |  (A0, A1, A2, A3)|
          +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (B0, B1, B2, | |  (C0, C1, C2, |
|   B3)        | |   B3)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A2, A3,    | |  (B2, B3,    |
|   C0)        | |   C0)        |
+---------------+ +---------------+
                  |       |
                  |  Carry  |
                  |       |
                  v       v
+---------------+ +---------------+
|  Full Adder  | |  Full Adder  |
|  (A3, C1,    | |  (B3, C1,    |
|   C2)        | |   C2)        |
+---------------+ +---------------+
```

## Applications

---

Decimal adders have numerous applications in various fields, including:

- Financial systems: Decimal addition is used in financial systems to perform addition of decimal numbers.
- Scientific applications: Decimal addition is used in scientific applications, such as scientific simulations and data analysis.
- Cryptography: Decimal addition is used in cryptographic algorithms, such as the RSA algorithm.
- Digital signal processing: Decimal addition is used in digital signal processing applications, such as filtering and convolution.

## Further Reading

---

- "Digital Design and Computer Organization" by Mano and Kameshwar
- "Verilog HDL for Digital Design" by Raghuram and Bhaskararao
- "Digital Arithmetic Circuits" by A. K. Saxena
- "Verilog Tutorial" by Edytron
- "Digital Signal Processing" by William A. Gardner

## Conclusion

---

In this module, we have explored the design of decimal adders using Verilog HDL. We have discussed five different design approaches, including ripple-carry, carry-save, Wallace tree, Kogge-Sarason, and Booth's modulo rounding. We have also discussed the applications of decimal adders and provided further reading suggestions.
