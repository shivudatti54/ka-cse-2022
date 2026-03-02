# Properties Of Regular Languages

## Introduction

Regular languages form a fundamental class in automata theory with well-defined mathematical properties. For the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus, understanding these properties is essential for exam success. This summary covers closure properties, pumping lemma, decision procedures, and minimization — key topics from Unit 3 of the Theory of Computation course.

---

## Key Properties

### 1. Closure Properties
Regular languages are closed under the following operations:

- **Union**: If L₁ and L₂ are regular, then L₁ ∪ L₂ is regular
- **Intersection**: L₁ ∩ L₂ is regular
- **Complement**: If L is regular, then L̅ (complement) is regular
- **Concatenation**: L₁L₂ is regular
- **Kleene Star**: L* is regular
- **Difference**: L₁ - L₂ is regular
- **Homomorphism**: h(L) is regular (substitution of symbols)
- **Inverse Homomorphism**: h⁻¹(L) is regular
- **Reversal**: Lʳ is regular

> **Important**: Regular languages are NOT closed under infinite union or infinite intersection.

### 2. Pumping Lemma for Regular Languages
Used to prove a language is **not regular**:

- If L is regular, there exists a pumping length *p* such that every string w ∈ L with |w| ≥ p can be divided into xyz where:
  1. |y| > 0
  2. |xy| ≤ p
  3. For all i ≥ 0, xyⁱz ∈ L

**Applications**: Proving languages like {aⁿbⁿ | n ≥ 0}, {ww | w ∈ Σ*}, and prime number strings are not regular.

### 3. Myhill-Nerode Theorem
Provides necessary and sufficient condition for regularity:

- Language L is regular **iff** the number of distinct equivalence classes in the Myhill-Nerode relation is finite
- Each equivalence class corresponds to a state in the minimal DFA
- Used for DFA minimization and proving regularity

### 4. Decision Properties
The following are **decidable** for regular languages:

| Property | Algorithm |
|----------|-----------|
| Emptiness | Check if accepting state is reachable |
| Finiteness | Check for cycles in DFA |
| Membership | Simulate DFA on input string |
| Equivalence (L₁ = L₂) | Compare minimized DFAs |
| Disjointness | Check L₁ ∩ L₂ = ∅ |
| Subset (L₁ ⊆ L₂) | Check L₁ ∩ L₂̅ = ∅ |

> **Note**: Universality (L = Σ*) is also decidable.

### 5. Minimization of DFA
- **Goal**: Reduce number of states while maintaining language
- **Method**: Partition refinement (Myhill-Nerode-based)
- **Result**: Unique (up to isomorphism) minimal DFA for each regular language

---

## Conclusion

Regular languages exhibit strong mathematical properties essential for both theoretical understanding and practical applications in compiler design and pattern matching. Mastery of closure properties, the pumping lemma, and decision procedures is crucial for the Delhi University Theory of Computation examination. Practice proving language regularity/irregularity and DFA minimization to ensure exam success.

**Suggested Reference**: "Introduction to Automata Theory, Languages, and Computation" by Hopcroft, Ullman & Motwani (as per DU syllabus)