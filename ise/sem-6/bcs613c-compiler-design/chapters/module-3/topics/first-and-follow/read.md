# First and Follow Sets in Parsing Techniques

## Introduction to First and Follow Sets

In compiler design, parsing is the process of analyzing a string of symbols to determine its grammatical structure with respect to a given formal grammar. Top-down parsing, specifically LL(1) parsing, requires two fundamental sets for each non-terminal symbol in a grammar: the **FIRST** set and the **FOLLOW** set. These sets are crucial for constructing predictive parsing tables and ensuring the grammar is suitable for efficient deterministic parsing.

The FIRST set helps determine which production rule to apply when expanding a non-terminal, while the FOLLOW set helps handle situations where a non-terminal can derive the empty string (ε). Together, they form the mathematical foundation for making parsing decisions without backtracking.

## The FIRST Set

### Definition

For any string of grammar symbols α, **FIRST(α)** is the set of terminals that begin the strings derived from α. If α can derive the empty string ε, then ε is also included in FIRST(α).

### Rules for Computing FIRST(X)

1. **If X is a terminal:** FIRST(X) = {X}
2. **If X is a non-terminal:** For each production X → Y₁Y₂...Yₖ
   - Add FIRST(Y₁) to FIRST(X)
   - If Y₁ can derive ε, add FIRST(Y₂) to FIRST(X)
   - If Y₁ and Y₂ can both derive ε, add FIRST(Y₃) to FIRST(X), and so on
   - If all Y₁ through Yₖ can derive ε, add ε to FIRST(X)
3. **If X → ε:** Add ε to FIRST(X)

### Algorithm for Computing FIRST Sets

```
for each non-terminal X:
    FIRST(X) = ∅

while sets are still changing:
    for each production X → Y₁Y₂...Yₖ:
        add all non-ε elements of FIRST(Y₁) to FIRST(X)
        if Y₁ can derive ε:
            add all non-ε elements of FIRST(Y₂) to FIRST(X)
            if Y₂ can derive ε:
                add all non-ε elements of FIRST(Y₃) to FIRST(X)
                ...
        if all Y₁ through Yₖ can derive ε:
            add ε to FIRST(X)
```

### Example 1: Simple Grammar

Consider the grammar:

```
E → T E'
E' → + T E' | ε
T → F T'
T' → * F T' | ε
F → ( E ) | id
```

Computing FIRST sets:

- FIRST(F) = {'(', 'id'}
- FIRST(T') = {'\*', ε}
- FIRST(T) = FIRST(F) = {'(', 'id'}
- FIRST(E') = {'+', ε}
- FIRST(E) = FIRST(T) = {'(', 'id'}

### Example 2: Grammar with ε-production

Consider:

```
S → A B C
A → a A | ε
B → b B | ε
C → c
```

Computing FIRST sets:

- FIRST(C) = {'c'}
- FIRST(B) = {'b', ε}
- FIRST(A) = {'a', ε}
- FIRST(S):
  - From S → A B C:
    - FIRST(A) = {'a', ε}
    - Since A can derive ε, add FIRST(B) = {'b', ε}
    - Since B can derive ε, add FIRST(C) = {'c'}
  - Therefore, FIRST(S) = {'a', 'b', 'c'}

## The FOLLOW Set

### Definition

For a non-terminal A, **FOLLOW(A)** is the set of terminals that can appear immediately to the right of A in some sentential form. That is, the set of terminals that can follow A in a derivation from the start symbol.

### Rules for Computing FOLLOW(A)

1. **Place $ in FOLLOW(S)** where S is the start symbol and $ is the end-of-input marker
2. **If there is a production B → αAβ:**
   - Add FIRST(β) (excluding ε) to FOLLOW(A)
   - If β can derive ε, add FOLLOW(B) to FOLLOW(A)
3. **If there is a production B → αA:** Add FOLLOW(B) to FOLLOW(A)

### Algorithm for Computing FOLLOW Sets

```
FOLLOW(S) = {$}  // S is start symbol
for each non-terminal X ≠ S:
    FOLLOW(X) = ∅

while sets are still changing:
    for each production A → αBβ:
        add FIRST(β) - {ε} to FOLLOW(B)
        if β can derive ε:
            add FOLLOW(A) to FOLLOW(B)
    for each production A → αB:
        add FOLLOW(A) to FOLLOW(B)
```

### Example: Computing FOLLOW Sets

Using the same expression grammar:

```
E → T E'
E' → + T E' | ε
T → F T'
T' → * F T' | ε
F → ( E ) | id
```

Computing FOLLOW sets:

1. FOLLOW(E) = {$} (from rule 1)
2. From F → ( E ): FOLLOW(E) += {')'} (from E in middle of production)
3. From E → T E': FOLLOW(E') = FOLLOW(E) = {$, ')'}
4. From E → T E': FOLLOW(T) = FIRST(E') - {ε} = {'+'}
   - Also, since E' → ε, FOLLOW(T) += FOLLOW(E) = {$, ')', '+'}
5. From T → F T': FOLLOW(T') = FOLLOW(T) = {$, ')', '+'}
6. From T → F T': FOLLOW(F) = FIRST(T') - {ε} = {'\*'}
   - Also, since T' → ε, FOLLOW(F) += FOLLOW(T) = {$, ')', '+', '\*'}

Final FOLLOW sets:

- FOLLOW(E) = {$, ')'}
- FOLLOW(E') = {$, ')'}
- FOLLOW(T) = {+, $, ')'}
- FOLLOW(T') = {+, $, ')'}
- FOLLOW(F) = {\*, +, $, ')'}

## Applications in LL(1) Parsing

### Constructing LL(1) Parsing Table

The FIRST and FOLLOW sets are used to build the predictive parsing table:

For each production A → α:

1. For each terminal a in FIRST(α), add A → α to M[A, a]
2. If ε is in FIRST(α), for each terminal b in FOLLOW(A), add A → α to M[A, b]

### LL(1) Grammar Conditions

A grammar is LL(1) if:

1. For any two distinct productions A → α and A → β:
   - FIRST(α) ∩ FIRST(β) = ∅
   - If ε is in FIRST(β), then FIRST(α) ∩ FOLLOW(A) = ∅

### Example: LL(1) Table Construction

Using our expression grammar:

| Non-Terminal | id    | +       | \*       | (     | )    | $    |
| ------------ | ----- | ------- | -------- | ----- | ---- | ---- |
| E            | E→TE' |         |          | E→TE' |      |      |
| E'           |       | E'→+TE' |          |       | E'→ε | E'→ε |
| T            | T→FT' |         |          | T→FT' |      |      |
| T'           |       | T'→ε    | T'→\*FT' |       | T'→ε | T'→ε |
| F            | F→id  |         |          | F→(E) |      |      |

## Comparison of FIRST and FOLLOW Sets

| Aspect             | FIRST Set                                          | FOLLOW Set                                                 |
| ------------------ | -------------------------------------------------- | ---------------------------------------------------------- |
| **Definition**     | Terminals that begin strings derived from a symbol | Terminals that can appear immediately after a non-terminal |
| **Contains ε?**    | Yes, if the symbol can derive ε                    | No, never contains ε                                       |
| **For terminals**  | The terminal itself                                | Not defined for terminals                                  |
| **Initialization** | Empty sets                                         | FOLLOW(S) = {$}                                            |
| **Primary use**    | Determine which production to apply                | Handle ε-productions correctly                             |

## Common Challenges and Solutions

### Left Recursion

Left-recursive grammars cause infinite loops in FIRST set computation. Must eliminate left recursion first:

```
Original: A → Aα | β
Transformed: A → βA'
           A' → αA' | ε
```

### Ambiguity

If FIRST(α) ∩ FIRST(β) ≠ ∅ for A → α and A → β, the grammar is ambiguous for LL(1) parsing. Requires grammar refactoring.

### Implementation Tips

1. Use iterative fixed-point algorithm until no changes occur
2. Maintain a boolean matrix for ε-derivation capability
3. Use stack or worklist algorithm for efficient computation

## Exam Tips

1. **Always start with ε-detection:** Before computing FIRST sets, determine which non-terminals can derive ε
2. **Follow the rules systematically:** Don't skip steps when computing FOLLOW sets
3. **Check for left recursion:** This will make your FIRST sets computation problematic
4. **Verify LL(1) conditions:** For exam questions, explicitly check if the grammar is LL(1)
5. **Practice with different grammars:** The more varied examples you practice, the better you'll understand edge cases
6. **Remember the special cases:**
   - FOLLOW never contains ε
   - The start symbol always has $ in its FOLLOW set
   - When a non-terminal appears at the end of a production, it inherits the FOLLOW of the left-hand side
