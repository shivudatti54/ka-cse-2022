# **Multiplexers and Demultiplexers**

## **Introduction**

A multiplexer (MUX) is a digital circuit that selects one of several input signals and sends it to a single output. It is an essential component in digital systems, used in a variety of applications such as data transmission, digital clock circuits, and programmable logic arrays. In this topic, we will explore the design of different types of multiplexers using Verilog programming language.

## **Types of Multiplexers**

### 1. 2:1 Multiplexer

A 2:1 multiplexer is a basic multiplexer that selects one of two input signals and sends it to a single output. The 2:1 multiplexer has three inputs: two select lines and one data input.

## **2:1 Multiplexer Truth Table**

| Select Line 1 | Select Line 2 | Data Input | Output |
| ------------- | ------------- | ---------- | ------ |
| 0             | 0             | A          | A      |
| 0             | 1             | B          | B      |
| 1             | 0             | C          | C      |
| 1             | 1             | D          | D      |

## **Verilog Code for 2:1 Multiplexer**

```verilog
module mux_21(
    input  wires[1:0] sel,
    input  wires[2:0] data,
    output wires[2:0] output
);

    always @*
        case(sel)
            0: output = data[0];
            1: output = data[1];
            default: output = 3'd0;
        endcase
endmodule
```

### 2. 3:1 Multiplexer

A 3:1 multiplexer is an extension of the 2:1 multiplexer that selects one of three input signals and sends it to a single output. The 3:1 multiplexer has four inputs: three select lines and one data input.

## **3:1 Multiplexer Truth Table**

| Select Line 1 | Select Line 2 | Select Line 3 | Data Input | Output |
| ------------- | ------------- | ------------- | ---------- | ------ |
| 0             | 0             | 0             | A          | A      |
| 0             | 0             | 1             | B          | B      |
| 0             | 1             | 0             | C          | C      |
| 0             | 1             | 1             | D          | D      |
| 1             | 0             | 0             | E          | E      |
| 1             | 0             | 1             | F          | F      |
| 1             | 1             | 0             | G          | G      |
| 1             | 1             | 1             | H          | H      |

## **Verilog Code for 3:1 Multiplexer**

```verilog
module mux_31(
    input  wires[2:0] sel,
    input  wires[3:0] data,
    output wires[3:0] output
);

    always @*
        case(sel)
            0: output = data[0];
            1: output = data[1];
            2: output = data[2];
            3: output = data[3];
            default: output = 4'd0;
        endcase
endmodule
```

### 3. 4:1 Multiplexer

A 4:1 multiplexer is an extension of the 3:1 multiplexer that selects one of four input signals and sends it to a single output. The 4:1 multiplexer has five inputs: four select lines and one data input.

## **4:1 Multiplexer Truth Table**

| Select Line 1 | Select Line 2 | Select Line 3 | Select Line 4 | Data Input | Output |
| ------------- | ------------- | ------------- | ------------- | ---------- | ------ |
| 0             | 0             | 0             | 0             | A          | A      |
| 0             | 0             | 0             | 1             | B          | B      |
| 0             | 0             | 1             | 0             | C          | C      |
| 0             | 0             | 1             | 1             | D          | D      |
| 0             | 1             | 0             | 0             | E          | E      |
| 0             | 1             | 0             | 1             | F          | F      |
| 0             | 1             | 1             | 0             | G          | G      |
| 0             | 1             | 1             | 1             | H          | H      |
| 1             | 0             | 0             | 0             | I          | I      |
| 1             | 0             | 0             | 1             | J          | J      |
| 1             | 0             | 1             | 0             | K          | K      |
| 1             | 0             | 1             | 1             | L          | L      |
| 1             | 1             | 0             | 0             | M          | M      |
| 1             | 1             | 0             | 1             | N          | N      |
| 1             | 1             | 1             | 0             | O          | O      |
| 1             | 1             | 1             | 1             | P          | P      |

## **Verilog Code for 4:1 Multiplexer**

```verilog
module mux_41(
    input  wires[3:0] sel,
    input  wires[4:0] data,
    output wires[4:0] output
);

    always @*
        case(sel)
            0: output = data[0];
            1: output = data[1];
            2: output = data[2];
            3: output = data[3];
            4: output = data[4];
            default: output = 5'd0;
        endcase
endmodule
```

## **Conclusion**

In this topic, we explored the design of different types of multiplexers using Verilog programming language. We saw how to implement 2:1, 3:1, and 4:1 multiplexers using Verilog code. These multiplexers are essential components in digital systems and are used in a variety of applications. By mastering the design of multiplexers, you can design more complex digital systems and improve your understanding of digital design principles.
