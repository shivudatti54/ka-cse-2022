# Data Representation & Arithmetic Operations

## Introduction
Data representation forms the foundation of computer architecture, dealing with how computers store, process, and manipulate numerical and character data. Understanding these concepts is essential for comprehending how arithmetic operations are performed at the hardware level.

---

## Key Concepts

### 1. Number Systems
- **Binary (Base-2)**: Foundation of digital computers (0, 1)
- **Octal (Base-8)**: Used for simplified binary representation
- **Decimal (Base-10)**: Human-readable format
- **Hexadecimal (Base-16)**: Compact binary representation (0-9, A-F)
- **Conversions**: Binary↔Decimal, Binary↔Octal, Binary↔Hexadecimal

### 2. Signed Number Representation
- **Signed Magnitude**: MSB represents sign; rest represent magnitude
- **1's Complement**: Invert all bits; two representations for zero
- **2's Complement**: Invert bits and add 1; single zero representation (preferred)
  - Range for n bits: -2^(n-1) to +2^(n-1) - 1

### 3. Binary Arithmetic Operations
- **Addition**: Basic rules (0+0=0, 1+0=1, 0+1=1, 1+1=0 with carry)
- **Subtraction**: Performed using 2's complement addition
- **Multiplication**: Shift-and-add method
- **Division**: Repeated subtraction or shift-and-subtract method

### 4. Floating-Point Representation
- **IEEE 754 Standard**:
  - Single precision (32-bit): 1 sign, 8 exponent, 23 mantissa
  - Double precision (64-bit): 1 sign, 11 exponent, 52 mantissa
- **Components**: Sign bit, Exponent (biased), Mantissa (normalized)
- **Special values**: Zero, Infinity, NaN, Denormalized numbers

### 5. BCD (Binary Coded Decimal)
- Each decimal digit represented by 4 binary bits
- Used in financial applications for precision

### 6. Error Detection
- **Parity Bit**: Even/Odd parity for single-bit error detection
- **Hamming Code**: Single-bit error correction

---

## Important Points for Exam

| Topic | Key Formula/Note |
|-------|------------------|
| 2's Complement | Negative number = Complement + 1 |
| Range (n bits) | -2^(n-1) to +2^(n-1) - 1 |
| Overflow Detection | Carry into MSB ≠ Carry out of MSB |
| Biased Exponent | Bias = 2^(k-1) - 1 (127 for single, 1023 for double) |

---

## Conclusion
Mastery of data representation and arithmetic operations is crucial for understanding computer architecture. The 2's complement system and IEEE 754 floating-point standard are particularly important for exam preparation. Focus on conversions, arithmetic operations, and overflow detection as these are frequently tested topics in Delhi University examinations.