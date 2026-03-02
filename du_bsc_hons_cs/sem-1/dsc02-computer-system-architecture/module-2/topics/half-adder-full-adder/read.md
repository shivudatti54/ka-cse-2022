# Half Adder and Full Adder

## Comprehensive Study Material for Computer System Architecture

---

## 1. Introduction

Adder circuits form the fundamental building blocks of arithmetic logic units (ALUs) in all digital computers and processors. Understanding adders is essential for comprehending how computers perform basic mathematical operations at the hardware level. This chapter covers two essential combinational circuits: the **Half Adder** and the **Full Adder**, which are designed to add binary numbers.

### Real-World Relevance

- **CPU Architecture**: Adders are the core components of ALUs, performing all arithmetic operations including subtraction, multiplication, and division (which are implemented through repeated addition).
- **Digital Signal Processing**: Used in DSP chips for real-time signal processing algorithms.
- **Cryptographic Hardware**: Modern encryption algorithms heavily rely on binary addition operations.
- **Microcontrollers**: Every microcontroller contains adder logic in its arithmetic processing unit.
- **Communication Systems**: Error detection codes (like checksums) use binary addition.

> **Delhi University NEP 2024 UGCF Context**: This topic aligns with Unit III (Combinational Logic Design) of the BSc (Hons) Computer Science syllabus, focusing on fundamental digital logic circuits essential for understanding computer architecture.

---

## 2. Fundamentals of Binary Addition

Before studying adder circuits, we must understand binary number addition:

| Binary | Decimal | Addition Rules |
|--------|---------|----------------|
| 0 + 0  | 0 + 0   | Sum = 0, Carry = 0 |
| 0 + 1  | 0 + 1   | Sum = 1, Carry = 0 |
| 1 + 0  | 1 + 0   | Sum = 1, Carry = 0 |
| 1 + 1  | 1 + 1   | Sum = 0, Carry = 1 |

**Key Observation**: When adding two binary digits, we get two outputs:
1. **Sum (S)**: The result of the addition
2. **Carry (C)**: The overflow to the next significant bit

---

## 3. Half Adder

### 3.1 Definition

A **Half Adder** is a combinational logic circuit that adds two single-bit binary numbers and produces a sum bit and a carry bit. It is called "half" because it doesn't account for a carry-in from a previous less significant addition.

### 3.2 Truth Table

The truth table for a Half Adder shows all possible combinations of two input bits (A and B):

| A | B | Sum (S) | Carry (C) |
|---|---|---------|-----------|
| 0 | 0 | 0       | 0         |
| 0 | 1 | 1       | 0         |
| 1 | 0 | 1       | 0         |
| 1 | 1 | 0       | 1         |

### 3.3 Boolean Expressions

From the truth table, we derive the Boolean expressions using **Sum of Products (SOP)** form:

**Sum Output (S)**:
- S = 1 when (A=0, B=1) OR (A=1, B=0)
- S = A'B + AB'
- **S = A ⊕ B** (XOR gate)

**Carry Output (C)**:
- C = 1 only when (A=1, B=1)
- C = AB
- **C = A · B** (AND gate)

### 3.4 Circuit Implementation

```
        ┌─────┐
   A ───┤     │
        │ XOR ├─── Sum (S)
   B ───┤     │
        └─────┘
        
        ┌─────┐
   A ───┤     │
        │ AND ├─── Carry (C)
   B ───┤     │
        └─────┘
```

**Gate Requirements**:
- 1 XOR Gate
- 1 AND Gate

### 3.5 Propagation Delay Analysis

| Gate Type | Propagation Delay |
|-----------|-------------------|
| XOR       | 2τ (typical)      |
| AND       | 1τ                |

The **Sum output** has a longer propagation delay (2τ) compared to the Carry output (1τ), which becomes critical in multi-bit adder designs.

---

## 4. Full Adder

### 4.1 Definition

A **Full Adder** is a combinational logic circuit that adds three single-bit binary numbers: two significant bits (A and B) and one carry-in bit (C_in) from the previous less significant position. It produces a sum output (S) and a carry-out output (C_out).

### 4.2 Truth Table

| A | B | C_in | Sum (S) | Carry (C_out) |
|---|---|------|---------|---------------|
| 0 | 0 | 0    | 0       | 0             |
| 0 | 0 | 1    | 1       | 0             |
| 0 | 1 | 0    | 1       | 0             |
| 0 | 1 | 1    | 0       | 1             |
| 1 | 0 | 0    | 1       | 0             |
| 1 | 0 | 1    | 0       | 1             |
| 1 | 1 | 0    | 0       | 1             |
| 1 | 1 | 1    | 1       | 1             |

### 4.3 Boolean Expressions

Using **Sum of Products (SOP)** method:

**Sum Output (S)**:
```
S = A'B'C_in + A'BC_in' + AB'C_in' + ABC_in
S = A ⊕ B ⊕ C_in
```

The sum output is the **odd function** of the three inputs (XOR of all three).

**Carry Output (C_out)**:
```
C_out = A'BC_in + AB'C_in + ABC_in' + ABC_in
C_out = AB + AC_in + BC_in
C_out = AB + C_in(A ⊕ B)
```

### 4.4 Circuit Implementation

**Method 1: Using Basic Gates**

```
            ┌─────┐
       A ───┤     │
            │ XOR ├────┐
       B ───┤     │    │    ┌─────┐
            └─────┘    ├───┤     │
                       │   │ XOR ├─── Sum (S)
       C_in ───────────┘   │     │
                           └─────┘
                           
       A ────┬─── AND ──┐
              │          │
       B ────┼─── AND ──┼── OR ─── Carry (C_out)
              │          │
       (A⊕B) ─┴─── AND ─┘
                    │
              C_in ─┘
```

**Method 2: Using Two Half Adders**

A full adder can be constructed using **two half adders** and one OR gate:

```
            ┌──────────────┐
       A ───┤              │
            │  Half Adder  ├── Sum1 ──┐
       B ───┤    (HA1)     │          │
            └──────────────┘          │
                                       │    ┌──────────────┐
                                       ├────┤              │
            ┌──────────────┐          │    │  Half Adder  │── Sum (S)
       A ───┤              │          │    │    (HA2)     │
            │  Half Adder  ├── Carry1─┘    └──────────────┘
       B ───┤    (HA1)     │                         │
            └──────────────┘                         │
                                                         │    ┌─────┐
            ┌──────────────┐                          ├───┤     │
       A ───┤              │                          │   │ OR  ├─── Carry (C_out)
            │  Half Adder  ├── Sum2 ──────────────────┘   │     │
       B ───┤    (HA2)     │                                └─────┘
            └──────────────┘
            
Note: This implementation shows conceptual design using two half adders
```

### 4.5 Gate Requirements

| Implementation | XOR | AND | OR | Total Gates |
|----------------|-----|-----|-----|-------------|
| Basic Gates    | 2   | 2   | 1   | 5           |
| Two Half Adders| 3   | 2   | 1   | 6           |

### 4.6 Propagation Delay Analysis

| Path | Delay |
|------|-------|
| A/B → Sum | 2τ (through two XOR gates) |
| A/B → C_out | 1τ (through one AND gate) |
| C_in → Sum | 2τ |
| C_in → C_out | 2τ |

**Critical Path**: The delay from C_in to both S and C_out is 2τ, which impacts the maximum operating frequency of multi-bit adders.

---

## 5. Example Calculations

### Example 1: Adding Two 4-bit Numbers Using Half Adders and Full Adders

**Problem**: Add A = 1010 (decimal 10) and B = 0111 (decimal 7)

**Solution using individual bit adders**:

```
Position 3 (MSB):  A₃=1, B₃=0
Position 2:       A₂=0, B₂=1  
Position 1:       A₂=1, B₂=1
Position 0 (LSB): A₀=0, B₀=1
```

**Full Adder Chain**:

| Bit Position | A | B | C_in | Sum | C_out | Decimal |
|--------------|---|---|------|-----|-------|---------|
| 0 (LSB) | 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 | 0 + carry 1 |
| 2 | 0 | 1 | 1 | 0 | 1 | 0 + carry 1 |
| 3 (MSB) | 1 | 0 | 1 | 0 | 1 | 0 + carry 1 |
| Final | | | 1 | | | |

**Result**: Sum = 0001 (if we consider 4 bits), but actually: **10001** (17 in decimal)
- 10 + 7 = 17 ✓

### Example 2: Full Adder Verification Using Boolean Algebra

**Problem**: Verify the full adder outputs for inputs A=1, B=1, C_in=1

**Solution**:

Using Boolean expressions:
- **S = A ⊕ B ⊕ C_in = 1 ⊕ 1 ⊕ 1 = 0 ⊕ 1 = 1**
- **C_out = AB + AC_in + BC_in = (1×1) + (1×1) + (1×1) = 1 + 1 + 1 = 1**

From truth table: When A=1, B=1, C_in=1 → S=1, C_out=1 ✓

---

## 6. Implementation Examples

### 6.1 Python Implementation

```python
def half_adder(a, b):
    """
    Implements a Half Adder
    Args:
        a: First binary bit (0 or 1)
        b: Second binary bit (0 or 1)
    Returns:
        tuple: (sum, carry)
    """
    sum_bit = a ^ b  # XOR operation
    carry_bit = a & b  # AND operation
    return sum_bit, carry_bit

def full_adder(a, b, c_in):
    """
    Implements a Full Adder
    Args:
        a: First binary bit (0 or 1)
        b: Second binary bit (0 or 1)
        c_in: Carry-in bit (0 or 1)
    Returns:
        tuple: (sum, carry_out)
    """
    # First half adder
    sum1, carry1 = half_adder(a, b)
    
    # Second half adder
    sum_out, carry2 = half_adder(sum1, c_in)
    
    # Final carry out
    carry_out = carry1 | carry2  # OR operation
    
    return sum_out, carry_out

def binary_adder(num1, num2):
    """
    Adds two binary numbers using full adders
    """
    # Convert to binary strings padded to same length
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    carry = 0
    
    # Process from LSB to MSB
    for i in range(max_len - 1, -1, -1):
        a = int(num1[i])
        b = int(num2[i])
        s, carry = full_adder(a, b, carry)
        result.insert(0, str(s))
    
    if carry:
        result.insert(0, '1')
    
    return ''.join(result)

# Testing
if __name__ == "__main__":
    # Test Half Adder
    print("=== Half Adder Tests ===")
    for a in [0, 1]:
        for b in [0, 1]:
            s, c = half_adder(a, b)
            print(f"HA: {a} + {b} = Sum:{s}, Carry:{c}")
    
    # Test Full Adder
    print("\n=== Full Adder Tests ===")
    for a in [0, 1]:
        for b in [0, 1]:
            for c_in in [0, 1]:
                s, c_out = full_adder(a, b, c_in)
                print(f"FA: {a} + {b} + {c_in} = Sum:{s}, Carry:{c_out}")
    
    # Test 4-bit binary addition
    print("\n=== 4-bit Binary Addition ===")
    print(f"1010 + 0111 = {binary_adder('1010', '0111')}")  # 10 + 7 = 17
    print(f"1111 + 0001 = {binary_adder('1111', '0001')}")  # 15 + 1 = 16
```

### 6.2 Verilog HDL Implementation

```verilog
// Half Adder Module
module half_adder (
    input a,
    input b,
    output sum,
    output carry
);
    assign sum = a ^ b;    // XOR gate
    assign carry = a & b;  // AND gate
endmodule

// Full Adder Module (using two half adders)
module full_adder (
    input a,
    input b,
    input c_in,
    output sum,
    output c_out
);
    wire sum1, carry1, carry2;
    
    // First half adder
    half_adder ha1 (.a(a), .b(b), .sum(sum1), .carry(carry1));
    
    // Second half adder
    half_adder ha2 (.a(sum1), .b(c_in), .sum(sum), .carry(carry2));
    
    // OR gate for final carry
    assign c_out = carry1 | carry2;
endmodule

// 4-bit Ripple Carry Adder
module ripple_carry_adder (
    input [3:0] a,
    input [3:0] b,
    output [3:0] sum,
    output c_out
);
    wire c0, c1, c2;
    
    // Instantiate 4 full adders
    full_adder fa0 (.a(a[0]), .b(b[0]), .c_in(1'b0), .sum(sum[0]), .c_out(c0));
    full_adder fa1 (.a(a[1]), .b(b[1]), .c_in(c0),   .sum(sum[1]), .c_out(c1));
    full_adder fa2 (.a(a[2]), .b(b[2]), .c_in(c1),   .sum(sum[2]), .c_out(c2));
    full_adder fa3 (.a(a[3]), .b(b[3]), .c_in(c2),   .sum(sum[3]), .c_out(c_out));
endmodule
```

---

## 7. Multiple Choice Questions

### Level 1: Basic Understanding

**Question 1**: How many output lines does a half adder have?
- (a) 1
- (b) 2 ✓
- (c) 3
- (d) 4

**Question 2**: The SUM output of a half adder is equivalent to:
- (a) AND gate
- (b) OR gate
- (c) XOR gate ✓
- (n) NAND gate

**Question 3**: How many inputs does a full adder have?
- (a) 2
- (b) 3 ✓
- (c) 4
- (d) 8

### Level 2: Intermediate Analysis

**Question 4**: For a half adder, when will the CARRY output be 1?
- (a) When both inputs are 0
- (b) When both inputs are 1 ✓
- (c) When any one input is 1
- (d) Never

**Question 5**: The carry output of a full adder is given by:
- (a) A ⊕ B ⊕ C_in
- (b) AB + AC_in + BC_in ✓
- (c) A + B + C_in
- (d) A'B'C_in + ABC_in

**Question 6**: A full adder can be constructed using:
- (a) Two half adders and one OR gate ✓
- (b) Two half adders and one AND gate
- (c) One half adder and one OR gate
- (d) One half adder and one AND gate

### Level 3: Advanced Application

**Question 7**: The propagation delay of the SUM output in a full adder (using basic gates) is:
- (a) 1τ
- (b) 2τ ✓
- (c) 3τ
- (d) 4τ

**Question 8**: In a 4-bit ripple carry adder, the worst-case propagation delay occurs when:
- (a) Carry propagates from FA0 to FA1
- (b) Carry propagates from FA0 to FA3 ✓
- (c) Sum is computed at MSB without carry
- (d) All inputs are zero

**Question 9**: The expression C_out = AB + C_in(A ⊕ B) represents:
- (a) Half adder carry
- (b) Full adder carry ✓
- (c) Multiplexer output
- (d) Demultiplexer output

### Level 4: Critical Thinking

**Question 10**: Which of the following is NOT a characteristic of a full adder compared to a half adder?
- (a) Has three inputs
- (b) Can be cascaded for multi-bit addition
- (c) Has higher propagation delay
- (d) Cannot be implemented using half adders ✓

**Question 11**: If A=1, B=0, and C_in=1 for a full adder, the outputs are:
- (a) Sum=0, C_out=0
- (b) Sum=0, C_out=1
- (c) Sum=1, C_out=0
- (d) Sum=1, C_out=1 ✓

**Question 12**: In a 4-bit parallel adder, the number of full adders required is:
- (a) 2
- (b) 3
- (c) 4 ✓
- (d) 5

---

## 8. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **Half Adder** | A combinational circuit that adds two single-bit binary numbers |
| **Full Adder** | A combinational circuit that adds three single-bit binary numbers |
| **Sum (S)** | The result bit of binary addition |
| **Carry (C)** | The overflow bit transferred to the next significant position |
| **C_in** | Carry input to a full adder from the previous less significant bit |
| **C_out** | Carry output from a full adder to the next more significant bit |
| **Propagation Delay** | Time taken for a change in input to reflect at the output (measured in τ) |
| **Ripple Carry Adder** | Multi-bit adder constructed by cascading full adders |
| **XOR Gate** | Gate used to implement SUM output (odd function detector) |
| **AND Gate** | Gate used to implement CARRY output |

---

## 9. Key Takeaways

1. **Half Adder Basics**: Adds two 1-bit numbers, produces SUM (via XOR) and CARRY (via AND). Cannot handle carry from previous bits.

2. **Full Adder Essentials**: Adds three 1-bit numbers (A, B, C_in), produces SUM and C_out. Can be cascaded for multi-bit addition.

3. **Boolean Expressions**:
   - Half Adder: S = A ⊕ B, C = A·B
   - Full Adder: S = A ⊕ B ⊕ C_in, C_out = AB + AC_in + BC_in

4. **Circuit Implementation**: A full adder can be built using two half adders and one OR gate, demonstrating modular design principles.

5. **Timing Analysis**: Propagation delay is critical in digital systems. The SUM output has higher delay (2τ) than CARRY (1τ) in half adders, affecting multi-bit adder performance.

6. **Real-World Applications**: Adders are fundamental to ALUs, enabling all arithmetic operations in processors. Understanding adders is essential for computer architecture.

7. **Cascading**: Multiple full adders can be connected in series (ripple carry adder) to add multi-bit numbers, though this introduces cumulative propagation delay.

8. **Hardware Description Languages**: Both Python (for simulation) and Verilog (for hardware design) can model adder circuits, demonstrating their universal importance in digital systems.

---

## References

1. Morris Mano, M. (2017). *Digital Logic and Computer Design* (5th ed.). Pearson Education.
2. Floyd, T.L. (2015). *Digital Fundamentals* (11th ed.). Pearson Education.
3. Delhi University NEP 2024 UGCF BSc (Hons) Computer Science Syllabus, Unit III.
4. Verilog HDL by Samir Palnitkar (2nd ed., Pearson Education).

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*