# Using First-Order Logic

## Introduction

First-Order Logic (FOL), also known as Predicate Logic, is a powerful symbolic representation framework that extends Propositional Logic to handle richer representations of knowledge. While Propositional Logic deals with atomic propositions that are either true or false, First-Order Logic introduces variables, predicates, and quantifiers, enabling us to represent statements about objects and their relationships in a more expressive and natural manner.

In Artificial Intelligence, knowledge representation is fundamental to building intelligent systems. First-Order Logic serves as the backbone for many AI applications because it provides a formal framework for representing facts about the world, reasoning about those facts, and deriving new conclusions. From expert systems to natural language processing, from automated theorem proving to knowledge graphs, FOL plays a crucial role. For students studying AI, understanding FOL is essential because it forms the foundation for more advanced topics like logic programming, automated reasoning, and knowledge-based systems.

The importance of FOL in computer science cannot be overstated. It allows us to express general rules and patterns rather than just specific facts. For instance, we can state that "all humans are mortal" as a single logical formula instead of listing millions of individual statements about specific humans. This ability to express general knowledge compactly makes FOL an indispensable tool for knowledge representation and reasoning.

## Key Concepts

### Syntax of First-Order Logic

The syntax of FOL consists of several building blocks that combine to form meaningful logical expressions. Understanding these components is crucial for constructing and interpreting FOL formulas.

**Constants** (or Individual Constants): These represent specific objects in the domain. Examples: John, Paris, x1, A (typically uppercase initial)

**Variables** (or Individual Variables): These represent unspecified objects and can take different values. Examples: x, y, z

**Predicates** (or Relation Symbols): These represent properties of objects or relationships between objects. Examples: Mortal(x), Likes(x,y), BrotherOf(x,y)

**Function Symbols**: These map tuples of objects to a single object. Examples: FatherOf(x), Plus(x,y), MotherOf(x)

**Quantifiers**: FOL introduces two crucial quantifiers:

- **Universal Quantifier (∀)**: States that a property holds for all objects in the domain. Symbol: ∀
- **Existential Quantifier (∃)**: States that there exists at least one object in the domain for which a property holds. Symbol: ∃

**Logical Connectives**: Same as propositional logic - ¬ (not), ∧ (and), ∨ (or), → (implication), ↔ (biconditional)

**Terms**: A term is a constant, variable, or function applied to terms. Examples: John, x, FatherOf(John), Plus(x,y)

**Atoms (Atomic Formulas)**: A predicate symbol applied to appropriate number of terms. Examples: Mortal(John), Likes(x,y), GreaterThan(x,5)

**Well-Formed Formulas (WFFs)**: Formulas are built from atoms using quantifiers and connectives according to proper formation rules.

### Semantics and Interpretation

The semantics of FOL defines the meaning of formulas. An **interpretation** assigns meaning to all symbols in the language:

- Each constant is assigned to a specific object in the domain
- Each predicate is assigned to a relation on the domain
- Each function symbol is assigned to a function from the domain to itself

An interpretation I = (D, I₀) consists of:

- D: Non-empty domain of discourse
- I₀: Mapping that assigns meanings to symbols

A formula is **true** under an interpretation if it evaluates to true based on the assigned meanings. A formula is **valid** (tautology) if it is true under all possible interpretations. A formula is **satisfiable** if there exists at least one interpretation under which it is true.

### Quantifiers and Their Scopes

The scope of a quantifier is the formula immediately following it. For example, in ∀x (P(x) → Q(x)), the scope of ∀x is (P(x) → Q(x)). Variables within the scope are **bound**; variables outside any quantifier are **free**.

Key properties:

- ∀x P(x) is true if P(x) is true for every x in the domain
- ∃x P(x) is true if P(x) is true for at least one x in the domain
- ¬∀x P(x) ≡ ∃x ¬P(x) (Negation of universal is existential of negation)
- ¬∃x P(x) ≡ ∀x ¬P(x) (Negation of existential is universal of negation)

### Knowledge Representation in FOL

FOL excels at representing various types of knowledge:

**Facts**: Simple statements about objects

```
Human(Socrates)
Mortal(Socrates)
```

**Rules**: General statements with variables

```
∀x (Human(x) → Mortal(x))
∀x ∀y (Father(x,y) → Parent(x,y))
```

**Relationships**: Binary and n-ary relations

```
∀x ∀y (Loves(x,y) → ∃z (Feeling(x,z)))
```

**Categorical Statements**:

- All S are P: ∀x (S(x) → P(x))
- Some S are P: ∃x (S(x) ∧ P(x))
- No S are P: ∀x (S(x) → ¬P(x))
- Some S are not P: ∃x (S(x) ∧ ¬P(x))

### Inference in First-Order Logic

Inference in FOL involves deriving new facts from known facts using inference rules. Key mechanisms include:

**Substitution**: Replacing a variable with a term. Example: Substitute x/John in P(x) gives P(John)

**Unification**: Finding a substitution that makes two atomic formulas identical. The UNIFY algorithm is fundamental to FOL inference. For example, Unify(P(x), P(John)) = {x/John}

**Modus Ponens (Generalized)**: From P(c) and ∀x (P(x) → Q(x)), infer Q(c)

**Universal Instantiation**: From ∀x P(x), infer P(c) for any constant c

**Existential Instantiation**: From ∃x P(x), introduce a new constant c to represent "something that satisfies P"

**Resolution**: A complete inference rule for FOL. The resolution principle involves:

- Negating the conclusion
- Adding it to premises
- Applying resolution to derive the empty clause (contradiction)

## Examples

### Example 1: Representing Family Relationships

**Problem**: Represent the following facts in FOL and answer queries using inference.

**Facts**:

1. John is the father of James
2. Mary is the mother of James
3. Every parent is a grandparent of their child's children

**Representation**:

```
Father(John, James)
Mother(Mary, James)
∀x ∀y ∀z ((Parent(x,y) ∧ Parent(y,z)) → Grandparent(x,z))
∀x (Father(x,y) → Parent(x,y))
∀x (Mother(x,y) → Parent(x,y))
```

**Query**: Is John a grandparent of someone?
Using universal instantiation and modus ponens:

- From Parent(John, James) and Parent(James, ?), we can infer Grandparent(John, ?)
- Therefore, John is a grandparent.

### Example 2: Unification Process

**Problem**: Find the most general unifier (MGU) for the following pairs:

a) P(x, f(y)) and P(g(z), f(z))

**Solution**:

- Compare positions: x must equal g(z), and f(y) must equal f(z)
- From x = g(z), we get substitution {x/g(z)}
- From f(y) = f(z), we get substitution {y/z}
- Combined: {x/g(z), y/z}
- This is the MGU

b) Q(x, y) and Q(a, b) where a and b are constants

**Solution**:

- x = a, y = b
- Substitution: {x/a, y/b}

c) R(x, x) and R(y, f(y))

**Solution**:

- First position: x = y
- Second position: x = f(y)
- From x = y, substitute: f(y) = f(x)
- This creates a circular dependency f(x) = x, which is impossible
- **No unifier exists** - these cannot be unified

### Example 3: Automated Reasoning with Resolution

**Problem**: Prove that Socrates is mortal given:

1. ∀x (Human(x) → Mortal(x))
2. Human(Socrates)

**Solution using Resolution**:

1. Convert to clause form:

- Clause 1: ¬Human(x) ∨ Mortal(x)
- Clause 2: Human(Socrates)

2. Negate the goal (Mortal(Socrates)): ¬Mortal(Socrates)

3. Apply resolution:

- Resolve clause 1 with negated goal: ¬Human(x) ∨ Mortal(x) resolved with ¬Mortal(Socrates)
- This gives: ¬Human(Socrates)
- Resolve this with clause 2: ¬Human(Socrates) resolved with Human(Socrates)
- This produces the empty clause (□)

4. Since we derived a contradiction, the negated goal is false, and therefore Mortal(Socrates) is true.

## Exam Tips

1. **Understand the difference between ∀ and ∃**: Remember that ∀x P(x) is equivalent to ¬∃x ¬P(x), and ∃x P(x) is equivalent to ¬∀x ¬P(x). This is crucial for negation problems.

2. **Free vs Bound Variables**: In ∀x P(x), x is bound. Only bound variables can be renamed (α-conversion). Free variables cannot be quantified.

3. **Scope of Quantifiers**: Be careful with nested quantifiers. ∀x ∃y P(x,y) means "for every x there exists some y", which is different from ∃y ∀x P(x,y).

4. **Unification Algorithm**: Remember the three conditions for unification failure: (a) different predicate symbols, (b) different numbers of arguments, (c) occurs check failure (trying to unify x with f(x)).

5. **Converting English to FOL**: Identify constants (specific objects), predicates (properties/relations), and quantifiers. Use implication (→) for "if-than" statements and conjunction (∧) for "and" statements.

6. **Resolution is Complete**: For first-order logic, resolution is refutation-complete - if a conclusion logically follows from premises, resolution can prove it (given sufficient search).

7. **Skolemization**: Remember that to use resolution, you must remove existential quantifiers through Skolemization, replacing existential variables with Skolem functions or constants.

8. **Common Mistake**: Don't confuse ∀x (P(x) ∧ Q(x)) with (∀x P(x)) ∧ (∀x Q(x)) - they are not equivalent in general. Similarly, (∃x P(x)) ∨ (∃x Q(x)) is not equivalent to ∃x (P(x) ∨ Q(x)).
