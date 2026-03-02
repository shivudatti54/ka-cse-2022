# Representation of Integers

## Introduction

The representation of integers forms the foundational cornerstone of digital computing and computer architecture. Integers, being the most fundamental data type in any computing system, must be stored and processed efficiently within the constraints of finite memory and hardware limitations. The way integers are represented directly impacts arithmetic operations, computational efficiency, and the overall design of processor architectures.

In this topic, we explore various methods of representing integers in computer systems, starting from the familiar positional number systems to more complex signed number representations. Understanding these representations is crucial for any computer scientist, as they explain the underlying mechanisms that enable modern computing devices to perform billions of arithmetic operations per second. This knowledge becomes particularly important when working with low-level programming, system programming, and understanding the limitations and quirks of computer arithmetic.

The study of integer representation encompasses several key areas: positional number systems (binary, octal, hexadecimal), conversion techniques between different bases, signed number representations (including sign-magnitude, one's complement, and two's complement), and binary arithmetic operations. Each representation has its advantages and trade-offs, which we will examine in detail throughout this module.

## Key Concepts

### Positional Number Systems

A positional number system represents numbers using a base (or radix) **r**, where each digit's position determines its weight as a power of r. The general form of a number in base-r system is:

**dₙ₋₁ dₙ₋₂ ... d₁ d₀ . d₋₁ d₋₂ ... d₋ₘ (base r)**

This represents: dₙ₋₁ × rⁿ⁻¹ + dₙ₋₂ × rⁿ⁻² + ... + d₀ × r⁰ + d₋₁ × r⁻¹ + ... + d₋ₘ × r⁻ᵐ

Where each digit dᵢ satisfies 0 ≤ dᵢ ≤ r-1.

**Binary (Base-2):** Uses digits 0 and 1. Each position represents powers of 2. Computer systems use binary because electronic switches have two states (on/off, high/low voltage).

**Octal (Base-8):** Uses digits 0-7. Historically important in computing because 8 = 2³, making conversion between binary and octal straightforward (each octal digit represents exactly 3 binary digits).

**Hexadecimal (Base-16):** Uses digits 0-9 and letters A-F (representing values 10-15). Since 16 = 2⁴, each hexadecimal digit represents exactly 4 binary bits. This is the most widely used representation in modern computing for displaying memory addresses, machine code, and color values.

### Base Conversion Methods

**Decimal to Binary:** Repeated division by 2, recording remainders. The binary number is the remainders read in reverse order.

**Binary to Decimal:** Sum of each bit multiplied by its positional weight (2ⁿ).

**Binary to Octal/Hexadecimal:** Group bits in threes (for octal) or fours (for hexadecimal), starting from the right (for fractional part, start from the left).

**Any Base to Decimal:** Use the positional formula: Σ dᵢ × rⁱ

**Decimal to Any Base:** Repeated division by the target base, similar to decimal-to-binary conversion.

### Signed Number Representations

In computer systems, representing negative integers requires special handling due to the fixed word size. Three primary methods exist:

**Sign-Magnitude Representation:**
The most intuitive approach uses one bit (typically the leftmost) to indicate the sign (0 for positive, 1 for negative), and the remaining bits represent the magnitude. For an n-bit word:
- Range: -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1)
- Has two representations of zero: +0 (000...0) and -0 (100...0)
- Simple for magnitude comparison but problematic for arithmetic

**One's Complement Representation:**
Negative numbers are obtained by inverting all bits of the positive number. For an n-bit word:
- Range: -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1)
- Still has two zeros: 000...0 (0) and 111...1 (-0)
- Addition requires end-around carry (carry out of the most significant bit is added back to the least significant bit)

**Two's Complement Representation:**
The standard in modern computers. Negative numbers are obtained by inverting all bits and adding 1:
- Range: -2ⁿ⁻¹ to +(2ⁿ⁻¹ - 1)
- Only one zero: 000...0
- Arithmetic operations work naturally without special cases
- Most significant bit still indicates sign, but with weighted value -2ⁿ⁻¹

The key advantage of two's complement is that addition and subtraction can be performed using the same hardware, as overflow bits are simply discarded.

### Binary Arithmetic Operations

**Binary Addition:**
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 0 with carry 1
- 1 + 1 + 1 = 1 with carry 1

**Binary Subtraction (using two's complement):**
To subtract B from A: Compute A + (two's complement of B), then discard any overflow.

**Binary Multiplication:**
Similar to decimal multiplication. Multiply by each bit of the multiplier, shift appropriately, and add.

**Binary Division:**
Long division process, similar to decimal division but using binary digits.

### Binary Coded Decimal (BCD)

BCD represents each decimal digit (0-9) using its 4-bit binary representation. While inefficient in storage (uses 4 bits for values 0-9 when 0-15 are possible), BCD provides easy conversion to/from human-readable decimal form and is used in financial applications where exact decimal representation is critical.

### Gray Code

A binary number system where successive values differ by only one bit. This is crucial for error reduction in position sensing and communication systems. The Gray code for n bits can be generated by reflecting binary codes and prefixing with 0 and 1.

## Examples

**Example 1: Convert decimal 47 to binary, octal, and hexadecimal**

*Solution:*

**Decimal to Binary (47):**
47 ÷ 2 = 23 remainder 1
23 ÷ 2 = 11 remainder 1
11 ÷ 2 = 5 remainder 1
5 ÷ 2 = 2 remainder 1
2 ÷ 2 = 1 remainder 0
1 ÷ 2 = 0 remainder 1

Reading remainders from bottom to top: 47₁₀ = 101111₂

**Binary to Octal:**
Group 101111 in threes (from right): 101 111
101₂ = 5, 111₂ = 7
So 47₁₀ = 57₈

**Binary to Hexadecimal:**
Group 101111 in fours (from right): 0010 1111
0010₂ = 2, 1111₂ = F
So 47₁₀ = 2F₁₆

**Example 2: Find the 8-bit two's complement representation of -35**

*Solution:*

Step 1: Write +35 in binary using 8 bits
35 = 00100011₂

Step 2: Invert all bits (one's complement)
00100011 → 11011100

Step 3: Add 1
11011100 + 1 = 11011101

Therefore, -35 in 8-bit two's complement = 11011101₂

*Verification:* Compute 11011101 + 00100011 (35):
11011101 + 00100011 = 1 00000000 (discard overflow)
Result = 00000000 ✓

**Example 3: Perform binary subtraction: 11001 - 01011 using two's complement**

*Solution:*

A = 11001 (25), B = 01011 (11)

Step 1: Find two's complement of B
Invert: 01011 → 10100
Add 1: 10100 + 1 = 10101

Step 2: Add A and two's complement of B
11001 + 10101 = 11110

Step 3: Since no overflow (both numbers positive, result positive), this is the answer
11110₂ = 14 (25 - 11 = 14) ✓

## Exam Tips

1. **Two's complement is most important:** Understand both conversion to/from two's complement and why it simplifies arithmetic operations. This is the most frequently tested concept.

2. **Range calculations:** Remember that for n-bit representation, two's complement range is -2ⁿ⁻¹ to +(2ⁿ⁻¹ - 1), while signed magnitude and one's complement range is -(2ⁿ⁻¹ - 1) to +(2ⁿ⁻¹ - 1).

3. **Quick conversion shortcuts:** Grouping binary digits in threes (octal) or fours (hexadecimal) is faster than decimal conversion for intermediate steps.

4. **Overflow detection:** In two's complement, overflow occurs when adding two positive numbers gives a negative result, or two negative numbers give a positive result.

5. **Single zero in two's complement:** Remember that two's complement has only one representation for zero, which is why it's preferred over other methods.

6. **Bit manipulation:** Understanding integer representation helps in bitwise operations, masking, and flags—common in system programming.

7. **Endianness:** Know the difference between little-endian and big-endian representation, though this is less emphasized in theory exams.

8. **Practice conversions:** Be thorough with decimal ↔ binary ↔ octal ↔ hexadecimal conversions as these appear frequently in problem sets.