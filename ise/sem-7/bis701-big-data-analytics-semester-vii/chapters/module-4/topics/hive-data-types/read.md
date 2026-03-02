# Data Types in Verilog

## Overview

Verilog provides various data types to model different aspects of digital hardware. Understanding these types is crucial for writing correct and synthesizable code.

## Net Types

Nets represent physical connections between hardware elements.

### Wire
The most commonly used net type:
```verilog
wire        single_bit;
wire [7:0]  byte_bus;
wire [31:0] data_bus;
```

### Other Net Types

| Type | Description | Use Case |
|------|-------------|----------|
| `wire` | Standard connection | Default for ports |
| `tri` | Same as wire | Explicit tri-state |
| `wand` | Wired-AND | Open-drain outputs |
| `wor` | Wired-OR | Open-collector |
| `supply0` | Constant 0 | Ground connection |
| `supply1` | Constant 1 | VCC connection |

## Variable Types

Variables hold values and can be assigned in procedural blocks.

### Reg
Holds a value until reassigned:
```verilog
reg        flag;
reg [7:0]  counter;
reg [15:0] data_reg;
```

**Important:** `reg` does NOT always mean a flip-flop! It's a storage element in simulation that may synthesize to combinational or sequential logic.

### Integer
32-bit signed value:
```verilog
integer i;
integer count = 0;
```

### Real
Floating-point (non-synthesizable):
```verilog
real pi = 3.14159;
real voltage;
```

### Time
64-bit for simulation time:
```verilog
time current_time;
current_time = $time;
```

## Value Set

Verilog has four logic values:

| Value | Meaning | Example |
|-------|---------|---------|
| `0` | Logic low | Ground |
| `1` | Logic high | VCC |
| `x` | Unknown | Uninitialized |
| `z` | High impedance | Tri-state |

## Vectors

Multi-bit signals using bit ranges:

```verilog
wire [7:0]  data;      // 8-bit vector, data[7] is MSB
reg  [31:0] address;   // 32-bit vector

// Accessing parts
data[7]                // Single bit
data[7:4]              // Upper nibble
data[3:0]              // Lower nibble
```

### Vector Declaration Conventions

```verilog
// Big-endian (recommended)
wire [7:0] data;       // data[7] is MSB

// Little-endian (less common)
wire [0:7] data;       // data[0] is MSB
```

## Arrays

### One-dimensional Arrays (Memories)
```verilog
reg [7:0] memory [0:255];    // 256 bytes
reg [31:0] ram [0:1023];     // 1K x 32-bit

// Access
memory[5] = 8'hAB;           // Write to address 5
data = memory[10];           // Read from address 10
```

### Two-dimensional Arrays
```verilog
reg [7:0] matrix [0:3][0:3];  // 4x4 matrix of bytes
```

## Number Representation

### Format: `<size>'<base><value>`

```verilog
8'b10101010    // 8-bit binary
8'hAA          // 8-bit hex (same value)
8'd170         // 8-bit decimal (same value)
8'o252         // 8-bit octal (same value)

// Negative numbers
-8'd5          // -5 in 8-bit signed
```

### Base Specifiers

| Base | Specifier | Example |
|------|-----------|---------|
| Binary | `'b` or `'B` | 4'b1010 |
| Octal | `'o` or `'O` | 4'o12 |
| Decimal | `'d` or `'D` | 4'd10 |
| Hexadecimal | `'h` or `'H` | 4'hA |

### Special Values
```verilog
8'bxxxx_xxxx   // All unknown
8'bzzzz_zzzz   // All high-Z
8'b1010_????   // Partial unknown
```

## Signed vs Unsigned

```verilog
// Unsigned (default)
reg [7:0] unsigned_val;

// Signed
reg signed [7:0] signed_val;
wire signed [15:0] signed_wire;

// Integer is always signed
integer signed_int;
```

## Parameters and Constants

```verilog
parameter WIDTH = 8;
parameter DEPTH = 256;
localparam ADDR_BITS = $clog2(DEPTH);

// Constants
`define MAX_COUNT 100
```

## Best Practices

1. **Use meaningful names** that indicate purpose
2. **Specify widths explicitly** to avoid width mismatches
3. **Use parameters** for configurable values
4. **Choose signed/unsigned** appropriately for arithmetic
5. **Initialize variables** in simulation for determinism
6. **Use underscores** in long numbers for readability

## Summary

- **wire**: Physical connections, continuous assignment
- **reg**: Procedural assignment, not always a register
- **Vectors**: Multi-bit signals with [MSB:LSB]
- **Arrays**: Memory modeling with reg arrays
- **Four values**: 0, 1, x, z
- **Number formats**: size'base value
