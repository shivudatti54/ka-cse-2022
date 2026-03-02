# Unification in Logic Programming

## Introduction

Unification is a fundamental concept in artificial intelligence, logic programming, and automated theorem proving. It serves as the core mechanism for pattern matching and variable binding in languages like Prolog and inference systems. In essence, unification is the process of making two logical expressions identical by finding suitable substitutions for variables. This process allows programs to reason about relationships between objects, perform symbolic computation, and implement intelligent search strategies.

The concept of unification was formalized by Robinson in 1965 and became the backbone of resolution-based theorem proving. It enables computers to perform symbolic manipulation without explicit programming of every possible case, making it essential for expert systems, natural language processing, and declarative programming paradigms. Understanding unification is crucial for any computer science student as it bridges the gap between mathematical logic and practical programming applications.

In the context of 's Computer Science curriculum, unification forms the theoretical foundation for understanding how logic programming languages work internally. It represents the mechanism through which variables get bound to values, allowing pattern matching and backtracking to occur in Prolog and similar languages.

## Key Concepts

### Substitution

A substitution is a mapping from variables to terms. It is represented as a set of pairs {x₁/t₁, x₂/t₂, ..., xₙ/tₙ} where each xᵢ is a variable and each tᵢ is a term. The application of a substitution θ to a term t, denoted as tθ, replaces all occurrences of the variables in the domain of θ with their corresponding terms. For example, if θ = {X/a, Y/f(Z)}, then applying θ to f(X, Y) results in f(a, f(Z)).

The identity substitution, denoted as ε or {}, makes no changes to terms. Substitutions can be composed: if θ₁ = {X/a} and θ₂ = {Y/b}, then θ₁θ₂ = {X/a, Y/b}. Composition is applied right to left, meaning first apply θ₂, then θ₁.

### Terms

Terms are the fundamental building blocks in unification. They can be constants (atoms like a, b, john), variables (X, Y, Z), or compound terms (structures like f(a), father(john), likes(X, Y)). Compound terms consist of a functor (a function symbol) and a list of arguments, which are themselves terms. The arity (number of arguments) is part of the functor's identity.

Complex terms can be nested, such as f(g(X), h(Y, a)). Understanding the structure of terms is essential for determining whether two terms can be unified and what substitutions are needed.

### Unifier

A unifier of two terms t₁ and t₂ is a substitution θ such that t₁θ = t₂θ. In other words, after applying the substitution, both terms become identical. Not all pairs of terms have a unifier. For instance, f(X) and g(Y) cannot be unified because their root functors are different (f ≠ g).

When two terms can be unified, there may exist multiple unifiers. For example, for terms f(X, a) and f(b, Y), both θ₁ = {X/b, Y/a} and θ₂ = {X/b, Y/a} are valid unifiers (in this case, there's only one).

### Most General Unifier (MGU)

Among all possible unifiers of two terms, the most general unifier (MGU) is the one that makes the least restrictive commitments. The MGU is unique (up to renaming of variables) and is considered the "best" unifier because it leaves the most flexibility for further unification.

If θ is an MGU of t₁ and t₂, then any other unifier θ' can be expressed as θ' = θλ for some substitution λ. For example, for terms f(X) and f(a), the MGU is {X/a}. However, {X/a, Y/b} is also a unifier of f(X) and f(a), but it's less general because it makes additional bindings.

### Occurs Check

The occurs check is a crucial part of a correct unification algorithm. It prevents the creation of infinite terms (cyclic structures) by ensuring that a variable is not unified with a term that contains that variable itself. Without the occurs check, unification could produce terms like X = f(X), which represents an infinite structure.

For example, unifying X with f(X) would lead to an infinite term. The occurs check verifies whether X appears in the term t before binding X to t. If X occurs in t, unification fails. Most practical Prolog implementations omit the occurs check for efficiency reasons, but this can lead to soundness issues in certain cases.

### Unification Algorithm

The unification algorithm works recursively by comparing the structure of two terms:

1. If both terms are identical constants or variables, return the identity substitution.
2. If one term is a variable, apply the occurs check and return the appropriate binding.
3. If both terms are compound terms, check if they have the same functor and arity. If not, unification fails. If yes, recursively unify the corresponding arguments pairwise.
4. The final substitution is the composition of all individual unifications.

The algorithm returns either the MGU or indicates failure when unification is impossible.

## Examples

### Example 1: Simple Constant Unification

Unify the terms: father(john) and father(john)

**Solution:**

- Both terms have the same functor (father) and same arity (1)
- Both arguments are the same constant (john)
- Since all corresponding components are identical, they unify with the identity substitution
- MGU: {}

This is the simplest case of unification where the terms are already identical.

### Example 2: Variable Binding

Unify the terms: likes(X, music) and likes(john, Y)

**Solution:**
Step 1: Both terms have functor "likes" and arity 2 - compatible.

Step 2: Unify first arguments:

- X (variable) and john (constant)
- Bind X = john
- Substitution θ₁ = {X/john}

Step 3: Unify second arguments:

- music (constant) and Y (variable)
- Bind Y = music
- Substitution θ₂ = {Y/music}

Step 4: Compose substitutions: θ = θ₁θ₂ = {X/john, Y/music}

**Verification:**

- likes(X, music)θ = likes(john, music)
- likes(john, Y)θ = likes(john, music)
- Both result in identical terms

MGU: {X/john, Y/music}

### Example 3: Nested Terms with Occurs Check

Unify the terms: f(X, g(X)) and f(h(Y), Z)

**Solution:**
Step 1: Both have functor "f" and arity 2 - compatible.

Step 2: Unify first arguments:

- X (variable) and h(Y) (compound term)
- Check occurs: Does X appear in h(Y)? No
- Bind X = h(Y)
- θ₁ = {X/h(Y)}

Step 3: Unify second arguments:

- g(X) and Z (variable)
- Substitute X in g(X): g(X)θ₁ = g(h(Y))
- Now unify g(h(Y)) with Z
- Check occurs: Does Z appear in g(h(Y))? No
- Bind Z = g(h(Y))
- θ₂ = {Z/g(h(Y))}

Step 4: Compose: θ = {X/h(Y), Z/g(h(Y))}

**Verification:**

- f(X, g(X))θ = f(h(Y), g(h(Y)))
- f(h(Y), Z)θ = f(h(Y), g(h(Y)))
- Both terms become identical

MGU: {X/h(Y), Z/g(h(Y))}

### Example 4: Failed Unification

Unify the terms: f(X, a) and g(X, b)

**Solution:**

- First terms have different functors: f ≠ g
- Since the root functors differ, these terms cannot be unified regardless of variable bindings
- Unification FAILS
- No MGU exists

This demonstrates that unification is not always possible and that structural compatibility is required.

## Exam Tips

1. **Understand the definition**: Remember that unification finds a substitution θ such that t₁θ = t₂θ. This is the most fundamental concept that appears in exam questions.

2. **MGU uniqueness**: The MGU is unique up to variable renaming. If you find two different MGUs, they should differ only in variable names.

3. **Occurs check importance**: Always remember to perform the occurs check when binding a variable to a compound term. Failure to do so can create infinite structures.

4. **Step-by-step approach**: In exam problems, show each step of unification clearly. First check functors, then unify arguments recursively.

5. **Common failure cases**: Know when unification fails: different functors, different arities, and occurs check failure.

6. **Composition order**: Remember that substitution composition is right-to-left: (tθ₁)θ₂ means apply θ₁ first, then θ₂.

7. **Practice with nested terms**: Most exam questions involve nested compound terms. Practice unifying terms with multiple levels of nesting.
