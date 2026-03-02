# Number Systems & Boolean Algebra

## Introduction
Number systems form the foundation of digital computing, enabling representation and manipulation of data. Modern computers rely on binary (base-2) system for fundamental operations, while hexadecimal (base-16) and octal (base-8) systems simplify human interaction with binary data. Boolean algebra, developed by George Boole, provides the mathematical framework for digital circuit design and logical operations in computers.

Understanding these systems is crucial for computer architecture design, memory addressing, error detection mechanisms, and low-level programming. For MCA students, mastery of number conversions and Boolean simplification techniques directly applies to digital logic design, compiler construction, and embedded systems development.

## Key Concepts
1. **Positional Number Systems**
   - Weighted systems where position determines value
   - General formula: N = Σd_i × b^i (b=base, d=digit)
   - Binary (b=2), Octal (b=8), Decimal (b=10), Hex (b=16)

2. **Conversion Techniques**
   - Binary ↔ Decimal: Sum-of-weights method
   - Binary ↔ Hex/Octal: Grouping bits (4 for hex, 3 for octal)
   - Fractional Conversions: Repeated multiplication/division

3. **Signed Number Representations**
   - Sign-magnitude: MSB as sign bit
   - 1's Complement: Bitwise NOT
   - 2's Complement: Standard for modern computers

4. **Boolean Algebra Fundamentals**
   - Basic operators: AND (·), OR (+), NOT (')
   - Laws: Commutative, Associative, Distributive, De Morgan's
   - Canonical forms: SOP (Sum of Products) and POS (Product of Sums)

5. **Karnaugh Maps (K-Maps)**
   - Graphical method for Boolean simplification
   - 2-6 variable optimization using adjacency grouping

## Examples

**Example 1: Hexadecimal to Binary Conversion**
Convert (A3F.2C)₁₆ to binary:
```
A = 1010, 3 = 0011, F = 1111, 2 = 0010, C = 1100
Result: 1010 0011 1111 . 0010 1100
        = 101000111111.001011
```

**Example 2: 2's Complement Subtraction**
Calculate 25 - 40 using 8-bit 2's complement:
```
25 = 00011001
40 = 00101000 → 2's complement = 11011000
25 + (-40) = 00011001 + 11011000 = 11110001 (which is -15 in decimal)
```

**Example 3: K-Map Simplification**
Simplify f(A,B,C,D) = Σ(0,2,4,5,6,7,8,10)
```
CD\AB| 00 01 11 10
-----|------------
00   | 1  0  1  1
01   | 1  1  1  0
11   | 0  0  0  0
10   | 1  1  0  1

Simplified expression: A'C' + B'D' + AB'
```

## Exam Tips
1. For base conversions, always verify results by reverse calculation
2. In 2's complement arithmetic, check for overflow when signs match
3. K-Map grouping: Look for largest possible groups (powers of 2)
4. Boolean simplification: Apply De Morgan's laws before grouping terms
5. For fractional conversions, note that many fractions cannot be represented exactly in binary
6. In signed number questions, explicitly state your representation method
7. Time management: Allocate 15-20 minutes for number system problems, 10-15 for Boolean algebra