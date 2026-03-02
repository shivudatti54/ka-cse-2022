# Propositional Versus First Order Inference

## Introduction

Inference, the process of deriving new facts from known knowledge, is a cornerstone of artificial intelligence. This topic explores the fundamental differences between inference in **Propositional Logic** and **First-Order Logic (FOL)**, two critical knowledge representation systems covered in your syllabus. Understanding this distinction is vital for grasping why FOL is a more powerful and expressive tool for representing real-world knowledge, despite its increased computational complexity.

While Propositional Logic serves as an excellent introduction to logical reasoning, its limitations become apparent when modeling complex environments like the Wumpus World. First-Order Logic overcomes these limitations by introducing variables, quantifiers, and functions, enabling reasoning about objects and their relationships.

## Key Concepts Explained

### 1. Propositional Logic Inference

Propositional Logic (also known as propositional calculus or sentential logic) is the simplest form of logic. Its basic elements are **atomic propositions** (or atoms) that can be either true or false. These atoms are combined using logical connectives like AND (∧), OR (∨), NOT (¬), IMPLIES (→), and IFF (↔).

**Inference in Propositional Logic** involves determining the truth value of a sentence based on the truth values of its constituent propositions and the application of logical rules.

- **Example Atom:** `WumpusIsAlive` – This is a single proposition that is either true or false.
- **Example Rule:** `WumpusIsAlive → SmellIsStrong` (If the Wumpus is alive, then there is a strong smell).

Common inference methods in Propositional Logic include:

- **Truth Tables:** Enumerating all possible combinations of truth values for the atoms in a knowledge base (KB) to see if the query is true in every model where the KB is true.
- **Model Checking:** Algorithmically checking if `KB ⊨ α` (KB entails sentence α).
- **Inference Rules:** Applying rules like **Modus Ponens**:
  `(A → B) and A` therefore `B`.
- **Resolution:** A complete inference algorithm for propositional logic that uses a single rule to derive new clauses until no new clauses can be derived or a contradiction is found.

```
Example of Modus Ponens:
Knowledge Base: [P → Q, P]
Inference Step: Therefore, Q.
```

**Limitation:** To represent a world with multiple objects, you need a separate proposition for each object and property. For example, to represent that pits cause breezes in adjacent squares, you must create a rule for _every single square_: `Pit₁,₁ → Breeze₁,₂`, `Pit₁,₁ → Breeze₂,₁`, etc. This leads to an explosion of rules and is very inefficient.

### 2. First-Order Logic Inference

First-Order Logic (Predicate Logic) is significantly more expressive. It extends Propositional Logic by introducing:

- **Objects:** The entities in the world (e.g., a specific square `[1,2]`, the agent, the Wumpus).
- **Variables:** (e.g., `x`, `y`, `s`) that stand for objects.
- **Predicates:** Symbols that represent relations or properties of objects (e.g., `Pit(x)`, `Adjacent(s1, s2)`, `Breeze(s)`).
- **Functions:** Mappings from objects to objects (e.g., `LeftSide(s)` returns the square to the left of `s`).
- **Quantifiers:**
  - **Universal Quantifier (∀):** "For all..." (e.g., `∀x, King(x) → Person(x)`).
  - **Existential Quantifier (∃):** "There exists..." (e.g., `∃x, Crown(x) ∧ OnHead(x, KingJohn)`).

**Inference in First-Order Logic** is consequently more complex and powerful. It involves instantiating variables with specific objects (called **ground terms**) and applying generalized versions of propositional inference rules.

The key process that enables this is **Unification**.

#### Unification

Unification is the algorithm for determining which substitutions for variables make two logical expressions identical. It is the core operation of FOL inference engines. The `UNIFY` function takes two sentences and returns a **substitution list** (a set of variable/term pairs `{v/t}`) that makes them match, or `FAIL` if no such substitution exists.

| Goal                                         | Substitution (θ)                                  |
| -------------------------------------------- | ------------------------------------------------- |
| `UNIFY(Knows(John, x), Knows(John, Jane))`   | `{x/Jane}`                                        |
| `UNIFY(Knows(John, x), Knows(y, Bill))`      | `{x/Bill, y/John}`                                |
| `UNIFY(Knows(John, x), Knows(y, Mother(y)))` | `{y/John, x/Mother(John)}`                        |
| `UNIFY(Knows(John, x), Knows(x, Elizabeth))` | `FAIL` (can't use `{x/John}` and `{x/Elizabeth}`) |

This allows a generalized rule to be applied to many specific cases. For example, a generalized Modus Ponens rule can be defined using unification.

#### Generalized Modus Ponens

This is a lifted version of the propositional Modus Ponens rule. It can be stated as: For atomic sentences \( p_i', q \), and \( p_i \), where there is a substitution \( \theta \) such that \( SUBST(\theta, p_i') = SUBST(\theta, p_i) \), for all \( i \):

\[
\frac{p_1', p_2', ..., p_n', \quad (p_1 \land p_2 \land ... \land p_n \rightarrow q)}{SUBST(\theta, q)}
\]

**Example:**

- Rule: `Animal(TailOf(x)) ∧ Has(x, Tail) → Mammal(x)` (_If the tail of x is an animal and x has a tail, then x is a mammal_)
- Facts: `Animal(TailOf(Cat))`, `Has(Cat, Tail)`
- Unification: `UNIFY( (Animal(TailOf(x)), Has(x, Tail)), (Animal(TailOf(Cat)), Has(Cat, Tail)) )` returns `θ = {x/Cat}`
- Inference: Therefore, apply `SUBST({x/Cat}, Mammal(x))` to infer `Mammal(Cat)`.

This one generalized rule can be applied to any object, unlike propositional logic which would require a separate rule for every single animal.

### 3. Forward and Backward Chaining

Two major families of inference algorithms use Generalized Modus Ponens.

- **Forward Chaining:** A data-driven approach. Start with the known facts in the knowledge base and apply all applicable rules to derive new facts. This process repeats until the desired query is derived or no new facts can be derived. It is useful for deducing all possible conclusions from the available data, e.g., in a diagnostic system.
- **Backward Chaining:** A goal-driven approach. Start with the query (the goal) and work backwards, seeing what rules would imply that goal. The premises of those rules become new sub-goals. This process continues until all sub-goals are matched against known facts. It is the basis of **logic programming** (e.g., Prolog) and is efficient for proving specific truths.

## Comparison: Propositional vs. First-Order Inference

| Feature                      | Propositional Logic Inference                              | First-Order Logic Inference                                                                                    |
| ---------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Expressiveness**           | Low. Can only represent facts, no objects or relations.    | High. Can represent objects, relations, functions, and general laws.                                           |
| **Elements**                 | Propositions (Boolean variables).                          | Objects, Variables, Predicates, Functions, Quantifiers.                                                        |
| **Rule Application**         | Specific. A rule like `P → Q` only applies to `P` and `Q`. | General. A rule like `∀x P(x) → Q(x)` can be applied to any object `A` via substitution.                       |
| **Key Inference Process**    | Boolean satisfiability (e.g., truth tables, resolution).   | **Unification** + Generalized Modus Ponens (or resolution).                                                    |
| **Scalability**              | Poor for large worlds. Rule count grows exponentially.     | Good for large worlds. Rules capture general patterns.                                                         |
| **Computational Complexity** | NP-Complete (SAT is the canonical NP-complete problem).    | Undecidable. No algorithm can say yes/no to all entailments. Semi-decidable (will find a proof if one exists). |
| **Use Case Example**         | Simple circuits, small puzzle games.                       | Natural language understanding, knowledge bases (e.g., Wikidata), complex game AI.                             |

```
ASCII Diagram: Forward vs. Backward Chaining

Forward Chaining (Data-Driven)
Facts: [A, B, C] --> Apply Rules --> New Facts: [D, E] --> Apply Rules --> New Fact: [F] --> ... --> Query [Z] is found!

Backward Chaining (Goal-Driven)
Goal: Prove Z? --> Rule: X ∧ Y → Z, so new subgoals: Prove X? Prove Y?
Subgoal Y? --> Fact: Y is true! ✅
Subgoal X? --> Rule: A ∧ B → X, so new subgoals: Prove A? Prove B?
Subgoal A? --> Fact: A is true! ✅
Subgoal B? --> Fact: B is true! ✅
Therefore, X is true, therefore Z is true. ✅
```

## Exam Tips

1.  **Understand Unification:** Be prepared to perform unification on two simple predicates. Write out the substitution set clearly. Remember that a variable cannot be unified with a term containing that same variable (e.g., `UNIFY(x, F(x))` fails due to the "occurs check").
2.  **Generalized Modus Ponens:** You will likely be given a rule and a set of facts and asked to state the conclusion. Identify the correct substitution `θ` first, then apply it to the conclusion of the rule.
3.  **Know the Differences:** Be ready to explain _why_ FOL is more expressive than propositional logic, using concrete examples (like the Wumpus World). Use the comparison table as a study guide.
4.  **Chaining:** Understand the difference between forward and backward chaining. An exam question might ask you to list one advantage of each (e.g., Forward: derives all facts. Backward: efficient for specific queries).
5.  **Complexity:** Remember the key terms: Propositional inference is **NP-Complete**, FOL inference is **Undecidable** but **Semi-decidable**.
