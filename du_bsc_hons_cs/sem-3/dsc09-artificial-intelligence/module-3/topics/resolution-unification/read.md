# Resolution and Unification in Artificial Intelligence

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Resolution and Unification** form the foundational reasoning mechanisms in automated theorem proving and logic programming. These techniques enable AI systems to derive new facts from existing knowledge, making them essential for knowledge representation, reasoning, and problem-solving applications.

### Real-World Relevance

Resolution and unification power numerous AI applications:

- **Automated Theorem Provers**: Systems like Coq, Isabelle, and ACL2 use resolution for mathematical proof verification
- **Logic Programming**: Prolog, the cornerstone of declarative programming, relies entirely on unification and resolution
- **Knowledge-Based Systems**: Expert systems use resolution to infer conclusions from rule bases
- **Natural Language Processing**: Unification-based grammars (HPSG, LFG) process syntactic structures
- **Robot Planning**: STRIPS-style planners use resolution for goal regression
- **Database Systems**: Query unification enables pattern matching in deductive databases

### Delhi University Syllabus Context

This topic aligns with the **BSc (Hons) Computer Science — NEP 2024 UGCF** curriculum under the Artificial Intelligence paper. Students must understand both theoretical foundations and practical implementations of resolution and unification to excel in automated reasoning concepts.

---

## 2. Logical Foundations: A Brief Review

### 2.1 Propositional Logic

Propositional logic deals with propositions that are either true or false. The resolution principle was originally developed for propositional logic by J. Alan Robinson in 1965.

**Key Operators:**

- ¬ (NOT/negation)
- ∧ (AND/conjunction)
- ∨ (OR/disjunction)
- → (IMPLIES/implication)
- ↔ (EQUIVALENCE/bi-conditional)

### 2.2 Predicate Logic (First-Order Logic)

Predicate logic extends propositional logic with:

- **Predicates**: Properties or relations (e.g., `Human(Socrates)`, `Loves(x, y)`)
- **Quantifiers**: Universal (∀) and Existential (∃)
- **Variables**: Represent unspecified objects
- **Constants**: Specific objects (e.g., `Socrates`, `Romeo`)
- **Functions**: Terms that return objects (e.g., `FatherOf(x)`)

---

## 3. Substitution

### 3.1 Definition

A **substitution** is a finite set of variable-term pairs:

```
θ = {x₁/t₁, x₂/t₂, ..., xₙ/tₙ}
```

Where each variable `xᵢ` is replaced by term `tᵢ`, and no variable appears as a proper part of any term (this is called the **occur check**).

### 3.2 Types of Substitutions

1. **Empty Substitution (ε)**: The substitution that maps nothing, i.e., θ = {}
2. **Ground Substitution**: All terms are ground (contain no variables)
3. **Most General Unifier (MGU)**: The "least specific" substitution that makes two expressions equal

### 3.3 Composition of Substitutions

Given two substitutions θ and σ, their composition θσ is formed by:
- Applying θ to each term in σ
- Adding any pairs from θ not affecting variables in σ

**Example:**

```
θ = {x/y, z/w}
σ = {x/a, y/b}

θσ = {x/aθ, y/bθ, z/w} = {x/a, y/b, z/w}
```

### 3.4 Application of Substitution

When applying substitution θ to an expression E (denoted Eθ):
- Replace each occurrence of variable x with its corresponding term t from θ
- Perform simultaneous replacement

**Example:**

```
E = P(x, f(y))
θ = {x/a, y/b}

Eθ = P(a, f(b))
```

---

## 4. Unification

### 4.1 Definition

**Unification** is the process of finding a substitution that makes two expressions identical. If such a substitution exists, the expressions are said to be **unifiable**.

### 4.2 Most General Unifier (MGU)

Among all unifiers of two expressions, the **Most General Unifier (MGU)** is the one that is most general — any other unifier can be obtained by composing it with some other substitution.

### 4.3 Unification Algorithm

The unification algorithm follows these rules:

```
UNIFY(e₁, e₂):
    if e₁ = e₂: return {}
    if is_variable(e₁): return UNIFY_VAR(e₁, e₂)
    if is_variable(e₂): return UNIFY_VAR(e₂, e₁)
    if is_compound(e₁) and is_compound(e₂):
        if functor(e₁) ≠ functor(e₂) or arity(e₁) ≠ arity(e₂): return FAIL
        return UNIFY(args(e₁), args(e₂))
    return FAIL

UNIFY_VAR(v, t):
    if v = t: return {}
    if occurs_check(v, t): return FAIL
    return {v/t}

UNIFY(l₁, l₂):
    if l₁ = []: return {}
    if l₂ = []: return {}
    rest = UNIFY(head(l₁), head(l₂))
    if rest = FAIL: return FAIL
    return UNIFY(apply(rest, tail(l₁)), apply(rest, tail(l₂))) ⊔ rest
```

### 4.4 Unification Examples

**Example 1: Simple Variable Unification**

```
Unify: P(x) and P(John)

θ = {x/John}
Result: Success, θ = {x/John}
```

**Example 2: Function Symbol Unification**

```
Unify: P(f(x), y) and P(f(g(z)), w)

Step 1: f(x) = f(g(z)) → x = g(z)
Step 2: y = w

θ = {x/g(z), y/w}
```

**Example 3: Failure Case (Occur Check)**

```
Unify: x and f(x)

This fails because x occurs within f(x).
Applying this substitution would create infinite terms: f(f(f(...)))
```

### 4.5 Python Implementation of Unification

```python
from typing import Dict, Optional, Any, List, Tuple
from dataclasses import dataclass

@dataclass
class Var:
    """Represents a variable in terms"""
    name: str
    
    def __str__(self):
        return self.name

@dataclass
class Const:
    """Represents a constant symbol"""
    name: str
    
    def __str__(self):
        return self.name

@dataclass
class Func:
    """Represents a function symbol"""
    name: str
    args: Tuple['Term', ...]
    
    def __str__(self):
        if not self.args:
            return self.name
        args_str = ', '.join(str(arg) for arg in self.args)
        return f"{self.name}({args_str})"

Term = Var | Const | Func

def occurs_check(var: Var, term: Term) -> bool:
    """Check if variable occurs in term"""
    if isinstance(term, Var):
        return var.name == term.name
    elif isinstance(term, Const):
        return False
    elif isinstance(term, Func):
        return any(occurs_check(var, arg) for arg in term.args)
    return False

def apply_substitution(term: Term, subst: Dict[str, Term]) -> Term:
    """Apply substitution to a term"""
    if isinstance(term, Var):
        return subst.get(term.name, term)
    elif isinstance(term, Const):
        return term
    elif isinstance(term, Func):
        return Func(term.name, tuple(apply_substitution(arg, subst) for arg in term.args))
    return term

def unify(t1: Term, t2: Term, subst: Optional[Dict[str, Term]] = None) -> Optional[Dict[str, Term]]:
    """Unify two terms, returning most general unifier or None"""
    if subst is None:
        subst = {}
    
    # If both terms are identical, no new substitution needed
    if str(t1) == str(t2):
        return subst
    
    # Handle variables
    if isinstance(t1, Var):
        if occurs_check(t1, t2):
            return None  # Unification fails (occur check)
        subst[t1.name] = t2
        return subst
    
    if isinstance(t2, Var):
        if occurs_check(t2, t1):
            return None
        subst[t2.name] = t1
        return subst
    
    # Handle function symbols
    if isinstance(t1, Func) and isinstance(t2, Func):
        if t1.name != t2.name or len(t1.args) != len(t2.args):
            return None  # Different function symbols or arities
        
        for arg1, arg2 in zip(t1.args, t2.args):
            subst = unify(apply_substitution(arg1, subst), 
                         apply_substitution(arg2, subst), 
                         subst)
            if subst is None:
                return None
        return subst
    
    # Constants or mismatched types
    if isinstance(t1, Const) and isinstance(t2, Const):
        if t1.name != t2.name:
            return None
        return subst
    
    return None

# Example usage
if __name__ == "__main__":
    # Example: Unify Father(x) and Father(John)
    t1 = Func("Father", (Var("x"),))
    t2 = Func("Father", (Const("John"),))
    
    result = unify(t1, t2)
    print(f"Unifying Father(x) and Father(John):")
    print(f"  MGU: {result}")  # Output: {'x': Const('John')}
    
    # Example: Unify P(x, f(y)) and P(a, f(b))
    t3 = Func("P", (Var("x"), Func("f", (Var("y"),))))
    t4 = Func("P", (Const("a"), Func("f", (Const("b"),))))
    
    result2 = unify(t3, t4)
    print(f"\nUnifying P(x, f(y)) and P(a, f(b)):")
    print(f"  MGU: {result2}")  # Output: {'x': Const('a'), 'y': Const('b')}
```

---

## 5. Clause Form (Conjunctive Normal Form)

### 5.1 Definition

The **Clause Form** (or Conjunctive Normal Form - CNF) is a standardized format for logical formulas required by the resolution principle. A formula in CNF is a conjunction of disjunctions of literals.

### 5.2 Steps to Convert to CNF

1. **Remove Implications**: Replace `P → Q` with `¬P ∨ Q`
2. **Move Negation Inwards**: Apply De Morgan's laws
   - `¬(P ∧ Q)` ≡ `¬P ∨ ¬Q`
   - `¬(P ∨ Q)` ≡ `¬P ∧ ¬Q`
   - `¬∀x P` ≡ `∃x ¬P`
   - `¬∃x P` ≡ `∀x ¬P`
3. **Standardize Variables**: Rename variables to avoid conflicts
4. **Remove Existential Quantifiers**: Skolemization
5. **Convert to Conjunctive Normal Form**: Distribute ∨ over ∧
6. **Create Clause Set**: Each conjunct becomes a clause

### 5.3 Skolemization

Existential quantifiers are removed by introducing **Skolem functions** or **Skolem constants**.

**Example:**

```
∀x ∃y Loves(x, y)

After Skolemization (y = f(x)):
∀x Loves(x, f(x))
```

### 5.4 CNF Conversion Example

**Original Formula:**
```
∀x (Human(x) → Mortal(x))
```

**Step-by-step conversion:**

1. Remove implication:
   ```
   ∀x (¬Human(x) ∨ Mortal(x))
   ```

2. Already negation is at atomic level

3. No existential quantifiers to remove

4. CNF (already in CNF):
   ```
   {¬Human(x) ∨ Mortal(x)}
   ```

**Another Example:**

```
¬(P ∨ Q) → R
```

1. Remove implication:
   ```
   ¬(¬(P ∨ Q)) ∨ R
   (P ∨ Q) ∨ R
   ```

2. Simplify:
   ```
   P ∨ Q ∨ R
   ```

3. CNF: `{P ∨ Q ∨ R}`

---

## 6. Resolution Principle

### 6.1 Historical Context

The resolution principle was developed by **J. Alan Robinson** in 1965. It provided a single, simple inference rule that could replace all traditional inference rules (modus ponens, modus tollens, etc.) in propositional and first-order logic. This breakthrough enabled the development of practical automated theorem provers.

### 6.2 Resolution Inference Rule

Resolution operates on **clauses** (disjunctions of literals). The basic resolution rule:

```
      C₁ ∨ L₁        C₂ ∨ L₂
    --------------------------------
      (C₁ ∨ C₂)θ
```

Where:
- `L₁` and `L₂` are complementary literals (one is the negation of the other)
- `θ` is the MGU of `L₁` and `L₂`
- `C₁` and `C₂` are the remaining clauses (the resolvents)

### 6.3 Types of Resolution

#### 6.3.1 Binary Resolution

Both parent clauses contain exactly one literal each that unifies to complementary literals.

```
    P(x) ∨ Q(x)      ¬P(f(y)) ∨ R(y)
    --------------------------------
         Q(f(a)) ∨ R(y)    [with θ = {x/f(a)}]
```

#### 6.3.2 Unit Resolution

At least one parent clause is a unit clause (contains exactly one literal).

```
    P ∨ Q      ¬P
    -----------
        Q
```

#### 6.3.3 Input Resolution

One parent clause is from the original set of axioms (input), and one is derived during the proof.

#### 6.3.4 Linear Resolution

Both parent clauses contain a "selected" literal, and one parent must be the result of the most recent resolution step.

#### 6.3.5 Resolution with Factoring

Before resolving, apply **factoring** to remove redundant literals:

```
P(x) ∨ P(f(y)) ∨ Q(z)
P(x) ∨ Q(z)     [factored]
```

### 6.4 Resolution Proof by Refutation

To prove a theorem `⊢ G` (i.e., `A₁, A₂, ..., Aₙ ⊢ G`):

1. Negate the goal: Add `¬G` to the knowledge base
2. Convert all formulas to CNF
3. Apply resolution repeatedly
4. Derive the **empty clause** (contradiction)
5. Conclude the original goal is provable

---

## 7. Resolution Strategies

Resolution strategies guide the search for proofs by restricting which resolvents are generated.

### 7.1 Unit Resolution Strategy

Only perform resolution when at least one parent clause is a unit clause. This is complete for propositional logic but incomplete for first-order logic.

### 7.2 Set of Support (SOS) Strategy

At least one parent clause must contain a literal from the negated goal or its descendants. This ensures resolution proceeds toward the goal.

### 7.3 Input Resolution Strategy

At least one parent clause must be from the original set of axioms. This is complete for propositional logic.

### 7.4 Linear Resolution Strategy

One parent clause must be the result of the most recent inference. This is complete and more restricted.

### 7.5 Unit Preference Strategy

Prefer resolving with unit clauses (clauses with single literals). This often leads to quicker proofs.

### 7.6 Breadth-First Strategy

Generate resolvents level by level. Complete but may generate many clauses.

### 7.7 Subset of Support Strategy

A refinement of Set of Support where the support set is a subset of clauses derived from the negated goal.

---

## 8. Resolution and Unification: Complete Example

### 8.1 Problem Statement

**Knowledge Base:**
1. All humans are mortal: `∀x (Human(x) → Mortal(x))`
2. Socrates is human: `Human(Socrates)`

**Goal:** Prove Socrates is mortal: `Mortal(Socrates)`

### 8.2 Solution

**Step 1: Convert to CNF**

1. `∀x (Human(x) → Mortal(x))` → `∀x (¬Human(x) ∨ Mortal(x))` → `{¬Human(x) ∨ Mortal(x)}`
2. `Human(Socrates)` → `{Human(Socrates)}`
3. Negate goal: `¬Mortal(Socrates)` → `{¬Mortal(Socrates)}`

**Step 2: Apply Resolution**

| Step | Clause 1 | Clause 2 | Resolvent | Substitution |
|------|----------|----------|-----------|--------------|
| 1 | ¬Human(x) ∨ Mortal(x) | Human(Socrates) | Mortal(x) ∨ Mortal(Socrates) [after x=Socrates] | {x/Socrates} |
| 2 | Mortal(Socrates) | ¬Mortal(Socrates) | □ (empty clause) | {} |

**Step 3: Conclusion**

The empty clause (contradiction) is derived, proving `Mortal(Socrates)` is entailed.

### 8.3 Python Implementation of Resolution

```python
from typing import List, Set, Optional, Dict
from dataclasses import dataclass, field
from collections import deque

@dataclass
class Literal:
    """Represents a literal (possibly negated)"""
    predicate: str
    args: tuple
    negated: bool = False
    
    def __str__(self):
        sign = "¬" if self.negated else ""
        return f"{sign}{self.predicate}{self.args}"
    
    def complement(self) -> 'Literal':
        """Return the complementary literal"""
        return Literal(self.predicate, self.args, not self.negated)

@dataclass
class Clause:
    """Represents a clause as a set of literals"""
    literals: Set[Literal] = field(default_factory=set)
    
    def __str__(self):
        if not self.literals:
            return "□"  # Empty clause
        return " ∨ ".join(str(l) for l in self.literals)
    
    def is_empty(self) -> bool:
        return len(self.literals) == 0

def resolve(c1: Clause, c2: Clause, subst: Dict) -> Optional[Clause]:
    """Attempt to resolve two clauses"""
    for lit1 in c1.literals:
        for lit2 in c2.literals:
            # Check if literals are complementary
            if (lit1.predicate == lit2.predicate and 
                lit1.negated != lit2.negated and
                len(lit1.args) == len(lit2.args)):
                
                # In a full implementation, unify arguments here
                # For this example, assume simple case
                if lit1.args == lit2.args:
                    # Remove complementary literals and apply substitution
                    new_literals = (c1.literals - {lit1}) | (c2.literals - {lit2})
                    return Clause(new_literals)
    return None

def resolution_prover(axioms: List[Clause], goal: Clause) -> bool:
    """
    Basic resolution refutation prover
    Returns True if goal is provable from axioms
    """
    # Add negated goal to clauses
    clauses = axioms + [goal]
    new_clauses = set(clauses)
    
    # Iterative resolution
    iteration = 0
    while new_clauses:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # Get all pairs
        all_clauses = list(new_clauses)
        for i, c1 in enumerate(all_clauses):
            for c2 in all_clauses[i+1:]:
                resolvent = resolve(c1, c2, {})
                if resolvent is not None:
                    print(f"Resolve: {c1} with {c2}")
                    print(f"  Result: {resolvent}")
                    
                    if resolvent.is_empty():
                        print("\n*** EMPTY CLAUSE DERIVED - PROOF COMPLETE ***")
                        return True
        
        # Check for new clauses (simplified - in practice, add generated clauses)
        break  # This is a simplified demonstration
    
    return False

# Example demonstration
if __name__ == "__main__":
    # Define clauses:
    # ¬Human(x) ∨ Mortal(x)
    c1 = Clause({Literal("Human", ("x",), True), Literal("Mortal", ("x",), False)})
    
    # Human(Socrates)
    c2 = Clause({Literal("Human", ("Socrates",), False)})
    
    # ¬Mortal(Socrates) (negated goal)
    goal = Clause({Literal("Mortal", ("Socrates",), True)})
    
    print("Resolution Proof Demonstration")
    print("=" * 40)
    print(f"Axiom 1: {c1}")
    print(f"Axiom 2: {c2}")
    print(f"Negated Goal: {goal}")
    print()
    
    # Manual resolution steps for demonstration
    print("Resolution Steps:")
    print(f"1. Resolve {c1} and {c2}:")
    print(f"   ¬Human(x) ∨ Mortal(x)  and  Human(Socrates)")
    print(f"   Unify: x = Socrates")
    print(f"   Result: Mortal(Socrates)")
    
    print(f"\n2. Resolve Mortal(Socrates) and ¬Mortal(Socrates):")
    print(f"   Mortal(Socrates)  and  ¬Mortal(Socrates)")
    print(f"   Result: □ (EMPTY CLAUSE)")
    print("\n   Therefore, Mortal(Socrates) is PROVEN!")
```

---

## 9. Assessment Section

### 9.1 Multiple Choice Questions

**Question 1:** What is the Most General Unifier (MGU) of the terms `P(x, f(y))` and `P(a, z)`?

A) `{x/a, z/f(y)}`  
B) `{x/a, y/b, z/f(b)}`  
C) `{x/a, z/f(y)}` where y is unchanged  
D) `{a/x, f(y)/z}`

**Answer: C** — The MGU substitutes x with a and z with f(y), leaving y unchanged as it's a variable in both expressions.

---

**Question 2:** In the resolution principle, what does the derivation of an empty clause indicate?

A) The search has failed  
B) The knowledge base is inconsistent  
C) A contradiction has been found, proving the goal  
D) The algorithm needs more axioms

**Answer: C** — The empty clause (□) represents a contradiction, which in refutation proof means the negated goal combined with axioms is unsatisfiable, thus the original goal is entailed.

---

**Question 3:** Which of the following is NOT a step in converting a formula to Conjunctive Normal Form (CNF)?

A) Remove implications  
B) Move negation inwards using De Morgan's laws  
C) Apply universal instantiation  
D) Skolemization (removing existential quantifiers)

**Answer: C** — Universal instantiation is different; CNF conversion involves standardizing variables, removing existential quantifiers via Skolemization, and distributing ∨ over ∧.

---

**Question 4:** What is the primary purpose of the occur check in unification?

A) To speed up the algorithm  
B) To prevent infinite terms during substitution  
C) To handle function symbols  
D) To find the most general unifier

**Answer: B** — The occur check prevents unification of a variable with a term containing that variable, which would create infinitely large terms.

---

**Question 5:** Which resolution strategy is complete for propositional logic?

A) Unit Resolution only  
B) Input Resolution  
C) Linear Resolution  
D) Both B and C

**Answer: D** — Both Input Resolution and Linear Resolution are complete for propositional logic, while Unit Resolution is not complete for first-order logic.

---

**Question 6:** Given the clauses `P ∨ Q` and `¬P ∨ R`, what is the resolvent?

A) `Q ∨ R`  
B) `P ∨ Q ∨ R`  
C) `Q ∨ ¬P`  
D) `R ∨ Q`

**Answer: A** — Resolving on P and ¬P (complementary literals) with empty substitution gives the disjunction of remaining literals: Q ∨ R.

---

**Question 7:** In first-order logic resolution, what must be done before applying the resolution rule?

A) Convert to predicate logic  
B) Compute the Most General Unifier  
C) Apply the inference rule multiple times  
D) Check for soundness

**Answer: B** — The resolution rule requires finding the MGU of complementary literals before producing the resolvent.

---

### 9.2 Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | **Unification** | The process of finding a substitution that makes two logical expressions identical |
| 2 | **Most General Unifier (MGU)** | The unifier that makes two expressions equal and is most general; any other unifier can be derived by composing with it |
| 3 | **Substitution** | A finite set of variable-term pairs that replaces variables with terms in expressions |
| 4 | **Occur Check** | A check in the unification algorithm that prevents unifying a variable with a term containing that variable |
| 5 | **Resolution Principle** | A single inference rule by J. Alan Robinson that can replace all traditional inference rules |
| 6 | **Clause** | A disjunction of literals (atomic formulas or their negations) |
| 7 | **CNF (Conjunctive Normal Form)** | A formula in the form of conjunction of disjunctions of literals |
| 8 | **Skolemization** | The process of removing existential quantifiers by introducing Skolem functions or constants |
| 9 | **Refutation** | A proof technique that proves a goal by showing its negation leads to a contradiction |
| 10 | **Empty Clause (□)** | A clause with no literals, representing a contradiction |
| 11 | **Binary Resolution** | Resolution where both parent clauses contribute exactly one complementary literal |
| 12 | **Unit Resolution** | Resolution where at least one parent clause is a unit clause (single literal) |
| 13 | **Set of Support Strategy** | Resolution strategy requiring at least one parent clause from the negated goal |
| 14 | **Linear Resolution** | Resolution where one parent is always the most recently derived clause |
| 15 | **Factoring** | The process of removing redundant literals from a clause before resolution |

---

## 10. Key Takeaways

1. **Unification** is the cornerstone of first-order logic reasoning. The algorithm finds substitutions that make two terms identical, with the **occur check** preventing infinite terms.

2. **Substitution** is a mapping from variables to terms. The **composition** of substitutions applies them sequentially, and the **MGU** represents the most general way to unify expressions.

3. **Clause Form (CNF)** is essential for resolution. The conversion involves removing implications, moving negations inward, standardizing variables, Skolemization, and distributing ∨ over ∧.

4. **Resolution** is a single, powerful inference rule that operates on clauses. The **refutation method** proves theorems by deriving a contradiction from the negated goal.

5. **Resolution Strategies** are crucial for making theorem proving practical. Key strategies include Unit Resolution, Set of Support, Input Resolution, and Linear Resolution—each with different completeness properties.

6. **Real-World Applications**: Resolution and unification power automated theorem provers, logic programming (Prolog), knowledge-based systems, and computational linguistics.

7. **Implementation**: Modern implementations use efficient unification algorithms with occur checks, indexing structures for clause storage, and sophisticated search strategies to handle combinatorial explosion.

8. **Completeness**: Resolution is refutation-complete for first-order logic, meaning if a conclusion follows from the axioms, resolution can eventually derive it (given appropriate strategies).

---

*Study Material prepared for Delhi University BSc (Hons) Computer Science — NEP 2024 UGCF AI Paper*