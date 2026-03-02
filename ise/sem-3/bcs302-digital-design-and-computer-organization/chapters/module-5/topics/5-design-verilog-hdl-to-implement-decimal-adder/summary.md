# Revision Notes: Verilog HDL for Decimal Adder

==============================================

### Overview

---

- Decimal adder is a digital circuit that adds two decimal numbers.
- Implemented using Verilog HDL (Hardware Description Language).

### Key Concepts

---

- **Decimal Adder Circuit:**
  - 4-bit or 5-bit decimal adder can be implemented using 2's complement or Gray's code.
  - Carry-out and borrow-out bits are generated.
- **Verilog Code Structure:**
  - Module definition (e.g., `module decimal_adder()`)
  - Input and output ports (e.g., `input [3:0] A`, `input [3:0] B`, `output [4:0] Sum`)
  - Logic gates and arithmetic operations (e.g., `or`, `and`, `nand`, `add`)
- **Verilog Syntax:**
  - `reg` keyword for registers (e.g., `reg [3:0] Sum`)
  - `assign` keyword for assigning values (e.g., `assign Sum = A + B + Sum`)
  - `initial` keyword for initial conditions (e.g., `initial Sum = 0`)

### Important Formulas and Definitions

---

- **2's Complement Addition:**
  - `Sum = A + B + (Borrow-out)`
  - `Borrow-out = (B[0] & !A[0])`
- **Gray's Code Addition:**
  - `Sum = A + B + (A ⊕ B)`

### Theorems

---

- **Law of Excluded Middle:**
  - `A or !A = 1`
  - `A and !A = 0`

### Important Verilog HDL Constructs

---

- **`always` block:** for sequential logic
- **`initial` statement:** for initial conditions
- **`assign` statement:** for assigning values

### Example Verilog Code

---

```verilog
module decimal_adder(
    input [3:0] A,
    input [3:0] B,
    output [4:0] Sum,
    output [1:0] Carry-out
);

reg [3:0] Sum;
reg [1:0] Carry-out;

always @(*) begin
    Sum = A + B + (Borrow-out);
    Carry-out = (B[0] & !A[0]);
end

assign Sum = A + B + Sum;
assign Carry-out = (B[0] & !A[0]);

initial Sum = 0;
initial Carry-out = 0;

endmodule
```

### Revision Tips

---

- Review Verilog syntax and semantics.
- Understand the decimal adder circuit and its components.
- Practice writing Verilog code for decimal adder circuits.
- Review important formulas and theorems related to digital arithmetic.
