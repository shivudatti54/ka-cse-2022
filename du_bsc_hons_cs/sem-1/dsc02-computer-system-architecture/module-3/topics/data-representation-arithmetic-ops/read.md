# Data Representation and Arithmetic Operations

## Comprehensive Study Material for Computer System Architecture

---

## 1. Introduction

Data representation and arithmetic operations form the foundation of how computers process information at the most fundamental level. Every piece of data—from simple text documents to complex graphical images—must be stored and manipulated in binary form (0s and 1s) within a computer system. Understanding how computers perform arithmetic operations on this binary data is crucial for any computer science student.

This topic is a core component of the **Computer System Architecture** course under the BSc (Hons) Computer Science program at Delhi University (NEP 2024 UGCF). The study of data representation helps us understand the limitations and capabilities of computer arithmetic, including issues like overflow, precision, and the representation of negative numbers. These concepts are essential for debugging programs, optimizing algorithms, and understanding hardware design.

In real-world applications, these concepts are vital in areas such as:
- **Embedded systems programming** where precise integer arithmetic is critical
- **Scientific computing** requiring floating-point precision
- **Cryptography** where bit-level operations are fundamental
- **Digital signal processing** using fixed-point arithmetic

---

## 2. Number Systems and Conversions

### 2.1 Overview of Number Systems

Computers fundamentally work with binary numbers (base-2), but we commonly encounter several number systems:

| Number System | Base | Digits Used | Example |
|---------------|------|-------------|---------|
| Binary | 2 | 0, 1 | 10110₂ |
| Octal | 8 | 0-7 | 26₈ |
| Decimal | 10 | 0-9 | 22₁₀ |
| Hexadecimal | 16 | 0-9, A-F | 16₁₆ |

### 2.2 Conversion Examples

**Example 1: Binary to Decimal Conversion**

Convert 110101₂ to decimal:

```
1×2⁵ + 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
= 32 + 16 + 0 + 4 + 0 + 1
= 53₁₀
```

**Example 2: Decimal to Binary Conversion**

Convert 47₁₀ to binary:

```
47 ÷ 2 = 23 remainder 1
23 ÷ 2 = 11 remainder 1
11 ÷ 2 = 5  remainder 1
5 ÷ 2  = 2  remainder 1
2 ÷ 2  = 1  remainder 0
1 ÷ 2  = 0  remainder 1

Reading remainders from bottom to top: 101111₂
```

**Example 3: Hexadecimal to Binary Conversion**

Convert A3F₁₆ to binary:

```
A = 1010, 3 = 0011, F = 1111
Result: 101000111111₂
```

---

## 3. Signed Number Representations

Computers must represent both positive and negative integers. There are three primary methods:

### 3.1 Sign-Magnitude Representation

In sign-magnitude, the most significant bit (MSB) represents the sign (0 for positive, 1 for negative), and the remaining bits represent the magnitude.

**Example: 8-bit sign-magnitude**
- +25 = 00011001₂
- -25 = 10011001₂

**Limitations:**
- Two representations for zero: +0 (00000000) and -0 (10000000)
- Arithmetic operations are complex

### 3.2 1's Complement Representation

The 1's complement of a binary number is obtained by inverting all bits (0 becomes 1, 1 becomes 0).

**Example: 8-bit 1's complement**
- +25 = 00011001₂
- -25 = 11100110₂ (complement of 00011001)

**Limitations:**
- Still has two representations for zero
- Addition requires end-around carry

### 3.3 2's Complement Representation (Most Common)

The 2's complement is the standard for modern computers. It's obtained by:
1. Finding the 1's complement
2. Adding 1 to the result

**Example: Represent -25 in 8-bit 2's complement**

```
+25 = 00011001
1's complement = 11100110
Add 1 = 11100111

Therefore, -25 = 11100111₂
```

**Verification:**
```
11100111
+ 00011001
-----------
100000000 (9 bits)
Discard overflow bit: 00000000 = 0 ✓
```

---

## 4. Binary Arithmetic Operations

### 4.1 Binary Addition

Binary addition follows simple rules:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Example: Add 11011₂ (27) and 10101₂ (21)**

```
    11011
  + 10101
  -------
   110000 (48)
```

### 4.2 Binary Subtraction

Subtraction can be performed using 2's complement (adding the negative):

**Example: Subtract 0101₂ (5) from 1100₂ (12)**

Using 2's complement method:
```
    1100
  - 0101
  
  = 1100 + (2's complement of 0101)
  = 1100 + 1011
  = 10111
  
  Discard overflow: 0111 (7) ✓
```

### 4.3 Binary Multiplication

**Example: Multiply 1011₂ (11) by 110₁ (6)**

```
        1011
      ×  110
      ------
        0000
       1011
      1011
     0000
    --------
    1000010 (66)
```

### 4.4 Binary Division

**Example: Divide 10010₂ (18) by 100₂ (4)**

```
10010 ÷ 100 = 100 remainder 10
- Quotient: 100₂ (4)
- Remainder: 010₂ (2)
```

---

## 5. Overflow and Underflow

### 5.1 Integer Overflow

Overflow occurs when the result of an arithmetic operation exceeds the range representable by the available bits.

**Example: 4-bit signed arithmetic**

Range: -8 to +7

```
  0111 (7)
+ 0001 (1)
------
  1000 (-8) ← OVERFLOW!
```

**Overflow Detection Rules (for signed arithmetic):**
1. Positive + Positive = Negative → Overflow
2. Negative + Negative = Positive → Overflow

### 5.2 Floating-Point Underflow

When a floating-point number becomes too small (close to zero) to be represented, it underflows to zero or a denormalized number.

### 5.3 Code Example: Overflow Detection in C

```c
#include <stdio.h>
#include <stdint.h>

int check_overflow_add(int a, int b) {
    // Using signed integer overflow detection
    if (a > 0 && b > 0 && a > __INT_MAX__ - b) {
        return 1; // Overflow would occur
    }
    if (a < 0 && b < 0 && a < __INT_MIN__ - b) {
        return 1; // Underflow would occur
    }
    return 0;
}

int main() {
    int x = 2147483647;
    int y = 1;
    
    if (check_overflow_add(x, y)) {
        printf("Overflow detected!\n");
    } else {
        printf("Result: %d\n", x + y);
    }
    return 0;
}
```

---

## 6. Complement Arithmetic

### 6.1 1's Complement

Used in some older computer systems. To subtract using 1's complement:

**Example: 1011 - 0101 using 1's complement**

```
  1011
- 0101
= 1011 + (1's complement of 0101) + 1 (end-around carry)
= 1011 + 1010 + 1
= 10110
End-around carry: 1 + 0110 = 0111
```

### 6.2 2's Complement

The standard method for modern computers, as discussed in Section 3.3.

---

## 7. Floating-Point Representation

### 7.1 IEEE 754 Standard

The IEEE 754 standard defines floating-point representation:

```
┌────────┬──────────────┬────────────────────┐
│  1 bit │   8 bits     │    23 bits         │
│ Sign   │ Exponent     │    Mantissa        │
└────────┴──────────────┴────────────────────┘
        (Single Precision)
```

### 7.2 Normalization

Normalized floating-point numbers have the form: **1.M × 2^E**

Where:
- M (Mantissa/Fraction) is the fractional part after the binary point
- E is the biased exponent

**Example: Normalize 0.00101₂**

```
0.00101₂ = 1.01₂ × 2⁻³
- Sign bit: 0 (positive)
- Exponent: -3 + 127 (bias) = 124 = 01111100₂
- Mantissa: 010000... (1.01 without the leading 1)
```

### 7.3 Special Values

| Value | Exponent | Mantissa |
|-------|----------|----------|
| +0 | 00000000 | 000...0 |
| -0 | 10000000 | 000...0 |
| +∞ | 11111111 | 000...0 |
| -∞ | 11111111 | 000...0 |
| NaN | 11111111 | non-zero |
| Denormals | 00000000 | non-zero |

### 7.4 Floating-Point Arithmetic Example

**Example: Add 1.5 × 10³ and 2.0 × 10²**

```
1.5 × 10³ = 1500
2.0 × 10² = 200
-----------
1700 = 1.7 × 10³
```

**Code Example: Floating-Point Representation in Python**

```python
import struct

def float_to_ieee754(value):
    # Convert float to 32-bit IEEE 754 representation
    packed = struct.pack('f', value)
    binary = ''.join(f'{byte:08b}' for byte in packed)
    return binary

def ieee754_to_float(binary):
    # Convert 32-bit IEEE 754 to float
    packed = bytes(int(binary[i:i+8], 2) for i in range(0, 32, 8))
    return struct.unpack('f', packed)[0]

# Example usage
value = -5.75
ieee754_repr = float_to_ieee754(value)
print(f"Value: {value}")
print(f"IEEE 754 Binary: {ieee754_repr}")
print(f"Sign: {ieee754_repr[0]}")
print(f"Exponent: {ieee754_repr[1:9]} ({int(ieee754_repr[1:9], 2)})")
print(f"Mantissa: {ieee754_repr[9:]}")

# Verify conversion back
recovered = ieee754_to_float(ieee754_repr)
print(f"Recovered value: {recovered}")
```

**Output:**
```
Value: -5.75
IEEE 754 Binary: 11000000111000000000000000000000
Sign: 1
Exponent: 10000001 (129)
Mantissa: 11000000000000000000000
Recovered value: -5.75
```

---

## 8. Endianness

Endianness refers to the byte order used to represent multi-byte data types.

### 8.1 Big-Endian

Most significant byte stored at the lowest address.

**Example: 0x12345678 in Big-Endian**
```
Address:  0    1    2    3
Data:    0x12 0x34 0x56 0x78
```

### 8.2 Little-Endian

Least significant byte stored at the lowest address.

**Example: 0x12345678 in Little-Endian**
```
Address:  0    1    2    3
Data:    0x78 0x56 0x34 0x12
```

### 8.3 Code Example: Detecting Endianness in C

```c
#include <stdio.h>

int main() {
    unsigned int num = 0x12345678;
    unsigned char *ptr = (unsigned char *)&num;
    
    printf("Checking endianness:\n");
    printf("First byte: 0x%02x\n", ptr[0]);
    
    if (ptr[0] == 0x78) {
        printf("System is Little-Endian\n");
    } else {
        printf("System is Big-Endian\n");
    }
    
    return 0;
}
```

---

## 9. Binary-Coded Decimal (BCD)

BCD represents each decimal digit with its 4-bit binary equivalent.

### 9.1 BCD Encoding

| Decimal | BCD |
|---------|-----|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

**Example: Encode 93 in BCD**

```
9 = 1001
3 = 0011
Result: 10010011₂
```

### 9.2 Packed BCD

Packed BCD stores two digits per byte.

**Example: 93 in packed BCD**

```
1001 0011 = 0x93
```

### 9.3 Code Example: BCD Conversion

```python
def decimal_to_bcd(decimal_num):
    """Convert decimal number to BCD representation"""
    bcd = ""
    for digit in str(decimal_num):
        bcd += format(int(digit), '04b')
    return bcd

def bcd_to_decimal(bcd_str):
    """Convert BCD string to decimal number"""
    decimal = ""
    for i in range(0, len(bcd_str), 4):
        decimal += str(int(bcd_str[i:i+4], 2))
    return int(decimal)

# Example usage
number = 93
bcd_representation = decimal_to_bcd(number)
print(f"Decimal {number} in BCD: {bcd_representation}")
print(f"Binary: {int(bcd_representation, 2):08x}H")

# Convert back
recovered = bcd_to_decimal(bcd_representation)
print(f"Recovered decimal: {recovered}")
```

**Output:**
```
Decimal 93 in BCD: 10010011
Binary: 00000093H
Recovered decimal: 93
```

---

## 10. Key Takeaways

1. **Number Systems**: Computers use binary (base-2), with conversions to decimal, octal, and hexadecimal being essential skills.

2. **Signed Number Representations**: 2's complement is the standard for representing negative numbers, offering a single representation for zero and simplified arithmetic operations.

3. **Binary Arithmetic**: Addition, subtraction, multiplication, and division follow systematic rules at the bit level.

4. **Overflow**: Integer overflow occurs when results exceed representable ranges; floating-point underflow occurs when values become too small.

5. **Floating-Point (IEEE 754)**: The standard defines normalization, special values (infinity, NaN, denormals), and ensures portability across systems.

6. **Endianness**: Big-endian and little-endian byte ordering affects how multi-byte data is interpreted, important for cross-platform programming.

7. **BCD**: Used in financial applications where exact decimal representation is crucial, avoiding binary floating-point rounding errors.

8. **Practical Applications**: These concepts are fundamental to compiler design, embedded systems, scientific computing, and system programming.

---

## 11. Numerical Problems and Conversion Exercises

### Exercise 1: Number System Conversions
- Convert 101110₂ to decimal
- Convert 89₁₀ to binary
- Convert 2A3₁₆ to decimal
- Convert 173₁₀ to hexadecimal

### Exercise 2: 2's Complement
- Represent -42 in 8-bit 2's complement
- Perform binary subtraction: 01001 - 00110 using 2's complement

### Exercise 3: Floating-Point
- Represent 6.5 in IEEE 754 single precision
- Determine the decimal value of: 0 10000010 10100000000000000000000

### Exercise 4: BCD
- Encode the decimal number 59 in BCD
- Decode BCD 01101001 to decimal

### Exercise 5: Endianness
- If 0xDEADBEEF is stored at address 1000 in a little-endian system, what bytes are at addresses 1000, 1001, 1002, and 1003?

---

## 12. Multiple Choice Questions

1. **What is the decimal value of 110101₂?**
   - (a) 53 ✓
   - (b) 52
   - (c) 54
   - (d) 51

2. **In 2's complement representation, the range for 8-bit signed integers is:**
   - (a) -127 to +127
   - (b) -128 to +127 ✓
   - (c) -256 to +255
   - (d) 0 to 255

3. **What is the 2's complement representation of -15 in 8 bits?**
   - (a) 11110001 ✓
   - (b) 00001111
   - (c) 11110000
   - (d) 10001111

4. **In IEEE 754 single precision, the exponent bias is:**
   - (a) 126
   - (b) 127 ✓
   - (c) 128
   - (d) 255

5. **Which representation has two zeros (+0 and -0)?**
   - (a) 2's complement
   - (b) Sign-magnitude ✓
   - (c) Both (a) and (b)
   - (d) None

6. **In big-endian storage, the most significant byte is stored at:**
   - (a) Lowest address ✓
   - (b) Highest address
   - (c) Middle address
   - (d) Any address

7. **BCD encodes each decimal digit using:**
   - (a) 2 bits
   - (b) 4 bits ✓
   - (c) 8 bits
   - (d) 16 bits

8. **What does the exponent field contain in a denormalized floating-point number?**
   - (a) All zeros ✓
   - (b) All ones
   - (c) Value of 1
   - (d) Cannot be determined

9. **Overflow in signed arithmetic occurs when:**
   - (a) Adding two positive numbers gives negative
   - (b) Adding two negative numbers gives positive
   - (c) Both (a) and (b) ✓
   - (d) None of the above

10. **The mantissa in normalized binary floating-point is always:**
    - (a) 0.xxxx
    - (b) 1.xxxx ✓
    - (c) Any value
    - (d) Greater than 2

11. **What is 01111111₂ + 00000001₂ in 8-bit signed arithmetic?**
    - (a) 10000000 ✓
    - (b) 01111111
    - (c) 10000001
    - (d) Overflow

12. **In which endianness is 0x1234 stored as 34 12?**
    - (a) Big-endian
    - (b) Little-endian ✓
    - (c) Network byte order
    - (d) Bi-endian

13. **The special value NaN in IEEE 754 has:**
    - (a) All exponent bits as 1, non-zero mantissa ✓
    - (b) All exponent bits as 0
    - (c) Sign bit as 1
    - (d) None

14. **What is the decimal representation of BCD 01101001?**
    - (a) 69 ✓
    - (b) 105
    - (c) 41
    - (d) 98

15. **For a 4-bit number in 2's complement, the maximum positive value is:**
    - (a) 7 ✓
    - (b) 8
    - (c) 15
    - (d) -8

---

## 13. Flashcards

### Flashcard 1: Binary Addition Rules
**Front:** What are the four rules of binary addition?
**Back:**
- 0 + 0 = 0 (carry 0)
- 0 + 1 = 1 (carry 0)
- 1 + 0 = 1 (carry 0)
- 1 + 1 = 0 (carry 1)

### Flashcard 2: 2's Complement
**Front:** How do you find the 2's complement of a negative number?
**Back:** Take the binary representation of the positive number, invert all bits (1's complement), then add 1.

### Flashcard 3: IEEE 754 Components
**Front:** What are the three components of an IEEE 754 single precision floating-point number?
**Back:** 
1. Sign bit (1 bit)
2. Exponent (8 bits)
3. Mantissa/Fraction (23 bits)

### Flashcard 4: Overflow Detection
**Front:** How do you detect signed overflow during addition?
**Back:** Overflow occurs when:
- Adding two positive numbers produces a negative result
- Adding two negative numbers produces a positive result

### Flashcard 5: Endianness
**Front:** What is the difference between big-endian and little-endian?
**Back:** Big-endian stores the most significant byte at the lowest memory address; little-endian stores the least significant byte at the lowest address.

### Flashcard 6: Normalized Floating-Point
**Front:** What does it mean for a binary floating-point number to be normalized?
**Back:** The mantissa is expressed in the form 1.M (where M is the fractional part), ensuring the leading bit is always 1.

### Flashcard 7: BCD
**Front:** What is BCD and why is it used?
**Back:** Binary-Coded Decimal represents each decimal digit (0-9) using 4 bits. It's used in applications requiring exact decimal representation (financial systems) to avoid floating-point rounding errors.

### Flashcard 8: Denormalized Numbers
**Front:** What are denormalized floating-point numbers?
**Back:** Numbers with exponent = 0 but mantissa ≠ 0. They represent very small values close to zero with reduced precision.

### Flashcard 9: Sign-Magnitude
**Front:** What is the main disadvantage of sign-magnitude representation?
**Back:** It has two representations for zero (+0 and -0), making arithmetic operations complex.

### Flashcard 10: Mantissa Range
**Front:** What is the range of the mantissa in normalized binary floating-point?
**Back:** 1.0 ≤ mantissa < 2.0 (or 1.M where M is a binary fraction from 0 to 0.111...)

---

## References

- Delhi University BSc (Hons) Computer Science NEP 2024 UGCF Syllabus
- Computer Organization and Design by David A. Patterson and John L. Hennessy
- IEEE Standard for Floating-Point Arithmetic (IEEE 754-2008)
- Digital Logic and Computer Organization by V. Rajaraman and T. Radhakrishnan