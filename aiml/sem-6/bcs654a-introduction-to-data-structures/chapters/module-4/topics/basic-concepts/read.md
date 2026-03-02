# Basic Propositional Logic

## What is a Proposition?

A declarative statement that is either TRUE or FALSE.

**Examples:**
- "2 + 2 = 4" (True)
- "Paris is in Germany" (False)
- "x > 5" (Not a proposition - depends on x)

## Logical Connectives

| Connective | Symbol | Name | Example |
|------------|--------|------|---------|
| NOT | ¬, ~ | Negation | ¬p |
| AND | ∧, · | Conjunction | p ∧ q |
| OR | ∨, + | Disjunction | p ∨ q |
| IF-THEN | →, ⊃ | Implication | p → q |
| IFF | ↔, ≡ | Biconditional | p ↔ q |
| XOR | ⊕ | Exclusive OR | p ⊕ q |

## Truth Tables

### Negation (NOT)
| p | ¬p |
|---|---|
| T | F |
| F | T |

### Conjunction (AND)
| p | q | p ∧ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### Disjunction (OR)
| p | q | p ∨ q |
|---|---|-------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### Implication (→)
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Key**: p → q is FALSE only when p is TRUE and q is FALSE.

### Biconditional (↔)
| p | q | p ↔ q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

**Key**: TRUE when both have same truth value.

## Operator Precedence

1. ¬ (NOT) - highest
2. ∧ (AND)
3. ∨ (OR)
4. → (Implication)
5. ↔ (Biconditional) - lowest

## Special Forms

### Tautology
Always TRUE regardless of variable values.
- Example: p ∨ ¬p

### Contradiction
Always FALSE regardless of variable values.
- Example: p ∧ ¬p

### Contingency
Can be TRUE or FALSE depending on values.
- Example: p ∧ q

## Converse, Inverse, Contrapositive

Given: p → q
- **Converse**: q → p
- **Inverse**: ¬p → ¬q
- **Contrapositive**: ¬q → ¬p

**Important**: p → q ≡ ¬q → ¬p (contrapositive is equivalent)

## Exam Tips

1. **Implication FALSE only when**: T → F
2. **p → q ≡ ¬p ∨ q** (material implication)
3. **Contrapositive is equivalent** to original
4. **Converse is NOT equivalent** to original
