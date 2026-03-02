# HDL Models of Combinational Circuits – Adder

### Introduction

- An adder is a digital circuit that performs binary addition.
- HDL (Hardware Description Language) models are used to describe digital circuits.

### Key Concepts

- **Half Adder**: A 2-bit adder that adds two binary digits (bits) and produces a sum and a carry-out bit.
  - Formula: `S(x, y) = x ⊕ y` and `C(x, y) = x ∧ y`
- **Full Adder**: A 3-bit adder that adds three binary digits (bits) and produces a sum and a carry-out bit.
  - Formula: `S(x, y, z) = (x ⊕ y) ⊕ z` and `C(x, y, z) = x ∧ y ∧ z`
- **Adder Chain**: A combination of half adders to form a full adder.
- **carry-in**: The carry-out bit from the previous stage of the adder chain.
- **carry-out**: The final carry-out bit of the adder chain.

### Theorems

- **Complement Law**: `x ⊕ x = 0` and `x ⊕ 0 = x`
- **Identity Law**: `x ⊕ 0 = x` and `x ⊕ x = 0`

### HDL Code

- Example in VHDL:

```vhdl
library IEEE;
use IEEE.STD_LOGIC;

entity adder is
    Port ( A : in  STD_LOGIC;
           B : in  STD_LOGIC;
           Sum : out  STD_LOGIC;
           Carry : out  STD_LOGIC);
end adder;

architecture Behavioral of adder is
begin
    Sum <= A xor B;
    Carry <= A and B;
end Behavioral;
```

- Example in Verilog:

```verilog
module adder(A, B, Sum, Carry);
    input A, B;
    output Sum, Carry;

    Sum <= A ^ B;
    Carry <= A & B;
endmodule
```

### Important Formulas

- `S(x, y) = x ⊕ y`
- `C(x, y) = x ∧ y`
- `S(x, y, z) = (x ⊕ y) ⊕ z`
- `C(x, y, z) = x ∧ y ∧ z`
