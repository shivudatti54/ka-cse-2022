# Introduction to Prolog

## Introduction

Prolog (Programming in Logic) is a high-level programming language that fundamentally differs from traditional imperative languages like C, Java, or Python. Developed in the 1970s at the University of Marseille, France by Alain Colmerauer and Philippe Roussel, Prolog is the primary representative of the Logic Programming paradigm. Unlike procedural languages where you specify *how* to solve a problem step by step, in Prolog you specify *what* is true about the problem using logical relationships. The system then automatically determines how to derive answers through logical inference.

In the context of Artificial Intelligence, Prolog holds special significance because of its natural fit with symbolic reasoning and knowledge representation. Many early AI systems, including natural language processing applications and expert systems, were built using Prolog. Its ability to handle pattern matching, backtracking, and automatic theorem proving makes it an ideal tool for problems involving search, constraint satisfaction, and logical deduction. For DU students studying AI, understanding Prolog provides insight into alternative computational paradigms and demonstrates the power of declarative programming.

This topic introduces the fundamental concepts of Prolog programming, including facts, rules, queries, unification, and backtracking. These concepts form the foundation for building intelligent systems that can reason about structured knowledge.

## Key Concepts

### 1. The Logic Programming Paradigm

Logic Programming is based on Horn clauses—logical statements that can be either facts or rules. A Prolog program consists of a database of facts and rules, and queries ask whether a particular goal can be derived from this knowledge base. The Prolog interpreter uses resolution and unification to answer queries, effectively performing automated reasoning.

### 2. Facts

Facts are basic assertions about the world that are unconditionally true. In Prolog, facts are written as predicates with specific arguments. The syntax follows the pattern: `predicate(argument1, argument2, ...).`

For example:
```prolog
% Facts about a family
male(john).
male(bob).
female(lisa).
female(mary).
parent(john, bob).
parent(john, lisa).
parent(mary, bob).
parent(mary, lisa).
```

In these facts, `male(john)` means "John is male" and is unconditionally true. Facts form the foundation of your knowledge base.

### 3. Rules

Rules express conditional relationships. They have the form `Head :- Body.` which reads as "Head is true if Body is true." The `:-` operator is called the "neck" symbol.

```prolog
% Rule: X is a parent of Y if X is a mother of Y
mother(X, Y) :- female(X), parent(X, Y).

% Rule: X is a sibling of Y if they share a parent
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Rule: X is a grandfather of Y
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).
```

Rules can contain multiple conditions separated by commas (meaning logical AND).

### 4. Variables and Anonymous Variables

Variables in Prolog start with uppercase letters or underscores. When you ask a query with a variable, Prolog attempts to find all values that make the query true.

```prolog
?- parent(john, X).
X = bob ;
X = lisa.

?- parent(X, Y).
X = john,
Y = bob ;
X = john,
Y = lisa ;
X = mary,
Y = bob ;
X = mary,
Y = lisa.
```

The underscore `_` is an anonymous variable used when you don't care about a particular value:

```prolog
% Who is male? (we don't need to know who)
?- male(_).
true.
```

### 5. Unification

Unification is the core mechanism by which Prolog matches terms. Two terms unify if they can be made identical by substituting variables with appropriate values.

Rules of unification:
- A variable unifies with any term, becoming bound to that term
- Two constants unify only if they are identical
- Two compound terms (predicates) unify if they have the same functor and arity, and all their arguments unify recursively

```prolog
?- X = john.          % X unifies with john
X = john.

?- father(john, X) = father(Y, bob).  % Unification creates bindings
X = bob,
Y = john.

?- likes(john, X) = likes(Y, pizza).
X = pizza,
Y = john.
```

### 6. Backtracking

Prolog uses backtracking to explore alternative solutions. When a goal fails, Prolog backtracks to the last choice point and tries a different alternative. This is fundamental to how Prolog searches for solutions.

```prolog
% Knowledge base
likes(john, pizza).
likes(john, pasta).
likes(jane, sushi).

% Query with backtracking
?- likes(john, X).
X = pizza ;    % Press semicolon for next solution
X = pasta.
```

The semicolon (;) triggers backtracking to find alternative solutions.

### 7. Recursion

Recursion in Prolog allows rules to be defined in terms of themselves, essential for processing hierarchical structures like lists and trees.

```prolog
% Ancestor relationship - recursive definition
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% This means: X is an ancestor of Y if:
% - X is a direct parent of Y, OR
% - X is a parent of some Z, and Z is an ancestor of Y
```

Testing:
```prolog
?- ancestor(john, bob).    % true - direct parent
true.

?- ancestor(john, lisa).   % true - direct parent
true.

?- ancestor(john, ann).    % true if ann is grandchild of john
true.  % (if such a fact exists)
```

### 8. Lists in Prolog

Lists are a fundamental data structure in Prolog. A list is either empty `[]` or [Head|Tail] where Head is the first element and Tail is the remaining list.

```prolog
% List notation
[1, 2, 3, 4]          % Simple list
[head | tail]        % Destructuring pattern
[X | Y]              % X is head, Y is tail
```

Common list operations:
```prolog
% Membership
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).

% Append
append([], L, L).
append([H | T], L2, [H | R]) :- append(T, L2, R).

% Length
length([], 0).
length([_ | T], N) :- length(T, M), N is M + 1.
```

### 9. Built-in Predicates

Prolog provides many built-in predicates for common operations:

- `is/2` - Arithmetic evaluation: `N is 3 + 4.`
- `=/2` - Unification (structure matching)
- `==/2` - Identity (no unification)
- `=../2` - Univ (decompose/compound term)
- `call/1` - Call a goal
- `fail/0` - Always fails (forces backtracking)
- `true/0` - Always succeeds
- `repeat/0` - Infinite succeed (for loops)
- `write/1` - Output to console
- `nl/0` - New line
- `halt/0` - Terminate program

## Examples

### Example 1: Family Relationship Database

Consider building a complete family relationship system:

```prolog
% Facts
male(john).
male(bob).
male(alice).
female(mary).
female(lisa).

parent(john, bob).
parent(john, lisa).
parent(mary, bob).
parent(mary, lisa).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

grandparent(X, Y) :- 
    parent(X, Z), 
    parent(Z, Y).

% Query: Who are bob's siblings?
?- sibling(bob, X).
X = lisa.

% Query: Who is bob's mother?
?- mother(X, bob).
X = mary.

% Query: Is john bob's father?
?- father(john, bob).
true.
```

### Example 2: List Processing - Finding Maximum

```prolog
% Base case: max of single element is the element itself
max_list([X], X).

% Recursive case: compare head with max of tail
max_list([H | T], Max) :- 
    max_list(T, TailMax),
    H >= TailMax, 
    Max = H.
max_list([H | T], Max) :- 
    max_list(T, TailMax),
    H < TailMax, 
    Max = TailMax.

% Query
?- max_list([3, 7, 2, 9, 1], M).
M = 9.
```

### Example 3: Simple Arithmetic in Prolog

```prolog
% Factorial - recursive definition
factorial(0, 1).
factorial(N, F) :- 
    N > 0, 
    M is N - 1, 
    factorial(M, F1), 
    F is N * F1.

% Fibonacci - recursive definition
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :- 
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2.

% Queries
?- factorial(5, F).
F = 120.

?- fibonacci(10, F).
F = 55.
```

## Exam Tips

1. **Understand the difference between `=` and `==`**: The predicate `=` performs unification (tries to make terms equal), while `==` checks for identity without unification. In exams, be clear about when each should be used.

2. **Remember the order matters**: Prolog searches from top to bottom and left to right in rules. The order of clauses affects efficiency and sometimes correctness. Know how to order facts and rules for optimal performance.

3. **Master the list notation**: Understand `[H|T]` notation thoroughly—Head is the first element, Tail is everything else. This is crucial for list manipulation questions.

4. **Practice trace/0**: The trace predicate shows step-by-step execution. Understand how to use it to debug and understand backtracking.

5. **Know when backtracking occurs**: Backtracking happens automatically when Prolog needs alternative solutions. You can control it with cut (!) or fail predicates.

6. **Difference between facts and rules**: Facts are unconditionally true; rules have conditions. Be able to convert English statements to Prolog facts and rules.

7. **Understand anonymous variables**: The underscore `_` represents an anonymous variable—useful when you need a variable but don't care about its value.

8. **Cut (!) operator**: Understand how the cut works to prune the search tree. Green cuts (efficiency) vs red cuts (correctness) is important concept.

9. **Negation as failure**: Prolog's `\+` (not) represents negation as failure—something is true if it cannot be proven. This differs from logical negation.

10. **Writing recursive rules**: Ensure your recursive rules have a base case and a recursive case, otherwise you'll get infinite loops.