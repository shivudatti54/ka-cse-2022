# Logic Gates and Truth Tables: Comprehensive Study Material

## *Computer System Architecture – BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*

---

## 1. Introduction

Logic gates form the fundamental building blocks of all digital electronic systems, from simple calculators to sophisticated computers and smartphones. In our increasingly digital world, understanding logic gates is essential for any computer science professional. Every operation your computer performs—from basic arithmetic to complex machine learning algorithms—eventually translates into combinations of logic gate operations at the hardware level.

This study material covers logic gates and truth tables comprehensively, aligning with the Delhi University BSc (Hons) Computer Science syllabus under NEP 2024 UGCF. We address all fundamental concepts including basic gates, universal gates, special gates, Boolean algebra, De Morgan's theorems, Karnaugh maps, timing diagrams, transistor-level implementation, and combinational circuit design.

---

## 2. Fundamental Logic Gates

### 2.1 AND Gate

The AND gate produces a HIGH (1) output **only when ALL inputs are HIGH**. If any input is LOW (0), the output will be LOW.

**Truth Table (2-input):**

| A | B | Y = A·B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Boolean Expression:** Y = A · B or Y = AB

**Symbol:** ![AND Gate Symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/AND_Gate.svg/120px-AND_Gate.svg.png)

**Real-world Application:** A security system that activates an alarm only when BOTH motion is detected AND the system is armed.

### 2.2 OR Gate

The OR gate produces a HIGH output when **AT LEAST ONE** input is HIGH.

**Truth Table (2-input):**

| A | B | Y = A + B |
|---|---|-----------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Boolean Expression:** Y = A + B

**Real-world Application:** A room lighting system where lights turn on if EITHER the manual switch OR a motion sensor is activated.

### 2.3 NOT Gate (Inverter)

The NOT gate inverts the input signal—it produces the complement of the input.

**Truth Table:**

| A | Y = A' |
|---|--------|
| 0 | 1 |
| 1 | 0 |

**Boolean Expression:** Y = A' or Y = ¬A

**Symbol:** Bubble indicates inversion

---

## 3. Universal Gates

Universal gates are particularly important because **either NAND or NOR alone can be used to implement any Boolean function**. This property makes them essential for integrated circuit manufacturing.

### 3.1 NAND Gate (Not-AND)

The NAND gate produces a LOW output **only when ALL inputs are HIGH**. In all other cases, the output is HIGH.

**Truth Table:**

| A | B | Y = (AB)' |
|---|---|-----------|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Key Definition:** NAND produces 0 only if all inputs are 1 (NOT "1 if none are 1").

**Boolean Expression:** Y = (AB)' = A' + B' (by De Morgan's theorem)

**Implementing Basic Gates with NAND:**

```
NOT Gate:     A NAND A = (AA)' = A'
AND Gate:     (A NAND B)' = AB
OR Gate:      (A' NAND B')' = A + B
```

### 3.2 NOR Gate (Not-OR)

The NOR gate produces a HIGH output **only when ALL inputs are LOW**. In all other cases, the output is LOW.

**Truth Table:**

| A | B | Y = (A + B)' |
|---|---|--------------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

**Boolean Expression:** Y = (A + B)' = A' · B'

**Implementing Basic Gates with NOR:**

```
NOT Gate:     A NOR A = (A + A)' = A'
OR Gate:      (A NOR B)' = A + B
AND Gate:     (A' NOR B')' = A · B
```

---

## 4. Special Logic Gates

### 4.1 XOR Gate (Exclusive OR)

The XOR output is HIGH when **inputs are DIFFERENT**.

**Truth Table:**

| A | B | Y = A ⊕ B |
|---|---|-----------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Boolean Expression:** Y = A ⊕ B = AB' + A'B

**Applications:**
- Parity bit generation for error detection
- Half adder sum output
- Controlled inverter circuits

### 4.2 XNOR Gate (Exclusive NOR)

The XNOR output is HIGH when **inputs are EQUAL**.

**Truth Table:**

| A | B | Y = (A ⊕ B)' |
|---|---|--------------|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Boolean Expression:** Y = (A ⊕ B)' = AB + A'B'

**Applications:**
- Equality comparators
- Parity bit checking
- Full adder carry output

---

## 5. Boolean Algebra and De Morgan's Theorems

De Morgan's theorems are fundamental to digital logic design, enabling gate replacement and simplification.

### 5.1 First Theorem

> **The complement of a product equals the sum of the complements:**
> **(AB)' = A' + B'**

**Proof via Truth Table:**

| A | B | AB | (AB)' | A' | B' | A' + B' |
|---|---|-----|-------|----|----|---------|
| 0 | 0 | 0  | 1     | 1  | 1  | 1       |
| 0 | 1 | 0  | 1     | 1  | 0  | 1       |
| 1 | 0 | 0  | 1     | 0  | 1  | 1       |
| 1 | 1 | 1  | 0     | 0  | 0  | 0       |

### 5.2 Second Theorem

> **The complement of a sum equals the product of the complements:**
> **(A + B)' = A' · B'**

**Example Application - Gate Conversion:**

Convert an AND gate to use only NAND gates:
```
Y = A · B
  = ((A · B)')'        [Double negation]
  = (A · B) NAND (A · B)  [NAND implementation]
```

### 5.3 Other Essential Boolean Theorems

| Theorem | Expression |
|---------|------------|
| Identity | A + 0 = A, A · 1 = A |
| Null | A + 1 = 1, A · 0 = 0 |
| Idempotent | A + A = A, A · A = A |
| Complement | A + A' = 1, A · A' = 0 |
| Commutative | A + B = B + A, AB = BA |
| Associative | (A + B) + C = A + (B + C) |
| Distributive | A + BC = (A + B)(A + C) |
| Absorption | A + AB = A, A(A + B) = A |

---

## 6. Deriving Boolean Expressions from Truth Tables

Given a truth table, we can derive the Boolean expression in Sum of Products (SOP) form:

**Example - Majority Function:**
Output is 1 when majority (more than half) of inputs are 1.

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

**SOP Expression (minterms where Y=1):**
```
Y = A'BC + AB'C + ABC' + ABC
Y = AB + BC + AC  [Simplified]
```

---

## 7. Karnaugh Maps (K-Maps)

K-maps provide a systematic method for simplifying Boolean expressions graphically.

### 7.1 2-Variable K-Map

| AB\C | 0 | 1 |
|------|---|---|
| 00   | 0 | 1 |
| 01   | 0 | 1 |
| 11   | 1 | 1 |
| 10   | 1 | 0 |

### 7.2 Grouping Rules

1. Groups must be powers of 2 (1, 2, 4, 8...)
2. Groups can wrap around edges
3. Maximize group size for maximum simplification
4. All 1s must be covered

### 7.3 Example - Simplify Y = Σm(1,3,5,7)

```
K-Map:
     B'  B
A'   0   1
A    1   1

Grouping: All four cells form one group of 4
Simplified: Y = B
```

---

## 8. Timing Diagrams

Timing diagrams show how outputs change concerning input changes over time, accounting for gate propagation delays.

### 8.1 Example: AND Gate Timing

```
     A: ___|‾‾‾|___|‾‾‾|___
     B: _____|‾‾‾|_____|‾‾‾|__
     Y: _____|‾‾‾|_____|‾‾‾|__
           0→1   1→0   0→1
```

**Key Points:**
- Output changes only after propagation delay (tP)
- For AND: output goes HIGH when BOTH inputs are HIGH
- For OR: output goes LOW when BOTH inputs are LOW
- XOR/XNOR exhibit characteristic "glitches" during transitions

### 8.2 Propagation Delay Impact

In cascaded gates, delays accumulate:

```
A → [NOT] → [AND] → Y
     tP1    tP2
Total delay = tP1 + tP2
```

---

## 9. Transistor-Level Implementation

Understanding how gates are implemented at the transistor level provides deeper insight into digital circuits.

### 9.1 CMOS NAND Gate

CMOS (Complementary Metal-Oxide-Semiconductor) technology uses paired p-type and n-type MOSFETs:

```
VDD ──┬─[P-MOS]──┬── Output Y
      │    │     │
      A ──┘     └── B
      │          
      B ──┬─[N-MOS]──┬── GND
          │    │     │
          A ──┘     └──
```

**Operation:**
- When A=B=1: Both N-MOS conduct, P-MOS off, Y=GND (0)
- When A=B=0: Both P-MOS conduct, N-MOS off, Y=VDD (1)
- In all other cases: one path conducts, output is HIGH

### 9.2 CMOS NOR Gate

```
VDD ──┬─[P-MOS]──┬── Output Y
      │    │     │
      A ──┘     └── B
      │          
      B ──┬─[N-MOS]──┬── GND
          │    │     │
          A ──┘     └──
```

---

## 10. Combinational Circuit Design: Complete Example

Let's design a circuit that detects if a 3-bit binary number is greater than 4.

### Step 1: Define the Problem

Input: 3-bit binary number (A, B, C) where A is MSB
Output: Y = 1 if number > 4 (i.e., 5, 6, or 7)

### Step 2: Truth Table

| A | B | C | Decimal | Y |
|---|---|---|---------|---|
| 0 | 0 | 0 | 0       | 0 |
| 0 | 0 | 1 | 1       | 0 |
| 0 | 1 | 0 | 2       | 0 |
| 0 | 1 | 1 | 3       | 0 |
| 1 | 0 | 0 | 4       | 0 |
| 1 | 0 | 1 | 5       | 1 |
| 1 | 1 | 0 | 6       | 1 |
| 1 | 1 | 1 | 7       | 1 |

### Step 3: Derive SOP Expression

```
Y = Σm(5,6,7)
Y = A'BC' + AB'C + ABC' + ABC
```

### Step 4: Simplify using K-Map

```
     BC
A\BC   00   01   11   10
 0      0    0    0    0
 1      0    1    1    1

Grouping: One group of 4 (right column)
Simplified: Y = A
```

### Step 5: Circuit Implementation

```
     A ──────────────┬──[AND]── Y
                     │    │
                     B    0
                     │
                     C    0
```

Wait—let's verify: A=1 means number ≥ 4. For >4, we need A=1 AND (B OR C). Let me recalculate:

```
Y = A(B + C)
  = AB + AC
```

**Verification:**
- 5 (101): A=1, B=0, C=1 → Y = 1(0+1) = 1 ✓
- 6 (110): A=1, B=1, C=0 → Y = 1(1+0) = 1 ✓
- 4 (100): A=1, B=0, C=0 → Y = 1(0+0) = 0 ✓

### Step 6: Implement in Code (Python)

```python
def greater_than_four(A, B, C):
    """Check if 3-bit binary number > 4"""
    return A and (B or C)

# Test all combinations
print("A B C | Decimal | >4?")
print("-" * 20)
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            decimal = (A << 2) | (B << 1) | C
            result = greater_than_four(A, B, C)
            print(f"{A} {B} {C} |    {decimal}    |   {int(result)}")
```

### Step 7: Implement using Logic Gates

```python
def circuit_implementation(A, B, C):
    # Using only AND, OR, NOT gates
    # Y = A(B + C)
    
    or_output = B or C          # OR gate
    y = A and or_output         # AND gate
    return y
```

---

## 11. Multiple Choice Questions (University-Level)

### Section A: Conceptual Questions

**1. The NAND gate is called a universal gate because:**
   a) It is available in all digital circuits
   b) Any Boolean function can be implemented using only NAND gates ✓
   c) It produces both AND and OR functions
   d) It is the most commonly used gate

**2. Which of the following is NOT a Boolean theorem?**
   a) Commutative Law
   b) Associative Law
   c) Pythagorean Theorem ✓
   d) Distributive Law

**3. The XOR gate implements the Boolean function:**
   a) AB + A'B' (XNOR)
   b) AB' + A'B ✓
   c) (AB)'
   d) (A + B)'

**4. For a 3-input NAND gate, the output is LOW when:**
   a) All inputs are LOW
   b) At least one input is LOW
   c) All inputs are HIGH ✓
   d) At least one input is HIGH

**5. De Morgan's theorem (A + B)' is equivalent to:**
   a) A' + B'
   b) A'B' ✓
   c) AB
   d) A + B

### Section B: Application-Based Questions

**6. How many 1s are present in the minterm expansion of Y = Σm(0,2,5,7) for a 3-variable function?**
   a) 2
   b) 3
   c) 4 ✓
   d) 5

**7. A K-map has 8 cells. What is the maximum number of variables it can handle?**
   a) 2
   b) 3 ✓
   c) 4
   d) 5

**8. In a 4-variable K-map, a group of 8 adjacent 1s eliminates how many variables?**
   a) 1
   b) 2
   c) 3 ✓
   d) 4

**9. The CMOS implementation of a NOT gate uses:**
   a) Two n-type MOSFETs in series
   b) Two p-type MOSFETs in parallel
   c) One p-type and one n-type MOSFET in series ✓
   d) Four MOSFETs

**10. A combinational circuit has a propagation delay of 5ns per gate. If a signal passes through 4 gates in series, the total delay is:**
    a) 5ns
    b) 10ns
    c) 20ns ✓
    d) 25ns

### Section C: Analysis Questions

**11. What is the simplified form of Y = A'B' + AB?**
    a) (A ⊕ B)'
    b) (A ⊕ B)
    c) A' + B'
    d) A + B ✓

**12. Which gate is used to implement a half-adder's sum output?**
    a) AND
    b) OR
    c) XOR ✓
    d) NAND

---

## 12. Flashcards

### Flashcard 1
> **Q: What is a logic gate?**
> **A:** An electronic circuit that performs a logical operation on one or more input signals to produce a single output.

### Flashcard 2
> **Q: Define the output condition for a NAND gate.**
> **A:** Output is LOW (0) only when ALL inputs are HIGH (1). In all other cases, output is HIGH.

### Flashcard 3
> **Q: State De Morgan's First Theorem.**
> **A:** (AB)' = A' + B' — The complement of a product equals the sum of complements.

### Flashcard 4
> **Q: Why are NAND and NOR gates called universal gates?**
> **A:** Because any Boolean function can be implemented using only NAND gates or only NOR gates.

### Flashcard 5
> **Q: What is the function of XOR gate?**
> **A:** XOR outputs HIGH (1) when inputs are DIFFERENT, and LOW (0) when inputs are EQUAL.

### Flashcard 6
> **Q: Define propagation delay.**
> **A:** The time interval between the change in input and the corresponding change in output of a logic gate.

### Flashcard 7
> **Q: What is a K-map used for?**
> **A:** Karnaugh maps are used for simplifying Boolean algebra expressions graphically.

### Flashcard 8
> **Q: What does CMOS stand for?**
> **A:** Complementary Metal-Oxide-Semiconductor — a technology for constructing integrated circuits.

### Flashcard 9
> **Q: What is the difference between combinational and sequential circuits?**
> **A:** Combinational circuits output depends only on current inputs; sequential circuits output depends on current inputs and previous states.

### Flashcard 10
> **Q: How do you implement NOT gate using NAND?**
> **A:** Connect both inputs of a NAND gate to the same signal: Y = (A · A)' = A'

---

## Key Takeaways

1. **Fundamental Gates**: AND, OR, and NOT are the three basic gates from which all other gates can be constructed.

2. **Universal Gates**: NAND and NOR are universal gates—any Boolean function can be implemented using only NAND or only NOR gates.

3. **NAND/NOR Correct Definitions**: 
   - NAND: Output is 0 ONLY when ALL inputs are 1
   - NOR: Output is 1 ONLY when ALL inputs are 0

4. **De Morgan's Theorems** are essential for gate replacement and circuit simplification:
   - (AB)' = A' + B'
   - (A + B)' = A'B'

5. **K-maps** provide visual simplification of Boolean expressions, with groups of 2ⁿ eliminating n variables.

6. **Timing diagrams** account for propagation delays and are crucial for analyzing circuit behavior in real-world applications.

7. **CMOS technology** uses complementary p-type and n-type MOSFETs for efficient, low-power gate implementation.

8. **Combinational circuit design** follows a systematic process: problem definition → truth table → Boolean expression → simplification → circuit implementation.

9. **Truth tables** fully describe the input-output relationship for any combinational logic circuit.

10. Understanding logic gates is foundational for computer architecture, digital system design, and embedded systems development.

---

*This study material aligns with the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus for Computer System Architecture.*