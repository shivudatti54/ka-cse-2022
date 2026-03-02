# **Closure Properties of Regular Languages, Equivalence and Minimization of Automata, Applications of Regular Expressions**

### Closure Properties of Regular Languages

- **Closure Properties:**
  - **Complement Closure:** The complement of a regular language is also regular.
  - **Union Closure:** The union of two regular languages is regular.
  - **Intersection Closure:** The intersection of two regular languages is regular.
  - **Kleene Closure:** The Kleene star of a regular language is regular.
- **Definition:** A language is regular if it can be accepted by a finite automaton.

### Equivalence of Regular Languages

- **Equivalence Theorem:** Two regular languages are equivalent if and only if they accept the same language.
- **Pumping Lemma:** If a regular language is equivalent to the language accepted by a finite automaton, then there exists a pumping length such that any string of the form:
  - $w_0w_1...w_p$
  - $w_i \neq \epsilon$ for all $0 \leq i \leq p$
  - $|w_0w_1...w_p| > p$
  - Can be replaced by:
  - $w_0w_1...w_pw_0...w_p$
  - $|w_0w_1...w_pw_0...w_p| = |w_0w_1...w_p| + p$
  - Accepts the same language.

### Minimization of Automata

- **Minimization Theorem:** The minimal automaton for a regular language is unique.
- **Definition:** The minimal automaton is a finite automaton that accepts the same language as the original automaton.

### Applications of Regular Expressions

- **Regular Expressions:** A way to describe regular languages using a syntax.
- **Notation:** $\Sigma$ is the alphabet, $\Sigma^*$ is the set of all strings over $\Sigma$, and $L = \{w \in \Sigma^* | P(w)\}$ where $P(w)$ is a predicate.
- **Examples:**
  - $\Sigma = \{a, b\}$
  - $L = \{a^nb^n | n \geq 0\}$
  - $L = \{ab^nb^na^n | n \geq 0\}$

### Important Formulas and Definitions

- **Myhill-Nerode Equivalence Relation:** $\sim$ is an equivalence relation on the set of states of a finite automaton.
- **Cycle Space:** The space spanned by the vectors corresponding to the cycles in a finite automaton.
- **Thompson's Construction:** A way to construct a deterministic finite automaton from a regular expression.

### Important Theorems

- **Böhm-Cohn-Schützenberger Theorem:** The set of all regular languages is closed under union.
- **Kleene's Theorem:** The set of all regular languages is equal to the set of all languages accepted by finite automata.
