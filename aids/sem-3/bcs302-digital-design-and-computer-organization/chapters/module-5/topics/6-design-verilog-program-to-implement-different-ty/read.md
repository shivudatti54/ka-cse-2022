# **6 Design Verilog Programs to Implement Different Types of Multiplexers**

## **Introduction**

In digital design, a multiplexer (MUX) is an electronic circuit that takes one or more input signals and selects one output signal to be sent to an output. In this study material, we will learn about different types of multiplexers and design Verilog programs to implement them.

## **Types of Multiplexers**

### 1. 2:1 Multiplexer

A 2:1 multiplexer is the most basic type of multiplexer. It takes two input signals and selects one output signal.

**Definition:** A 2:1 multiplexer is a circuit that selects one of two input signals and sends it to the output.

**Truth Table:**

| A   | B   | Select | Output |
| --- | --- | ------ | ------ |
| 0   | 0   | 0      | B0     |
| 0   | 0   | 1      | B1     |
| 0   | 1   | 0      | A0     |
| 0   | 1   | 1      | A1     |
| 1   | 0   | 0      | A0     |
| 1   | 0   | 1      | A1     |
| 1   | 1   | 0      | B0     |
| 1   | 1   | 1      | B1     |

**Verilog Program:**

```verilog
module mux2_1(A, B, Select, Output);
    input A, B, Select;
    output Output;
    assign Output = (Select == 1) ? B : A;
endmodule
```

### 2. 4:1 Multiplexer

A 4:1 multiplexer takes four input signals and selects one output signal.

**Definition:** A 4:1 multiplexer is a circuit that selects one of four input signals and sends it to the output.

**Truth Table:**

| A   | B   | C   | D   | Select | Output |
| --- | --- | --- | --- | ------ | ------ |
| 0   | 0   | 0   | 0   | 0      | D0     |
| 0   | 0   | 0   | 0   | 1      | D1     |
| 0   | 0   | 0   | 0   | 2      | D2     |
| 0   | 0   | 0   | 0   | 3      | D3     |
| 0   | 0   | 0   | 1   | 0      | C0     |
| 0   | 0   | 0   | 1   | 1      | C1     |
| 0   | 0   | 0   | 1   | 2      | B0     |
| 0   | 0   | 0   | 1   | 3      | B1     |
| 0   | 0   | 1   | 0   | 0      | B0     |
| 0   | 0   | 1   | 0   | 1      | B1     |
| 0   | 0   | 1   | 0   | 2      | A0     |
| 0   | 0   | 1   | 0   | 3      | A1     |
| 0   | 0   | 1   | 1   | 0      | C0     |
| 0   | 0   | 1   | 1   | 1      | C1     |
| 0   | 0   | 1   | 1   | 2      | B0     |
| 0   | 0   | 1   | 1   | 3      | B1     |
| 0   | 1   | 0   | 0   | 0      | A0     |
| 0   | 1   | 0   | 0   | 1      | A1     |
| 0   | 1   | 0   | 0   | 2      | B0     |
| 0   | 1   | 0   | 0   | 3      | B1     |
| 0   | 1   | 0   | 1   | 0      | C0     |
| 0   | 1   | 0   | 1   | 1      | C1     |
| 0   | 1   | 0   | 1   | 2      | B0     |
| 0   | 1   | 0   | 1   | 3      | B1     |
| 0   | 1   | 1   | 0   | 0      | A0     |
| 0   | 1   | 1   | 0   | 1      | A1     |
| 0   | 1   | 1   | 0   | 2      | B0     |
| 0   | 1   | 1   | 0   | 3      | B1     |
| 0   | 1   | 1   | 1   | 0      | C0     |
| 0   | 1   | 1   | 1   | 1      | C1     |
| 0   | 1   | 1   | 1   | 2      | B0     |
| 0   | 1   | 1   | 1   | 3      | B1     |
| 1   | 0   | 0   | 0   | 0      | D0     |
| 1   | 0   | 0   | 0   | 1      | D1     |
| 1   | 0   | 0   | 0   | 2      | D2     |
| 1   | 0   | 0   | 0   | 3      | D3     |
| 1   | 0   | 0   | 1   | 0      | C0     |
| 1   | 0   | 0   | 1   | 1      | C1     |
| 1   | 0   | 0   | 1   | 2      | B0     |
| 1   | 0   | 0   | 1   | 3      | B1     |
| 1   | 0   | 1   | 0   | 0      | B0     |
| 1   | 0   | 1   | 0   | 1      | B1     |
| 1   | 0   | 1   | 0   | 2      | A0     |
| 1   | 0   | 1   | 0   | 3      | A1     |
| 1   | 0   | 1   | 1   | 0      | C0     |
| 1   | 0   | 1   | 1   | 1      | C1     |
| 1   | 0   | 1   | 1   | 2      | B0     |
| 1   | 0   | 1   | 1   | 3      | B1     |
| 1   | 1   | 0   | 0   | 0      | A0     |
| 1   | 1   | 0   | 0   | 1      | A1     |
| 1   | 1   | 0   | 0   | 2      | B0     |
| 1   | 1   | 0   | 0   | 3      | B1     |
| 1   | 1   | 0   | 1   | 0      | C0     |
| 1   | 1   | 0   | 1   | 1      | C1     |
| 1   | 1   | 0   | 1   | 2      | B0     |
| 1   | 1   | 0   | 1   | 3      | B1     |
| 1   | 1   | 1   | 0   | 0      | B0     |
| 1   | 1   | 1   | 0   | 1      | B1     |
| 1   | 1   | 1   | 0   | 2      | A0     |
| 1   | 1   | 1   | 0   | 3      | A1     |
| 1   | 1   | 1   | 1   | 0      | C0     |
| 1   | 1   | 1   | 1   | 1      | C1     |
| 1   | 1   | 1   | 1   | 2      | B0     |
| 1   | 1   | 1   | 1   | 3      | B1     |

**Verilog Program:**

```verilog
module mux4_1(A, B, C, D, Select, Output);
    input A, B, C, D, Select;
    output Output;
    assign Output = (Select == 1) ? D : (Select == 2) ? C : (Select == 3) ? B : A;
endmodule
```

### 3. 8:1 Multiplexer

An 8:1 multiplexer takes eight input signals and selects one output signal.

**Definition:** An 8:1 multiplexer is a circuit that selects one of eight input signals and sends it to the output.

**Truth Table:**

| A   | B   | C   | D   | E   | F   | G   | H   | Select | Output |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0      | H0     |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1      | H1     |
| ... | ... | ... | ... | ... | ... | ... | ... | ...    | ...    |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 0      | H0     |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1      | H1     |

**Verilog Program:**

```verilog
module mux8_1(A, B, C, D, E, F, G, H, Select, Output);
    input A, B, C, D, E, F, G, H, Select;
    output Output;
    assign Output = (Select == 1) ? H : (Select == 2) ? G : (Select == 3) ? F : (Select == 4) ? E : (Select == 5) ? D : (Select == 6) ? C : (Select == 7) ? B : A;
endmodule
```

**4. N:1 Multiplexer**

An N:1 multiplexer is a circuit that takes N input signals and selects one output signal.

**Definition:** An N:1 multiplexer is a circuit that selects one of N input signals and sends it to the output.

**Truth Table:**

| A1 | A2 | ... | An | Select | Output |
| --- | --- | ... | --- | --- | --- |
| 0 | 0 | ... | 0 | 0 | An |
| 0 | 0 | ... | 0 | 1 | An-1 |
| ... | ... | ... | ... | ... | ... |
| 1 | 0 | ... | 0 | 0 | An |
| 1 | 0 | ... | 0 | 1 | An-1 |
| ... | ... | ... | ... | ... | ... |
| 1 | 1 | ... | 0 | 0 | An |
| 1 | 1 | ... | 0 | 1 | An-1 |
| ... | ... | ... | ... | ... | ... |
| 1 | 1 | ... | 0 | ... | ... |
| 1 | 1 | ... | 0 | N-1 | An-1 |
| 1 | 1 | ... | 0 | N | An |

**Verilog Program:**

```verilog
module mux_n(A1, A2, ..., An, Select, Output);
    input A1, A2, ..., An, Select;
    output Output;
    assign Output = (Select == 1) ? An : (Select == 2) ? An-1 : ... : (Select == N) ? A1 : A2;
endmodule
```

### 5. Priority Encoder

A priority encoder is a circuit that takes N input signals and selects the output signal with the highest priority.

**Definition:** A priority encoder is a circuit that selects the output signal with the highest priority from N input signals.

**Truth Table:**

| A1 | A2 | ... | AN | Output |
| --- | --- | ... | --- | --- |
| 0 | 0 | ... | 0 | 0 |
| 0 | 0 | ... | 0 | 1 |
| ... | ... | ... | ... | ... |
| 1 | 1 | ... | 0 | 1 |
| 1 | 1 | ... | 0 | 2 |
| ... | ... | ... | ... | ... |
| 1 | 1 | ... | 0 | N |

**Verilog Program:**

```verilog
module priority_encoder(A1, A2, ..., An, Output);
    input A1, A2, ..., An;
    output Output;
    assign Output = (A1 == 1) ? 1 : (A2 == 1) ? 2 : ... : (An == 1) ? N : 0;
endmodule
```

### 6. MUX with Enable

A multiplexer with an enable input is a circuit that takes N input signals and selects one output signal based on the enable input.

**Definition:** A multiplexer with an enable input is a circuit that takes N input signals and selects one output signal based on the enable input.

**Truth Table:**

| A1 | A2 | ... | An | Enable | Output |
| --- | --- | ... | --- | --- | --- |
| 0 | 0 | ... | 0 | 0 | 0 |
| 0 | 0 | ... | 0 | 1 | A1 |
| ... | ... | ... | ... | 1 | ... |
| 1 | 1 | ... | 0 | 0 | 0 |
| 1 | 1 | ... | 0 | 1 | A1 |
| ... | ... | ... | ... | 1 | ... |
| 1 | 1 | ... | 0 | 0 | 1 |
| 1 | 1 | ... | 0 | 1 | A1 |
| ... | ... | ... | ... | 1 | ... |
| 1 | 1 | ... | 0 | 0 | N |
| 1 | 1 | ... | 0 | 1 | A1 |
| ... | ... | ... | ... | 1 | ... |
| 1 | 1 | ... | 0 | 0 | 0 |
| 1 | 1 | ... | 0 | 1 | A1 |
| ... | ... | ... | ... | 1 | ... |

**Verilog Program:**

```verilog
module mux_with_enable(A1, A2, ..., An, Enable, Output);
    input A1, A2, ..., An, Enable;
    output Output;
    assign Output = (Enable == 1) ? An : (Enable == 0) ? A1 : A2;
endmodule
```

## **Conclusion**

In this study material, we have learned about different types of multiplexers, including 2:1, 4:1, 8:1, and N:1 multiplexers. We have also learned about priority encoders and multiplexers with enable inputs. We have designed Verilog programs to implement these multiplexers and encoders. These are fundamental concepts in digital design and are used extensively in digital circuits.
