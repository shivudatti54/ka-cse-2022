# Logic Gates and Truth Tables

## Introduction
Logic gates are the fundamental building blocks of digital circuits in computer system architecture. These electronic devices perform logical operations on one or more binary inputs to produce a single binary output. Understanding logic gates and their truth tables is essential for designing and analyzing digital systems, forming the foundation of Boolean algebra and computer hardware.

---

## Basic Logic Gates

### 1. AND Gate
- **Symbol:** ⋅ or ∧
- **Operation:** Output is 1 only when ALL inputs are 1
- **Truth Table:**
  | A | B | A·B |
  |---|---|-----|
  | 0 | 0 |  0  |
  | 0 | 1 |  0  |
  | 1 | 0 |  0  |
  | 1 | 1 |  1  |

### 2. OR Gate
- **Symbol:** + or ∨
- **Operation:** Output is 1 when ANY input is 1
- **Truth Table:**
  | A | B | A+B |
  |---|---|-----|
  | 0 | 0 |  0  |
  | 0 | 1 |  1  |
  | 1 | 0 |  1  |
  | 1 | 1 |  1  |

### 3. NOT Gate (Inverter)
- **Symbol:** ' or ¬
- **Operation:** Inverts the input (0→1, 1→0)
- **Truth Table:**
  | A | A' |
  |---|----|
  | 0 |  1 |
  | 1 |  0 |

---

## Derived Gates

### 4. NAND Gate (Universal Gate)
- **Symbol:** ⊼
- **Operation:** Inverted AND – output is 0 only when all inputs are 1
- Can be used to create any other logic gate

### 5. NOR Gate (Universal Gate)
- **Symbol:** ⊽
- **Operation:** Inverted OR – output is 1 only when all inputs are 0
- Also used to construct any other logic gate

### 6. XOR Gate (Exclusive OR)
- **Symbol:** ⊕
- **Operation:** Output is 1 when inputs are different
- **Truth Table:**
  | A | B | A⊕B |
  |---|---|-----|
  | 0 | 0 |  0  |
  | 0 | 1 |  1  |
  | 1 | 0 |  1  |
  | 1 | 1 |  0  |

### 7. XNOR Gate (Equivalence)
- **Symbol:** ⊙
- **Operation:** Output is 1 when inputs are same (complement of XOR)

---

## Key Properties (De Morgan's Theorems)

- **(A + B)' = A' · B'**
- **(A · B)' = A' + B'**

---

## Conclusion
Logic gates and truth tables form the cornerstone of digital electronics and computer architecture. Mastery of basic gates (AND, OR, NOT), derived gates (NAND, NOR, XOR, XNOR), and their truth tables is crucial for understanding circuit design, Boolean algebra simplification, and computer hardware fundamentals—key topics for Delhi University B.Sc. (H) CS NEP 2024 examination.

**Exam Tip:** Remember that NAND and NOR are "universal gates" as any Boolean function can be implemented using only NAND or only NOR gates.