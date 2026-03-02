# Church Turing Thesis — Quick Revision Summary

## Introduction

The **Church Turing Thesis** is a foundational concept in the Theory of Computation that establishes the theoretical limits of what can be computed by any mechanical process. It forms the bridge between computability theory and practical computing, defining the boundary between solvable and unsolvable problems.

*(As per Delhi University BSc (Hons) CS NEP 2024 UGCF Syllabus — Unit: Computability Theory)*

---

## Key Concepts

### What is the Church Turing Thesis?
- States that **Turing machines** can compute any function that can be computed by any algorithmic process
- Proposes that the class of **Turing-computable functions** equals the class of **effectively calculable functions**
- A thesis (not a theorem) — proposed as a fundamental hypothesis about the nature of computation

### Historical Background
- **Alonzo Church** (1936): Introduced **lambda calculus**
- **Alan Turing** (1936): Introduced **Turing machines**
- Both models were proven **equivalent** in computing power
- Addressed the **Entscheidungsproblem** (Decision Problem) posed by Hilbert

### Important Models of Computation
- **Turing Machine**: Abstract device with infinite tape, read/write head, and finite states
- **Lambda Calculus**: Mathematical system for expressing computation via function abstraction and application
- **Recursive Functions**: Gödel-Kleene formulation using primitive recursive functions
- All three models are **computationally equivalent**

### Significance & Implications
- Defines the concept of **algorithm** rigorously
- Establishes that any digital computer (with sufficient memory) can simulate any other
- Provides theoretical foundation for **computability theory**
- Helps identify **undecidable problems** (e.g., Halting Problem)

### Decision Problem (Entscheidungsproblem)
- Asked whether there exists an algorithm to determine the truth/falsity of any mathematical statement
- Church and Turing independently proved this is **impossible**
- This result is one of the most important in theoretical computer science

---

## Conclusion

The Church Turing Thesis remains a cornerstone of computer science, defining the theoretical boundaries of computation. Understanding this thesis is essential for comprehending algorithmic limits, undecidability, and the fundamental capabilities of modern computing systems.

---

**Key Reference**: *Introduction to the Theory of Computation* by Michael Sipser — Chapter 3 (for Delhi University syllabus)