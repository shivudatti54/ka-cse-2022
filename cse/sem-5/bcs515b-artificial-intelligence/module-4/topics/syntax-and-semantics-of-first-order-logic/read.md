# Syntax and Semantics of First-Order Logic

## Introduction

First-Order Logic (FOL), also known as Predicate Logic or First-Order Predicate Calculus, is a powerful logical system that extends Propositional Logic by introducing quantifiers, predicates, and variables. While propositional logic deals with complete statements that are either true or false, first-order logic allows us to represent and reason about objects, their properties, and relationships between them.

The importance of First-Order Logic in computer science cannot be overstated. It serves as the foundation for various critical applications including automated theorem proving, knowledge representation, formal verification, database query languages (like SQL), and artificial intelligence. In software engineering, FOL is used in formal methods for specifying and verifying program properties. For CSE students, understanding FOL is essential as it forms the theoretical basis for many advanced topics in compilers, artificial intelligence, and software engineering.

This module covers two fundamental aspects of First-Order Logic: syntax (the formal structure of well-formed formulas) and semantics (the meaning and truth values assigned to these formulas). A thorough grasp of both aspects is crucial for solving problems related to logical inference, theorem proving, and formal specification.

## Key Concepts

### 1. Alphabet of First-Order Logic

The alphabet of FOL consists of the following symbols:

- **Logical Connectives**: ¬ (not), ∧ (and), ∨ (or), → (implication), ↔ (biconditional)
- **Quantifiers**: ∀ (universal - "for all"), ∃ (existential - "there exists")
- **Variables**: x, y, z, w, etc. (typically lowercase letters)
- **Constant Symbols**: a, b, c, etc. (represent specific objects)
- **Function Symbols**: f, g, h, etc. (represent functions mapping tuples to objects)
- **Predicate Symbols**: P, Q, R, etc. (represent properties or relations)
- **Parentheses**: ( and ) for grouping
- **Equality Symbol**: = (optional, but commonly included)

### 2. Terms

A **term** is a syntactically valid expression that denotes an object. Terms are defined recursively:

- Every constant symbol is a term
- Every variable is a term
- If f is an n-ary function symbol and t₁, t₂, ..., tₙ are terms, then f(t₁, t₂, ..., tₙ) is a term
- Nothing else is a term

**Examples**: x, f(x, y), g(a), successor(successor(0))

### 3. Atomic Formulas

An **atomic formula** (atom) is formed by:

- If P is an n-ary predicate symbol and t₁, t₂, ..., tₙ are terms, then P(t₁, t₂, ..., tₙ) is an atomic formula
- If equality is included, t₁ = t₂ is an atomic formula

**Examples**: P(x), Likes(x, y), GreaterThan(x, 5), x = y

### 4. Well-Formed Formulas (WFFs)

The set of well-formed formulas is defined recursively:

- Every atomic formula is a WFF
- If φ is a WFF, then ¬φ is a WFF
- If φ and ψ are WFFs, then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) are WFFs
- If φ is a WFF and x is a variable, then ∀x φ and ∃x φ are WFFs
- Nothing else is a WFF

**Important Note**: In ∀x φ and ∃x φ, the quantifier binds the variable x. The occurrence of x within φ is called **bound**. Variables that are not bound are **free**.

### 5. Scope of Quantifiers

In formulas like ∀x P(x) or ∃x (P(x) → Q(y)), the quantifier's **scope** is the formula immediately following it. A variable is bound if it falls within the scope of its quantifier.

**Example**: In ∀x (P(x) → ∃y Q(x, y)), the scope of ∀x is (P(x) → ∃y Q(x, y)), and the scope of ∃y is Q(x, y).

### 6. Semantics - Interpretations

The **semantics** of FOL assigns meaning to formulas through interpretations. An interpretation I consists of:

- **Domain (D)**: A non-empty set of objects
- **Assignment to Constant Symbols**: Each constant symbol c is assigned an element cᵢ ∈ D
- **Assignment to Function Symbols**: Each n-ary function symbol f is assigned a function fᵢ: Dⁿ → D
- **Assignment to Predicate Symbols**: Each n-ary predicate symbol P is assigned a relation Pᵢ ⊆ Dⁿ

### 7. Semantics - Variable Assignments

A **variable assignment** s maps each variable to an element in the domain. The truth value of terms and formulas depends on both the interpretation and the variable assignment.

**Term Valuation**: The value of a term under (I, s):

- If t is a constant c, val(t) = cᵢ
- If t is a variable x, val(t) = s(x)
- If t is f(t₁, ..., tₙ), val(t) = fᵢ(val(t₁), ..., val(tₙ))

### 8. Truth of Formulas

The truth of formulas is defined recursively:

- **Atomic Formula**: P(t₁, ..., tₙ) is true iff (val(t₁), ..., val(tₙ)) ∈ Pᵢ
- **Negation**: ¬φ is true iff φ is false
- **Conjunction**: φ ∧ ψ is true iff both φ and ψ are true
- **Disjunction**: φ ∨ ψ is true iff at least one is true
- **Implication**: φ → ψ is true iff φ is false or ψ is true
- **Universal Quantification**: ∀x φ is true iff φ is true for all possible values of x in D
- **Existential Quantification**: ∃x φ is true iff there exists at least one value of x in D for which φ is true

### 9. Valid, Satisfiable, and Unsatisfiable Formulas

- **Valid (Tautologically True)**: A formula is valid if it is true under every interpretation (⊨ φ)
- **Satisfiable**: A formula is satisfiable if there exists some interpretation that makes it true
- **Unsatisfiable (Contradictory)**: A formula is unsatisfiable if no interpretation makes it true
- **Logical Consequence**: φ ⊨ ψ means ψ is true in every interpretation where φ is true

## Examples

### Example 1: Constructing and Evaluating a WFF

**Problem**: Given interpretation I with domain D = {1, 2}, constant a = 1, predicate P = {(1,), (2,)}, evaluate P(a) and ¬P(a).

**Solution**:

Step 1: Identify the term and predicate

- Term: a (constant symbol)
- Predicate: P (unary predicate)

Step 2: Evaluate P(a)

- val(a) = 1 (assignment to constant a)
- P(a) is true iff 1 ∈ Pᵢ = {(1,), (2,)}
- Since 1 ∈ Pᵢ, P(a) is TRUE

Step 3: Evaluate ¬P(a)

- ¬P(a) is true iff P(a) is false
- Since P(a) is true, ¬P(a) is FALSE

### Example 2: Evaluating Quantified Formulas

**Problem**: Consider domain D = {1, 2, 3}, predicate Q(x, y) = {(1,1), (2,2), (3,3)} (identity relation). Evaluate ∀x ∃y Q(x, y) and ∃y ∀x Q(x, y).

**Solution**:

Step 1: Evaluate ∀x ∃y Q(x, y)

- For x = 1: Does ∃y Q(1, y) hold? Yes, y = 1 gives Q(1,1) which is in the relation
- For x = 2: Does ∃y Q(2, y) hold? Yes, y = 2 gives Q(2,2)
- For x = 3: Does ∃y Q(3, y) hold? Yes, y = 3 gives Q(3,3)
- Since for every x, there exists a y making Q(x, y) true, ∀x ∃y Q(x, y) is TRUE

Step 2: Evaluate ∃y ∀x Q(x, y)

- We need to find a single y that works for all x
- For y = 1: Q(1,1) true, but Q(2,1) is NOT in relation (only (2,2) exists)
- For y = 2: Q(2,2) true, but Q(1,2) is NOT in relation
- For y = 3: Q(3,3) true, but Q(1,3) is NOT in relation
- No single y works for all x, so ∃y ∀x Q(x, y) is FALSE

**Important Observation**: ∀x ∃y Q(x, y) ≠ ∃y ∀x Q(x, y) - the order of quantifiers matters!

### Example 3: Determining Satisfiability

**Problem**: Determine whether the formula ∀x P(x) → ∃x P(x) is valid.

**Solution**:

Step 1: Analyze logically

- The formula states: "If all x have property P, then there exists some x with property P"
- This is intuitively true because if every element satisfies P, then certainly some element satisfies P

Step 2: Formal verification

- Case 1: ∀x P(x) is TRUE
- Then every element in domain satisfies P
- Therefore, ∃x P(x) is TRUE
- Implication: TRUE → TRUE = TRUE
- Case 2: ∀x P(x) is FALSE
- Implication: FALSE → (anything) = TRUE
- In all cases, the formula evaluates to TRUE

**Conclusion**: ∀x P(x) → ∃x P(x) is VALID (tautologically true in FOL)

## Exam Tips

1. **Understand Bound vs Free Variables**: Remember that a variable is bound only if it falls within the scope of a quantifier. Free variables require an assignment to determine truth values.

2. **Quantifier Order Matters**: The order of different quantifiers (∀ and ∃) cannot be swapped without potentially changing the meaning. ∀x ∃y R(x, y) is generally different from ∃y ∀x R(x, y).

3. **De Morgan's Laws for Quantifiers**: Remember that ¬∀x φ ≡ ∃x ¬φ and ¬∃x φ ≡ ∀x ¬φ. These are frequently used in proof and simplification problems.

4. **Evaluating Implications**: In FOL, φ → ψ is false only when φ is true and ψ is false. This is crucial for determining truth values of implications.

5. **Know the Definitions**: Be clear about the differences between valid, satisfiable, and unsatisfiable formulas. These are fundamental concepts that appear frequently in exams.

6. **Scope of Quantifiers**: When drawing syntax trees or analyzing complex formulas, always correctly identify the scope of each quantifier to determine which variables are bound.

7. **Interpreting Terms**: Remember the recursive definition of term valuation - constants map to domain elements, variables to assignments, and function symbols to functions.

8. **Practice with Interpretations**: When solving problems, explicitly state the interpretation (domain, constant assignments, predicate meanings) before evaluating formulas.
