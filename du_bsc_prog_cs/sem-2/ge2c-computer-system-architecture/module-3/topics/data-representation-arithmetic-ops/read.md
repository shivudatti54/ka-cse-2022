# Data Representation and Arithmetic Operations

## Introduction

Data representation forms the foundational layer of how computers process information. At the most fundamental level, computers understand only binary digits (0s and 1s), and every piece of data—whether text, images, audio, or numbers—must ultimately be represented in this binary format. Understanding how different types of data are encoded, stored, and manipulated within a computer system is essential for any computer science student, particularly those studying computer system architecture.

This topic becomes especially critical when we consider arithmetic operations, which form the backbone of computational tasks. From simple calculations in a calculator to complex scientific simulations, all arithmetic operations rely on how numbers are represented internally. The choice of number representation system directly impacts computational efficiency, accuracy, and the range of values that can be processed. In this module, we will explore various number systems, signed number representations, binary arithmetic operations, and floating-point representations, providing you with a comprehensive understanding of how computers perform mathematical computations.

## Key Concepts

### 1. Number Systems

A number system defines how we represent quantities using symbols. The four fundamental number systems relevant to computer science are:

**Decimal System (Base-10):** The familiar system using digits 0-9. Each position represents a power of 10.

**Binary System (Base-2):** The language of computers, using digits 0 and 1. Each position represents a power of 2.

**Octal System (Base-8):** Uses digits 0-7. Frequently used as a shorthand for binary (each octal digit represents 3 binary bits).

**Hexadecimal System (Base-16):** Uses digits 0-9 and letters A-F. Each hex digit represents 4 binary bits, making it ideal for representing memory addresses and machine code.

**Conversions:** Converting between number systems involves understanding positional values. For example, the binary number 1101₂ equals 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13 in decimal.

### 2. Signed Number Representation

When representing negative numbers in binary, computers use several methods:

**Sign-Magnitude Representation:** The most significant bit (MSB) represents the sign (0 for positive, 1 for negative), and the remaining bits represent the magnitude. For an 8-bit system, +5 is 00000101 and -5 is 10000101. This method is simple but has two representations of zero (+0 and -0).

**1's Complement:** To find the 1's complement of a binary number, invert all bits (change 0s to 1s and 1s to 0s). For example, +5 (00000101) becomes -5 (11111010). This also has two zero representations.

**2's Complement:** The standard method used by modern computers. To find 2's complement, first compute 1's complement, then add 1 to the result. For -5: start with +5 (00000101), 1's complement is 11111010, add 1 gives 11111011. This method has a single zero representation (00000000) and simplifies arithmetic operations.

**Range:** For an n-bit number using 2's complement, the range is -2^(n-1) to +2^(n-1) - 1. For 8 bits: -128 to +127.

### 3. Binary Arithmetic Operations

**Binary Addition:** Follows the same rules as decimal addition, with carries:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 0 with carry 1

**Binary Subtraction:** Can be performed using 2's complement method (adding the 2's complement of the subtrahend) or through direct borrowing method.

**Binary Multiplication:** Similar to decimal multiplication, using AND operations for each bit:
- 1 × 1 = 1
- 1 × 0 = 0
- 0 × 1 = 0
- 0 × 0 = 0

**Binary Division:** Follows long division methodology, subtracting multiples of the divisor from the dividend.

### 4. Binary Coded Decimal (BCD)

BCD represents each decimal digit using 4 binary bits. For example, the decimal number 93 is represented as 10010011 in BCD. While intuitive for decimal display, BCD is inefficient (uses more bits than necessary) and arithmetic operations are more complex.

### 5. Floating-Point Representation

Real numbers with fractional parts require floating-point representation. The IEEE 754 standard is universally used:

**Format:** A floating-point number has three components:
- Sign bit (S): 0 for positive, 1 for negative
- Exponent (E): Biased representation
- Mantissa/Fraction (F): The significant digits

**Single Precision (32-bit):** 1 sign bit + 8 exponent bits + 23 fraction bits
**Double Precision (64-bit):** 1 sign bit + 11 exponent bits + 52 fraction bits

**Normalized Form:** The mantissa is adjusted so there's exactly one non-zero digit to the left of the decimal point (1.xxxxx in binary), and this leading 1 is implicit (not stored).

**Bias:** For single precision, the bias is 127. Actual exponent = stored exponent - 127.

**Special Values:**
- Zero: All exponent and mantissa bits are 0
- Infinity: All exponent bits are 1, mantissa is 0
- NaN (Not a Number): All exponent bits are 1, mantissa is non-zero
- Denormalized: Exponent is 0, mantissa is non-zero

## Examples

### Example 1: Decimal to Binary and Hexadecimal Conversion

**Problem:** Convert the decimal number 250 to binary and hexadecimal.

**Solution:**

*Step 1: Decimal to Binary*
Divide by 2 repeatedly and record remainders:
- 250 ÷ 2 = 125 remainder 0
- 125 ÷ 2 = 62 remainder 1
- 62 ÷ 2 = 31 remainder 0
- 31 ÷ 2 = 15 remainder 1
- 15 ÷ 2 = 7 remainder 1
- 7 ÷ 2 = 3 remainder 1
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1

Reading remainders from bottom to top: 250₁₀ = 11111010₂

*Step 2: Binary to Hexadecimal*
Group binary digits into groups of 4 (from right):
1111 1010

- 1111₂ = F₁₆
- 1010₂ = A₁₆

Therefore: 250₁₀ = 11111010₂ = FA₁₆

### Example 2: 2's Complement Subtraction Using Addition

**Problem:** Perform 75 - 42 using 8-bit 2's complement representation.

**Solution:**

*Step 1:* Represent 75 in 8-bit binary: 01001011
*Step 2:* Represent 42 in 8-bit binary: 00101010
*Step 3:* Find 2's complement of 42:
- 1's complement: 11010101
- Add 1: 11010110

*Step 4:* Add 75 + (-42):
```
  01001011  (75)
+ 11010110  (-42)
-----------
 100100001
```

*Step 5:* The 9th bit (carry) is discarded for 8-bit result:
Result: 00100001₂ = 33₁₀

This confirms: 75 - 42 = 33 ✓

### Example 3: IEEE 754 Single Precision Conversion

**Problem:** Represent the decimal number -5.75 in IEEE 754 single precision format.

**Solution:**

*Step 1:* Convert to binary: 5.75 = 101.11₂
*Step 2:* Normalize: 1.0111 × 2²
*Step 3:* Sign bit: 1 (negative)
*Step 4:* Exponent: 2 + 127 = 129 = 10000001₂
*Step 5:* Mantissa: Remove the implicit 1, pad to 23 bits: 01110000000000000000000

*Result:* 1 10000001 01110000000000000000000

In hexadecimal: C0E00000₁₆

## Exam Tips

1. **2's Complement is Essential:** Expect questions requiring you to find 2's complement representations and perform subtraction using the addition method. Remember the two-step process: invert bits, then add 1.

2. **Range Calculations:** Memorize the range formulas: For n-bit 2's complement, range is -2^(n-1) to +2^(n-1)-1. For unsigned binary, range is 0 to 2^n - 1.

3. **Overflow Detection:** In signed arithmetic, overflow occurs when the carry into the sign bit differs from the carry out. For unsigned arithmetic, overflow occurs when there's a carry out of the MSB.

4. **IEEE 754 Special Cases:** Know how to identify and represent zero, infinity, NaN, and denormalized numbers from their bit patterns.

5. **Quick Conversions:** Remember that each hex digit = 4 binary bits, and each octal digit = 3 binary bits. This makes conversions much faster.

6. **Negative Exponents in Floating Point:** Remember the bias (127 for single, 1023 for double). The actual exponent = stored exponent - bias.

7. **Show Your Work:** In exams, always show the step-by-step process, especially for conversions and arithmetic operations, as partial marks are awarded for methodology.

8. **BCD vs. Pure Binary:** Understand when BCD is used (financial applications requiring exact decimal representation) and its inefficiency compared to pure binary.