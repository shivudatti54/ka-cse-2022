# Number Systems
## Computer System Architecture — Delhi University (NEP 2024 UGCF)

### Introduction
Number systems form the foundation of digital computers. Understanding different number representations and their conversions is essential for computer architecture, as all data processing ultimately operates on binary numbers.

### Types of Number Systems

- **Decimal System** — Base-10, digits 0-9
- **Binary System** — Base-2, digits 0-1 (fundamental to computers)
- **Octal System** — Base-8, digits 0-7
- **Hexadecimal System** — Base-16, digits 0-9 and A-F

### Key Conversions

- Binary ↔ Decimal, Binary ↔ Octal, Binary ↔ Hexadecimal
- Quick conversion: 3 binary digits = 1 octal digit; 4 binary digits = 1 hex digit

### Binary Arithmetic

- **Addition**: 0+0=0, 0+1=1, 1+1=0 (carry 1), 1+1+1=1 (carry 1)
- **Substraction**: Using 2's complement method
- **Multiplication**: Shift and add method
- **Division**: Repeated subtraction/shift method

### Signed Number Representations

- **Signed Magnitude**: MSB represents sign, remaining bits represent magnitude
- **1's Complement**: Invert all bits; MSB is sign bit
- **2's Complement**: Invert bits and add 1 (most widely used)
  - Range for n bits: -2ⁿ⁻¹ to +2ⁿ⁻¹ - 1

### Floating Point Representation

- **IEEE 754 Standard** (single precision: 32-bit, double precision: 64-bit)
- Structure: Sign bit | Exponent | Mantissa (Significand)
- Normalized form: ±1.xxxxx₂ × 2ᵉ

### Special Codes

- **BCD (Binary Coded Decimal)**: Each decimal digit represented by 4 binary bits
- **Gray Code**: Adjacent numbers differ by only one bit (useful for error detection)
- **ASCII**: 7-bit/8-bit character encoding

### Important Concepts for Exams

- 2's complement simplifies arithmetic operations
- Overflow occurs when result exceeds representable range
- Hex is widely used to represent binary concisely

### Conclusion
A thorough grasp of number systems is crucial for understanding computer architecture, data representation, and low-level programming. Master conversions, 2's complement, and floating-point representation as these are frequently tested in exams.

---
*Reference: Delhi University BSc (Hons) CS NEP 2024 UGCF Syllabus — Unit I: Data Representation*