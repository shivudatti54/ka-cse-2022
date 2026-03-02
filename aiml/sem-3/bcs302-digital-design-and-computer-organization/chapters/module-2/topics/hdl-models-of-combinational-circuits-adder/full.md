# **HDL Models of Combinational Circuits – Adder**

## **Introduction**

In digital design and computer organization, combinational logic circuits are fundamental building blocks for designing complex digital systems. The adder, a basic combinational circuit, performs arithmetic addition and is a crucial component in various digital systems. In this topic, we will delve into the world of HDL models of combinational circuits, focusing on the adder and its applications.

## **Historical Context**

The concept of combinational logic circuits dates back to the 1930s, when Claude Shannon introduced the idea of combinational logic in his seminal paper "A Logical Calculation of the Number of Mutually Exclusive Signal Patterns in a Binary System." The first digital computers, such as ENIAC (1946) and UNIVAC (1951), relied on combinational logic circuits to perform arithmetic operations.

The development of integrated circuits (ICs) in the 1950s and 1960s enabled the mass production of combinational logic circuits. This led to the creation of more complex digital systems, including calculators, computers, and communication equipment.

## **Adder Circuit**

An adder is a combinational logic circuit that performs arithmetic addition of two or more binary numbers. The adder circuit takes two or more inputs, each representing a binary digit (bit), and produces an output that represents the sum of the input bits.

## **Types of Adders**

There are several types of adders, including:

- **Half Adder**: adds two bits and produces a sum and a carry bit.
- **Full Adder**: adds three bits (two input bits and a carry bit) and produces a sum, carry out, and carry bit.
- **Carry-In Adder**: adds multiple bits with a carry-in input and produces a sum and a carry-out bit.

## **HDL Models of Adders**

HDL (Hardware Description Language) models of adders are used to describe the behavior of the adder circuit using a high-level programming language. HDL models are used to design, simulate, and test digital circuits before they are implemented in hardware.

## **Verilog Model of Adder**

Here is a simple Verilog model of a full adder:

```verilog
module full_adder(A, B, C_in, S, C_out);
    input A, B, C_in;
    output S, C_out;

    assign S = (A ^ B) ^ C_in;
    assign C_out = (A & B) | ((A ^ B) & C_in);

endmodule
```

This Verilog model defines a full adder circuit with inputs A, B, and C_in, and outputs S and C_out.

## **VHDL Model of Adder**

Here is a simple VHDL model of a full adder:

```vhdl
entity full_adder is
    Port ( A : in  STD_LOGIC;
           B : in  STD_LOGIC;
           C_in : in  STD_LOGIC;
           S : out  STD_LOGIC;
           C_out : out  STD_LOGIC);
end full_adder;

architecture Behavioral of full_adder is
begin
    S <= (A xor B) xor C_in;
    C_out <= (A and B) or ((A xor B) and C_in);
end Behavioral;
```

This VHDL model defines a full adder circuit with inputs A, B, and C_in, and outputs S and C_out.

## **Case Study: Designing an 8-Bit Adder**

In this case study, we will design an 8-bit adder using HDL models. The adder will take two 4-bit input numbers and produce an 8-bit output sum.

**Verilog Model of 8-Bit Adder**

```verilog
module eight_bit_adder(A, B, S, C_out);
    input [3:0] A, B;
    output [7:0] S;
    output [1:0] C_out;

    reg [3:0] sum;
    reg [1:0] carry;

    always @ (*)
        sum = A[3] + B[3] + carry;
        carry = A[2] + B[2] + carry;
        S[3] = sum & ~carry;
        S[2] = (sum >> 1) & carry;
        S[1] = (sum >> 2) & carry;
        S[0] = (sum >> 3) & carry;
        C_out <= carry;

endmodule
```

This Verilog model defines an 8-bit adder circuit with inputs A and B, and outputs S and C_out.

**VHDL Model of 8-Bit Adder**

```vhdl
entity eight_bit_adder is
    Port ( A : in  STD_LOGIC_VECTOR (3 downto 0);
           B : in  STD_LOGIC_VECTOR (3 downto 0);
           S : out  STD_LOGIC_VECTOR (7 downto 0);
           C_out : out  STD_LOGIC_VECTOR (1 downto 0));
end eight_bit_adder;

architecture Behavioral of eight_bit_adder is
    signal sum : STD_LOGIC_VECTOR (3 downto 0);
    signal carry : STD_LOGIC_VECTOR (1 downto 0);

begin
    process(A, B)
        variable carry_var : STD_LOGIC_VECTOR (1 downto 0);
    begin
        sum <= A[3] + B[3] + carry_var;
        carry_var <= A[2] + B[2] + carry_var;
        S(3) <= sum & not carry_var;
        S(2) <= (sum shift 1) & carry_var;
        S(1) <= (sum shift 2) & carry_var;
        S(0) <= (sum shift 3) & carry_var;
        C_out <= carry_var;
    end process;
end Behavioral;
```

This VHDL model defines an 8-bit adder circuit with inputs A and B, and outputs S and C_out.

## **Applications of Adders**

Adders have numerous applications in digital systems, including:

- **Computers**: Adders are used to perform arithmetic operations in computers, such as addition, subtraction, and multiplication.
- **Communication Equipment**: Adders are used in communication equipment, such as modems and switches, to perform arithmetic operations.
- **Calculators**: Adders are used in calculators to perform arithmetic operations, such as addition and subtraction.

## **Conclusion**

In conclusion, combinational logic circuits, such as adders, are fundamental building blocks for designing complex digital systems. HDL models of adders are used to describe the behavior of the adder circuit using a high-level programming language. The Verilog and VHDL models presented in this topic demonstrate the design and implementation of an adder circuit using HDL models.

## **Further Reading**

- **"Digital Logic: Design and Implementation"** by James M. Stitt
- **"Hardware Description Languages: Principles and Practice"** by Ian S. Dhillon
- **"Digital Computing and Its Applications"** by C.L. Liu and T.N. Triebel
- **"The Art of Electronics"** by Paul Horowitz and Winfield Hill
