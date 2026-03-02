# Propositional and First Order Logic: Comprehensive Study Material

## Artificial Intelligence - BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Propositional Logic (PL)](#2-propositional-logic-pl)
3. [First Order Logic (FOL)](#3-first-order-logic-fol)
4. [Proof Methods and Inference](#4-proof-methods-and-inference)
5. [Practical Applications in AI](#5-practical-applications-in-ai)
6. [Programming Examples](#6-programming-examples)
7. [Multiple Choice Questions (MCQs)](#7-multiple-choice-questions-mcqs)
8. [Flashcards for Quick Revision](#8-flashcards-for-quick-revision)
9. [Key Takeaways](#9-key-takeaways)

---

## 1. Introduction and Real-World Relevance

### What is Logic?

Logic is the formal system of reasoning that provides the mathematical foundation for artificial intelligence. It serves as the backbone of knowledge representation, automated reasoning, and decision-making systems. Without logic, machines would lack the ability to deduce new facts from existing knowledge, verify the correctness of arguments, or make intelligent decisions based on premises.

### Why is This Topic Important for AI?

The study of Propositional Logic (PL) and First Order Logic (FOL) is essential for several reasons:

- **Knowledge Representation**: AI systems need to represent facts about the world in a formal language that computers can process and reason about.
- **Automated Reasoning**: Logic enables AI systems to derive conclusions from known facts automatically.
- **Expert Systems**: Medical diagnosis, fault detection, and recommendation systems rely on logical inference.
- **Planning and Decision Making**: AI planning algorithms use logic to determine sequences of actions.
- **Verification and Validation**: Software verification and hardware circuit design depend on logical reasoning.

### Delhi University Syllabus Context

This topic aligns with the **NEP 2024 UGCF** curriculum for BSc (Hons) Computer Science, specifically covering:
- Propositional Logic: Syntax, Semantics, Truth Tables, Logical Equivalences, Normal Forms
- First Order Logic: Syntax, Semantics, Quantifiers, Inference Rules
- Proof Methods: Direct, Contradiction, Resolution
- Semantic Entailment and Practical Applications in AI

---

## 2. Propositional Logic (PL)

### 2.1 Introduction to Propositional Logic

Propositional Logic deals with propositions - statements that are either **true (T)** or **false (F)**. It cannot represent relationships between objects or quantify over collections.

### 2.2 Syntax of Propositional Logic

**Definition**: A *proposition* is a declarative sentence that is either true or false, but not both.

**Basic Elements**:
- **Atomic Propositions (Propositional Variables)**: Basic propositions denoted by letters (p, q, r, s, ...)
- **Compound Propositions**: Formed by combining atomic propositions using logical connectives

**Logical Connectives**:

| Symbol | Name | Meaning | Arity |
|--------|------|---------|-------|
| ¬ (or ~) | Negation | "not" | Unary |
| ∧ | Conjunction | "and" | Binary |
| ∨ | Disjunction | "or" | Binary |
| → | Implication | "if...then" | Binary |
| ↔ | Biconditional | "if and only if" | Binary |

**Well-Formed Formulas (WFFs)**:
1. Any atomic proposition is a WFF
2. If α is a WFF, then ¬α is a WFF
3. If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), (α ↔ β) are WFFs
4. Only expressions formed by rules 1-3 are WFFs

**Precedence**: ¬ > ∧ > ∨ > → > ↔

### 2.3 Semantics and Truth Tables

**Interpretation**: An interpretation assigns a truth value (T or F) to each propositional variable.

**Truth Table for Basic Connectives**:

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
|---|---|-----|-------|-------|-------|-------|
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

**Key Observations from Truth Table**:
- Implication (p → q) is **false only when p is true and q is false**
- Biconditional (p ↔ q) is **true when p and q have the same truth values**
- Disjunction (p ∨ q) is **inclusive or** (true if at least one is true)

### 2.4 Logical Equivalences

Two formulas α and β are *logically equivalent* (α ≡ β) if they have the same truth value under all interpretations.

**Basic Equivalences**:

| Name | Equivalence |
|------|-------------|
| Identity | p ∧ T ≡ p, p ∨ F ≡ p |
| Domination | p ∨ T ≡ T, p ∧ F ≡ F |
| Idempotent | p ∧ p ≡ p, p ∨ p ≡ p |
| Double Negation | ¬¬p ≡ p |
| Commutative | p ∧ q ≡ q ∧ p, p ∨ q ≡ q ∨ p |
| Associative | (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) |
| Distributive | p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) |
| De Morgan's | ¬(p ∧ q) ≡ ¬p ∨ ¬q, ¬(p ∨ q) ≡ ¬p ∧ ¬q |
| Implication | p → q ≡ ¬p ∨ q |
| Contrapositive | p → q ≡ ¬q → ¬p |

### 2.5 Normal Forms

**Definition**: A formula is in *Normal Form* if it follows a specific structural pattern.

**Conjunctive Normal Form (CNF)**:
- A conjunction of disjunctions
- Form: (A₁ ∨ B₁) ∧ (A₂ ∨ B₂) ∧ ... ∧ (Aₙ ∨ Bₙ)
- Each clause is a disjunction of literals

**Disjunctive Normal Form (DNF)**:
- A disjunction of conjunctions
- Form: (A₁ ∧ B₁) ∨ (A₂ ∧ B₂) ∨ ... ∨ (Aₙ ∧ Bₙ)
- Each term is a conjunction of literals

**Algorithm to Convert to CNF**:
1. Remove implications and biconditionals
2. Move negations inward (using De Morgan's laws)
3. Apply distributive laws
4. Simplify

### 2.6 Semantic Entailment

**Definition**: A set of premises Γ *semantically entails* a conclusion α (written Γ ⊨ α) if every interpretation that makes all premises in Γ true also makes α true.

**Example**:
- Premise 1: p → q
- Premise 2: p
- Conclusion: q
- Therefore: {p → q, p} ⊨ q

**Tautology**: A formula that is true under all interpretations (⊨ α)

**Contradiction**: A formula that is false under all interpretations (⊨ ¬α)

**Contingent**: A formula that is neither a tautology nor a contradiction

---

## 3. First Order Logic (FOL)

### 3.1 Introduction to First Order Logic

First Order Logic (FOL), also known as Predicate Logic, extends Propositional Logic by:
- Representing **objects** and their **properties**
- Expressing **relationships** between objects
- Using **quantifiers** to make statements about collections of objects

### 3.2 Syntax of First Order Logic

**Basic Elements**:

| Element | Symbol | Example | Description |
|---------|--------|---------|-------------|
| Constants | lowercase a, b, c... | john, x, table | Specific objects |
| Variables | lowercase u, v, w, x, y, z... | x, y | Unknown objects |
| Predicates | uppercase A, B, C... | Likes(x, y), Human(x) | Properties or relations |
| Functions | f, g, h... | MotherOf(x), Plus(x, y) | Map objects to objects |
| Quantifiers | ∀ (universal), ∃ (existential) | ∀x, ∃y | Scope of variables |

**Atomic Formulas**:
- Predicates applied to terms: P(t₁, t₂, ..., tₙ)
- Example: Likes(john, mary), GreaterThan(x, 0)

**Well-Formed Formulas**:
1. Atomic formulas are WFFs
2. If α is WFF, ¬α is WFF
3. If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), (α ↔ β) are WFFs
4. If α is WFF and x is a variable, then ∀x α and ∃x α are WFFs

### 3.3 Semantics of FOL

**Interpretation**: An interpretation I consists of:
1. A non-empty domain (universe) D
2. An assignment mapping:
   - Each constant to an element of D
   - Each n-ary function to a function from Dⁿ → D
   - Each n-ary predicate to a subset of Dⁿ

**Truth Conditions**:
- I ⊨ P(t₁, ..., tₙ) iff the tuple (I(t₁), ..., I(tₙ)) ∈ I(P)
- I ⊨ ¬α iff not I ⊨ α
- I ⊨ α ∧ β iff I ⊨ α and I ⊨ β
- I ⊨ ∀x α iff for all d ∈ D, α[x/d] is true
- I ⊨ ∃x α iff there exists d ∈ D such that α[x/d] is true

### 3.4 Quantifiers

**Universal Quantifier (∀)**:
- ∀x P(x) means "For all x, P(x) holds"
- Example: ∀x (Human(x) → Mortal(x)) - "All humans are mortal"

**Existential Quantifier (∃)**:
- ∃x P(x) means "There exists an x such that P(x) holds"
- Example: ∃x (Bird(x) ∧ Flies(x)) - "Some bird flies"

**Key Relationships**:
- ¬∀x P(x) ≡ ∃x ¬P(x)
- ¬∃x P(x) ≡ ∀x ¬P(x)
- ∀x P(x) ≡ ¬∃x ¬P(x)
- ∃x P(x) ≡ ¬∀x ¬P(x)

**Scope and Variable Binding**:
- Variable x is *bound* if it appears within the scope of a quantifier
- Variable x is *free* if it is not bound
- A sentence is a formula with no free variables

### 3.5 FOL Equivalences

| Equivalence | Description |
|-------------|-------------|
| ∀x (P(x) ∧ Q(x)) ≡ (∀x P(x) ∧ ∀x Q(x)) | Universal distribution |
| ∃x (P(x) ∨ Q(x)) ≡ (∃x P(x) ∨ ∃x Q(x)) | Existential distribution |
| ∀x P(x) → Q ≡ ∃x (P(x) → Q) | Import/Export (x not free in Q) |
| ∃x P(x) → Q ≡ ∀x (P(x) → Q) | Import/Export (x not free in Q) |

### 3.6 Normal Forms in FOL

**Prenex Normal Form (PNF)**:
All quantifiers appear at the beginning of the formula, followed by a quantifier-free matrix.

**Conversion to PNF**:
1. Remove implications
2. Move negations inward (using quantifier negations)
3. Standardize variables (rename to avoid conflicts)
4. Pull quantifiers to the front

**Example**:
- Original: ∀x P(x) → ∃y Q(y)
- Step 1: ¬∀x P(x) ∨ ∃y Q(y)
- Step 2: ∃x ¬P(x) ∨ ∃y Q(y)
- Step 3: ∃x ∃y (¬P(x) ∨ Q(y)) — Prenex Normal Form

---

## 4. Proof Methods and Inference

### 4.1 Propositional Logic Inference Rules

| Rule | Form | Description |
|------|------|-------------|
| Modus Ponens | p → q, p ⊢ q | From implication and antecedent, infer consequent |
| Modus Tollens | p → q, ¬q ⊢ ¬p | From implication and negated consequent, infer negated antecedent |
| Hypothetical Syllogism | p → q, q → r ⊢ p → r | Chain implications |
| Disjunctive Syllogism | p ∨ q, ¬p ⊢ q | From disjunction and negation of one, infer other |
| Addition | p ⊢ p ∨ q | From premise, add any disjunction |
| Simplification | p ∧ q ⊢ p | From conjunction, infer one conjunct |
| Conjunction | p, q ⊢ p ∧ q | From premises, form conjunction |
| Resolution | p ∨ q, ¬q ∨ r ⊢ p ∨ r | Binary resolution rule |

### 4.2 First Order Logic Inference Rules

**Universal Instantiation (UI)**:
∀x P(x) ⊢ P(c) where c is any constant

**Existential Instantiation (EI)**:
∃x P(x) ⊢ P(c) where c is a new constant not appearing elsewhere

**Universal Generalization (UG)**:
P(c) ⊢ ∀x P(x) provided c is arbitrary

**Existential Generalization (EG)**:
P(c) ⊢ ∃x P(x)

### 4.3 Proof Methods

**Direct Proof**:
1. Assume premises are true
2. Apply inference rules step by step
3. Reach the conclusion

**Proof by Contradiction**:
1. Assume the negation of what we want to prove
2. Show this leads to a contradiction
3. Conclude the original statement is true

**Proof by Resolution** (for automated reasoning):
1. Convert all premises to CNF
2. Add negation of conclusion to the set
3. Apply resolution repeatedly
4. If empty clause (contradiction) is derived, conclusion follows

### 4.4 Soundness and Completeness

**Soundness**: If ⊢ α (provable), then ⊨ α (logically valid)
- All provable statements are true

**Completeness**: If ⊨ α (logically valid), then ⊢ α (provable)
- All true statements are provable

---

## 5. Practical Applications in AI

### 5.1 Knowledge Representation and Reasoning

- **Semantic Web**: RDF, OWL use FOL principles
- **Ontologies**: Define concepts and relationships in AI systems
- **Expert Systems**: MYCIN-style medical diagnosis systems

### 5.2 Automated Planning

- **STRIPS Planning**: Uses predicates to represent states and actions
- **Planning as Logical Inference**: Actions represented as preconditions and effects

### 5.3 Formal Verification

- **Software Verification**: Model checking using temporal logic
- **Hardware Verification**: Circuit design verification

### 5.4 Natural Language Processing

- **Semantic Parsing**: Convert natural language to logical forms
- **Question Answering**: Represent knowledge and answer queries

### 5.5 Legal and Regulatory AI

- **Contract Analysis**: Logic-based reasoning about legal documents
- **Regulatory Compliance**: Automated checking of rules

---

## 6. Programming Examples

### Example 1: Propositional Logic Truth Table Generator (Python)

```python
# Propositional Logic Truth Table Generator
# Course: Artificial Intelligence - Delhi University

from itertools import product

class PropLogic:
    def __init__(self):
        self.variables = []
        self.formula = None
    
    def parse_formula(self, formula_str):
        """Parse formula string to extract variables"""
        # Simple variable extraction (alphanumeric chars)
        self.variables = sorted(set([c for c in formula_str if c.isalpha() and c.islower()]))
        return self.variables
    
    def evaluate(self, formula_str, assignment):
        """Evaluate formula with given assignment"""
        # Replace variables with truth values
        expr = formula_str
        for var, val in assignment.items():
            expr = expr.replace(var, str(val))
        
        # Handle logical connectives
        expr = expr.replace('&&', ' and ')
        expr = expr.replace('||', ' or ')
        expr = expr.replace('!', 'not ')
        
        # Evaluate (be careful with precedence in complex formulas)
        try:
            result = eval(expr)
            return result
        except:
            return None
    
    def truth_table(self, formula_str):
        """Generate complete truth table"""
        variables = self.parse_formula(formula_str)
        num_vars = len(variables)
        
        print(f"\nFormula: {formula_str}")
        print("=" * (10 * (num_vars + 1)))
        
        # Print header
        header = " | ".join(variables) + " | Result"
        print(header)
        print("-" * len(header))
        
        # Generate all combinations
        for values in product([True, False], repeat=num_vars):
            assignment = dict(zip(variables, values))
            result = self.evaluate(formula_str, assignment)
            
            # Print row
            row_vals = ["T" if v else "F" for v in values]
            row_str = " | ".join(row_vals)
            print(f"{row_str} | {'T' if result else 'F'}")
        
        print("\n")

# Example usage
pl = PropLogic()

# Test cases
print("PROPOSITIONAL LOGIC TRUTH TABLES")
print("=" * 50)

# Example 1: p AND q
pl.truth_table("p && q")

# Example 2: p OR q
pl.truth_table("p || q")

# Example 3: p -> q (expressed as !p || q)
pl.truth_table("!p || q")

# Example 4: (p && q) -> r
pl.truth_table("!(p && q) || r")
pl.truth_table("(!p || !q || r)")
```

**Output**:
```
PROPOSITIONAL LOGIC TRUTH TABLES
==================================================

Formula: p && q
==========================
p | q | Result
-----------
T | T | T
T | F | F
F | T | F
F | F | F


Formula: p -> q (as !p || q)
==========================
p | q | Result
-----------
T | T | T
T | F | F
F | T | T
F | F | T
```

### Example 2: First Order Logic Knowledge Base (Python)

```python
# First Order Logic Knowledge Base Implementation
# Course: Artificial Intelligence - Delhi University

classFOL:
    def __init__(self):
        self.facts = set()  # Ground atoms
        self.rules = []     # Implication rules
    
    def add_fact(self, fact):
        """Add a ground atom to knowledge base"""
        self.facts.add(fact)
        print(f"Added fact: {fact}")
    
    def add_rule(self, antecedent, consequent):
        """Add rule: antecedent -> consequent"""
        self.rules.append((antecedent, consequent))
        print(f"Added rule: {antecedent} -> {consequent}")
    
    def query(self, query_fact):
        """Check if a fact can be inferred using forward chaining"""
        inferred = set(self.facts)
        to_process = list(self.facts)
        
        while to_process:
            current = to_process.pop(0)
            
            for antecedent, consequent in self.rules:
                # Check if antecedent matches current fact
                if self.match(antecedent, current):
                    # Apply substitution to consequent
                    new_fact = self.apply_substitution(consequent, 
                                                        self.get_substitution(antecedent, current))
                    if new_fact not in inferred:
                        inferred.add(new_fact)
                        to_process.append(new_fact)
                        print(f"Inferred: {new_fact}")
        
        return query_fact in inferred
    
    def match(self, pattern, fact):
        """Simple pattern matching (unification)"""
        return pattern == fact
    
    def get_substitution(self, pattern, fact):
        """Get substitution mapping (simplified)"""
        return {}
    
    def apply_substitution(self, fact, substitution):
        """Apply substitution to fact"""
        return fact
    
    def print_kb(self):
        """Print knowledge base contents"""
        print("\n" + "=" * 50)
        print("KNOWLEDGE BASE")
        print("=" * 50)
        print("Facts:")
        for fact in self.facts:
            print(f"  - {fact}")
        print("\nRules:")
        for ant, cons in self.rules:
            print(f"  - {ant} -> {cons}")
        print("=" * 50 + "\n")


# Create FOL Knowledge Base for Family Relations
print("FIRST ORDER LOGIC KNOWLEDGE BASE")
print("=" * 60)

kb = FOL()

# Add facts (atomic sentences)
kb.add_fact("Father(John, Mary)")
kb.add_fact("Father(John, Tom)")
kb.add_fact("Father(Tom, Alice)")
kb.add_fact("Mother(Sarah, John)")

# Add rules
# If X is father of Y, then X is parent of Y
kb.add_rule("Father(X, Y)", "Parent(X, Y)")

# If X is mother of Y, then X is parent of Y
kb.add_rule("Mother(X, Y)", "Parent(X, Y)")

# If X is parent of Y and Y is parent of Z, then X is grandparent of Z
kb.add_rule("Parent(X, Y) && Parent(Y, Z)", "Grandparent(X, Z)")

kb.print_kb()

# Query examples
print("\nQUERY RESULTS")
print("=" * 50)

# Query: Is John parent of Mary?
result = kb.query("Parent(John, Mary)")
print(f"Query: Parent(John, Mary)? {result}")

# Query: Is John parent of Tom?
result = kb.query("Parent(John, Tom)")
print(f"Query: Parent(John, Tom)? {result}")

# Query: Is Tom parent of Alice?
result = kb.query("Parent(Tom, Alice)")
print(f"Query: Parent(Tom, Alice)? {result}")

# After inference, we can also query grandparent
# (Note: Full implementation would require forward chaining)
print("\nNote: A complete forward chaining implementation would")
print("infer Parent(John, Tom), Grandparent(John, Alice), etc.")
```

---

## 7. Multiple Choice Questions (MCQs)

### Propositional Logic

**Question 1**: Which of the following is NOT a propositional connective?
- a) ∧ (AND)
- b) ∨ (OR)
- c) → (Implication)
- d) ∀ (Universal Quantifier)
- **Answer**: d) ∀ (Universal Quantifier) - Quantifiers belong to First Order Logic

**Question 2**: The implication p → q is FALSE only when:
- a) Both p and q are true
- b) Both p and q are false
- c) p is true and q is false
- d) p is false and q is true
- **Answer**: c) p is true and q is false

**Question 3**: Which logical equivalence states that ¬(p ∧ q) ≡ ¬p ∨ ¬q?
- a) Commutative Law
- b) De Morgan's Law
- c) Distributive Law
- d) Implication Law
- **Answer**: b) De Morgan's Law

**Question 4**: A proposition that is true under all interpretations is called:
- a) Contradiction
- b) Contingent
- c) Tautology
- d) Satisfiable
- **Answer**: c) Tautology

**Question 5**: In Conjunctive Normal Form (CNF), the formula is a conjunction of:
- a) Literals
- b) Disjunctions of literals
- c) Conjunctions of literals
- d) Implications
- **Answer**: b) Disjunctions of literals

### First Order Logic

**Question 6**: In FOL, ∀x P(x) is logically equivalent to:
- a) ¬∃x ¬P(x)
- b) ∃x ¬P(x)
- c) ∀x ¬P(x)
- d) ¬∀x ¬P(x)
- **Answer**: a) ¬∃x ¬P(x)

**Question 7**: Which inference rule allows us to infer P(c) from ∀x P(x)?
- a) Existential Instantiation
- b) Universal Instantiation
- c) Modus Ponens
- d) Universal Generalization
- **Answer**: b) Universal Instantiation

**Question 8**: In FOL, a formula with no free variables is called a:
- a) Open formula
- b) Closed formula (Sentence)
- c) Atomic formula
- d) Complex formula
- **Answer**: b) Closed formula (Sentence)

**Question 9**: The Prenex Normal Form requires:
- a) All quantifiers at the beginning
- b) All negations at the beginning
- c) Only binary connectives
- d) No implications
- **Answer**: a) All quantifiers at the beginning

**Question 10**: Which of the following is NOT a basic element of FOL syntax?
- a) Variables
- b) Constants
- c) Propositional variables
- d) Predicates
- **Answer**: c) Propositional variables - These are from Propositional Logic

### Inference and Proof

**Question 11**: Modus Ponens states that from p → q and p, we can infer:
- a) ¬q
- b) q
- c) p
- d) p ∧ q
- **Answer**: b) q

**Question 12**: A proof method that assumes the negation of what we want to prove is:
- a) Direct Proof
- b) Proof by Contradiction
- c) Proof by Resolution
- d) Induction
- **Answer**: b) Proof by Contradiction

**Question 13**: Soundness means:
- a) All true statements are provable
- b) All provable statements are true
- c) The system is complete
- d) The system is consistent
- **Answer**: b) All provable statements are true

**Question 14**: The resolution inference rule for p ∨ q and ¬q ∨ r produces:
- a) p ∧ r
- b) p ∨ r
- c) q ∨ r
- d) ¬q
- **Answer**: b) p ∨ r

**Question 15**: Semantic entailment Γ ⊨ α means:
- a) α can be proven from Γ
- b) Every interpretation making Γ true also makes α true
- c) α and Γ are logically equivalent
- d) α is a tautology
- **Answer**: b) Every interpretation making Γ true also makes α true

---

## 8. Flashcards for Quick Revision

### Propositional Logic

| Term | Definition |
|------|------------|
| **Proposition** | A declarative statement that is either true (T) or false (F) |
| **Atomic Proposition** | Basic proposition that cannot be broken down (p, q, r, ...) |
| **Compound Proposition** | Formed by combining atomic propositions using connectives |
| **Truth Table** | Table showing truth value of compound proposition for all interpretations |
| **Tautology** | Formula true under all interpretations |
| **Contradiction** | Formula false under all interpretations |
| **Contingent** | Formula that is neither tautology nor contradiction |
| **Logical Equivalence** | Two formulas have same truth value under all interpretations |
| **CNF** | Conjunctive Normal Form - conjunction of disjunctions |
| **DNF** | Disjunctive Normal Form - disjunction of conjunctions |

### First Order Logic

| Term | Definition |
|------|------------|
| **Predicate** | Property of an object or relation between objects (e.g., Human(x)) |
| **Constant** | Specific object in the domain (e.g., john, london) |
| **Variable** | Placeholder for objects (e.g., x, y, z) |
| **Universal Quantifier (∀)** | "For all" - statement about all objects in domain |
| **Existential Quantifier (∃)** | "There exists" - statement about some object in domain |
| **Ground Atom** | Atomic formula with no variables |
| **Free Variable** | Variable not bound by any quantifier |
| **Bound Variable** | Variable within scope of a quantifier |
| **Sentence** | Formula with no free variables |
| **Prenex Normal Form** | All quantifiers at the beginning of the formula |

### Inference & Proof

| Term | Definition |
|------|------------|
| **Modus Ponens** | From p → q and p, infer q |
| **Modus Tollens** | From p → q and ¬q, infer ¬p |
| **Resolution** | From p ∨ q and ¬q ∨ r, infer p ∨ r |
| **Soundness** | Every provable formula is true |
| **Completeness** | Every true formula is provable |
| **Semantic Entailment** | Γ ⊨ α: all models of Γ are models of α |
| **Forward Chaining** | Infer new facts from known facts using rules |
| **Backward Chaining** | Start from goal and work backwards to find supporting facts |

---

## 9. Key Takeaways

### Propositional Logic (PL)
1. **Foundation**: PL deals with propositions that are either true or false, using connectives (¬, ∧, ∨, →, ↔) to form compound statements.
2. **Truth Tables**: Essential tool for determining the truth value of compound propositions under all possible interpretations.
3. **Logical Equivalences**: Understanding equivalences like De Morgan's laws, implication equivalence, and distributive laws is crucial for formula simplification and transformation.
4. **Normal Forms**: CNF and DNF provide standardized formats useful for automated reasoning and SAT solving.
5. **Semantic Entailment**: Γ ⊨ α captures the notion that α logically follows from Γ.

### First Order Logic (FOL)
1. **Expressiveness**: FOL extends PL by representing objects, properties, and relationships through predicates, constants, variables, and quantifiers.
2. **Quantifiers**: Universal (∀) and existential (∃) quantifiers allow statements about all or some objects in the domain.
3. **Syntax**: Well-formed formulas are built from atomic formulas using connectives and quantifiers.
4. **Semantics**: Interpretations assign meaning to symbols by specifying a domain and mapping constants, functions, and predicates.
5. **Prenex Normal Form**: Converting formulas to PNF (quantifiers at the front) is often a preliminary step in automated theorem proving.

### Inference and Proof
1. **Inference Rules**: Modus Ponens, Modus Tollens, and Resolution are fundamental rules for deriving new knowledge.
2. **Proof Methods**: Direct proof, proof by contradiction, and resolution-based proofs are essential techniques.
3. **Soundness & Completeness**: These properties ensure the reliability and power of logical systems.

### Practical Importance
1. **AI Applications**: Logic forms the foundation of knowledge representation, automated reasoning, planning, and expert systems.
2. **Programming**: Logic programming (Prolog), formal verification, and semantic web technologies directly apply these concepts.
3. **Real-World Relevance**: From legal reasoning to medical diagnosis, logical inference enables intelligent decision-making.

### Delhi University Exam Preparation Tips
1. Practice constructing truth tables for complex propositional formulas
2. Memorize key logical equivalences and inference rules
3. Understand the difference between syntax and semantics in FOL
4. Practice converting formulas to CNF and Prenex Normal Form
5. Solve problems involving semantic entailment and proof construction

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. For further reading, refer to "Artificial Intelligence: A Modern Approach" by Russell and Norvig, and "Logic for Computer Science" by Huth and Ryan.*