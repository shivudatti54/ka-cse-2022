# Hardware Description Language – Verilog Model of a Simple Circuit


## Table of Contents

- [Hardware Description Language – Verilog Model of a Simple Circuit](#hardware-description-language--verilog-model-of-a-simple-circuit)
- [1. Introduction to Hardware Description Languages](#1-introduction-to-hardware-description-languages)
  - [1.1 Need for HDLs in Digital Design](#11-need-for-hdls-in-digital-design)
- [2. Fundamental Concepts in Verilog](#2-fundamental-concepts-in-verilog)
  - [2.1 Module: The Basic Building Block](#21-module-the-basic-building-block)
  - [2.2 Port Types and Data Types](#22-port-types-and-data-types)
  - [2.3 Scalar and Vector Declarations](#23-scalar-and-vector-declarations)
- [3. Modeling Styles in Verilog](#3-modeling-styles-in-verilog)
  - [3.1 Gate-Level (Structural) Modeling](#31-gate-level-structural-modeling)
  - [3.2 Dataflow Modeling](#32-dataflow-modeling)
  - [3.3 Behavioral Modeling](#33-behavioral-modeling)
  - [3.4 Comparison of Modeling Styles](#34-comparison-of-modeling-styles)
- [4. Practical Examples and Applications](#4-practical-examples-and-applications)
  - [4.1 Full Adder (1-bit)](#41-full-adder-1-bit)
  - [4.2 D Flip-Flop (Sequential Circuit)](#42-d-flip-flop-sequential-circuit)
  - [4.3 Parameterized Module: N-bit Mux](#43-parameterized-module-n-bit-mux)
- [5. Testbench Development](#5-testbench-development)
  - [5.1 Basic Testbench Structure](#51-basic-testbench-structure)
  - [5.2 Clock Generation in Testbench](#52-clock-generation-in-testbench)
  - [5.3 Common System Tasks](#53-common-system-tasks)
- [6. Synthesis Considerations](#6-synthesis-considerations)
  - [6.1 Synthesizable vs Non-Synthesizable Constructs](#61-synthesizable-vs-non-synthesizable-constructs)
  - [6.2 Coding Style Guidelines](#62-coding-style-guidelines)
- [7. Summary](#7-summary)
  - [Suggested Reading](#suggested-reading)

## 1. Introduction to Hardware Description Languages

A **Hardware Description Language (HDL)** is a specialized modeling language used to describe the structure and behavior of digital electronic systems at various levels of abstraction. Unlike conventional software programming languages that specify sequential instructions to be executed by a processor, HDLs describe hardware that operates **concurrently** (in parallel), where all signals and components are active simultaneously.

**Verilog**, standardized as IEEE 1364, is one of the two predominant HDLs used in industry (the other being VHDL). It was developed in 1983 by Gateway Design Automation and later acquired by Cadence Design Systems, eventually becoming an IEEE standard in 1990. Verilog provides a unified framework for modeling, simulation, synthesis, and formal verification of digital systems ranging from simple combinational logic to complex system-on-chip (SoC) designs.

### 1.1 Need for HDLs in Digital Design

The evolution of digital systems from small-scale integration (SSI) circuits containing few gates to modern very-large-scale integration (VLSI) chips with billions of transistors necessitates sophisticated design methodologies. HDLs address several critical requirements:

**1.1.1 Design Abstraction:** HDLs enable designers to work at multiple abstraction levels—behavioral, register-transfer level (RTL), gate-level, and switch-level—allowing management of complexity through hierarchical design.

**1.1.2 Simulation Before Fabrication:** Virtual prototyping through simulation enables verification of functionality, timing, and architectural decisions before expensive silicon fabrication, significantly reducing development costs and time-to-market.

**1.1.3 Automatic Synthesis:** Modern synthesis tools automatically transform RTL descriptions into optimized gate-level netlists, enabling rapid design space exploration and optimization.

**1.1.4 Reusability and Parametrization:** HDL modules can be parameterized and instantiated across multiple designs, promoting design reuse and productivity.

**1.1.5 Formal Verification Support:** HDL descriptions serve as golden references for formal verification techniques, ensuring functional correctness.

## 2. Fundamental Concepts in Verilog

### 2.1 Module: The Basic Building Block

In Verilog, a **module** represents a fundamental design entity that encapsulates the interface (ports) and implementation (internal logic) of a digital circuit. The module serves as the unit of hierarchy, enabling modular design methodology.

```verilog
module module_name #(parameter WIDTH = 8) (
 input wire clk, // Clock input
 input wire rst_n, // Active-low reset
 input wire [WIDTH-1:0] data_in, // Parallel data input
 input wire load, // Load enable
 output reg [WIDTH-1:0] data_out // Registered output
);
 // Internal declarations
 wire [WIDTH-1:0] next_state;

 // Combinational logic
 assign next_state = load ? data_in : data_out;

 // Sequential logic (flip-flop)
 always @(posedge clk or negedge rst_n) begin
 if (!rst_n)
 data_out <= 'b0;
 else
 data_out <= next_state;
 end
endmodule
```

**Syntax Elements:**

- **Module declaration:** `module module_name;` begins the definition
- **Port list:** Defines external connections with direction (input/output/inout)
- **Port declaration:** Specifies data type and direction
- **Internal declarations:** Wires, regs, and other internal signals
- **Module body:** Contains the functional implementation
- **Endmodule:** Terminates the module definition

### 2.2 Port Types and Data Types

**Port Types:**
| Port Type | Description | Usage |
|-----------|-------------|-------|
| `input` | Unidirectional signal receiving data into the module | Primary inputs, control signals |
| `output` | Unidirectional signal transmitting data out of the module | Primary outputs, status signals |
| `inout` | Bidirectional signal for tri-state communication | Bus interfaces, bidirectional ports |

**Data Types:**

Verilog supports two primary data types:

1. **wire:** Represents a physical wire or connection that cannot store a value. It must be continuously driven. Used for:

- Combinational logic outputs
- Interconnecting components in structural models
- Continuous assignment targets

```verilog
wire [7:0] data_bus; // 8-bit wide wire
wire clk, rst; // Single-bit wires
```

2. **reg:** Represents a storage element that can hold a value.:

- Variables assigned within Used in procedural blocks `always` or `initial` blocks
- Outputs of behavioral descriptions
- Sequential logic storage elements

```verilog
reg [3:0] counter; // 4-bit register
reg flag; // Single-bit register
```

### 2.3 Scalar and Vector Declarations

**Scalars:** Single-bit signals declared without a range specification.

```verilog
wire a; // Single-bit wire
reg b; // Single-bit register
```

**Vectors:** Multi-bit signals declared with a range [MSB:LSB].

```verilog
wire [7:0] data_in; // 8-bit input bus (bit 7 is bit 0 is MSB, LSB)
reg [0:15] shift_reg; // 16-bit register (bit 0 is MSB, bit 15 is LSB)
output [3:0] addr; // 4-bit output address bus
```

## 3. Modeling Styles in Verilog

Verilog supports multiple modeling paradigms, each appropriate for different abstraction levels and design phases.

### 3.1 Gate-Level (Structural) Modeling

Gate-level modeling describes circuits by instantiating primitive logic gates and their interconnections. This lowest level of abstraction directly corresponds to the physical gate-level netlist and is particularly useful for:

- Representing final synthesized netlists
- Modeling critical timing paths
- Understanding physical implementation

**Built-in Primitive Gates:**

| Gate Type | Symbol | Description | Number of Inputs |
| --------- | ------ | ----------- | ---------------- |
| `and`     | &      | AND gate    | 2 or more        |
| `or`      | \|     | OR gate     | 2 or more        |
| `not`     | ~      | Inverter    | 1                |
| `nand`    | ~&     | NAND gate   | 2 or more        |
| `nor`     | ~\|    | NOR gate    | 2 or more        |
| `xor`     | ^      | XOR gate    | 2 or more        |
| `xnor`    | ~^     | XNOR gate   | 2 or more        |
| `buf`     |        | Buffer      | 1 or more        |

**Syntax for Gate Instantiation:**

```verilog
gate_type instance_name (output, input1, input2, ..., inputN);
```

**Example: Gate-Level Implementation of F = xy + x'z**

```verilog
module simple_circuit_gate (
 input wire x,
 input wire y,
 input wire z,
 output wire F
);
 // Internal nets for gate interconnections
 wire w1, w2, w3;

 // Structural description: F = xy + x'z
 not g1 (w1, x); // w1 = x' (inverter)
 and g2 (w2, x, y); // w2 = x AND y = xy
 and g3 (w3, w1, z); // w3 = w1 AND z = x'z
 or g4 (F, w2, w3); // F = w2 OR w3 = xy + x'z

endmodule
```

**Timing Considerations:** Each gate instantiation has an inherent propagation delay. Verilog supports delay specifications:

```verilog
// Gate with propagation delay
and #5 g1 (out, a, b); // 5 time units delay

// Gate with rise and fall delays
and #(3,4) g2 (out, a, b); // 3 time units rise, 4 time units fall

// Gate with min:typical:max delays
and #(3:4:5, 4:5:6) g3 (out, a, b);
```

### 3.2 Dataflow Modeling

Dataflow modeling uses **continuous assignments** to describe combinational logic behavior. The `assign` keyword specifies how signals flow from inputs to outputs, with the right-hand side continuously driving the left-hand side wire.

**Continuous Assignment Syntax:**

```verilog
assign [delay] signal_name = expression;
```

**Key Characteristics:**

- Left-hand side must be a `wire` (or related type)
- Right-hand side is a combinational expression
- Evaluated continuously whenever any operand changes
- Implements declarative (what) rather than procedural (how) logic

**Operator Precedence:** Verilog operators follow C-like precedence:

| Operator Type | Symbols                  | Precedence (High to Low) |
| ------------- | ------------------------ | ------------------------ |
| Unary         | ~, &, ~&, \|, ~\|, ^, ~^ | Highest                  |
| Arithmetic    | \*, /, %                 |                          |
| Shift         | <<, >>, <<<, >>>         |                          |
| Relational    | <, <=, >, >=             |                          |
| Equality      | ==, !=, ===, !==         |                          |
| Reduction     | &, ~&, \|, ~\|, ^, ~^    |                          |
| Logical       | &&, \|\|                 |                          |
| Conditional   | ?:                       | Lowest                   |

**Example: Dataflow Implementation of F = xy + x'z**

```verilog
module simple_circuit_dataflow (
 input wire x,
 input wire y,
 input wire z,
 output wire F
);
 // Continuous assignment: F = xy + x'z
 assign F = (x & y) | (~x & z);

endmodule
```

**Verification via Truth Table:** For input combinations (x, y, z):

| x   | y   | z   | ~x  | x&y | ~x&z | F (=xy+x'z) |
| --- | --- | --- | --- | --- | ---- | ----------- |
| 0   | 0   | 0   | 1   | 0   | 0    | 0           |
| 0   | 0   | 1   | 1   | 0   | 1    | 1           |
| 0   | 1   | 0   | 1   | 0   | 0    | 0           |
| 0   | 1   | 1   | 1   | 0   | 1    | 1           |
| 1   | 0   | 0   | 0   | 0   | 0    | 0           |
| 1   | 0   | 1   | 0   | 0   | 0    | 0           |
| 1   | 1   | 0   | 0   | 1   | 0    | 1           |
| 1   | 1   | 1   | 0   | 1   | 0    | 1           |

### 3.3 Behavioral Modeling

Behavioral modeling uses procedural blocks to describe circuit behavior algorithmically, focusing on **what** the circuit does rather than **how** it is implemented.

**The `always` Block:**

The `always` block is the primary construct for behavioral modeling:

```verilog
always @(sensitivity_list) begin
 // procedural statements
end
```

**Sensitivity List:** Specifies when the block should be re-evaluated. Common patterns:

- **Combinational:** `@(a or b or c)` or `@(*)` (implicit)
- **Sequential (edge-triggered):** `@(posedge clk)` or `@(negedge rst)`

**Example: 2-to-1 Multiplexer (Behavioral)**

```verilog
module mux_2x1_behavioral (
 input wire a,
 input wire b,
 input wire sel,
 output reg y
);
 always @(*) begin
 if (sel == 1'b0)
 y = a;
 else
 y = b;
 end
endmodule
```

**Blocking vs Non-Blocking Assignments:**

This distinction is critical for correct synthesis and simulation:

| Assignment Type | Symbol | Usage               | Execution Model                                       |
| --------------- | ------ | ------------------- | ----------------------------------------------------- |
| Blocking        | `=`    | Combinational logic | Evaluated and assigned immediately                    |
| Non-Blocking    | `<=`   | Sequential logic    | Evaluated simultaneously, sampled at end of time step |

**Rule of Thumb:**

- Use **non-blocking** (`<=`) for sequential logic (flip-flops, registers)
- Use **blocking** (`=`) for combinational logic within `always` blocks

```verilog
// Correct: Sequential logic with non-blocking
always @(posedge clk) begin
 q <= d; // Non-blocking: scheduled, not immediate
end

// Correct: Combinational logic with blocking
always @(*) begin
 y = a & b; // Blocking: immediate evaluation
end

// INCORRECT EXAMPLE: Using blocking for flip-flop leads to simulation mismatch
always @(posedge clk) begin
 q = d; // Wrong for sequential logic!
end
```

### 3.4 Comparison of Modeling Styles

| Aspect           | Gate-Level  | Dataflow           | Behavioral       |
| ---------------- | ----------- | ------------------ | ---------------- |
| Abstraction      | Low (gates) | Medium (operators) | High (algorithm) |
| Synthesis        | Direct      | Direct             | Direct           |
| Readability      | Low         | Medium             | High             |
| Flexibility      | Low         | Medium             | High             |
| Simulation Speed | Fast        | Medium             | Medium           |
| Timing Detail    | Explicit    | Implicit           | Implicit         |

## 4. Practical Examples and Applications

### 4.1 Full Adder (1-bit)

The full adder adds three input bits (A, B, and Carry-in) to produce sum and carry-out.

**Logic:**

- Sum: S = A ⊕ B ⊕ Cin
- Carry: Cout = (A·B) + (Cin·(A ⊕ B))

```verilog
// Gate-level full adder
module full_adder_gate (
 input wire a,
 input wire b,
 input wire cin,
 output wire sum,
 output wire cout
);
 wire s1, c1, c2;

 xor g1 (s1, a, b);
 xor g2 (sum, s1, cin);
 and g3 (c1, s1, cin);
 and g4 (c2, a, b);
 or g5 (cout, c1, c2);
endmodule

// Dataflow full adder
module full_adder_dataflow (
 input wire a,
 input wire b,
 input wire cin,
 output wire sum,
 output wire cout
);
 assign sum = a ^ b ^ cin;
 assign cout = (a & b) | (cin & (a ^ b));
endmodule

// Behavioral full adder
module full_adder_behavioral (
 input wire a,
 input wire b,
 input wire cin,
 output reg sum,
 output reg cout
);
 always @(*) begin
 {cout, sum} = a + b + cin; // Binary addition
 end
endmodule
```

### 4.2 D Flip-Flop (Sequential Circuit)

The D flip-flop is a fundamental memory element that captures the input value on the active clock edge.

```verilog
// Synchronous D flip-flop with asynchronous reset
module d_ff_async_rst (
 input wire clk,
 input wire rst_n, // Active-low asynchronous reset
 input wire d,
 output reg q
);
 always @(posedge clk or negedge rst_n) begin
 if (!rst_n)
 q <= 1'b0; // Asynchronous reset
 else
 q <= d; // Capture D on rising edge
 end
endmodule

// D flip-flop with synchronous reset
module d_ff_sync_rst (
 input wire clk,
 input wire rst_n, // Synchronous reset (active-low)
 input wire d,
 output reg q
);
 always @(posedge clk) begin
 if (!rst_n)
 q <= 1'b0;
 else
 q <= d;
 end
endmodule
```

### 4.3 Parameterized Module: N-bit Mux

Parameterization enables design reuse for different data widths:

```verilog
module mux_2x1_nbit #(
 parameter WIDTH = 8 // Default width
)(
 input wire [WIDTH-1:0] a,
 input wire [WIDTH-1:0] b,
 input wire sel,
 output wire [WIDTH-1:0] y
);
 assign y = sel ? b : a;
endmodule

// Instantiation with different widths
mux_2x1_nbit #(.WIDTH(4)) mux4 (a4, b4, sel, y4); // 4-bit
mux_2x1_nbit #(.WIDTH(16)) mux16 (a16, b16, sel, y16); // 16-bit
```

## 5. Testbench Development

A **testbench** is a Verilog module that provides stimulus to verify the design under test (DUT). Testbenches are typically not synthesizable—they exist solely for simulation.

### 5.1 Basic Testbench Structure

```verilog
module tb_simple_circuit;
 // Declare stimulus signals (reg because driven)
 reg x, y, z;
 // Declare observation signals (wire because monitored)
 wire F;

 // Instantiate the DUT
 simple_circuit_dataflow uut (
 .x(x),
 .y(y),
 .z(z),
 .F(F)
 );

 // Stimulus generation
 initial begin
 $display("Time\t x y z | F"); // Print header
 $display("==================");

 // Apply all 8 input combinations
 x = 0; y = 0; z = 0; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 0; y = 0; z = 1; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 0; y = 1; z = 0; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 0; y = 1; z = 1; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 1; y = 0; z = 0; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 1; y = 0; z = 1; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 1; y = 1; z = 0; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 x = 1; y = 1; z = 1; #10;
 $display("%0t\t %b %b %b | %b", $time, x, y, z, F);

 $finish; // Terminate simulation
 end

 // Optional: Monitor changes
 initial begin
 $monitor("At time %t: x=%b, y=%b, z=%b, F=%b", $time, x, y, z, F);
 end
endmodule
```

### 5.2 Clock Generation in Testbench

For sequential circuits, generating a clock signal is essential:

```verilog
// Clock generation: 10 time units period
initial begin
 clk = 0;
 forever #5 clk = ~clk; // Toggle every 5 time units
end

// Alternative: using repeat
initial begin
 clk = 0;
 repeat (20) #5 clk = ~clk; // 20 cycles
end
```

### 5.3 Common System Tasks

| Task       | Description                         | Example                        |
| ---------- | ----------------------------------- | ------------------------------ |
| `$display` | Print formatted text (with newline) | `$display("Value = %d", var);` |
| `$write`   | Print formatted text (no newline)   | `$write("Value = %d", var);`   |
| `$monitor` | Print when arguments change         | `$monitor("A=%b", A);`         |
| `$time`    | Return current simulation time      | `$time`                        |
| `$finish`  | Terminate simulation                | `$finish;`                     |
| `$stop`    | Pause simulation (interactive)      | `$stop;`                       |
| `$fopen`   | Open file for writing               | `$fopen("log.txt");`           |

## 6. Synthesis Considerations

### 6.1 Synthesizable vs Non-Synthesizable Constructs

Not all Verilog code can be synthesized into hardware. Designers must use only synthesizable constructs:

**Synthesizable:**

- `module`, `input`, `output`, `inout`
- `wire`, `reg`, `integer`, `parameter`
- `assign`, `always`, `@`, `posedge`, `negedge`
- `if`, `case`, `for` (with restrictions)
- `begin`, `end`, `casez`, `casex`
- Blocking and non-blocking assignments

**Non-Synthesizable (simulation only):**

- `initial` blocks (for testbenches)
- `#delay` specifications
- `$display`, `$monitor`, `$time`, `$finish`
- `fork`, `join`
- Real number types
- Advanced timing controls

### 6.2 Coding Style Guidelines

1. **Use meaningful identifiers:** `enable_counter` not `en` or `c`
2. **Comment thoroughly:** Explain intent, not just code
3. **Use consistent naming:** `clk`, `rst_n`, `data_in`, `data_out`
4. **One module per file:** Facilitates version control
5. **Indentation and formatting:** Enhance readability

## 7. Summary

Verilog Hardware Description Language provides a comprehensive framework for modeling, simulating, and synthesizing digital systems. Key takeaways include:

1. **Module-based design:** The module encapsulates interface and implementation, serving as the fundamental unit of hierarchy.

2. **Three modeling paradigms:**

- **Gate-level:** Direct instantiation of primitives; lowest abstraction
- **Dataflow:** Continuous assignments; declarative description
- **Behavioral:** Procedural blocks; algorithmic description

3. **Data types:** `wire` for connections, `reg` for storage elements.

4. **Assignment types:** Blocking (`=`) for combinational logic; non-blocking (`<=`) for sequential logic.

5. **Testbench development:** Simulation verifies functionality before synthesis; testbenches need not be synthesizable.

6. **Synthesis awareness:** Use only synthesizable constructs for hardware implementation.

### Suggested Reading

- **Digital Design:** Morris Mano and Michael Ciletti (Pearson)
- **Verilog HDL:** Samir Palnitkar (Pearson)
- **IEEE Standard for Verilog Hardware Description Language:** IEEE Std 1364-2005
