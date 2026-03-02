# Boolean Algebra & Digital Circuits
## Computer System Architecture - BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

### Introduction

Boolean Algebra forms the mathematical foundation of digital circuits and computer architecture. This topic, covered under **Paper: Computer Organization & Architecture (DSC-3)**, deals with binary variables and logical operations essential for designing and analyzing digital systems. It enables efficient circuit minimization and forms the basis for all computing operations.

---

### Key Concepts

**1. Boolean Algebra Fundamentals**
- Binary variables: 0 (FALSE) and 1 (TRUE)
- Basic operations: AND (·), OR (+), NOT (')
- Commutative, Associative, Distributive laws
- De Morgan's Theorems:
  - (A + B)' = A' · B'
  - (A · B)' = A' + B'
- Absorption and Consensus theorems

**2. Logic Gates**
- **Basic Gates**: AND, OR, NOT
- **Universal Gates**: NAND, NOR (can implement any Boolean function)
- **Special Gates**: XOR (parity), XNOR (equivalence)
- Truth tables for 2-input gates
- Gate realization from Boolean expressions

**3. Boolean Function Minimization**
- **Algebraic Simplification** using Boolean theorems
- **Karnaugh Map (K-Map)**: Up to 4 variables
  - Grouping of 1s (powers of 2)
  - Don't care conditions
- **Quine-McCluskey Method**: Tabular minimization for more variables
- Simplification reduces gate count and circuit cost

**4. Combinational Circuits**
- **Arithmetic Circuits**: Half adder, Full adder, Half subtractor, Full subtractor
- **Multiplexer (MUX)**: Data selector - 2ⁿ inputs, n select lines
- **Demultiplexer (DEMUX)**: Data distributor
- **Decoder/Encoder**: Binary to decimal conversion
- **Comparator**: Magnitude comparison

**5. Sequential Circuits**
- **Flip-Flops**: SR, JK, D, T (edge-triggered, asynchronous inputs)
- **Registers**: Shift registers (SIPO, PIPO, SISO, PISO)
- **Counters**: Synchronous and Asynchronous (MOD-N counters)
- Memory elements with clock pulse

**6. Canonical & Standard Forms**
- **SOP (Sum of Products)**: Minterm expansion (∑m)
- **POS (Product of Sums)**: Maxterm expansion (∏M)
- Conversion between forms using truth tables

---

### Delhi University Syllabus Reference (NEP 2024)
As per UGCF, this module covers:
- Boolean algebra and logic gates
- Minimization techniques (K-map)
- Combinational circuit design
- Sequential circuit fundamentals

---

### Conclusion

Boolean Algebra and Digital Circuits are fundamental to computer architecture. Mastery of Boolean theorems, logic gates, and minimization techniques enables efficient digital circuit design. Understanding combinational and sequential circuits is essential for exam success and practical digital system implementation.