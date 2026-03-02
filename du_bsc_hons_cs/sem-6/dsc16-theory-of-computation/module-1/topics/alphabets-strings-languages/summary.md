# Alphabets, Strings & Languages — Theory of Computation

**Reference:** Delhi University — BSc (Hons) CS, NEP 2024 UGCF (Unit I)

---

## Introduction

The Theory of Computation begins with three fundamental building blocks: **alphabets**, **strings**, and **languages**. These concepts form the foundation for understanding formal languages, automata, and computational models studied throughout the course.

---

## 1. Alphabets (Σ)

- An **alphabet** is a finite, non-empty set of symbols.
- Denoted by **Σ** (sigma).
- **Examples:** Σ = {0, 1} (binary alphabet), Σ = {a, b, c}, Σ = {a, b, …, z}

---

## 2. Strings

- A **string** (or word) is a finite sequence of symbols from an alphabet.
- **Length of a string** — number of symbols it contains; denoted |w|.
- **Empty string** — string with zero symbols, denoted by **ε** (epsilon) or **λ**; |ε| = 0.
- **Operations on strings:**
  - **Concatenation:** xy joins string x followed by y; εw = wε = w
  - **Reverse:** wᴿ reverses the order of symbols
  - **Prefix/Suffix/Substring:** w = xyz → x is prefix, z is suffix, y is substring
  - **Power:** w⁰ = ε, wⁿ⁺¹ = wⁿw

---

## 3. Languages

- A **language** is a **set of strings** formed from an alphabet Σ.
- Written as L ⊆ Σ* (where Σ* is the set of *all* possible strings over Σ).
- **Types of languages:**
  - **Empty language:** L = ∅
  - **Singleton language:** L = {ε}
  - **Universal language:** L = Σ* (contains every possible string)
  - **Finite language:** contains a finite number of strings
  - **Infinite language:** contains infinitely many strings

---

## 4. Operations on Languages

Let L, L₁, L₂ be languages over Σ:

- **Union:** L₁ ∪ L₂ = { w | w ∈ L₁ or w ∈ L₂ }
- **Intersection:** L₁ ∩ L₂ = { w | w ∈ L₁ and w ∈ L₂ }
- **Complement:** L̄ = Σ* − L
- **Concatenation:** L₁L₂ = { xy | x ∈ L₁, y ∈ L₂ }
- **Kleene Star (closure):** L* = L⁰ ∪ L¹ ∪ L² ∪ … (includes ε)
- **Positive Closure:** L⁺ = L¹ ∪ L² ∪ … (excludes ε)

---

## 5. Key Notations

- **Σ*** — set of *all* strings (including ε) over Σ
- **Σⁿ** — set of all strings of length exactly n
- **|L|** — cardinality (number of strings in language L)

---

## Conclusion

Understanding alphabets, strings, and languages is essential for studying formal language theory, automata, and computability. These basic definitions and operations prepare students for topics like finite automata, regular expressions, context-free grammars, and the Chomsky hierarchy — core to the Theory of Computation and crucial for the Delhi University examinations.