# Propositional and First-Order Logic

## Introduction
Logic serves as the foundation of knowledge representation and reasoning in Artificial Intelligence. It provides a formal framework for encoding knowledge and deriving conclusions through inference mechanisms. This summary covers the two fundamental logical systems: Propositional Logic and First-Order Logic (FOL), essential for the Delhi University AI syllabus.

---

## Propositional Logic

### Overview
- **Definition**: Logic dealing with propositions (statements that are either True or False)
- **Purpose**: Represents facts that can be true or false, enabling basic reasoning

### Syntax
- **Atomic Propositions**: Basic propositions (P, Q, R)
- **Logical Connectives**:
  - ¬ (Negation/NOT)
  - ∧ (Conjunction/AND)
  - ∨ (Disjunction/OR)
  - → (Implication/IF-THEN)
  - ↔ (Biconditional/IFF)

### Semantics
- **Truth Tables**: Define truth values for all connectives
- **Interpretation/Model**: Assignment of truth values to propositions
- **Tautology**: Always true (e.g., P ∨ ¬P)
- **Contradiction**: Always false (e.g., P ∧ ¬P)
- **Satisfiable**: Can be true under some interpretation

### Inference Rules
- **Modus Ponens**: From P and P → Q, infer Q
- **Modus Tollens**: From P → Q and ¬Q, infer ¬P
- **Resolution**: Clause-based inference rule for automated reasoning
- **Soundness**: If premises are true, conclusion is true
- **Completeness**: If conclusion follows, it can be derived

---

## First-Order Logic (FOL)

### Need for FOL
- Propositional Logic lacks **expressiveness** (cannot represent relationships like "All humans are mortal")
- FOL introduces **objects**, **predicates**, and **quantifiers**

### Syntax
- **Constants**: Specific objects (e.g., John, Mumbai)
- **Variables**: Represent objects (e.g., x, y)
- **Predicates**: Properties or relations (e.g., Mortal(x), Likes(x, y))
- **Functions**: Map objects to objects (e.g., FatherOf(x))
- **Quantifiers**:
  - ∀ (Universal): "For all"
  - ∃ (Existential): "There exists"

### Semantics
- **Interpretation**: Assigns meaning to constants, predicates, and functions
- **Herbrand Base**: Set of all ground atoms
- **Herbrand Model**: Minimal model satisfying clauses

### Key Differences from Propositional Logic
| Feature | Propositional | First-Order |
|---------|--------------|-------------|
| Expressiveness | Limited | High |
| Objects | Not supported | Supported |
| Quantifiers | Not supported | Supported |
| Reasoning | Simple | Complex |

### Inference in FOL
- **Universal Instantiation**: Substitute ∀x P(x) with P(c)
- **Existential Instantiation**: Replace ∃x P(x) with P(c) for new constant c
- **Generalized Modus Ponens**: Combines unification and Modus Ponens
- **Resolution**: Extended to handle quantifiers through unification

---

## Applications in AI
- **Knowledge Representation**: Encoding facts about the world
- **Automated Reasoning**: Deriving new facts from known information
- **Expert Systems**: Logical inference for decision-making
- **Natural Language Processing**: Semantic representation
- **Planning**: Logical formulation of goals and actions

---

## Conclusion
Propositional Logic provides a basic framework for reasoning with truth values, while First-Order Logic extends this to handle objects and relationships, making it significantly more powerful for AI applications. Mastery of syntax, semantics, and inference rules is crucial for exam success and practical AI implementation.