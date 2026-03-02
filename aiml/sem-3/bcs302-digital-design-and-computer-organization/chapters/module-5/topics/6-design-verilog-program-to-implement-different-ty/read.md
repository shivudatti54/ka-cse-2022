# **Designing Multiplexers in Verilog**

## **Introduction**

A multiplexer (MUX) is a digital circuit that selects one of several input signals and routes it to a single output. It is a fundamental building block in digital design and is used extensively in digital systems, including digital computers, data acquisition systems, and communication systems. In this topic, we will learn how to design and implement different types of multiplexers using Verilog.

## **Types of Multiplexers**

- **2:1 MUX (2-to-1 Multiplexer)**: A 2:1 MUX is a basic multiplexer that selects one of two input signals and routes it to a single output.
- **3:1 MUX (3-to-1 Multiplexer)**: A 3:1 MUX is a multiplexer that selects one of three input signals and routes it to a single output.
- **4:1 MUX (4-to-1 Multiplexer)**: A 4:1 MUX is a multiplexer that selects one of four input signals and routes it to a single output.

## **Designing 2:1 MUX in Verilog**

### Definition

A 2:1 MUX is a multiplexer that selects one of two input signals (A and B) and routes it to a single output.

### Verilog Implementation

```verilog
module mux2_1(A, B, Sel, Out);
    input A, B, Sel;
    output Out;

    assign Out = (Sel == 0) ? A : B;
endmodule
```

### Explanation

In the Verilog implementation, we define a 2:1 MUX module with inputs A, B, and Sel, and output Out. The Sel input is used to select one of the two input signals (A or B). The output Out is assigned the value of either A or B based on the value of Sel.

### Example Usage

```verilog
module test_mux2_1();
    reg A, B, Sel;
    wire Out;

    mux2_1 mux2_1_inst(A, B, Sel, Out);

    assign A = 0;
    assign B = 1;
    assign Sel = 0;

    initial begin
        $display("Output: %d", Out);
        $display("A: %d, B: %d, Sel: %d", A, B, Sel);
        $display("Output after 1 clock cycle: %d", Out);
        $display("A after 1 clock cycle: %d, B after 1 clock cycle: %d, Sel after 1 clock cycle: %d", A, B, Sel);
    end

    always @(posedge clock)
        begin
            A = 0;
            B = 1;
            Sel = 0;
        end
endmodule
```

## **Designing 3:1 MUX in Verilog**

### Definition

A 3:1 MUX is a multiplexer that selects one of three input signals (A, B, and C) and routes it to a single output.

### Verilog Implementation

```verilog
module mux3_1(A, B, C, Sel, Out);
    input A, B, C, Sel;
    output Out;

    assign Out = (Sel == 0) ? A : (Sel == 1) ? B : C;
endmodule
```

### Explanation

In the Verilog implementation, we define a 3:1 MUX module with inputs A, B, C, and Sel, and output Out. The Sel input is used to select one of the three input signals (A, B, or C). The output Out is assigned the value of either A, B, or C based on the value of Sel.

### Example Usage

```verilog
module test_mux3_1();
    reg A, B, C, Sel;
    wire Out;

    mux3_1 mux3_1_inst(A, B, C, Sel, Out);

    assign A = 0;
    assign B = 1;
    assign C = 1;
    assign Sel = 0;

    initial begin
        $display("Output: %d", Out);
        $display("A: %d, B: %d, C: %d, Sel: %d", A, B, C, Sel);
        $display("Output after 1 clock cycle: %d", Out);
        $display("A after 1 clock cycle: %d, B after 1 clock cycle: %d, C after 1 clock cycle: %d, Sel after 1 clock cycle: %d", A, B, C, Sel);
    end

    always @(posedge clock)
        begin
            A = 0;
            B = 1;
            C = 1;
            Sel = 0;
        end
endmodule
```

## **Designing 4:1 MUX in Verilog**

### Definition

A 4:1 MUX is a multiplexer that selects one of four input signals (A, B, C, and D) and routes it to a single output.

### Verilog Implementation

```verilog
module mux4_1(A, B, C, D, Sel, Out);
    input A, B, C, D, Sel;
    output Out;

    assign Out = (Sel == 0) ? A : (Sel == 1) ? B : (Sel == 2) ? C : D;
endmodule
```

### Explanation

In the Verilog implementation, we define a 4:1 MUX module with inputs A, B, C, D, and Sel, and output Out. The Sel input is used to select one of the four input signals (A, B, C, or D). The output Out is assigned the value of either A, B, C, or D based on the value of Sel.

### Example Usage

```verilog
module test_mux4_1();
    reg A, B, C, D, Sel;
    wire Out;

    mux4_1 mux4_1_inst(A, B, C, D, Sel, Out);

    assign A = 0;
    assign B = 1;
    assign C = 1;
    assign D = 1;
    assign Sel = 0;

    initial begin
        $display("Output: %d", Out);
        $display("A: %d, B: %d, C: %d, D: %d, Sel: %d", A, B, C, D, Sel);
        $display("Output after 1 clock cycle: %d", Out);
        $display("A after 1 clock cycle: %d, B after 1 clock cycle: %d, C after 1 clock cycle: %d, D after 1 clock cycle: %d, Sel after 1 clock cycle: %d", A, B, C, D, Sel);
    end

    always @(posedge clock)
        begin
            A = 0;
            B = 1;
            C = 1;
            D = 1;
            Sel = 0;
        end
endmodule
```
