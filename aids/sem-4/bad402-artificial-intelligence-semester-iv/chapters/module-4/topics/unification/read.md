# Unification in First Order Logic

## Introduction

Unification is a fundamental concept in First Order Logic (FOL) and automated reasoning. It serves as the core mechanism behind inference procedures like **forward chaining** and **backward chaining**, which are essential for knowledge-based agents in Artificial Intelligence. In simple terms, unification is the process of finding a substitution that makes two logical expressions identical. This allows an AI system to match facts in its knowledge base with patterns in rules, enabling logical inference and problem-solving.

## What is Unification?

Unification is an algorithm that takes two logical expressions and attempts to find a **substitution** (a set of variable assignments) that makes them syntactically identical. If such a substitution exists, the expressions are said to be **unifiable**, and the substitution is called the **unifier**.

### Key Definitions

- **Term**: A constant, a variable, or a function applied to terms.
  - Constants: `a`, `b`, `John`, `5`
  - Variables: `x`, `y`, `z`, `?who`
  - Functions: `father_of(x)`, `f(a, b)`
- **Literal**: An atomic formula (a predicate applied to terms) or its negation. E.g., `Likes(John, x)`, `¬Knows(y, AI)`.
- **Substitution**: A finite set of assignments `θ = {v₁/t₁, v₂/t₂, ..., vₙ/tₙ}`, where each `vᵢ` is a distinct variable and each `tᵢ` is a term different from `vᵢ`. Applying a substitution `θ` to an expression `E` (written `Eθ`) means replacing every occurrence of variable `vᵢ` in `E` with the corresponding term `tᵢ`.
- **Unifier**: A substitution `θ` that makes two expressions identical. For two expressions `E₁` and `E₂`, if `E₁θ = E₂θ`, then `θ` is a unifier for `E₁` and `E₂`.
- **Most General Unifier (MGU)**: The most general unifier `θ` for two expressions is a unifier such that any other unifier `γ` can be expressed as `θ` composed with another substitution `σ` (i.e., `γ = θσ`). The MGU is unique up to variable renaming.

## The Unification Algorithm

The unification algorithm is a recursive process that compares two expressions structure by structure. The core idea is to find a substitution that resolves all differences between the two expressions.

### Algorithm Steps

**Input:** Two expressions, `e1` and `e2`.
**Output:** The Most General Unifier (MGU) `θ` if they are unifiable, or `FAIL` if not.

1.  **Initialize:** Start with an empty substitution `θ = {}`.
2.  **Check for Identical Expressions:** If `e1` and `e2` are identical, return `θ` (the current substitution).
3.  **Variable Cases:**
    - If `e1` is a variable `v` and `v` does not occur in `e2`, extend the substitution `θ = θ ∪ {v/e2}` and apply this new substitution to both expressions. Recurse with the updated expressions and substitution.
    - Similarly, if `e2` is a variable `v` and `v` does not occur in `e1`, extend `θ = θ ∪ {v/e1}` and proceed.
    - **(Occurs Check)** If a variable is being unified with a term that contains that same variable (e.g., `x` and `f(x)`), unification fails. This prevents infinite structures.
4.  **Function/Constant Cases:**
    - If both `e1` and `e2` are constants or functions:
      - If they are different constants (`a` vs. `b`), return `FAIL`.
      - If they are the same constant, proceed.
      - If they are functions (`f(args1)` and `g(args2)`):
        - If the function symbols differ (`f` ≠ `g`), return `FAIL`.
        - If the arity (number of arguments) differs, return `FAIL`.
        - Otherwise, recursively unify the argument lists `args1` and `args2` one by one, accumulating the substitution `θ` at each step.
5.  **Return Result:** If all steps complete without failure, return the accumulated substitution `θ` as the MGU.

### ASCII Diagram of the Algorithm Flow

```
                   Start
                     |
                     v
            +-------------------+
            | Unify(e1, e2, θ) |
            +-------------------+
                     |
         +-----------+-----------+
         |                       |
e1 == e2?                 e1 != e2
   |                             |
   v                             v
Return θ                 +-------+-------+
                         |               |
                   Is e1 a var?    Is e2 a var?
                     /     \         /     \
                    /       \       /       |
             Yes & No Occurs  Yes & No Occurs
                  /   \         /   \
                 /     \       /     |
           θ += {e1/e2}  FAIL  θ += {e2/e1} FAIL
                 |             |
                 v             v
          Recurse with new θ  Recurse with new θ
                         |
                 Are they both functions?
                         |
             +-----------+-----------+
             |                       |
        f != g or           f == g & same arity
      arity mismatch                 |
             |                       v
             v              Recurse on arguments
           FAIL
```

## Examples of Unification

Let's walk through several examples to illustrate the algorithm.

### Example 1: Simple Unification

Unify `Knows(John, x)` and `Knows(John, Jane)`.

1.  Predicates match (`Knows`).
2.  First argument: `John` and `John` are identical constants.
3.  Second argument: `x` (variable) and `Jane` (constant).
    - `x` does not occur in `Jane`, so substitution `θ = {x/Jane}` is valid.
4.  **MGU:** `{x/Jane}`. The unified expression is `Knows(John, Jane)`.

### Example 2: Unification with Functions

Unify `Knows(John, father_of(y))` and `Knows(John, father_of(Jane))`.

1.  Predicates match.
2.  First arguments match (`John`).
3.  Second arguments: `father_of(y)` and `father_of(Jane)`.
    - Function symbols match (`father_of`).
    - Arity is the same (1 argument).
    - Recurse to unify the arguments: `y` and `Jane`.
      - `y` is a variable not in `Jane`. Substitution `θ = {y/Jane}`.
4.  **MGU:** `{y/Jane}`. The unified expression is `Knows(John, father_of(Jane))`.

### Example 3: The Occurs Check (Failure Case)

Unify `P(x, f(x))` and `P(f(y), y)`.

1.  Predicates match.
2.  Unify first arguments: `x` and `f(y)`.
    - `x` is a variable. `x` does not occur in `f(y)`. Substitution `θ₁ = {x/f(y)}`. Apply it to both expressions.
    - Expression 1 becomes `P(f(y), f(f(y)))`
    - Expression 2 becomes `P(f(y), y)`
3.  Now unify the second arguments of these new expressions: `f(f(y))` and `y`.
    - `y` is a variable. We must check if `y` occurs in `f(f(y))`.
    - It does! (`y` is inside the term `f(f(y))`). This would require an infinite substitution `y = f(f(f(f(...))))`. Unification fails.
4.  **Result:** `FAIL`. The expressions are not unifiable.

## The Role of Unification in Inference

Unification is not used in isolation. It is the engine for key inference methods:

- **Forward Chaining:** A data-driven inference method. Unification is used to match the left-hand side (antecedent) of implication rules (`Horn clauses`) with facts in the Knowledge Base (KB). If a rule's premises are found in the KB (via unification), its conclusion is added to the KB.
- **Backward Chaining:** A goal-driven inference method. Unification is used to match a query (goal) against the right-hand side (consequent) of rules. If a goal matches the conclusion of a rule, the system then sets the rule's premises as new sub-goals to be proven.

### Comparison: Unification in Propositional vs. First Order Logic

| Feature             | Propositional Logic            | First Order Logic (with Unification)                           |
| :------------------ | :----------------------------- | :------------------------------------------------------------- |
| **Representation**  | Propositions (Boolean facts)   | Predicates, Objects, Relations, Functions                      |
| **Matching**        | Simple syntactic equality      | Complex syntactic equality via substitution                    |
| **Inference Power** | Limited, often inefficient     | Powerful, enables reasoning about relationships                |
| **Example Rule**    | `Human ⇒ Mortal`               | `Human(x) ⇒ Mortal(x)`                                         |
| **Example Fact**    | `Human(Socrates)`              | `Human(Socrates)`                                              |
| **Inference**       | Modus Ponens applies directly. | Modus Ponens requires unifying `x` with `Socrates` first.      |
| **Efficiency**      | Faster for small domains.      | More computationally expensive but necessary for expressivity. |

## Exam Tips

1.  **Practice the Algorithm:** Be able to execute the unification algorithm step-by-step on paper. This is a common exam question.
2.  **Master the Occurs Check:** Always remember to check if a variable appears inside the term it is being unified with. Forgetting the occurs check is a common mistake. `Unify(x, f(x))` should always fail.
3.  **Apply the Substitution:** When you add a new variable assignment `{v/t}` to your substitution `θ`, you must apply this new `θ` to _both_ expressions before proceeding to unify the next parts. This is crucial for correctness.
4.  **MGU is Key:** Understand that the goal is to find the **Most General Unifier**. A substitution like `{x/y, y/a}` is less general than `{x/y}`. The latter is the MGU; the former is a specific instance of it (`{x/y}{y/a} = {x/a, y/a}`).
5.  **Relate to Inference:** Be prepared to explain _why_ unification is necessary. Connect it to how forward/backward chaining work in First Order Logic, as this demonstrates a deeper understanding.
