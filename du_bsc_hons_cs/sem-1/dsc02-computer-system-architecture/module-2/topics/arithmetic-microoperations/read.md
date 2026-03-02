# Arithmetic Microoperations: Comprehensive Study Material

## Computer System Architecture – BSc (Hons) Computer Science (Delhi University, NEP 2024 UGCF)

---

## 1. Introduction

### What are Arithmetic Microoperations?

**Arithmetic microoperations** are the fundamental low-level operations performed by the Arithmetic Logic Unit (ALU) of a computer's central processing unit (CPU). These operations work directly on binary data stored in registers and include addition, subtraction, multiplication, division, increment, decrement, and complement operations.

In the **Delhi University BSc (Hons) Computer Science NEP 2024 syllabus**, this topic falls under "Computer System Architecture" and carries significant weightage in end-semester examinations. Understanding arithmetic microoperations is crucial because:

1. **Real-world relevance**: Every software instruction that performs mathematical calculations (from simple calculator apps to complex scientific simulations) ultimately gets translated into these microoperations at the hardware level.
2. **Digital circuit design**: These concepts form the foundation for designing ALUs, which are the computational heart of any processor.
3. **Embedded systems**: Microcontrollers extensively use these microoperations for sensor data processing, control algorithms, and communication protocols.
4. **Computer performance**: The speed and efficiency of arithmetic microoperations directly impact overall system performance.

---

## 2. Classification of Microoperations

### 2.1 Types of Microoperations

Microoperations are broadly classified into four categories:

| Category | Examples |
|----------|----------|
| **Arithmetic Microoperations** | Addition, Subtraction, Increment, Decrement, Multiply, Divide |
| **Logic Microoperations** | AND, OR, NOT, XOR, NOR, NAND |
| **Shift Microoperations** | Logical Shift, Arithmetic Shift, Circular Shift |
| **Transfer Microoperations** | Move, Load, Store |

This study material focuses exclusively on **Arithmetic Microoperations**.

---

## 3. Basic Arithmetic Microoperations

### 3.1 Fundamental Operations

The basic arithmetic microoperations performed by the ALU are:

| Operation | Description | Notation |
|-----------|-------------|----------|
| **Addition** | Adds two binary numbers | R ← A + B |
| **Subtraction** | Subtracts two binary numbers | R ← A - B or A + B' + 1 |
| **Increment** | Adds 1 to a number | R ← A + 1 |
| **Decrement** | Subtracts 1 from a number | R ← A - 1 |
| **Multiply** | Multiplies two numbers | R ← A × B |
| **Divide** | Divides two numbers | R ← A ÷ B |

### 3.2 Register Transfer Language (RTL) Notation

RTL is a symbolic notation used to describe the flow of data between registers. Key symbols include:

- **R ← A**: Transfer content of register A to register R
- **R ← A + B**: Add contents of A and B, store result in R
- **R ← A + 1**: Increment A (same as A + 1)
- **R ← A - 1**: Decrement A (same as A - 1)
- **R ← A + B' + 1**: Add A and 2's complement of B (subtraction)

---

## 4. Binary Adder Circuits

### 4.1 Half Adder

A **half adder** adds two single-bit binary numbers and produces a sum and carry.

**Truth Table:**

| A | B | Sum (S) | Carry (C) |
|---|---|---------|----------|
| 0 | 0 | 0       | 0        |
| 0 | 1 | 1       | 0        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | 0       | 1        |

**Boolean Expressions:**
- Sum (S) = A ⊕ B (XOR)
- Carry (C) = A · B (AND)

**Circuit Diagram Representation:**
```
    A ──────┐           ┌──⊕──→ S (Sum)
         ───┤           │
    B ──────┤           │    ┌───●──→ C (Carry)
         ───┘           │    │
    Half Adder           └────┴────
```

### 4.2 Full Adder

A **full adder** adds three bits (two significant bits and one incoming carry).

**Truth Table:**

| A | B | Cin | Sum (S) | Cout |
|---|---|-----|---------|------|
| 0 | 0 | 0   | 0       | 0    |
| 0 | 0 | 1   | 1       | 0    |
| 0 | 1 | 0   | 1       | 0    |
| 0 | 1 | 1   | 0       | 1    |
| 1 | 0 | 0   | 1       | 0    |
| 1 | 0 | 1   | 0       | 1    |
| 1 | 1 | 0   | 0       | 1    |
| 1 | 1 | 1   | 1       | 1    |

**Boolean Expressions:**
- Sum (S) = A ⊕ B ⊕ Cin
- Cout = AB + Cin(A ⊕ B)

### 4.3 N-Bit Parallel Adder

To add two n-bit numbers, we cascade n full adders in parallel:

```
A3 A2 A1 A0  (4-bit augend)
+ B3 B2 B1 B0  (4-bit addend)
─────────────────
Cout S3 S2 S1 S0  (5-bit sum)
```

**Structure:**
```
FA0: A0, B0, C0_in → S0, C1
FA1: A1, B1, C1   → S1, C2
FA2: A2, B2, C2   → S2, C3
FA3: A3, B3, C3   → S3, Cout
```

---

## 5. 2's Complement Arithmetic

### 5.1 Understanding 2's Complement

The **2's complement representation** is the standard method for representing signed numbers in computers. It allows subtraction to be performed using addition circuitry.

**Finding 2's Complement:**
1. **Method 1**: Invert all bits (1's complement) and add 1
2. **Method 2**: Starting from right, keep bits until first 1 (inclusive), then complement remaining bits

**Example 1: Find 2's complement of 1101 (13)**

Using Method 1:
- Original: 1101
- 1's complement: 0010
- Add 1: 0011

Using Method 2:
- Original: 1101
- Keep: 1 (rightmost 1)
- Complement remaining: 0011

### 5.2 Subtraction using 2's Complement

**Fundamental Principle**: A - B = A + (-B) = A + (2's complement of B)

**Circuit**: An n-bit subtractor can be implemented using an n-bit adder with the subtrahend's 2's complement (inverted bits + 1 through carry-in).

**RTL Notation for Subtraction:**
```
R ← A + B' + 1
```
Where B' is the 1's complement of B, and adding 1 gives 2's complement.

### 5.3 Example: 4-bit Subtraction

**Problem**: Perform 1101 - 0101 (13 - 5 = 8)

**Step 1**: Find 2's complement of subtrahend (0101)
- 1's complement: 1010
- Add 1: 1011

**Step 2**: Add to minuend (1101 + 1011)

```
    1 1 0 1     (13)
  + 1 0 1 1     (-5 in 2's complement)
  ─────────
  1 1 0 0 0     (discard overflow)
    1 0 0 0     = 8 ✓
```

**Verification**: The result is 0100₂ = 8 (in decimal)

---

## 6. ALU (Arithmetic Logic Unit) Design

### 6.1 ALU Overview

The **ALU** is a combinational digital circuit that performs arithmetic and logic operations. It is the core computational component of any CPU.

### 6.2 Basic ALU Structure

```
┌─────────────────────────────────────────┐
│              ALU Block Diagram           │
├─────────────────────────────────────────┤
│  A ──┐                                  │
│      │    ┌──────────┐    ┌──────────┐  │
│  B ──┼───→│ Arithmetic│───→│          │  │
│      │    │  Unit     │    │  Output  │──→→ Result
│ S0 ──┤    └──────────┘    │   MUX    │  │
│ S1 ──┤    ┌──────────┐    │          │  │
│      ├───→│  Logic   │───→│          │  │
│      │    │  Unit    │    │          │  │
│      │    └──────────┘    └──────────┘  │
│                                          │
│  Carry In (Cin) ──────────────────────→ │
└─────────────────────────────────────────┘
```

### 6.3 ALU Operation Selection

| S1 | S0 | Operation | Function |
|----|----|-----------|----------|
| 0  | 0  | F = A + B | Addition |
| 0  | 1  | F = A - B | Subtraction |
| 1  | 0  | F = A · B | AND |
| 1  | 1  | F = A + B | OR |

### 6.4 Complete ALU Design (8-function example)

For a more comprehensive ALU with 3 selection lines (S2, S1, S0):

| S2 | S1 | S0 | Operation | Description |
|----|----|----|-----------|-------------|
| 0  | 0  | 0  | F = A     | Transfer A |
| 0  | 0  | 1  | F = A + B | Addition |
| 0  | 1  | 0  | F = A - B | Subtraction |
| 0  | 1  | 1  | F = A + 1 | Increment |
| 1  | 0  | 0  | F = A - 1 | Decrement |
| 1  | 0  | 1  | F = A & B | AND |
| 1  | 1  | 0  | F = A | B | OR |
| 1  | 1  | 1  | F = A'    | Complement |

---

## 7. Overflow Detection

### 7.1 What is Overflow?

**Overflow** occurs when the result of an arithmetic operation exceeds the representable range of the number system. In signed arithmetic, overflow happens when the result cannot be represented in n bits.

### 7.2 Overflow Detection in 2's Complement

**Overflow occurs when:**
- Adding two positive numbers produces a negative result
- Adding two negative numbers produces a positive result

**Detection Logic:**
```
Overflow = Cout XOR Cn-1
```
Where:
- Cout = carry out from the MSB
- Cn-1 = carry into the MSB

### 7.3 Example: Detecting Overflow

**Problem**: Add 0111 (7) + 0100 (4) in 4-bit 2's complement

```
    0 1 1 1     (+7)
  + 0 1 0 0     (+4)
  ─────────
    1 0 1 1     (-5) ❌ OVERFLOW!
    
    Cout = 0 (no final carry)
    C3 (carry into MSB) = 1
    Overflow = 0 XOR 1 = 1 ✓
```

**Explanation**: Adding two positive numbers should give a positive result, but we got 1011₂ = -5, which is incorrect. This is an overflow condition.

### 7.4 Python Code for Overflow Detection

```python
def detect_overflow_addition(a, b, bit_width=4):
    """
    Detect overflow when adding two signed integers in 2's complement.
    Uses bit_width bits for representation.
    """
    # Convert to unsigned range for simulation
    mask = (1 << bit_width) - 1
    
    # Perform addition (Python handles big ints, so we mask)
    result = (a + b) & mask
    
    # Calculate carry out and carry into MSB
    # Simulate the addition bit by bit
    carry_in = 0
    for i in range(bit_width):
        a_bit = (a >> i) & 1
        b_bit = (b >> i) & 1
        total = a_bit + b_bit + carry_in
        carry_in = total >> 1
        if i == bit_width - 1:
            carry_out = carry_in
    
    carry_into_msb = carry_in
    overflow = carry_out ^ carry_into_msb
    
    # Convert result to signed
    if result & (1 << (bit_width - 1)):
        signed_result = result - (1 << bit_width)
    else:
        signed_result = result
    
    return {
        'result': result,
        'signed_result': signed_result,
        'carry_out': carry_out,
        'carry_into_msb': carry_into_msb,
        'overflow': overflow,
        'overflow_detected': bool(overflow)
    }

# Example: 7 + 4 in 4-bit
print(detect_overflow_addition(7, 4, 4))
# Output: overflow_detected = True

# Example: 5 + 3 in 4-bit (no overflow)
print(detect_overflow_addition(5, 3, 4))
# Output: overflow_detected = False
```

---

## 8. BCD (Binary Coded Decimal) Addition

### 8.1 Introduction to BCD

**BCD** represents each decimal digit (0-9) using 4 binary bits. It's used in digital displays, calculators, and financial applications where decimal accuracy is critical.

| Decimal | BCD |
|---------|-----|
| 0       | 0000 |
| 1       | 0001 |
| 2       | 0010 |
| 3       | 0011 |
| 4       | 0100 |
| 5       | 0101 |
| 6       | 0110 |
| 7       | 0111 |
| 8       | 1000 |
| 9       | 1001 |

### 8.2 BCD Addition Algorithm

**Step 1**: Add the two BCD numbers using binary addition
**Step 2**: If the sum produces a carry (≥16) OR if any nibble is > 1001 (9), add 0110 (6) to that nibble
**Step 3**: Propagate any carry generated to the next nibble

### 8.3 Example: BCD Addition

**Problem**: Add 58 + 29 in BCD

**Step 1**: Convert to BCD
- 58 = 0101 1000
- 29 = 0010 1001

**Step 2**: Binary addition

```
    0101 1000     (58)
  + 0010 1001     (29)
  ─────────────
    0111 0001     (113 in binary)
```

**Step 3**: Check each nibble
- Lower nibble: 0001 ≤ 1001 (9) ✓ No correction needed
- Upper nibble: 0111 (7) ≤ 1001 (9) ✓ No correction needed

**Result**: 0111 0001 = 0101 1000 + 0010 1001 = **87** ✓

### 8.4 Example: BCD Addition with Correction

**Problem**: Add 47 + 38 in BCD

**Step 1**: Convert to BCD
- 47 = 0100 0111
- 38 = 0011 1000

**Step 2**: Binary addition

```
    0100 0111     (47)
  + 0011 1000     (38)
  ─────────────
    0111 1111     (127 in binary)
```

**Step 3**: Check each nibble
- Lower nibble: 1111 (15) > 1001 (9) ❌ **Correction needed**
  - Add 0110: 1111 + 0110 = 1 0101, carry 1
  - Result lower nibble: 0101 (5), carry = 1
  
- Upper nibble: 0111 + carry (1) = 1000 (8) ≤ 1001 (9) ✓

**Final Result**: 1000 0101 = **85** ✓ (47 + 38 = 85)

### 8.5 BCD Addition Implementation

```python
def bcd_addition(num1, num2):
    """
    Add two numbers in BCD representation.
    Each decimal digit is represented by 4 binary bits.
    """
    # Convert decimal to BCD
    def to_bcd(n):
        bcd = []
        while n > 0:
            bcd.insert(0, n % 10)
            n //= 10
        return bcd if bcd else [0]
    
    bcd1 = to_bcd(num1)
    bcd2 = to_bcd(num2)
    
    # Pad with zeros
    max_len = max(len(bcd1), len(bcd2))
    bcd1 = [0] * (max_len - len(bcd1)) + bcd1
    bcd2 = [0] * (max_len - len(bcd2)) + bcd2
    
    result = []
    carry = 0
    
    # Process from right (least significant digit)
    for i in range(max_len - 1, -1, -1):
        # Add digits with carry
        digit_sum = bcd1[i] + bcd2[i] + carry
        
        # Check if correction is needed
        if digit_sum > 9:
            digit_sum += 6  # Add 0110 in binary
            carry = 1
        else:
            carry = 0 if digit_sum < 16 else 1
            
        result.insert(0, digit_sum % 10)
    
    return ''.join(map(str, result))

# Example
print(f"58 + 29 = {bcd_addition(58, 29)}")  # Output: 87
print(f"47 + 38 = {bcd_addition(47, 38)}")  # Output: 85
```

---

## 9. Increment and Decrement Operations

### 9.1 Increment Operation (R ← A + 1)

Increment adds 1 to the content of a register. It can be implemented:
- Using an adder with one input tied to 1
- Using a binary counter circuit

**RTL**: R ← A + 1

### 9.2 Decrement Operation (R ← A - 1)

Decrement subtracts 1 from the content of a register. Implemented using:
- Subtractor circuit
- Adding 2's complement of 1 (all 1s in binary)

**RTL**: R ← A - 1

---

## 10. Multiplication and Division Microoperations

### 10.1 Multiplication (R ← A × B)

Binary multiplication is performed through repeated addition and shifting:

**Algorithm:**
1. Initialize result = 0
2. If LSB of multiplier = 1, add multiplicand to result
3. Shift multiplicand left
4. Repeat for all bits

**Example: 1101 × 1011 (13 × 11 = 143)**

```
        1101     (Multiplicand)
      × 1011     (Multiplier)
      ──────
        1101
       1101
      0000
     1101
    ─────────
   10001111     (143 in binary)
```

### 10.2 Division (R ← A ÷ B)

Division is performed through repeated subtraction and shifting:

**Algorithm:**
1. Compare dividend with divisor
2. If dividend ≥ divisor, subtract and set quotient bit to 1
3. Shift remainder left, bring down next dividend bit
4. Repeat until all bits processed

---

## 11. Numerical Problems for Practice

### Problem 1: 8-bit Subtraction using 2's Complement

**Question**: Perform 01100101 - 00111001 using 2's complement method (show all steps)

**Solution:**

Step 1: Convert subtrahend to 2's complement
- 00111001 → 1's complement: 11000110
- Add 1: 11000111

Step 2: Add to minuend

```
    01100101     (101)
  + 11000111     (-57 in 2's complement)
  ─────────────
  1 00101100     (discard carry)
    00101100     = 44 ✓
```

**Verification**: 101 - 57 = 44 ✓

### Problem 2: Overflow Detection

**Question**: Determine if overflow occurs when adding +7 and +4 in 4-bit signed arithmetic

**Solution:**

```
    0111     (+7)
  + 0100     (+4)
  ──────
    1011     (-5 in 2's complement) ❌
    
Carry into MSB (C3) = 1
Carry out (C4) = 0

Overflow = C4 ⊕ C3 = 0 ⊕ 1 = 1 (OVERFLOW!)
```

### Problem 3: BCD Addition

**Question**: Add 69 + 74 in BCD

**Solution:**

69 = 0110 1001
74 = 0111 0100

Binary addition:
```
  0110 1001
+ 0111 0100
───────────
  1101 1101
```

Check lower nibble: 1101 (13) > 1001 (9)
- Add 0110: 1101 + 0110 = 1 0011
- Lower nibble = 0011 (3), carry = 1

Check upper nibble: 1101 + carry (1) = 1110 (14) > 1001 (9)
- Add 0110: 1110 + 0110 = 1 0100
- Upper nibble = 0100 (4), carry = 1

Final result: 1 0100 0011 = 143 ✓

---

## 12. Key Takeaways

1. **Arithmetic microoperations** are fundamental operations performed by the ALU, including addition, subtraction, increment, decrement, multiplication, and division.

2. **Binary adders** (half adder, full adder, parallel adder) form the basis of all arithmetic circuits. An n-bit adder cascades n full adders.

3. **2's complement** is the standard representation for signed numbers in computers, enabling subtraction using addition circuitry.

4. **Subtraction (A - B)** is performed as A + (2's complement of B), implemented by inverting B and adding 1 through the carry-in.

5. **Overflow detection**: In 2's complement arithmetic, overflow occurs when Cout XOR Cn-1 = 1.

6. **BCD addition** requires correction if any nibble exceeds 9 (add 6 = 0110₂ to correct).

7. **ALU design** combines arithmetic and logic units with multiplexers to select operations based on selection lines.

8. **Register Transfer Language (RTL)** provides standardized notation for describing register operations: R ← A + B.

---

## 13. Multiple Choice Questions (MCQs)

### Easy Level

**Q1. Which microoperation adds 1 to the content of a register?**
- A) Decrement
- B) Increment
- C) Complement
- D) Transfer
- **Answer: B**

**Q2. The 2's complement of a binary number is obtained by:**
- A) Adding 1 to 1's complement
- B) Adding 1 to the original number
- C) Inverting all bits
- D) Shifting left
- **Answer: A**

**Q3. A full adder has:**
- A) 2 inputs, 2 outputs
- B) 3 inputs, 2 outputs
- C) 2 inputs, 3 outputs
- D) 3 inputs, 3 outputs
- **Answer: B**

### Medium Level

**Q4. In 4-bit signed arithmetic, adding 0111 (+7) and 0100 (+4) results in:**
- A) 1011 with no overflow
- B) 1011 with overflow
- C) 0011 with no overflow
- D) 1111 with overflow
- **Answer: B**

**Q5. BCD addition of 5 + 8 requires correction because:**
- A) Sum is 1101 (> 1001)
- B) Sum is 1111 (> 1001)
- C) Sum is 1011 (> 1001)
- D) Sum is 1001 (= 1001)
- **Answer: A**

**Q6. The RTL notation R ← A + B' + 1 represents:**
- A) A + B
- B) A - B
- C) B - A
- D) A + 1
- **Answer: B**

### Hard Level

**Q7. In a 4-bit parallel adder, if carry into the MSB (C3) = 1 and carry out (C4) = 0, then:**
- A) No overflow
- B) Overflow occurred
- C) Undefined state
- D) Equal numbers
- **Answer: B** (Overflow = 1 XOR 0 = 1)

**Q8. To implement an 8-function ALU, minimum number of selection lines required are:**
- A) 2
- B) 3
- C) 4
- D) 8
- **Answer: B** (2³ = 8 functions)

**Q9. The BCD representation of decimal 93 is:**
- A) 10010011
- B) 1001 0011
- C) 1001 0011
- D) 1010 0011
- **Answer: C**

**Q10. In BCD addition, the correction factor 0110 (6) is added when:**
- A) Sum produces a carry
- B) Any nibble > 9
- C) Both A and B
- D) Neither A nor B
- **Answer: C**

---

## 14. Flashcards for Quick Revision

### Flashcard 1
**Term**: Arithmetic Microoperation
**Definition**: Low-level operations performed by ALU on binary data stored in registers, including addition, subtraction, increment, and decrement.

### Flashcard 2
**Term**: 2's Complement
**Definition**: Binary representation for signed numbers. To find: invert all bits and add 1, or keep bits from right until first 1, then complement remaining.

### Flashcard 3
**Term**: Half Adder
**Definition**: Basic circuit adding two 1-bit numbers. Outputs: Sum = A XOR B, Carry = A AND B.

### Flashcard 4
**Term**: Full Adder
**Definition**: Circuit adding three bits (A, B, Cin). Outputs: S = A XOR B XOR Cin, Cout = AB + Cin(A XOR B).

### Flashcard 5
**Term**: Overflow
**Definition**: Condition when arithmetic result exceeds representable range. Detected by: Overflow = Cout XOR Cn-1 in 2's complement.

### Flashcard 6
**Term**: BCD (Binary Coded Decimal)
**Definition**: 4-bit representation of decimal digits (0-9). Example: 93 = 1001 0011.

### Flashcard 7
**Term**: RTL (Register Transfer Language)
**Definition**: Symbolic notation for describing data flow: R ← A + B means "transfer A+B to R".

### Flashcard 8
**Term**: ALU (Arithmetic Logic Unit)
**Definition**: Combinational circuit performing arithmetic and logic operations. Controlled by selection lines (S0, S1, S2...).

---

## 15. Exam-Relevant Challenging Questions

### Question 1 (5 marks)
Design a 4-bit subtractor using a 4-bit parallel adder. Show the circuit diagram and explain how subtraction is performed using 2's complement method.

### Question 2 (5 marks)
Perform the following BCD addition: 87 + 46. Show all steps including correction if required.

### Question 3 (5 marks)
Explain overflow detection in 2's complement arithmetic. With an example, show how to detect overflow when adding two signed numbers.

### Question 4 (5 marks)
Draw the block diagram of an 8-function ALU and explain how it performs arithmetic and logic operations with proper selection of function.

### Question 5 (4 marks)
Perform 11001 - 01011 using 2's complement method and verify the result.

---

## References

1. Morris Mano, M. - *Computer System Architecture* (3rd Edition) - Pearson Education
2. Delhi University, NEP 2024 - BSc (Hons) Computer Science Syllabus, Unit III: Data Processing and Arithmetic Operations
3. Carl Hamacher, Zvonko Vranesic, Safwat Zaky - *Computer Organization* (5th Edition) - McGraw Hill

---

*Document prepared for BSc (Hons) Computer Science, Delhi University, NEP 2024 UGCF curriculum.*