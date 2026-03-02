# Resolution in AI

## Introduction to Resolution

Resolution is a fundamental rule of inference used in automated theorem proving and logic programming. It provides a complete and sound method for determining the satisfiability of a set of propositional or first-order logic clauses, which makes it essential for knowledge-based systems and AI applications.

The resolution principle was introduced by John Alan Robinson in 1965 and forms the theoretical foundation for many AI systems, including Prolog interpreters and automated reasoning systems. It operates on formulas in **conjunctive normal form (CNF)** and systematically applies the resolution rule to derive new clauses until either a contradiction is found or no new clauses can be derived.

## Key Concepts

### Conjunctive Normal Form (CNF)

Before applying resolution, logical expressions must be converted to CNF. A formula is in CNF if it is a conjunction of one or more clauses, where each clause is a disjunction of literals.

**Example conversion to CNF:**
Original: ¬(A ∧ B) ∨ C
Step 1: Eliminate implications: (A ∧ B) → C becomes ¬(A ∧ B) ∨ C
Step 2: Apply De Morgan's: ¬A ∨ ¬B ∨ C
Step 3: The expression is now in CNF as it's a single clause with three literals

### The Resolution Rule

The resolution rule states that if we have two clauses containing complementary literals, we can infer a new clause (the resolvent) by combining all literals from both clauses except the complementary ones.

Formally, for propositional logic:
Given: (P ∨ Q) and (¬P ∨ R)
We can derive: (Q ∨ R)

This can be represented as:

```
    P ∨ Q, ¬P ∨ R
    -------------
        Q ∨ R
```

### Resolution Refutation

Resolution is typically used as a refutation proof technique. To prove that a knowledge base (KB) entails a query α (KB ⊢ α), we:

1. Convert KB to CNF
2. Convert ¬α to CNF
3. Add ¬α to KB
4. Apply resolution repeatedly until:
   - Derive an empty clause (contradiction): Proof that α is true
   - No new clauses can be derived: α cannot be proven

The empty clause (□) represents a contradiction, showing that the assumption ¬α is inconsistent with KB, thus proving α.

## Resolution in Propositional Logic

### Algorithm for Propositional Resolution

```
function PL-RESOLUTION(KB, α):
    clauses = set of clauses in CNF representation of KB ∧ ¬α
    new = {}
    while true:
        for each pair of clauses (Ci, Cj) in clauses:
            resolvents = PL-RESOLVE(Ci, Cj)
            if □ ∈ resolvents: return true
            new = new ∪ resolvents
        if new ⊆ clauses: return false
        clauses = clauses ∪ new
```

### Example: Propositional Resolution

Prove: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B) ⊢ C

1. Convert to CNF and add negation of query:
   Clauses: {A ∨ B, ¬A ∨ C, ¬B, ¬C}

2. Resolve A ∨ B and ¬A ∨ C:
   Resolvent: B ∨ C

3. Resolve B ∨ C and ¬B:
   Resolvent: C

4. Resolve C and ¬C:
   Resolvent: □ (empty clause)

Since we derived □, the query C is proven.

```
Clause set: {A ∨ B, ¬A ∨ C, ¬B, ¬C}

Step 1: Resolve (A ∨ B) and (¬A ∨ C) → (B ∨ C)
Step 2: Resolve (B ∨ C) and ¬B → C
Step 3: Resolve C and ¬C → □
```

## Resolution in First-Order Logic

First-order resolution extends propositional resolution by handling variables, quantifiers, and predicates through unification.

### Unification

Unification is the process of finding a substitution that makes two logical expressions identical. A substitution θ = {v1/t1, v2/t2, ..., vn/tn} replaces variables with terms.

**Example:** Unify P(x, f(y)) and P(a, f(z))
θ = {x/a, y/z} or {x/a, z/y}

### Resolution Rule for FOL

The resolution rule for first-order logic:
Given two clauses: [L1 ∨ ... ∨ Lm] and [M1 ∨ ... ∨ Mn]
Where L_i and M_j are literals, and there exists unification θ such that L_iθ = ¬M_jθ

Then we can derive: [L1θ ∨ ... ∨ L_{i-1}θ ∨ L_{i+1}θ ∨ ... ∨ Lmθ ∨ M1θ ∨ ... ∨ M_{j-1}θ ∨ M_{j+1}θ ∨ ... ∨ Mnθ]

### Algorithm for First-Order Resolution

```
function FOL-RESOLUTION(KB, α):
    clauses = set of clauses in CNF representation of KB ∧ ¬α
    while true:
        new = {}
        for each pair of clauses (ci, cj) in clauses:
            (resolvents, θ) = RESOLVE(ci, cj)
            if resolvents contains □: return true
            new = new ∪ resolvents
        if new ⊆ clauses: return false
        clauses = clauses ∪ new
```

### Example: First-Order Resolution

Prove: ∀x (Dog(x) → Animal(x)), Dog(Fido) ⊢ Animal(Fido)

1. Convert to CNF:
   ¬Dog(x) ∨ Animal(x)
   Dog(Fido)
   ¬Animal(Fido) (negation of query)

2. Resolve ¬Dog(x) ∨ Animal(x) with Dog(Fido) using θ = {x/Fido}:
   Resolvent: Animal(Fido)

3. Resolve Animal(Fido) with ¬Animal(Fido):
   Resolvent: □

Proof complete.

## Strategies for Efficient Resolution

Several strategies improve the efficiency of resolution:

### Unit Preference Strategy

Prefer resolution steps where one clause is a unit clause (single literal). This tends to produce shorter resolvents and moves toward the empty clause faster.

**Example:** Given clauses: P ∨ Q, ¬P ∨ R, ¬Q, ¬R
Unit preference would resolve with ¬Q or ¬R first.

### Set-of-Support Strategy

Divide clauses into two sets: SOS (initially containing ¬α) and others. Only resolve clauses where at least one comes from SOS. This focuses the search on relevant clauses.

### Input Resolution

Each resolution step must involve at least one of the input clauses (original clauses). Complete for Horn clauses but not for general logic.

### Linear Resolution

Start with a clause and always resolve the most recent resolvent with another clause. More efficient but still complete.

## Applications of Resolution

### Theorem Proving

Resolution is the basis for automated theorem provers that verify mathematical theorems and logical consequences.

### Logic Programming

Prolog uses a form of resolution (SLD resolution) for its inference mechanism. Queries are answered by attempting to derive the empty clause.

### Knowledge-Based Systems

Resolution enables systems to reason with knowledge bases and answer queries about the world.

### Planning and Problem Solving

Resolution can be used to derive plans by representing actions and states as logical formulae.

## Comparison with Other Inference Methods

| Method                | Complete               | Sound | Efficiency | Notes                                                 |
| --------------------- | ---------------------- | ----- | ---------- | ----------------------------------------------------- |
| **Resolution**        | Yes                    | Yes   | Moderate   | General purpose, works for both propositional and FOL |
| **Forward Chaining**  | Yes (for Horn clauses) | Yes   | High       | Data-driven, good for deductive databases             |
| **Backward Chaining** | Yes (for Horn clauses) | Yes   | High       | Goal-driven, used in Prolog                           |
| **Model Checking**    | Yes                    | Yes   | Varies     | Good for finite domains, used in verification         |
| **Tableaux Method**   | Yes                    | Yes   | Moderate   | Alternative to resolution, uses tree expansion        |

## Limitations and Considerations

1. **Combinatorial Explosion**: The number of possible resolvents can grow exponentially
2. **Requires CNF**: Conversion to CNF can increase formula size exponentially
3. **Not Always Efficient**: For some problems, resolution may be less efficient than specialized methods
4. **Incomplete for Non-Clausal Forms**: Resolution works only on CNF

## Exam Tips

1. **Remember the steps**: Conversion to CNF → Negate query → Apply resolution until □
2. **Practice unification**: This is crucial for first-order resolution problems
3. **Use strategies**: Mention efficiency strategies like unit preference in answers
4. **Watch for complementary literals**: Identify pairs that can be resolved
5. **Draw resolution trees**: Visual representations can help in complex proofs
6. **Understand the empty clause**: □ means contradiction and proves the query
7. **Know the differences**: Be prepared to compare resolution with other inference methods
