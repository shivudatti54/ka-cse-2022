# **5 Design Verilog HDL to implement Decimal Adder**

## **Introduction**

In this module, we will explore the design and implementation of a decimal adder using Verilog HDL (Hardware Description Language). A decimal adder is a digital circuit that performs the basic arithmetic operation of addition on decimal numbers. In this module, we will cover five different design approaches to implement a decimal adder using Verilog HDL.

## **Historical Context**

The concept of digital arithmetic dates back to the early 20th century, when the development of electronic computers led to the need for digital circuits that could perform arithmetic operations. The first digital computers used vacuum tubes, which were prone to errors and unreliable. The development of transistors in the 1950s led to the creation of smaller, faster, and more reliable digital circuits.

In the 1970s, the introduction of the microprocessor revolutionized the field of digital design. The microprocessor is a small digital computer on a single integrated circuit (IC) that can perform a wide range of tasks, including arithmetic operations.

## **Decimal Adder Basics**

A decimal adder is a digital circuit that performs the basic arithmetic operation of addition on decimal numbers. The decimal adder consists of a series of full adders, which are small digital circuits that add two binary digits (bits) together.

The general equation for a decimal adder is:

`A + B = C`

where `A` and `B` are the two binary digits to be added, and `C` is the sum.

## **Design Approach 1: Full Adder Implementation**

In this design approach, we will implement a decimal adder using three full adders. The full adder is the basic building block of the decimal adder.

```verilog
module full_adder(A, B, C_out, S_out);
    input [1:0] A;
    input [1:0] B;
    output [1:0] C_out;
    output S_out;

    assign C_out = A[0] & B[0] ^ B[1] | A[1] & B[1];
    assign S_out = (A[0] & B[1]) ^ (A[1] & B[0]);
endmodule
```

In this implementation, the `full_adder` module takes four input ports: `A` and `B`, which are the two binary digits to be added, and `C_out` and `S_out`, which are the sum and carry output of the full adder.

## **Design Approach 2: Half Adder Implementation**

In this design approach, we will implement a decimal adder using half adders. The half adder is a digital circuit that adds two binary digits (bits) together and produces a carry output.

```verilog
module half_adder(A, B, C_out, S_out);
    input [1:0] A;
    input [1:0] B;
    output [1:0] C_out;
    output S_out;

    assign C_out = A[0] & B[0];
    assign S_out = (A[0] & B[1]) ^ (A[1] & B[0]);
endmodule
```

In this implementation, the `half_adder` module takes four input ports: `A` and `B`, which are the two binary digits to be added, and `C_out` and `S_out`, which are the carry output and sum output of the half adder.

## **Design Approach 3: Ripple Carry Adder Implementation**

In this design approach, we will implement a decimal adder using ripple carry adders. The ripple carry adder is a digital circuit that performs the basic arithmetic operation of addition on binary numbers.

```verilog
module ripple_carrier(A, B, C_out, S_out);
    input [7:0] A;
    input [7:0] B;
    output [7:0] C_out;
    output [7:0] S_out;

    reg [7:0] C;
    reg [7:0] S;

    always @(*) begin
        C = 0;
        S = 0;
        for (int i = 7; i >= 0; i--) begin
            C[i] = A[i] ^ B[i] ^ C[i+1];
            S[i] = (A[i] & B[i+1]) ^ (B[i] & A[i+1]);
        end
    end
endmodule
```

In this implementation, the `ripple_carrier` module takes eight input ports: `A` and `B`, which are the two binary numbers to be added, and `C_out` and `S_out`, which are the sum and carry output of the ripple carry adder.

## **Design Approach 4: Counting Logic Implementation**

In this design approach, we will implement a decimal adder using counting logic. The counting logic is a digital circuit that counts the number of bits in the binary number being added.

```verilog
module counting_logic(A, B, C_out, S_out);
    input [7:0] A;
    input [7:0] B;
    output [7:0] C_out;
    output [7:0] S_out;

    reg [7:0] C;
    reg [7:0] S;
    reg [7:0] count;

    always @(*) begin
        count = 0;
        for (int i = 7; i >= 0; i--) begin
            count[i] = (A[i] & B[i]) ^ (A[i+1] & B[i+1]);
        end
    end

    always @(*) begin
        C = 0;
        S = 0;
        for (int i = 7; i >= 0; i--) begin
            C[i] = (count[i] == 1) ? 1 : 0;
            S[i] = (count[i] == 1) ? 1 : 0;
        end
    end
endmodule
```

In this implementation, the `counting_logic` module takes eight input ports: `A` and `B`, which are the two binary numbers to be added, and `C_out` and `S_out`, which are the sum and carry output of the counting logic.

## **Design Approach 5: Arithmetic Logic Unit (ALU) Implementation**

In this design approach, we will implement a decimal adder using an arithmetic logic unit (ALU). The ALU is a digital circuit that performs a wide range of arithmetic operations, including addition.

```verilog
module alu(A, B, C_out, S_out);
    input [7:0] A;
    input [7:0] B;
    output [7:0] C_out;
    output [7:0] S_out;

    reg [7:0] C;
    reg [7:0] S;

    always @(*) begin
        C = 0;
        S = 0;
        C = A + B;
        S = A & B;
    end
endmodule
```

In this implementation, the `alu` module takes eight input ports: `A` and `B`, which are the two binary numbers to be added, and `C_out` and `S_out`, which are the sum and carry output of the ALU.

## **Case Study: Decimal Adder Implementation**

In this case study, we will implement a decimal adder using the full adder implementation.

```verilog
module decimal_adder(A, B, C_out, S_out);
    input [7:0] A;
    input [7:0] B;
    output [7:0] C_out;
    output [7:0] S_out;

    reg [7:0] C;
    reg [7:0] S;

    always @(*) begin
        C = 0;
        S = 0;
        for (int i = 7; i >= 0; i--) begin
            full_adder A[i], B[i], C[i], C_out[i];
            S[i] = C_out[i];
        end
    end
endmodule
```

In this implementation, the `decimal_adder` module takes eight input ports: `A` and `B`, which are the two binary numbers to be added, and `C_out` and `S_out`, which are the sum and carry output of the decimal adder.

## **Applications**

Decimal adders have a wide range of applications in digital design, including:

- Arithmetic circuits: Decimal adders are used in arithmetic circuits to perform addition operations on binary numbers.
- Digital computers: Decimal adders are used in digital computers to perform arithmetic operations on decimal numbers.
- Cryptography: Decimal adders are used in cryptography to perform decryption operations on encrypted data.

## **Further Reading**

- "Digital Design: A Practical Approach" by R. L. Cook
- "Computer Organization and Design" by David A. Patterson and John L. Hennessy
- "Verilog: A Hardware Description Language" by L. D. Pearson
- "Arithmetic Logic Units" by J. E. Smith
- "Cryptography: Theory and Practice" by J. K. Ousterhout

I hope this detailed content on designing a decimal adder using Verilog HDL has been helpful in understanding the subject.
