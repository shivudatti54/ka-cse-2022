# Propositional and Predicate Logic

## Introduction
Propositional and predicate logic form the foundational framework for mathematical reasoning in computer science. Propositional logic deals with simple declarative statements (propositions) and their combinations using logical connectives. Predicate logic extends this by introducing quantifiers and variables, enabling more expressive statements about objects and their relationships.

These logical systems are essential for:
- Designing digital circuits and Boolean algebra applications
- Formulating database queries (SQL uses predicate logic)
- Developing algorithms and proving program correctness
- Artificial Intelligence (knowledge representation and automated reasoning)

In the DU MCA curriculum, mastery of this topic is critical for subsequent courses in algorithms, theory of computation, and software verification. Industry applications range from developing search algorithms to creating formal specifications for safety-critical systems.

## Key Concepts
1. **Propositions**: Atomic statements with definite truth values (e.g., "It is raining")
2. **Logical Connectives**:
   - Negation (¬)
   - Conjunction (∧)
   - Disjunction (∨)
   - Implication (→)
   - Biconditional (↔)
3. **Truth Tables**: Systematic representation of compound proposition truth values
4. **Tautologies & Contradictions**: Statements always true/false regardless of component truth values
5. **Logical Equivalence**: p ≡ q if p ↔ q is tautology
6. **Predicates**: Statements containing variables (e.g., P(x): "x > 5")
7. **Quantifiers**:
   - Universal (∀): "For all"
   - Existential (∃): "There exists"
8. **Nested Quantifiers**: Multiple quantifiers in sequence (e.g., ∀x∃y P(x,y))

## Examples

**Example 1: Truth Table Construction**
Construct truth table for (p ∧ ¬q) → r

**Solution**:
| p | q | r | ¬q | p ∧ ¬q | (p ∧ ¬q) → r |
|---|---|---|----|--------|--------------|
| T | T | T | F  | F      | T            |
| T | T | F | F  | F      | T            |
| T | F | T | T  | T      | T            |
| T | F | F | T  | T      | F            |
| F | T | T | F  | F      | T            |
| F | T | F | F  | F      | T            |
| F | F | T | T  | F      | T            |
| F | F | F | T  | F      | T            |

**Example 2: Logical Equivalence Proof**
Prove ¬(p ∨ q) ≡ ¬p ∧ ¬q (De Morgan's Law)

**Solution**:
1. Construct truth tables for both sides:
```
p | q | p∨q | ¬(p∨q) | ¬p | ¬q | ¬p∧¬q
T | T | T   | F      | F  | F  | F
T | F | T   | F      | F  | T  | F
F | T | T   | F      | T  | F  | F
F | F | F   | T      | T  | T  | T
```
2. Compare last two columns - identical truth values
3. Hence, proved

**Example 3: Predicate Logic Translation**
Express "Every student has a unique ID" in predicate logic

**Solution**:
Let S(x): x is a student
ID(x,y): x has ID y

∀x(S(x) → ∃y(ID(x,y) ∧ ∀z(ID(x,z) → y = z)))

## Exam Tips
1. Memorize key equivalences: De Morgan's laws, implication conversion (p→q ≡ ¬p∨q)
2. Practice quick truth table construction (use 2ⁿ rows for n variables)
3. For nested quantifiers, order matters: ∀x∃y ≠ ∃y∀x
4. In proofs, clearly state each step and equivalence used
5. Convert English statements to logic systematically:
   - Identify quantifiers first
   - Determine predicate scope
6. Watch for domain restrictions in predicate logic
7. Use indirect proof techniques (contrapositive, contradiction) for implication problems