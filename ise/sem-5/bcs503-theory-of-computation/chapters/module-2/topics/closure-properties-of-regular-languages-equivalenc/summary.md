# **Closure Properties of Regular Languages, Equivalence and Minimization of Automata, Applications of Regular Expressions**

### Closure Properties

- **Closure Properties of Regular Languages:**
  - **Union:** $L_1 \cup L_2 \in \text{REG}$ if $L_1, L_2 \in \text{REG}$
  - **Intersection:** $L_1 \cap L_2 \in \text{REG}$ if $L_1, L_2 \in \text{REG}$
  - ** Kleene Closure:** $\Sigma^* \in \text{REG}$
  - **Complement:** $L \subseteq \Sigma^* \in \text{REG}$ if $L \in \text{REG}$

### Equivalence and Minimization of Automata

- **Equivalence of Automata:**
  - Two automata $M_1$ and $M_2$ are equivalent if and only if $L(M_1) = L(M_2)$
  - Equivalence can be checked using the product of automata
- **Minimization of Automata:**
  - Minimization of a deterministic finite automaton (DFA) can be done using the power set construction or the Myhill-Nerode equivalence
  - Minimization of a nondeterministic finite automaton (NFA) can be done using the pumping lemma

### Applications of Regular Expressions

- **Regular Expression to DFA:**
  - Can be done using the Nondeterministic Finite Automaton (NFA) construction
- **Regular Expression to NFA:**
  - Can be done using the Thompson's construction
- **Minimization of Regular Expressions:**
  - Can be done using the minimization of the NFA constructed from the regular expression

### Important Formulas, Definitions, and Theorems

- **Regular Expression:** A string of characters that can be used to describe a set of strings.
- **Deterministic Finite Automaton (DFA):** A finite automaton that can only be in one state at a time.
- **Nondeterministic Finite Automaton (NFA):** A finite automaton that can be in multiple states at a time.
- **Equivalence Theorem:** Two automata are equivalent if and only if they accept the same set of strings.
- **Pumping Lemma:** A lemma that states that every regular language has a pumping length.

Note: This summary is a concise revision guide and is not a comprehensive treatment of the subject.
