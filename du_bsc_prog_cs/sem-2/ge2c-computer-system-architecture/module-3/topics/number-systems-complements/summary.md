# Number Systems Complements

**For BSc Physical Science (CS) – Delhi University, NEP 2024**

---

## Introduction
Complements are fundamental arithmetic operations in digital computer systems, enabling efficient representation of signed numbers and simplification of subtraction operations. This topic covers complement number systems essential for understanding computer arithmetic and digital logic design.

---

## Key Concepts

### 1. Types of Number Systems
- **Binary** (base-2): Uses digits 0 and 1
- **Octal** (base-8): Uses digits 0-7
- **Decimal** (base-10): Uses digits 0-9
- **Hexadecimal** (base-16): Uses digits 0-9 and A-F

### 2. Complement Types

**Diminished Radix Complement (r-1's Complement)**
- For binary: **1's complement** – invert all bits (0→1, 1→0)
- For decimal: **9's complement** – subtract each digit from 9
- Formula: (rⁿ - 1) - N where n = number of digits

**Radix Complement (r's Complement)**
- For binary: **2's complement** – most widely used for signed representation
- For decimal: **10's complement** – subtract from next power of 10
- Formula: rⁿ - N (or add 1 to r-1's complement)
- **Key property**: 2's complement of a number N = (~N) + 1

### 3. Signed Number Representation
- **Signed Magnitude**: MSB represents sign, remaining bits represent magnitude (limited use)
- **2's Complement**: Standard representation for signed integers
  - Positive numbers: same as unsigned
  - Negative numbers: 2's complement of absolute value
  - Range for n bits: -2ⁿ⁻¹ to +(2ⁿ⁻¹ - 1)
  - Only one representation for zero

### 4. Arithmetic Operations Using Complements

**Addition with 2's Complement**
- Add the numbers normally, including sign bits
- Discard any carry out from MSB
- Overflow occurs when signs are same but result sign differs

**Substraction using Complements**
- Method: N1 - N2 = N1 + (2's complement of N2)
- Take complement of subtrahend and add to minuend
- Discard end-around carry (for 1's complement)
- Check for end-around borrow for 1's complement

### 5. Advantages of Complements
- Simplifies hardware (only adder circuit needed for addition/subtraction)
- Eliminates separate subtractor circuit
- 2's complement has single zero representation
- Natural handling of signed arithmetic

---

## Conclusion
Complement arithmetic forms the backbone of digital computer systems. Mastery of 1's and 2's complements for binary, and 9's and 10's complements for decimal systems, is essential for understanding computer architecture, digital logic design, and assembly-level programming. The 2's complement system remains the industry standard for representing signed integers in modern processors.

*Based on Delhi University BSc (Hons) CS Syllabus – NEP 2024*