# Resolution in Logic

## Introduction

Resolution is a fundamental inference rule in mathematical logic and artificial intelligence that serves as the cornerstone for automated theorem proving and logic programming. Developed by Alan Robinson in 1965, resolution provides a complete inference mechanism for propositional logic and first-order predicate logic. Unlike other inference rules such as modus ponens or unit resolution, resolution operates on clauses in conjunctive normal form (CNF) and can derive new clauses through a systematic unification process.

The importance of resolution in computer science cannot be overstated. It forms the theoretical basis for Prolog (logic programming language), automated reasoning systems, knowledge representation, and expert systems. In 's Artificial Intelligence curriculum, resolution serves as the primary method for logical inference, enabling computers to automatically prove theorems and derive conclusions from given facts and rules. Understanding resolution is essential for any CSE engineer working with AI, knowledge-based systems, or formal methods.

## Key Concepts

### 1. Clause Form and Conjunctive Normal Form (CNF)

Before applying resolution, any logical formula must be converted to clause form. A clause is a disjunction of literals (atoms or their negations). The conversion process involves several steps:

- **Eliminate implications**: Replace (P → Q) with (¬P ∨ Q)
- **Move negation inward**: Apply De Morgan's laws and eliminate double negations
- **Standardize variables**: Rename variables to avoid conflicts
- **Skolemize**: Remove existential quantifiers by introducing Skolem functions/constants
- **Drop universal quantifiers**: All remaining variables are universally quantified
- **Convert to CNF**: Transform to conjunction of disjunctions
- **Represent as clauses**: Each disjunct becomes a clause

### 2. Resolution in Propositional Logic

The resolution rule for propositional logic operates on two clauses containing complementary literals. If one clause contains literal P and another contains ¬P, we can resolve them to derive a new clause called the resolvent.

**Resolution Rule**: Given two clauses:

- C₁: (L₁ ∨ L₂ ∨ ... ∨ Lₘ ∨ P)
- C₂: (M₁ ∨ M₂ ∨ ... ∨ Mₙ ∨ ¬P)

The resolvent is: (L₁ ∨ L₂ ∨ ... ∨ Lₘ ∨ M₁ ∨ M₂ ∨ ... ∨ Mₙ)

**Example**: Resolve (P ∨ Q) and (¬P ∨ R)

- Complementary literals: P and ¬P
- Resolvent: (Q ∨ R)

### 3. Unification in Predicate Logic

Unification is the process of finding a substitution that makes two literals identical. It is essential for resolution in first-order logic.

**Most General Unifier (MGU)**: The substitution that makes two literals equal with the most general (least restrictive) binding.

**Unification Algorithm**:

1. If terms are identical, return empty substitution
2. If one is a variable, apply occurs check, return substitution
3. If both are compound terms, unify their functors and arguments recursively
4. If terms differ in structure or function, unification fails

**Example**: Unify P(x, f(y)) and P(g(a), f(b))

- MGU: {x/g(a), y/b}

### 4. Resolution in Predicate Logic

For first-order logic, resolution combines unification with the propositional resolution rule.

**Binary Resolution**: Given two clauses C₁ and C₂ with complementary literals L₁ and L₂, where MGU θ unifies L₁ and L₂:

- Resolvent = (C₁θ - L₁θ) ∨ (C₂θ - L₂θ)

**Example**: Given clauses:

- C₁: P(x) ∨ Q(x)
- C₂: ¬P(f(y)) ∨ R(y)

Resolve using MGU {x/f(y)}:

- Resolvent: Q(f(y)) ∨ R(y)

### 5. Resolution Strategies

Several strategies control the resolution search space:

1. **Unit Resolution**: At least one parent clause must be a unit clause (single literal)
2. **Set of Support**: At least one parent must contain a negated literal from the original goal
3. **Linear Resolution**: One parent must be the resolvent from the previous step
4. **Input Resolution**: One parent must be from the original set of clauses
5. **Subsumption**: If one clause subsumes another, the more specific clause is removed

### 6. Horn Clauses and Modus Ponens

A Horn clause contains at most one positive literal. Horn clauses are important because:

- They can be efficiently processed
- They support forward and backward chaining
- They form the basis of logic programming (Prolog)

**Prolog Syntax**: Facts are unit Horn clauses; rules are non-unit Horn clauses.

### 7. Refutation Resolution (Proof by Contradiction)

To prove a statement using resolution, we:

1. Negate the statement to be proved
2. Add all known facts and the negated statement as clauses
3. Apply resolution repeatedly until deriving the empty clause (contradiction)
4. The empty clause (□) indicates inconsistency, proving the original statement

## Examples

### Example 1: Propositional Resolution

**Problem**: Given facts:

1. (P → Q)
2. (Q → R)
3. P

Prove: R

**Solution**:

Step 1: Convert to CNF

- (P → Q) ≡ (¬P ∨ Q)
- (Q → R) ≡ (¬Q ∨ R)

Step 2: Add negated goal (¬R) as clause

- Clauses: {¬P ∨ Q, ¬Q ∨ R, P, ¬R}

Step 3: Apply resolution

1. Resolve (¬P ∨ Q) and P:

- Resolvent: Q

2. Resolve Q and (¬Q ∨ R):

- Resolvent: R

3. Resolve R and ¬R:

- Resolvent: □ (empty clause)

Since we derived the empty clause, the original statement is proved.

### Example 2: Predicate Logic Resolution

**Problem**: Given:

- All humans are mortal (∀x)(Human(x) → Mortal(x))
- Socrates is human (Human(Socrates))

Prove: Socrates is mortal

**Solution**:

Step 1: Convert to clause form

- ∀x(¬Human(x) ∨ Mortal(x))
- Human(Socrates)

Step 2: Negate goal Mortal(Socrates) and convert

- ¬Mortal(Socrates)

Step 3: Clauses:

1. ¬Human(x) ∨ Mortal(x)
2. Human(Socrates)
3. ¬Mortal(Socrates)

Step 4: Resolution

1. Resolve clause 1 and 2 with MGU {x/Socrates}:

- Resolvent: Mortal(Socrates)

2. Resolve Mortal(Socrates) with clause 3:

- Resolvent: □

### Example 3: Unification

**Problem**: Find MGU for:

- P(f(x), g(y, a))
- P(f(h(z)), g(z, b))

**Solution**:

Step 1: Match functors: P(f(...), g(...)) matches P(f(...), g(...)) ✓

Step 2: First argument:

- f(x) and f(h(z))
- x and h(z)
- MGU: {x/h(z)}

Step 3: Apply substitution to second argument:

- g(y, a) becomes g(y, a)
- g(z, b) becomes g(z, b)

Step 4: Second argument:

- g(y, a) and g(z, b)
- y and z, a and b
- Cannot unify (a ≠ b)

**Result**: Unification FAILS - these two literals cannot be unified.

## Exam Tips

1. **Know the conversion steps**: Remember the exact sequence for converting to clause form (implication elimination → negation movement → standardization → skolemization → universal quantifier removal → CNF conversion)

2. **Practice unification**: Be thorough with the unification algorithm and always apply the occurs check (variable cannot be substituted with a term containing that variable)

3. **Resolution produces new clauses**: The resolvent contains all literals except the complementary pair

4. **Empty clause means contradiction**: Deriving □ proves the negated statement leads to inconsistency, hence the original is true

5. **Horn clauses are efficient**: Remember that Prolog programs consist of Horn clauses

6. **Strategy selection matters**: Unit resolution is complete for Horn clauses but not for general clauses

7. **Understand subsumption**: A clause C₁ subsumes C₂ if there exists a substitution θ such that C₁θ ⊆ C₂

8. **Skolem functions preserve satisfiability**: Remember that skolemization preserves the satisfiability but not the truth of the original formula
