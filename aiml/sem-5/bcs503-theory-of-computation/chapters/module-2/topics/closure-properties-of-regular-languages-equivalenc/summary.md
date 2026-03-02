# **Closure Properties of Regular Languages, Equivalence and Minimization of Automata, Applications of Regular Expressions**

### Closure Properties of Regular Languages

- **Closure Properties:**
  - **Closure under Union:** If A and B are regular languages, then A ∪ B is regular.
  - **Closure under Concatenation:** If A and B are regular languages, then AB is regular.
  - **Closure under Kleene Star:** If A is a regular language, then A\* is regular.
  - **Closure under Complement:** If A is a regular language, then A' (complement) is regular.

### Equivalence of Regular Languages

- **Equivalence Theorem:** Two regular languages A and B are equivalent if and only if they have the same language set and same number of states in their minimal automata.

### Minimization of Automata

- **Minimization Theorem:** Every regular language can be represented by a minimal automaton.

### Applications of Regular Expressions

- **Regular Expression Idempotent Laws:**
  - (A ∪ B) ∪ A = A ∪ (B ∪ A)
  - A ∪ (A* B) = A* ∪ (A B)
- **Regular Expression De Morgan's Law:**
  - (A ∩ B)' = A' ∪ B'
  - (A ∪ B)' = A' ∩ B'

### Important Formulas and Theorems

- **Myhill-Nerode Equivalence Theorem:** Two automata are equivalent if and only if they accept the same language and have the same number of states.
- **Kleene's Theorem:** A regular language can be represented by a finite automaton with a finite number of states.

### Quick Revision Key Points

- Regular languages are closed under union, concatenation, Kleene star, and complement.
- Equivalence of regular languages is determined by the number of states in their minimal automata.
- Minimization of automata is possible using the minimization theorem.
- Regular expressions can be simplified using idempotent laws and De Morgan's law.
