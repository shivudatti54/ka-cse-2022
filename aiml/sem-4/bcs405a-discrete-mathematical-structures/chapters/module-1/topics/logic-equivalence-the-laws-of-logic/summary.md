# Logic Equivalence – The Laws of Logic

### Definitions and Notations

- **Logical Equivalence**: Two propositions or expressions are logically equivalent if they have the same truth value in every possible interpretation.
- **¬** (Negation)
- **∧** (Conjunction)
- **∨** (Disjunction)
- **→** (Implication)
- **⊥** (Contradiction)
- **⊤** (Tautology)

### Laws of Logic

#### Laws of Identity

- **Law of Identity**: A proposition is logically equivalent to itself. ($p \Leftrightarrow p$)
- **Law of Non-Contradiction**: A proposition cannot be both true and false. ($p \Leftrightarrow \neg p$)
- **Law of Excluded Middle**: A proposition is either true or false. ($p \Leftrightarrow \neg p \lor p$)

#### Laws of Negation

- **De Morgan's Laws**:
  - $\neg(p \land q) \Leftrightarrow \neg p \lor \neg q$
  - $\neg(p \lor q) \Leftrightarrow \neg p \land \neg q$
- **Double Negation Law**: $\neg \neg p \Leftrightarrow p$
- **Law of Universality**: $\neg \forall x p \Leftrightarrow \exists x \neg p$
- **Law of particularity**: $\neg \exists x p \Leftrightarrow \forall x \neg p$

#### Laws of Conjunction

- **Commutative Law**: $p \land q \Leftrightarrow q \land p$
- **Associative Law**: $(p \land q) \land r \Leftrightarrow p \land (q \land r)$
- **Distributive Law**: $p \land (q \lor r) \Leftrightarrow (p \land q) \lor (p \land r)$

#### Laws of Disjunction

- **Commutative Law**: $p \lor q \Leftrightarrow q \lor p$
- **Associative Law**: $(p \lor q) \lor r \Leftrightarrow p \lor (q \lor r)$

#### Laws of Implication

- **Law of Excluded Middle**: $p \Rightarrow q \Leftrightarrow \neg p \lor q$
- **Law of Contrapositive**: $p \Rightarrow q \Leftrightarrow \neg q \Rightarrow \neg p$

#### Laws of Equivalence

- **Law of Equivalence**: $p \Leftrightarrow q \Leftrightarrow (p \land q) \lor (\neg p \land \neg q)$
- **Law of Conjunction with Negation**: $p \Leftrightarrow q \Leftrightarrow (p \land q) \lor (p \land \neg q) \lor (\neg p \land q)$

### Important Formulas and Theorems

- **Fitch's Theorem**: All the laws of logic can be derived from the laws of non-contradiction and excluded middle.
- **Hilbert's Axioms**: A set of 9 axioms that form the basis of modern logic.
