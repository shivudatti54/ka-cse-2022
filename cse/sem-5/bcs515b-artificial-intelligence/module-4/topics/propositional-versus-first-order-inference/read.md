# Propositional versus First-Order Inference

## Introduction

Inference in artificial intelligence refers to the process of deriving new facts from known facts using logical reasoning. Two fundamental logical frameworks used for representation and reasoning are **Propositional Logic** and **First-Order Logic** (also known as Predicate Logic). Understanding the differences between these two approaches is crucial for designing intelligent systems capable of representing real-world knowledge and performing automated reasoning.

Propositional Logic deals with propositions that are either true or false, without considering the internal structure of statements. While it provides a foundation for logical reasoning, it suffers from significant limitations when representing complex real-world scenarios. First-Order Logic extends propositional logic by incorporating objects, predicates, and quantifiers, enabling more expressive and concise knowledge representation. This module explores the inference mechanisms in both logics, compares their capabilities, and discusses their practical applications in AI systems.

## Key Concepts

### Propositional Logic

Propositional Logic is the simplest form of logical representation where statements (propositions) can be either true (T) or false (F). The basic elements include:

- **Atomic propositions**: Simple statements like "It is raining" (R) or "The ground is wet" (W)
- **Logical connectives**: ∧ (AND), ∨ (OR), ¬ (NOT), → (implication), ↔ (biconditional)
- **Knowledge base**: A set of propositional formulas representing known facts

**Inference in Propositional Logic** involves using inference rules to derive new propositions from existing ones. The fundamental inference rule is **Modus Ponens**: From P and (P → Q), infer Q.

**Limitations of Propositional Logic**:

1. Cannot represent general rules about categories of objects
2. Requires separate propositions for each instance
3. Lacks ability to express quantities (all, some, none)
4. Leads to combinatorial explosion in knowledge bases

For example, to state "All humans are mortal," propositional logic would require separate statements for each human: "Socrates is human" → "Socrates is mortal," "Plato is human" → "Plato is mortal," and so on.

### First-Order Logic

First-Order Logic (FOL) extends propositional logic by introducing:

- **Objects**: Individual entities in the domain (e.g., Socrates, John, cat)
- **Predicates**: Properties or relations between objects (e.g., Human(x), Likes(x,y))
- **Quantifiers**: ∀ (universal) and ∃ (existential)
- **Variables**: Placeholders for objects (x, y, z)

The statement "All humans are mortal" can be simply expressed as: ∀x (Human(x) → Mortal(x))

**Syntax of FOL**:

- Terms: Constants (Socrates), Variables (x), Functions (Father(x))
- Atomic formulas: Predicates applied to terms (Human(Socrates))
- Complex formulas: Using connectives and quantifiers

**Inference in First-Order Logic** involves more complex mechanisms:

1. **Universal Instantiation**: From ∀x P(x), infer P(c) for any constant c
2. **Existential Instantiation**: From ∃x P(x), infer P(c) for a new constant c
3. **Modus Ponens** (generalized): From P → Q and P, infer Q
4. **Unification**: The process of making two atomic formulas identical by substituting variables

### Key Differences: Propositional vs First-Order Inference

| Aspect                   | Propositional Logic      | First-Order Logic                     |
| ------------------------ | ------------------------ | ------------------------------------- |
| **Expressiveness**       | Limited to boolean facts | Can express relationships, quantities |
| **Inference Complexity** | NP-complete              | Semi-decidable                        |
| **Representation**       | Requires ground atoms    | Uses variables and quantifiers        |
| **Scalability**          | Poor for large domains   | Better for general rules              |
| **Automation**           | Easier to implement      | More complex algorithms               |

### Unification Algorithm

Unification is a fundamental operation in FOL inference. It finds a substitution that makes two atomic formulas identical.

**Unification Algorithm Steps**:

1. If the two expressions are identical, return empty substitution
2. If one is a variable, apply occurs check and return appropriate substitution
3. If both are compound expressions, unify their operators and then their arguments
4. If predicates or functions differ, unification fails

**Example**: Unify P(x, f(y)) and P(g(z), f(a))

- Result: {x/g(z), y/a}

### Resolution in First-Order Logic

Resolution is a complete inference rule for FOL. The **Resolution Principle** states:

If (A ∨ B) and (¬B ∨ C) are true, then (A ∨ C) is true.

For first-order resolution:

1. Convert knowledge base to clause form (conjunctive normal form)
2. Negate the goal statement
3. Apply resolution repeatedly until either:

- Empty clause is derived (proof by contradiction)
- No more resolutions possible (failure)

### Forward and Backward Chaining

Both propositional and first-order systems use forward and backward chaining:

- **Forward Chaining**: Start from known facts, apply rules forward to derive conclusions
- **Backward Chaining**: Start from goal, work backwards to find supporting facts

Horn clauses (at most one positive literal) enable efficient forward and backward chaining in both logics.

## Examples

### Example 1: Propositional Logic Inference

Given:

- P → Q (If it rains, the ground gets wet)
- P (It is raining)

Using Modus Ponens, we infer: Q (The ground is wet)

This requires explicit propositional symbols P and Q. If we have 100 different situations involving rain, we need 100 different propositions.

### Example 2: First-Order Logic Inference

Given:

- ∀x (Rains(x) → Wet(x)) (For all x, if it rains at x, ground is wet at x)
- Rains(LocationA)

Using Universal Instantiation and Modus Ponens:

1. Instantiate: Rains(LocationA) → Wet(LocationA)
2. Apply Modus Ponens with Rains(LocationA)
3. Infer: Wet(LocationA)

This single rule works for any location!

### Example 3: Resolution Proof in FOL

Problem: Prove that Socrates is mortal given:

- ∀x (Human(x) → Mortal(x))
- Human(Socrates)

**Proof by Resolution**:

1. Convert to clause form:

- ¬Human(x) ∨ Mortal(x)
- Human(Socrates)

2. Negate goal: ¬Mortal(Socrates)
3. Resolution steps:

- Resolve ¬Human(x) ∨ Mortal(x) with Human(Socrates) → Mortal(Socrates)
- Resolve Mortal(Socrates) with ¬Mortal(Socrates) → Empty clause

4. QED: Socrates is mortal

## Exam Tips

1. **Remember the key limitation** of propositional logic: it cannot represent general rules about categories—it requires explicit facts for each instance.

2. **Know the quantifier inference rules**: Universal Instantiation and Existential Instantiation are fundamental to FOL inference.

3. **Unification is crucial**: Be able to perform unification on simple predicate formulas and identify when unification fails (especially the occurs check).

4. **Resolution is complete**: For first-order logic, resolution is sound and complete for entailment.

5. **Expressiveness comparison**: FOL can express "all," "some," "none" using quantifiers—propositional cannot.

6. **Horn clauses enable efficiency**: Forward and backward chaining work efficiently on Horn clause knowledge bases in both logics.

7. **Modus Ponens applies to both**: The basic inference rule P → Q, P ⊢ Q works in both propositional and first-order logic.

8. **Time complexity matters**: Propositional inference is NP-complete, while FOL is semi-decidable (no guarantee of finding proof in finite time).
