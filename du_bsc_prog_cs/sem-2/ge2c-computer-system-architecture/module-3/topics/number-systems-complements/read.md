# Number Systems and Complements
## GE2C: Computer System Architecture
### BSc Physical Science (CS) - Delhi University, NEP 2024

---

## Table of Contents
1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Number Systems Overview](#2-number-systems-overview)
3. [Signed Number Representations](#3-signed-number-representations)
4. [Complements in Number Systems](#4-complements-in-number-systems)
5. [Subtraction Using Complements](#5-subtraction-using-complements)
6. [Overflow Detection](#6-overflow-detection)
7. [Conversions Between Bases](#7-conversions-between-bases)
8. [Binary Arithmetic Operations](#8-binary-arithmetic-operations)
9. [Practical Examples with Code](#9-practical-examples-with-code)
10. [Multiple Choice Questions](#10-multiple-choice-questions)
11. [Flashcards](#11-flashcards)
12. [Key Takeaways](#12-key-takeaways)

---

## 1. Introduction and Real-World Relevance

### What are Number System Complements?

In digital computers, arithmetic operations are performed using binary number systems. The **complement** is a fundamental concept that simplifies the implementation of arithmetic operations, particularly subtraction, within digital circuits. Instead of building complex subtractor circuits, computers use complement arithmetic to transform subtraction into addition.

### Real-World Relevance

Understanding complements is essential for:

1. **Digital Circuit Design**: ALU (Arithmetic Logic Unit) design relies heavily on complement arithmetic for efficient implementation
2. **Error Detection**: Complements are used in checksums and error-detecting codes
3. **Signed Number Representation**: All modern computers use 2's complement to represent negative numbers
4. **Cryptography**: Modular arithmetic, which uses complements, is fundamental to encryption algorithms
5. **Embedded Systems**: Understanding overflow and underflow is critical for reliable system design
6. **Networking**: IP address calculations and subnet masking use binary operations

### Delhi University Syllabus Context

This topic aligns with **Unit II: Data Representation** of the GE2C syllabus under NEP 2024, covering:
- Number systems and conversions
- Signed magnitude, 1's complement, and 2's complement representations
- Binary arithmetic operations
- Overflow detection and handling

---

## 2. Number Systems Overview

### 2.1 Types of Number Systems

| Number System | Base (Radix) | Digits Used | Example |
|--------------|--------------|-------------|---------|
| Decimal | 10 | 0-9 | 127₁₀ |
| Binary | 2 | 0,1 | 1111111₂ |
| Octal | 8 | 0-7 | 177₈ |
| Hexadecimal | 16 | 0-9, A-F | 7F₁₆ |

### 2.2 Positional Value

Each digit's value depends on its position (weight) in the number.

**Example: 127₁₀**
```
Position:    2    1    0
Weight:      10²  10¹  10⁰
Value:       100  10   1
Number:      1    2    7
Contribution: 100 + 20 + 7 = 127
```

**Example: 1011₂**
```
Position:    3    2    1    0
Weight:      2³   2²   2¹   2⁰
Value:       8    4    2    1
Number:      1    0    1    1
Contribution: 8 + 0 + 2 + 1 = 11₁₀
```

### 2.3 General Conversion Formula

Any number in base `r` can be converted to decimal using:

```
N = Σ(dᵢ × rⁱ)
```
Where `dᵢ` is the digit at position `i` and `r` is the base.

---

## 3. Signed Number Representations

When representing negative numbers in binary, we need a systematic approach. There are three primary methods:

### 3.1 Sign-Magnitude Representation

In **sign-magnitude** representation:
- The **most significant bit (MSB)** represents the sign: `0` for positive, `1` for negative
- The remaining bits represent the magnitude

**Example: Represent +7 and -7 using 8-bit sign-magnitude**

```
+7:  0 0000111  →  00000111
-7:  1 0000111  →  10000111
```

**Advantages:**
- Simple to understand
- Easy to determine sign

**Disadvantages:**
- Two representations of zero: +0 (00000000) and -0 (10000000)
- Arithmetic operations are complex
- Requires special handling

**Range (n bits)**: -(2^(n-1) - 1) to +(2^(n-1) - 1)

For 8-bit: -127 to +127 (256 possible values, but 2 for zero)

### 3.2 1's Complement Representation

In **1's complement**:
- Positive numbers are represented normally
- Negative numbers are obtained by inverting (flipping) all bits of the positive number

**Example: Represent +5 and -5 using 8-bit 1's complement**

```
+5:  00000101
-5:  Invert all bits: 11111010
```

**Example: Represent +45 and -45 using 8-bit 1's complement**

```
+45: 00101101
-45: 11010010
```

**Properties of 1's Complement:**
- Still has two zeros: +0 (00000000) and -0 (11111111)
- Range: -(2^(n-1) - 1) to +(2^(n-1) - 1)
- To perform subtraction: add the 1's complement of the subtrahend and add 1 (end-around carry)

### 3.3 2's Complement Representation

**2's complement** is the most widely used method in modern computers:

- Positive numbers are represented normally
- Negative numbers are obtained by:
  1. Taking the 1's complement (inverting all bits)
  2. Adding 1 to the result

**Example: Represent +7 and -7 using 8-bit 2's complement**

```
+7:  00000111

Step 1: 1's complement of 7 = 11111000
Step 2: Add 1:              = 11111001

-7 in 2's complement = 11111001
```

**Verification:**
```
11111001
+ 00000111
──────────
100000000
  ↑
  Discard (carry out of MSB)
──────────
00000000  ✓ Correct! (7 + (-7) = 0)
```

**Key Properties:**
- **Only one zero**: 00000000
- The complement of the complement returns to original value
- Range: -2^(n-1) to +(2^(n-1) - 1)
- For 8-bit: -128 to +127 (256 values, perfectly balanced)

**Example: Find the decimal value of 11111001 (2's complement)**

```
Step 1: MSB is 1, so it's negative
Step 2: Find 2's complement to get magnitude
        11111001 - 1 = 11111000
        Invert:     00000111 = 7
        
Result: -7
```

### 3.4 Comparison of Signed Representations

| Aspect | Sign-Magnitude | 1's Complement | 2's Complement |
|--------|---------------|----------------|----------------|
| Zero representation | Two (0, -0) | Two (0, -0) | One (0) |
| Range (8-bit) | -127 to +127 | -127 to +127 | -128 to +127 |
| Arithmetic complexity | Complex | Moderate | Simple |
| Hardware implementation | Difficult | Moderate | Easy |
| Most significant bit | Sign bit | Sign bit | Sign bit (with weight -2^(n-1)) |

---

## 4. Complements in Number Systems

### 4.1 Definition of Complements

Complements are used to simplify subtraction in digital computers. There are two types:

1. **r's Complement (Radix Complement)**
2. **(r-1)'s Complement (Diminished Radix Complement)**

Where `r` is the base (radix) of the number system.

### 4.2 (r-1)'s Complement (Diminished Radix Complement)

For a number `N` in base `r` with `n` digits:

**(r-1)'s complement of N = (rⁿ - 1) - N**

**Examples:**

**Decimal (r=10), n=2:**
```
N = 45
(10-1)'s complement = 99 - 45 = 54
```

**Binary (r=2), n=8:**
```
N = 00101101 (45)
(2-1)'s complement = 11111111 - 00101101 = 11010010
```
This is exactly the **1's complement** we discussed earlier!

**Octal (r=8), n=3:**
```
N = 127
(8-1)'s complement = 777 - 127 = 650
```

### 4.3 r's Complement (Radix Complement)

For a number `N` in base `r` with `n` digits:

**r's complement of N = (rⁿ - N)** (if N ≠ 0)
**r's complement of 0 = 0**

Alternatively, **r's complement = (r-1)'s complement + 1**

**Examples:**

**Decimal (r=10), n=2:**
```
N = 45
r's complement = 100 - 45 = 55
```
Or: (99 - 45) + 1 = 54 + 1 = 55 ✓

**Binary (r=2), n=8:**
```
N = 00101101 (45)
r's complement = 100000000 - 00101101 = 11010011
```
Or: 1's complement (11010010) + 1 = 11010011 ✓

This is exactly the **2's complement**!

**Octal (r=8), n=3:**
```
N = 127
r's complement = 1000 - 127 = 651
```
Or: 777 - 127 + 1 = 650 + 1 = 651 ✓

### 4.4 Complement Table for Common Bases

| Base (r) | (r-1)'s Complement | r's Complement |
|----------|-------------------|----------------|
| 2 (Binary) | 1's Complement | 2's Complement |
| 8 (Octal) | 7's Complement | 8's Complement |
| 10 (Decimal) | 9's Complement | 10's Complement |
| 16 (Hexadecimal) | F's Complement | 16's Complement |

---

## 5. Subtraction Using Complements

### 5.1 Why Use Complements for Subtraction?

Digital computers use complements because:
- **Simplifies hardware**: Only adders are needed, not subtractors
- **Consistent processing**: All arithmetic operations use the same circuit
- **Error reduction**: Fewer circuit components mean fewer potential failure points

### 5.2 Subtraction Using 2's Complement

**Method:**
1. Find the 2's complement of the subtrahend (number being subtracted)
2. Add it to the minuend (number being subtracted from)
3. If there's a **carry out** from the MSB, discard it (result is positive)
4. If there's **no carry**, the result is in 2's complement form (negative)

**Case 1: Larger - Smaller (Positive Result)**

Example: **45 - 23** (using 8-bit)

```
Minuend (45):    00101101
Subtrahend (23): 00010111

2's complement of 23:
  1's complement: 11101000
  Add 1:          11101001

Add to minuend:
  00101101
+ 11101001
──────────
 100010110
  ↑
  Discard carry

Result: 00010110 = 22 ✓
```

**Case 2: Smaller - Larger (Negative Result)**

Example: **23 - 45** (using 8-bit)

```
Minuend (23):    00010111
Subtrahend (45): 00101101

2's complement of 45:
  1's complement: 11010010
  Add 1:          11010011

Add to minuend:
  00010111
+ 11010011
──────────
 11101010

No carry out!

Result is in 2's complement form (negative)
Find magnitude: 2's complement of 11101010
  11101010 - 1 = 11101001
  Invert:        00010110 = 22

Answer: -22 ✓
```

### 5.3 Subtraction Using 1's Complement

**Method:**
1. Find the 1's complement of the subtrahend
2. Add it to the minuend
3. If there's a **carry out**, add it back to the result (end-around carry)
4. If there's **no carry**, find the 1's complement of the result (negative)

**Example: 45 - 23** (using 8-bit 1's complement)

```
Minuend (45):    00101101
Subtrahend (23): 00010111

1's complement of 23: 11101000

Add:
  00101101
+ 11101000
──────────
 100010101
  ↑
  Carry out

End-around carry:
  00010101
+ 1
──────────
  00010110 = 22 ✓
```

**Example: 23 - 45** (using 8-bit 1's complement)

```
Minuend (23):    00010111
Subtrahend (45): 00101101

1's complement of 45: 11010010

Add:
  00010111
+ 11010010
──────────
 11101001

No carry! Result is in 1's complement (negative)

1's complement of 11101001 = 00010110 = 22

Answer: -22 ✓
```

### 5.4 Summary: Subtraction Rules

| Condition | 2's Complement | 1's Complement |
|-----------|-----------------|-----------------|
| Carry out present | Discard carry, result is positive | Add end-around carry, result is positive |
| No carry out | Result is in 2's complement (negative) | Result is in 1's complement (negative) |

---

## 6. Overflow Detection

### 6.1 What is Overflow?

**Overflow** occurs when the result of an arithmetic operation cannot be represented in the given number of bits. It happens when:
- Adding two positive numbers gives a negative result
- Adding two negative numbers gives a positive result

### 6.2 Overflow Detection in 2's Complement

**Rule:** Overflow occurs when the **carry into the MSB** and **carry out of the MSB** are **different**.

**Example: Overflow Case (Positive + Positive = Negative)**

```
  0111 (+7)
+ 0101 (+5)
──────────
  1100 (-4) ❌ Overflow!

Carry into MSB: 1 (from adding 111)
Carry out of MSB: 0

Different? YES → Overflow!
```

```
  0111
+ 0101
─────
  1100

Step-by-step:
  1+1 = 0, carry 1
  1+0+1 = 0, carry 1  
  1+1+1 = 1, carry 1
  0+0+1 = 1, carry 0
  
Carry into MSB: 1
Carry out of MSB: 0
Different! Overflow! ✓
```

**Example: Overflow Case (Negative + Negative = Positive)**

```
  1100 (-4)
+ 1010 (-6)
──────────
  0110 (+6) ❌ Overflow!

Carry into MSB: 1
Carry out of MSB: 1

Same? NO → Overflow! (carry in ≠ carry out)
```

### 6.3 Quick Overflow Detection Rules

| Operation | Condition | Example |
|-----------|-----------|---------|
| Positive + Positive | Result MSB = 1 | 7 + 5 = -4 ❌ |
| Negative + Negative | Result MSB = 0 | -4 + -6 = +6 ❌ |
| Any subtraction | Same as addition with converted number | — |

**Note:** Overflow cannot occur when adding numbers of opposite signs!

### 6.4 Overflow in 1's Complement

In 1's complement, overflow is detected when:
- There's an end-around carry AND
- The result's sign bit differs from the operands' sign bits

---

## 7. Conversions Between Bases

### 7.1 Binary ↔ Decimal

**Binary to Decimal:**
```
101101₂ = 1×2⁵ + 0×2⁴ + 1×2³ + 1×2² + 0×2¹ + 1×2⁰
       = 32 + 0 + 8 + 4 + 0 + 1 = 45
```

**Decimal to Binary (Division-Remainder Method):**
```
45 ÷ 2 = 22 remainder 1
22 ÷ 2 = 11 remainder 0
11 ÷ 2 = 5  remainder 1
5  ÷ 2 = 2  remainder 1
2  ÷ 2 = 1  remainder 0
1  ÷ 2 = 0  remainder 1

Read remainders bottom-up: 101101 ✓
```

### 7.2 Binary ↔ Octal

**Binary to Octal:** Group 3 bits from right (add leading zeros if needed)
```
101101₂ = 101 101
         = 5   5    = 55₈ ✓
```

**Octal to Binary:** Each octal digit → 3 binary bits
```
72₈ = 7 2 = 111 010 = 111010₂ ✓
```

### 7.3 Binary ↔ Hexadecimal

**Binary to Hex:** Group 4 bits from right
```
10110101₂ = 1011 0101
           = B    5    = B5₁₆ ✓
```

**Hex to Binary:** Each hex digit → 4 binary bits
```
AF₁₆ = A F = 1010 1111 = 10101111₂ ✓
```

### 7.4 Decimal ↔ Octal

**Decimal to Octal:**
```
345 ÷ 8 = 43 remainder 1
43 ÷ 8  = 5  remainder 3
5 ÷ 8   = 0  remainder 5

Result: 531₈ ✓
```

**Octal to Decimal:**
```
531₈ = 5×8² + 3×8¹ + 1×8⁰
     = 5×64 + 3×8 + 1×1
     = 320 + 24 + 1 = 345 ✓
```

### 7.5 Quick Conversion Table

| Decimal | Binary | Octal | Hex |
|---------|--------|-------|-----|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 15 | 1111 | 17 | F |
| 16 | 10000 | 20 | 10 |
| 45 | 101101 | 55 | 2D |
| 127 | 1111111 | 177 | 7F |
| 255 | 11111111 | 377 | FF |

---

## 8. Binary Arithmetic Operations

### 8.1 Binary Addition

```
  1011    (11)
+ 0110    (6)
──────
 10001    (17)
```

### 8.2 Binary Subtraction (Direct)

```
  1011    (11)
- 0110    (6)
──────
  0101    (5)
```

### 8.3 Binary Multiplication

```
     1011    (11)
   ×  1101    (13)
   ─────────
     1011
    0000
   1011
  1011
──────────
10001111    (143)
```

### 8.4 Binary Division

```
       101
    ───────
110 ) 11110
     110
     ────
       110
       110
       ───
         0
```

---

## 9. Practical Examples with Code

### 9.1 Python Implementation of 2's Complement

```python
def to_twos_complement(n: int, bits: int) -> int:
    """Convert decimal to n-bit 2's complement"""
    if n < 0:
        raise ValueError("Number of bits must be positive")
    if n >= 0 and n < 8:
        raise ValueError("Number too large for specified bits")
    
    if n >= 0:
        return n & ((1 << bits) - 1)  # Mask to n bits
    return n

def from_twos_complement(binary: int, bits: int) -> int:
    """Convert n-bit 2's complement to decimal"""
    if binary & (1 << (bits - 1)):
        # Negative: invert and add 1, then negate
        return -((~binary + 1) & ((1 << bits) - 1))
    return binary

# Example usage
print(to_twos_complement(45, 8))      # Output: 45
print(to_twos_complement(-45, 8))     # Output: 211 (which is 11010011 in binary)
print(from_twos_complement(211, 8))   # Output: -45

# Verify subtraction
a = 45
b = 23
result = a - b
twos_a = to_twos_complement(a, 8)
twos_b = to_twos_complement(b, 8)
twos_result = (twos_a + (~twos_b + 1)) & 0xFF
print(f"45 - 23 = {from_twos_complement(twos_result, 8)}")  # Output: 22
```

### 9.2 Overflow Detection Function

```python
def detect_overflow_add(a: int, b: int, bits: int) -> bool:
    """Detect overflow when adding two n-bit signed numbers"""
    # Convert to n-bit representation
    a_masked = a & ((1 << bits) - 1)
    b_masked = b & ((1 << bits) - 1)
    
    # Perform addition
    result = a_masked + b_masked
    result_masked = result & ((1 << bits) - 1)
    
    # Check if result sign is different from operands
    a_sign = (a_masked >> (bits - 1)) & 1
    b_sign = (b_masked >> (bits - 1)) & 1
    result_sign = (result_masked >> (bits - 1)) & 1
    
    # Overflow when adding same signs gives different result sign
    if a_sign == b_sign and result_sign != a_sign:
        return True
    return False

# Test cases
print(detect_overflow_add(7, 5, 4))   # True (7+5=12 overflows in 4-bit)
print(detect_overflow_add(-4, -6, 4)) # True (-4+-6=-10 overflows)
print(detect_overflow_add(3, 4, 4))   # False (3+4=7 fits)
```

---

## 10. Multiple Choice Questions

### Level 1: Basic Knowledge

1. **In 2's complement representation, the most significant bit represents:**
   - a) The sign only
   - b) The sign and has a weight of -2^(n-1)
   - c) The magnitude
   - d) Nothing special
   
   **Answer: (b)**

2. **The 2's complement of 00001100 (12) is:**
   - a) 11110100
   - b) 11110011
   - c) 11110110
   - d) 00001100
   
   **Answer: (a)**

3. **In 8-bit representation, the range of values in 2's complement is:**
   - a) -127 to +127
   - b) -128 to +127
   - c) 0 to 255
   - d) -256 to +255
   
   **Answer: (b)**

### Level 2: Application

4. **Subtract 00101010 (42) from 01100100 (100) using 2's complement (8-bit):**
   - a) 00111010
   - b) 11000110
   - c) 10111010
   - d) 00111000
   
   **Answer: (a) 58**

5. **What is the decimal value of 11111110 in 2's complement (8-bit)?**
   - a) 254
   - b) -2
   - c) -1
   - d) -126
   
   **Answer: (b) -2**

6. **When adding +70 and +80 in 8-bit signed arithmetic:**
   - a) No overflow occurs
   - b) Overflow occurs, result is negative
   - c) Overflow occurs, result is positive
   - d) The result is zero
   
   **Answer: (b)**

### Level 3: Advanced/Analysis

7. **The 1's complement of 01100110 is:**
   - a) 10011001
   - b) 10011000
   - c) 01100111
   - d) 11100110
   
   **Answer: (a)**

8. **Subtraction using complements is preferred in digital computers because:**
   - a) It is faster than direct subtraction
   - b) It simplifies hardware by using only adders
   - c) It eliminates the need for negative numbers
   - d) It uses less memory
   
   **Answer: (b)**

9. **Convert the octal number 175 to binary:**
   - a) 1111101
   - b) 1111101
   - c) 1111101
   - d) 1111101
   
   **Answer: (b) 1111101**

10. **In sign-magnitude representation, the binary pattern 10000000 represents:**
    - a) +128
    - b) -0
    - c) -128
    - d) -0 or -128 depending on implementation
    
    **Answer: (b) -0**

### Level 4: Challenging/Comprehensive

11. **Perform subtraction using 1's complement: 10010010 - 01011001 (8-bit)**
    - a) 00110111
    - b) 11001001
    - c) 00110100
    - d) 11001011
    
    **Answer: (a) 00110111 (55)**

12. **Which of the following statements is TRUE about overflow detection in 2's complement?**
    - a) Overflow can occur when adding numbers of opposite signs
    - b) Overflow is detected when carry into MSB equals carry out of MSB
    - c) Overflow cannot be detected without looking at individual bits
    - d) Adding -128 and +127 in 8-bit causes overflow
    
    **Answer: (d)**

13. **The hexadecimal number A3F is equal to:**
    - a) 2619 in decimal
    - b) 101000111111 in binary
    - c) 12177 in octal
    - d) All of the above
    
    **Answer: (d)**

14. **In 1's complement arithmetic, after adding 01110111 and 11100000, what is the next step if there's a carry out?**
    - a) Discard the carry
    - b) Add the carry to the result
    - c) Invert all bits
    - d) The result is complete
    
    **Answer: (b)**

15. **If a computer uses 4-bit 2's complement, which of the following operations will cause overflow?**
    - a) 0110 + 0010
    - b) 1010 + 1100
    - c) 0100 + 0100
    - d) 1100 + 0011
    
    **Answer: (b) -6 + -4 = -10, but -10 cannot be represented in 4-bit**

---

## 11. Flashcards

### Flashcard 1
**Q: What is the 2's complement representation of -28 in 8 bits?**

**A:** 
1. Start with 28: 00011100
2. 1's complement: 11100011
3. Add 1: 11100100

Answer: **11100100**

---

### Flashcard 2
**Q: What is the decimal value of 10111010 in 8-bit 2's complement?**

**A:**
- MSB is 1, so it's negative
- Find magnitude: 2's complement of 10111010
- Subtract 1: 10111001
- Invert: 01000110 = 70
- Answer: **-70**

---

### Flashcard 3
**Q: Why is 2's complement preferred over 1's complement and sign-magnitude?**

**A:**
1. Single zero representation (00000000)
2. Simple hardware for addition/subtraction
3. Range extends one more on negative side (-128 to +127 for 8-bit)
4. Overflow detection is straightforward

---

### Flashcard 4
**Q: State the rule for overflow detection in 2's complement addition.**

**A:**
Overflow occurs when:
- Carry INTO the MSB ≠ Carry OUT OF the MSB

Or equivalently:
- Adding two positives gives negative result
- Adding two negatives gives positive result

---

### Flashcard 5
**Q: Convert octal 275 to decimal and hexadecimal.**

**A:**
Decimal:
275₈ = 2×8² + 7×8¹ + 5×8⁰ = 128 + 56 + 5 = **189**

Hexadecimal:
189 ÷ 16 = 11 remainder 13
= B (11) and D (13)
= **BD₁₆**

---

### Flashcard 6
**Q: Subtract 38 from 25 using 2's complement (8-bit).**

**A:**
25 - 38 = -13

2's complement of 38 (00100110):
- 1's complement: 11011001
- Add 1: 11011010

Add to 25 (00011001):
```
  00011001
+ 11011010
──────────
  11110011
```

No carry → Result is in 2's complement = -13 ✓

---

### Flashcard 7
**Q: What is the 9's complement of 456? What about 10's complement?**

**A:**
9's complement of 456 = 999 - 456 = **543**

10's complement = 9's complement + 1 = 543 + 1 = **544**

---

### Flashcard 8
**Q: How many bits are needed to represent -128 in 2's complement?**

**A:**
-128 in 2's complement = 10000000 (9 bits!)

In 8-bit: -128 cannot be represented directly in sign-magnitude or 1's complement, but CAN in 2's complement.

Actually, 8-bit 2's complement: **10000000** represents -128 ✓

---

## 12. Key Takeaways

### Core Concepts
1. **Complements** are fundamental to digital computer arithmetic, enabling subtraction through addition
2. **2's complement** is the universal standard for signed number representation in modern computers
3. Understanding **overflow detection** is crucial for writing reliable numeric code

### Signed Number Representations
| Representation | Zero | Range (8-bit) | Usage |
|---------------|------|---------------|-------|
| Sign-Magnitude | Two (+0, -0) | -127 to +127 | Rarely used |
| 1's Complement | Two (+0, -0) | -127 to +127 | Some legacy systems |
| 2's Complement | One (0) | -128 to +127 | **Universal standard** |

### Subtraction Using Complements
- **2's complement**: Add 2's complement of subtrahend; discard carry if present
- **1's complement**: Add 1's complement of subtrahend; use end-around carry

### Overflow Detection
- In 2's complement: Overflow when carry-in to MSB ≠ carry-out from MSB
- Cannot overflow when adding numbers of opposite signs

### Conversions
- Binary ↔ Octal: Group 3 bits
- Binary ↔ Hex: Group 4 bits
- Use positional weights for decimal conversions

### For Delhi University Exam
- Memorize the complement definitions and formulas
- Practice conversion problems between all bases
- Be able to perform subtraction using both 1's and 2's complement
- Understand overflow conditions thoroughly
- Know the range calculations for different bit lengths

---

*This study material is prepared for GE2C Computer System Architecture, BSc Physical Science (CS), Delhi University NEP 2024.*