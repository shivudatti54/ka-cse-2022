# Predicate Logic in Knowledge Representation

## Introduction to Predicate Logic

Predicate Logic, also known as First-Order Logic (FOL), is a formal system used in mathematics, philosophy, linguistics, and computer science for representing knowledge about the world in a structured way. It extends propositional logic by dealing with predicates and quantifiers, allowing us to express properties of objects and relationships between them.

In artificial intelligence, predicate logic serves as a fundamental tool for knowledge representation, enabling AI systems to reason about facts, make inferences, and solve problems in a logically sound manner.

## Basic Components of Predicate Logic

### Constants, Variables, and Functions

Predicate logic builds upon several basic elements:

- **Constants**: Represent specific objects or entities (e.g., John, Paris, 5)
- **Variables**: Represent unspecified objects (e.g., x, y, z)
- **Functions**: Map objects to other objects (e.g., fatherOf(John))
- **Predicates**: Represent properties or relations (e.g., Human(John), Likes(John, Mary))
- **Quantifiers**: Express generalizations (∀ for "for all", ∃ for "there exists")

### Syntax and Semantics

The syntax of predicate logic defines how to form well-formed formulas:
```
<atomic formula> ::= <predicate>(<term>,...,<term>)
<term> ::= <constant> | <variable> | <function>(<term>,...,<term>)
<formula> ::= <atomic formula> | ¬<formula> | <formula>∧<formula> | 
              <formula>∨<formula> | <formula>→<formula> | 
              ∀<variable><formula> | ∃<variable><formula>
```

The semantics provides meaning to these formulas through interpretations that map symbols to objects, properties, and relations in a domain.

## Quantifiers in Predicate Logic

### Universal Quantifier (∀)

The universal quantifier (∀) asserts that a property holds for all objects in the domain.

**Example**: ∀x Human(x) → Mortal(x)
"All humans are mortal."

### Existential Quantifier (∃)

The existential quantifier (∃) asserts that there exists at least one object for which a property holds.

**Example**: ∃x Human(x) ∧ Wise(x)
"There exists a human who is wise."

### Nested Quantifiers

Quantifiers can be nested to express more complex statements:

**Example**: ∀x∃y Loves(x, y)
"Everyone loves someone."

**Example**: ∃x∀y Loves(x, y)
"Someone loves everyone."

## Representing Knowledge with Predicate Logic

### Representing Facts

Simple facts can be represented as atomic formulas:

- Student(John) - "John is a student"
- Teaches(DrSmith, CS101) - "Dr. Smith teaches CS101"
- OlderThan(John, Mary) - "John is older than Mary"

### Representing Rules

Implications allow us to represent rules:

∀x Student(x) ∧ Studies(x, AI) → InterestedIn(x, Robotics)
"All students who study AI are interested in Robotics."

### Representing Complex Domains

Predicate logic can model complex domains with multiple entities and relationships:

```
∀x Person(x) → ∃y Mother(y, x)
∀x∀y Mother(x, y) → Female(x) ∧ Parent(x, y)
∀x∀y Parent(x, y) → Older(x, y)
```

## Inference in Predicate Logic

### Modus Ponens and Modus Tollens

These inference rules from propositional logic extend to predicate logic:

- **Modus Ponens**: From P → Q and P, infer Q
- **Modus Tollens**: From P → Q and ¬Q, infer ¬P

### Universal Instantiation

From ∀x P(x), infer P(c) for any constant c in the domain.

**Example**: From ∀x Human(x) → Mortal(x) and Human(Socrates), infer Mortal(Socrates)

### Existential Instantiation

From ∃x P(x), infer P(c) for some new constant c.

**Example**: From ∃x Wise(x), infer Wise(c) for a new constant c representing a wise person.

### Resolution Principle

The resolution rule can be extended to predicate logic by using unification to find substitutions that make predicates identical.

## Unification

Unification is the process of finding a substitution that makes two expressions identical. It's crucial for inference in predicate logic.

**Example**: Unify P(x, f(y)) and P(a, f(z)) with substitution {x/a, y/z}

## Conversion to Clause Form

To apply resolution, formulas must be converted to clause form:

1. Eliminate implications
2. Move negations inward
3. Standardize variables
4. Skolemize existential quantifiers
5. Convert to prenex form
6. Convert to conjunctive normal form
7. Write as clauses

## Comparison with Other Representation Schemes

| Representation | Expressiveness | Inference Complexity | Naturalness |
|----------------|----------------|----------------------|-------------|
| Propositional Logic | Low | Efficient | Low |
| **Predicate Logic** | **High** | **Semi-decidable** | **High** |
| Semantic Networks | Medium | Efficient | Medium |
| Frames | Medium | Efficient | High |
| Production Rules | Medium | Efficient | Medium |

## Advantages and Limitations

### Advantages of Predicate Logic

- Precise and unambiguous representation
- Well-defined syntax and semantics
- Supports complex reasoning and inference
- Modular knowledge representation
- Foundation for many AI systems

### Limitations of Predicate Logic

- Computational complexity of inference
- Inability to handle uncertainty directly
- Monotonicity (cannot retract conclusions)
- Limited expressiveness for certain domains

## Applications in AI

Predicate logic finds applications in:
- Theorem proving systems
- Expert systems
- Natural language processing
- Knowledge bases
- Planning systems
- Semantic web

## Example: Family Relationships

```
// Constants
John, Mary, Bob

// Predicates
Parent(x, y), Father(x, y), Mother(x, y), Sibling(x, y)

// Axioms
∀x∀y Parent(x, y) → (Father(x, y) ∨ Mother(x, y))
∀x∀y Father(x, y) → Male(x)
∀x∀y Mother(x, y) → Female(x)
∀x∀y Sibling(x, y) ↔ (∃z Parent(z, x) ∧ Parent(z, y) ∧ x ≠ y)

// Facts
Parent(John, Bob), Parent(Mary, Bob), Male(John), Female(Mary)
```

From these, we can infer Sibling(Bob, Bob) is false and other relationships.

## Exam Tips

1. **Understand quantifier scope**: Pay attention to which variables are bound by which quantifiers.
2. **Practice conversion to clause form**: This is often required for resolution proofs.
3. **Master unification**: Be comfortable with finding the most general unifier for pairs of expressions.
4. **Distinguish between syntax and semantics**: Understand the difference between well-formed formulas and their interpretations.
5. **Practice with different domains**: Work through examples from various domains (family relationships, arithmetic, etc.).
6. **Compare with propositional logic**: Be prepared to explain how predicate logic extends propositional logic.
7. **Know the limitations**: Understand what predicate logic cannot represent well, such as uncertainty or procedural knowledge.