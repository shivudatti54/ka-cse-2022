# Syntax and Semantics of First Order Logic

## Introduction to First Order Logic

First Order Logic (FOL), also known as First Order Predicate Calculus, is a powerful formal system used in mathematics, philosophy, linguistics, and computer science (particularly Artificial Intelligence) for representing knowledge and reasoning about it. While Propositional Logic deals with simple propositions that are either true or false, FOL extends this by introducing objects, properties, relations, and quantifiers, making it vastly more expressive.

In AI, FOL serves as a foundation for knowledge representation, allowing intelligent agents to reason about their environment. The Wumpus World, introduced in the previous module, is a classic example where FOL's expressive power is needed to represent the agent's knowledge about pits, breezes, gold, and the Wumpus itself.

## Syntax of First Order Logic

The syntax of FOL defines the formal structure of well-formed formulas—the rules for constructing valid expressions in the language.

### Basic Elements

```
Constants:    a, b, c, ... (represent specific objects)
Variables:    x, y, z, ... (represent unspecified objects)
Functions:    f, g, h, ... (map objects to objects)
Predicates:   P, Q, R, ... (represent relations or properties)
Connectives:  ∧, ∨, ¬, →, ↔
Quantifiers:  ∀ (for all), ∃ (there exists)
Equality:     = (optional but commonly included)
Punctuation:  ( , ) , ,
```

### Terms

Terms are expressions that refer to objects in the domain:

- Constants are terms
- Variables are terms
- If f is an n-ary function symbol and t₁, t₂, ..., tₙ are terms, then f(t₁, t₂, ..., tₙ) is a term

**Examples:**

- Constants: `john`, `mary`, `book1`
- Variables: `x`, `y`, `z`
- Function application: `father(john)`, `successor(0)`

### Atomic Formulas

Atomic formulas are the simplest well-formed formulas:

- If P is an n-ary predicate symbol and t₁, t₂, ..., tₙ are terms, then P(t₁, t₂, ..., tₙ) is an atomic formula
- If t₁ and t₂ are terms, then t₁ = t₂ is an atomic formula (if equality is included)

**Examples:**

- `Student(john)`
- `Loves(mary, john)`
- `GreaterThan(5, 3)`
- `father(john) = michael`

### Well-Formed Formulas

Well-formed formulas (wffs) are defined recursively:

1. Every atomic formula is a wff
2. If φ is a wff, then ¬φ is a wff
3. If φ and ψ are wffs, then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) are wffs
4. If φ is a wff and x is a variable, then ∀x φ and ∃x φ are wffs
5. Nothing else is a wff

**Examples of valid wffs:**

- `∀x (Student(x) → ∃y (Book(y) ∧ Reads(x, y)))`
- `∃x (Student(x) ∧ ∀y (Book(y) → Reads(x, y)))`
- `¬∃x (Person(x) ∧ ∀y (Person(y) → Kills(x, y)))`

## Semantics of First Order Logic

While syntax defines the structure of formulas, semantics gives them meaning by specifying how to interpret these structures in relation to a domain of discourse.

### Interpretation

An interpretation I = (D, I₀) consists of:

1. A non-empty set D called the domain of discourse
2. An interpretation function I₀ that assigns:
   - To each constant symbol: an element of D
   - To each n-ary function symbol: a function from Dⁿ to D
   - To each n-ary predicate symbol: a relation on Dⁿ (a subset of Dⁿ)

**Example Interpretation:**
Let's interpret the formula `∀x ∃y Loves(x, y)`

Domain D = {Alice, Bob, Charlie}

Interpretation:

- Constants: None in this formula
- Predicate Loves: {(Alice, Bob), (Bob, Charlie), (Charlie, Alice)}

This interpretation makes the formula true since everyone loves someone.

### Variable Assignment

A variable assignment v assigns to each variable an element of the domain D. Given an interpretation I and variable assignment v, we can compute the truth value of any formula.

### Satisfaction Relation

The satisfaction relation ⊨ defines when a formula is true in an interpretation under a variable assignment:

1. I, v ⊨ P(t₁, ..., tₙ) iff (I(t₁), ..., I(tₙ)) ∈ I(P)
2. I, v ⊨ ¬φ iff I, v ⊭ φ
3. I, v ⊨ φ ∧ ψ iff I, v ⊨ φ and I, v ⊨ ψ
4. I, v ⊨ φ ∨ ψ iff I, v ⊨ φ or I, v ⊨ ψ
5. I, v ⊨ φ → ψ iff if I, v ⊨ φ then I, v ⊨ ψ
6. I, v ⊨ ∀x φ iff for all d ∈ D, I, v[x/d] ⊨ φ
7. I, v ⊨ ∃x φ iff there exists d ∈ D such that I, v[x/d] ⊨ φ

Where v[x/d] is the variable assignment that is identical to v except that it assigns d to x.

### Models, Validity, and Satisfiability

- A formula φ is **satisfiable** if there exists some interpretation I and variable assignment v such that I, v ⊨ φ
- A formula φ is **valid** (tautology) if for every interpretation I and every variable assignment v, I, v ⊨ φ
- An interpretation I is a **model** of a formula φ if for every variable assignment v, I, v ⊨ φ

## Quantifiers and Their Usage

### Universal Quantifier (∀)

∀x φ means "for all x, φ holds"

**Examples:**

- `∀x (Student(x) → Studies(x))` - "All students study"
- `∀x ∀y (Sibling(x, y) → Sibling(y, x))` - "Siblinghood is symmetric"

### Existential Quantifier (∃)

∃x φ means "there exists an x such that φ holds"

**Examples:**

- `∃x (Student(x) ∧ Smart(x))` - "There exists a smart student"
- `∃x ∀y (Professor(x) ∧ Teaches(x, y))` - "There's a professor who teaches everyone"

### Quantifier Scope and Bound Variables

The scope of a quantifier is the formula immediately following it. A variable is bound if it's within the scope of a quantifier with that variable; otherwise, it's free.

**Example:**
In `∀x (P(x) ∧ Q(x)) → ∃y R(x, y)`, the first x is bound, the second x is free, and y is bound.

### Nesting Quantifiers

The order of quantifiers matters significantly:

| Formula           | Meaning                             |
| ----------------- | ----------------------------------- |
| ∀x ∃y Loves(x, y) | Everyone loves someone              |
| ∃y ∀x Loves(x, y) | There's someone whom everyone loves |

## Comparison with Propositional Logic

| Aspect                       | Propositional Logic       | First Order Logic                  |
| ---------------------------- | ------------------------- | ---------------------------------- |
| **Expressiveness**           | Limited                   | Highly expressive                  |
| **Basic elements**           | Propositions              | Objects, relations, functions      |
| **Quantification**           | None                      | Universal and existential          |
| **Domain**                   | Not explicitly defined    | Explicit domain of discourse       |
| **Inference**                | Relatively simple         | More complex but powerful          |
| **Knowledge representation** | Suitable for simple facts | Suitable for complex relationships |

## Examples and Applications

### Example 1: Family Relationships

```
Constants: john, mary
Functions: father, mother
Predicates: Male, Female, Parent, Child, Sibling

Axioms:
1. ∀x ∀y (Child(x, y) ↔ Parent(y, x))
2. ∀x ∀y (Sibling(x, y) ↔ ∃z (Parent(z, x) ∧ Parent(z, y) ∧ x ≠ y))
3. Male(john)
4. Female(mary)
5. Parent(john, father(john))
```

### Example 2: The Wumpus World

```
Predicates:
- Breeze(x, y): There's a breeze at location (x, y)
- Pit(x, y): There's a pit at location (x, y)
- Gold(x, y): There's gold at location (x, y)
- Wumpus(x, y): The Wumpus is at location (x, y)

Axioms:
1. ∀x ∀y (Breeze(x, y) ↔ ∃u ∃v (Adjacent((x,y), (u,v)) ∧ Pit(u, v)))
2. ∀x ∀y (Gold(x, y) → Glitters(x, y))
3. ¬Wumpus(1,1) ∧ ¬Pit(1,1)  // Starting position is safe
```

### Example 3: Mathematical Concepts

```
Predicates:
- Number(x): x is a number
- LessThan(x, y): x is less than y
- Prime(x): x is a prime number

Axioms:
1. ∀x (Number(x) → ∃y (Number(y) ∧ LessThan(x, y)))  // No greatest number
2. ∀x (Prime(x) ↔ (Number(x) ∧ x > 1 ∧ ∀y ∀z (y*z = x → (y=1 ∨ z=1 ∨ y=x ∨ z=x))))
```

## Common Pitfalls and Misconceptions

1. **Confusing ∀ and ∃**: Remember that ∀x ∃y φ means "for every x, there's some y" while ∃y ∀x φ means "there's some y that works for all x."

2. **Misplacing parentheses**: Quantifiers apply to the immediately following formula. ∀x P(x) ∧ Q(x) means (∀x P(x)) ∧ Q(x), not ∀x (P(x) ∧ Q(x)).

3. **Empty domains**: By convention, the domain of discourse is never empty in FOL.

4. **Free variables**: Formulas with free variables are not statements—they become statements only when all variables are bound.

## Exam Tips

1. **When translating natural language to FOL**, identify the objects, properties, relations, and quantifiers first.

2. **For semantic questions**, construct small example interpretations to test formulas.

3. **Remember the precedence rules**: Quantifiers have higher precedence than connectives. ∀x P(x) → Q(x) means (∀x P(x)) → Q(x), not ∀x (P(x) → Q(x)).

4. **For showing validity or satisfiability**, try to find counterexamples for validity proofs and examples for satisfiability proofs.

5. **Practice with different domains**: Work with mathematical domains, social domains, and spatial domains to build flexibility.

6. **Pay attention to equality**: Remember that = is a special predicate with fixed meaning (reflexive, symmetric, transitive).

7. **For nested quantifiers**, work from the outside in when interpreting their meaning.
