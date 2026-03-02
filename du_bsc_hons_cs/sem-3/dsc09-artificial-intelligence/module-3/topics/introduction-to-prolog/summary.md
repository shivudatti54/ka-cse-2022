# Introduction to Prolog - Summary

## Key Definitions and Concepts

- **Prolog**: A declarative logic programming language where programs specify what is true rather than how to compute it.
- **Fact**: An unconditional assertion in Prolog (e.g., `male(john).`)
- **Rule**: A conditional statement with head and body connected by `:-` (e.g., `mother(X, Y) :- female(X), parent(X, Y).`)
- **Query**: A question asked to the Prolog interpreter to retrieve information from the knowledge base.
- **Unification**: The process of making two terms identical by binding variables to appropriate values.
- **Backtracking**: Prolog's mechanism to explore alternative solutions when the current path fails.
- **Variable**: A term starting with uppercase letter or underscore that can be bound to values during unification.
- **Anonymous Variable**: The underscore `_` represents a variable whose value is not needed.

## Important Formulas and Theorems

- **List notation**: `[H|T]` where H is head (first element), T is tail (remaining list)
- **Empty list**: `[]` represents an empty list
- **Membership**: `member(X, [X|_]). member(X, [_|T]) :- member(X, T).`
- **Append**: `append([], L, L). append([H|T], L2, [H|R]) :- append(T, L2, R).`
- **Recursion pattern**: Base case + recursive case with decreasing complexity

## Key Points

1. Prolog is based on Horn clauses and automated theorem proving through resolution.
2. Facts represent unconditional truths; rules represent conditional relationships.
3. Variables begin with uppercase letters; constants (atoms) begin with lowercase letters.
4. Unification binds variables to values to make terms identical; it is the core matching mechanism.
5. Backtracking allows Prolog to find all possible solutions to a query.
6. Lists in Prolog are built recursively as [Head|Tail].
7. The order of clauses and goals significantly affects Prolog program behavior.
8. Recursion requires a base case to terminate and a recursive case to make progress.
9. The cut (!) operator prunes the search tree to improve efficiency.
10. Prolog's `\+` represents negation as failure—proving something is false by failing to prove it true.

## Common Mistakes to Avoid

1. **Using lowercase for variables**: Variables must start with uppercase; using lowercase creates atoms instead of variables.
2. **Forgetting the base case in recursion**: Always include a terminating condition; otherwise infinite loops occur.
3. **Not using semicolons correctly**: Remember that `,` means AND (conjunction), `;` means OR (disjunction).
4. **Confusing `=` with `==`**: `=` performs unification (creates bindings), `==` checks identity without binding.
5. **Incorrect list destructuring**: Ensure proper [Head|Tail] pattern matching; Tail must always be a list.

## Revision Tips

1. Practice writing simple family relationship programs to solidify facts, rules, and queries.
2. Trace through examples using pencil and paper—write down variable bindings at each step.
3. Memorize the standard list manipulation predicates (member, append, length).
4. Understand the difference between structural recursion and arithmetic recursion.
5. Review the order of goal execution in rules—left-to-right matters.
6. Practice converting English statements to Prolog facts and rules.
7. Use the trace predicate to visualize backtracking and understand execution flow.