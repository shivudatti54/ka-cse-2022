# Number Systems

## Computer System Architecture — BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Number Systems** form the fundamental backbone of all digital computing and computer architecture. At the most basic level, computers operate using **binary digits (bits)** — sequences of 0s and 1s — because the physical components of a computer (transistors, capacitors) exist in one of two states: ON (conducting current) or OFF (not conducting current). This binary foundation extends to all computing operations, from simple arithmetic to complex machine learning algorithms.

For a Computer Science student at Delhi University, understanding number systems is essential because:

- **Digital Logic Design** relies on Boolean algebra and binary operations
- **Computer Organization** deals with how data is stored, represented, and processed at the machine level
- **Assembly Language Programming** requires working directly with binary and hexadecimal representations
- **Cryptography and Network Security** use hexadecimal and other representations extensively
- **Memory Addressing** uses hexadecimal notation for readability

This study material covers all critical aspects of number systems as prescribed in the Delhi University BSc (Hons) Computer Science syllabus under the NEP 2024 UGCF curriculum.

---

## 2. Types of Number Systems

### 2.1 Decimal Number System (Base-10)

The decimal system is the human-native number system, using digits 0 through 9. It is a **positional weight system** where each position represents a power of 10.

**Example**: The number 4592 represents:
- (4 × 10³) + (5 × 10²) + (9 × 10¹) + (2 × 10⁰) = 4000 + 500 + 90 + 2 = 4592

### 2.2 Binary Number System (Base-2)

Computers use the binary system with only two digits: **0** and **1**. Each digit is called a **bit** (binary digit). A group of 8 bits is called a **byte**.

**Example**: The binary number 110101₂ represents:
- (1 × 2⁵) + (1 × 2⁴) + (0 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)
- = 32 + 16 + 0 + 4 + 0 + 1 = 53₁₀

### 2.3 Octal Number System (Base-8)

The octal system uses digits 0 through 7. It was historically important in computing because 8 = 2³, making conversion between binary and octal straightforward. Each octal digit represents exactly 3 binary bits.

**Example**: The octal number 327₈ represents:
- (3 × 8²) + (2 × 8¹) + (7 × 8⁰) = 192 + 16 + 7 = 215₁₀

### 2.4 Hexadecimal Number System (Base-16)

The hexadecimal system uses digits 0-9 and letters A-F (representing values 10-15). It is extensively used in **memory addressing, color codes in web development, and machine code representation**. Each hex digit represents exactly 4 binary bits (a **nibble**).

**Example**: The hexadecimal number 3A9₁₆ represents:
- (3 × 16²) + (10 × 16¹) + (9 × 16⁰) = 768 + 160 + 9 = 937₁₀

---

## 3. Conversions Between Number Systems

### 3.1 Binary to Decimal Conversion

**Method**: Multiply each bit by its positional weight (power of 2) and sum the results.

**Example**: Convert 101101₂ to decimal:
```
Position:    5   4   3   2   1   0
Bit:         1   0   1   1   0   1
Weights:    32  16   8   4   2   1

101101₂ = (1×32) + (0×16) + (1×8) + (1×4) + (0×2) + (1×1)
        = 32 + 0 + 8 + 4 + 0 + 1 = 45₁₀
```

### 3.2 Decimal to Binary Conversion

**Method**: Repeated division by 2, recording remainders. Read remainders from bottom to top.

**Example**: Convert 47₁₀ to binary:
```
47 ÷ 2 = 23 remainder 1
23 ÷ 2 = 11 remainder 1
11 ÷ 2 = 5  remainder 1
5  ÷ 2 = 2  remainder 1
2  ÷ 2 = 1  remainder 0
1  ÷ 2 = 0  remainder 1

Reading from bottom: 101111₂
```

### 3.3 Binary to Hexadecimal Conversion

**Method**: Group binary digits into groups of 4 (nibbles), starting from the right. Convert each nibble to its hexadecimal equivalent.

**Example**: Convert 110101101001₂ to hexadecimal:
```
Group into nibbles: 1101 0110 1001
                     D    6    9

110101101001₂ = D69₁₆
```

### 3.4 Hexadecimal to Binary Conversion

**Method**: Each hex digit expands to exactly 4 binary bits.

**Example**: Convert 7F2A₁₆ to binary:
```
7 = 0111
F = 1111
2 = 0010
A = 1010

7F2A₁₆ = 0111111100101010₂
```

### 3.5 Decimal to Hexadecimal Conversion

**Method**: Repeated division by 16, similar to decimal-to-binary conversion.

**Example**: Convert 1000₁₀ to hexadecimal:
```
1000 ÷ 16 = 62 remainder 8
62 ÷ 16 = 3 remainder 14 (E)
3 ÷ 16 = 0 remainder 3

Reading from bottom: 3E8₁₆
```

---

## 4. Binary Arithmetic

### 4.1 Binary Addition

Binary addition follows the same principles as decimal addition, with only four possible combinations:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 | 0   | 0     |
| 0 | 1 | 1   | 0     |
| 1 | 0 | 1   | 0     |
| 1 | 1 | 0   | 1     |

**Example**: Add 10110₂ and 11001₂:
```
    10110
  + 11001
  -------
   101111
```
Verification: 22 + 25 = 47, and 101111₂ = 47 ✓

### 4.2 Binary Subtraction

Binary subtraction can be performed using **straight subtraction** or **2's complement method** (preferred in computers).

**Example**: Subtract 1010₂ from 11001₂ (11001 - 01010):
```
    11001
  - 01010
  -------
    01111 (15₁₀)
```

### 4.3 Binary Multiplication

Binary multiplication follows the same process as decimal, but simpler due to only using 0 and 1.

**Example**: Multiply 1011₂ by 110₂:
```
       1011
     ×  110
     ------
       0000 (1011 × 0)
      1011  (1011 × 1, shifted)
     1011   (1011 × 1, shifted)
    --------
     1000010
```
Verification: 11 × 6 = 66, and 1000010₂ = 66 ✓

---

## 5. Signed Number Representations

When representing negative numbers in computers, we need special representations since computers can only store bits.

### 5.1 Sign Magnitude Representation

The **most significant bit (MSB)** represents the sign (0 for positive, 1 for negative), and the remaining bits represent the magnitude.

**Example** (using 8 bits):
- +25 = 00011001
- -25 = 10011001

**Limitations**: Has both +0 (00000000) and -0 (10000000), complicating arithmetic.

### 5.2 One's Complement

The **one's complement** of a binary number is obtained by inverting all bits (0→1, 1→0).

**Example** (8-bit):
- +25 = 00011001
- -25 = 11100110 (one's complement of 00011001)

**Limitations**: Still has two representations for zero.

### 5.3 Two's Complement (Most Widely Used)

The **two's complement** is obtained by adding 1 to the one's complement. This is the standard representation in modern computers because:

- Only one representation of zero
- Arithmetic operations work naturally
- The range is asymmetric: for n bits, range is -2^(n-1) to +2^(n-1) - 1

**Example** (8-bit representation of -25):
```
Step 1: +25 = 00011001
Step 2: One's complement = 11100110
Step 3: Add 1 = 11100111

Therefore, -25 in 2's complement (8-bit) = 11100111
```

**Verification**: 11100111 + 00011001 = 100000000 (9 bits), dropping the carry gives 00000000 ✓

**Python Code for Two's Complement**:
```python
def to_twos_complement(value, bit_width=8):
    """Convert integer to two's complement representation"""
    if value >= 0:
        return format(value, f'0{bit_width}b')
    else:
        # For negative: take absolute, invert bits, add 1
        positive_repr = (1 << bit_width) + value
        return format(positive_repr, f'0{bit_width}b')

def from_twos_complement(binary_str):
    """Convert two's complement binary to integer"""
    bit_width = len(binary_str)
    value = int(binary_str, 2)
    # If MSB is 1, it's negative
    if value >= (1 << (bit_width - 1)):
        value -= (1 << bit_width)
    return value

# Example usage
print(to_twos_complement(-25, 8))  # Output: 11100111
print(from_twos_complement('11100111'))  # Output: -25
```

---

## 6. Floating-Point Representation

Floating-point numbers represent real numbers in computers using **scientific notation** in binary. The IEEE 754 standard defines formats for single-precision (32-bit) and double-precision (64-bit) numbers.

### 6.1 IEEE 754 Single-Position Format (32-bit)

| Component | Bits | Description |
|-----------|------|-------------|
| Sign (S) | 1 | 0 = positive, 1 = negative |
| Exponent (E) | 8 | Biased by 127 |
| Mantissa (M) | 23 | Fractional part (implicit leading 1) |

**Value**: (-1)^S × 1.M × 2^(E-127)

**Example**: Represent 5.75 in IEEE 754 single-precision:
```
Step 1: Convert to binary: 5.75 = 101.11
Step 2: Normalize: 1.0111 × 2²
Step 3: Exponent = 2 + 127 = 129 = 10000001
Step 4: Mantissa = 01110000000000000000000

Sign: 0
Exponent: 10000001
Mantissa: 01110000000000000000000

Final: 01000000101110000000000000000000
```

---

## 7. Endianness (Byte Order)

**Endianness** defines the byte order (most significant to least significant) when storing multi-byte data types in memory.

### 7.1 Big Endian

The **most significant byte** is stored at the **lowest memory address**. Used by Motorola processors, network protocols (TCP/IP).

**Example**: Storing 0x12345678:
```
Address:  0x00  0x01  0x02  0x03
Data:      12   34   56   78
```

### 7.2 Little Endian

The **least significant byte** is stored at the **lowest memory address**. Used by Intel/AMD x86 processors.

**Example**: Storing 0x12345678:
```
Address:  0x00  0x01  0x02  0x03
Data:      78   56   34   12
```

**Why It Matters**: When writing network code, file parsers, or cross-platform applications, understanding endianness prevents subtle bugs. The x86 architecture's little-endian nature means integer 1 is stored as 0x00000001 in memory: 01 00 00 00.

---

## 8. Binary Coded Decimal (BCD)

**BCD** represents each decimal digit (0-9) using its 4-bit binary representation. It provides direct decimal representation without binary conversion.

### 8.1 BCD Encoding

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

**Example**: Encode decimal 93 in BCD:
```
9 = 1001
3 = 0011
93 in BCD = 10010011
```

### 8.2 Advantages and Disadvantages

**Advantages**:
- Simple decimal input/output conversion
- No rounding errors for decimal quantities
- Used in financial applications

**Disadvantages**:
- Wasteful storage (6 of 16 possible 4-bit codes unused)
- Arithmetic operations are more complex
- Less efficient than binary

---

## 9. Key Takeaways

1. **Number systems** (binary, octal, hexadecimal, decimal) are positional weight systems with different bases; computers fundamentally use binary (base-2).

2. **Conversions** between systems require understanding positional values and grouping bits (particularly for binary ↔ hex conversions using nibbles).

3. **Binary arithmetic** (addition, subtraction, multiplication) follows the same logic as decimal but with simpler rules due to only two digits.

4. **Two's complement** is the standard for signed number representation in modern computers due to its arithmetic convenience and unique zero representation.

5. **Floating-point** (IEEE 754) enables representation of real numbers using sign, exponent, and mantissa fields.

6. **Endianness** determines byte order in memory; x86 uses little-endian while networks use big-endian convention.

7. **BCD** provides direct decimal representation useful for financial applications but is less storage-efficient than binary.

---

## 10. Multiple Choice Questions

**Q1. What is the decimal equivalent of the binary number 101101?**
- (a) 45
- (b) 43
- (c) 41
- (d) 47

**Answer: (a) 45**

**Q2. In two's complement representation using 8 bits, what is the range of representable integers?**
- (a) -128 to +127
- (b) -127 to +128
- (c) -256 to +255
- (d) -255 to +256

**Answer: (a) -128 to +127**

**Q3. The hexadecimal number system has a base of:**
- (a) 8
- (b) 2
- (c) 10
- (d) 16

**Answer: (d) 16**

**Q4. In IEEE 754 single-precision format, how many bits are allocated for the exponent?**
- (a) 23
- (b) 8
- (c) 1
- (d) 32

**Answer: (b) 8**

**Q5. Which byte order is used by Intel x86 processors?**
- (a) Big Endian
- (b) Little Endian
- (c) Network Byte Order
- (d) Bi-Endian

**Answer: (b) Little Endian**

**Q6. What is the two's complement of 00001100 (8-bit)?**
- (a) 11110100
- (b) 11110011
- (c) 00001100
- (d) 11110010

**Answer: (a) 11110100**

**Q7. BCD stands for:**
- (a) Binary Coded Decimal
- (b) Bit Coded Digital
- (a) Binary Coded Decimal
- (c) Basic Coded Decimal
- (d) Boolean Coded Decimal

**Answer: (a) Binary Coded Decimal**

**Q8. How many bits are in a nibble?**
- (a) 2
- (b) 4
- (c) 8
- (d) 16

**Answer: (b) 4**

---

## 11. Flashcards for Quick Review

### Flashcard 1
**Q: Why do computers use binary instead of decimal?**
**A:** Computer hardware components (transistors) have two stable states (ON/OFF), making binary physically easy to implement. Decimal would require detecting 10 distinct voltage levels, which is impractical and error-prone.

### Flashcard 2
**Q: What is the advantage of two's complement over sign-magnitude?**
**A:** Two's complement has only one representation of zero (00000000) and enables simpler arithmetic circuits. Adding a positive and negative number in two's complement produces the correct result automatically, unlike sign-magnitude.

### Flashcard 3
**Q: Why is hexadecimal preferred over binary for displaying memory addresses?**
**A:** Hexadecimal is more compact (1 hex digit = 4 binary digits) and more human-readable than long binary strings. For example, memory address 0xFFFFFFFF is cleaner than its 32-bit binary equivalent.

### Flashcard 4
**Q: What is the difference between big-endian and little-endian when reading a 32-bit integer from memory?**
**A:** Big-endian stores the most significant byte at the lowest address (like reading left-to-right). Little-endian stores the least significant byte first. Both store the same data in memory, just in different byte orders.

### Flashcard 5
**Q: In floating-point representation, why is the mantissa normalized (always has leading 1)?**
**A:** The normalized form (1.M) ensures maximum precision with the available bits. By having an implicit leading 1, we effectively get 24 bits of precision in a 23-bit mantissa field, maximizing accuracy.

---

*Study Material prepared for Delhi University BSc (Hons) Computer Science (NEP 2024 UGCF) - Computer System Architecture*