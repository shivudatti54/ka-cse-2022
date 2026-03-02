# Construction of SLR Parsing Tables

## Introduction to SLR Parsing

SLR (Simple LR) parsing is a fundamental bottom-up parsing technique in compiler design. It represents the simplest method in the family of LR parsers, providing a systematic approach to syntax analysis. SLR parsers use parsing tables to determine the sequence of shift and reduce operations needed to parse an input string according to a given context-free grammar.

The key advantage of SLR parsing over simpler methods like recursive descent or LL parsing is its ability to handle a broader class of grammars, including those that are left-recursive, which are common in programming languages.

## Core Concepts

### LR(0) Items

An LR(0) item is a production from the grammar with a dot (•) positioned somewhere in the right-hand side. The dot indicates how much of the production has been seen so far during parsing.

**Example**: For production A → XYZ, we have four possible items:

- A → •XYZ
- A → X•YZ
- A → XY•Z
- A → XYZ•

The items represent different states of recognition for the production.

### Viable Prefixes

A viable prefix is a prefix of a right-sentential form that can appear on the stack of an LR parser. It never extends beyond the right end of the handle (the substring that will be reduced next).

### Closure Operation

The closure operation for a set of items I is defined as:

1. Add every item in I to CLOSURE(I)
2. If A → α•Bβ is in CLOSURE(I) and B → γ is a production, then add B → •γ to CLOSURE(I)

This operation ensures that all possible items that could be recognized next are included.

### Goto Operation

The Goto operation, GOTO(I, X), where I is a set of items and X is a grammar symbol, is defined as the closure of the set of all items [A → αX•β] such that [A → α•Xβ] is in I.

This operation represents the transition from one state to another when symbol X is seen.

## Constructing the Canonical LR(0) Collection

The canonical collection of LR(0) items provides the states for the SLR parsing table. The construction process:

1. Start with the augmented grammar: Add S' → S to the original grammar
2. Compute the initial state: I₀ = CLOSURE({[S' → •S]})
3. For each state I and each grammar symbol X, compute GOTO(I, X)
4. Continue until no new states can be generated

**Example Grammar**:

```
E → E + T | T
T → T * F | F
F → (E) | id
```

Augmented grammar:

```
0. S' → E
1. E → E + T
2. E → T
3. T → T * F
4. T → F
5. F → (E)
6. F → id
```

Initial state I₀:

```
CLOSURE({[S' → •E]}) = {
  [S' → •E],
  [E → •E + T],
  [E → •T],
  [T → •T * F],
  [T → •F],
  [F → •(E)],
  [F → •id]
}
```

## Building the SLR Parsing Table

The SLR parsing table has two parts:

1. ACTION table: Determines shift/reduce operations
2. GOTO table: Determines state transitions after reductions

### Steps for Table Construction

1. **Construct the canonical collection of LR(0) items** C = {I₀, I₁, ..., Iₙ}
2. **Determine the parsing actions** for each state Iᵢ:
   - If [A → α•aβ] is in Iᵢ and GOTO(Iᵢ, a) = Iⱼ, then set ACTION[i, a] = "shift j"
   - If [A → α•] is in Iᵢ, then set ACTION[i, a] = "reduce A → α" for all a in FOLLOW(A)
   - If [S' → S•] is in Iᵢ, then set ACTION[i, $] = "accept"
3. **Set GOTO table** for non-terminals: If GOTO(Iᵢ, A) = Iⱼ, then set GOTO[i, A] = j
4. **Mark all undefined entries** as "error"

### FOLLOW Set Calculation

The FOLLOW set for a non-terminal A contains all terminals that can appear immediately to the right of A in some sentential form.

**Rules for FOLLOW**:

1. $ is in FOLLOW(S') for the start symbol
2. If A → αBβ, then all terminals in FIRST(β) (except ε) are in FOLLOW(B)
3. If A → αB or A → αBβ where FIRST(β) contains ε, then FOLLOW(A) ⊆ FOLLOW(B)

**Example FOLLOW sets** for our grammar:

- FOLLOW(E) = {$, +, )}
- FOLLOW(T) = {$, +, \*, )}
- FOLLOW(F) = {$, +, \*, )}

## Example: SLR Table Construction

Let's construct the SLR table for our expression grammar:

**State I₀**:

```
[S' → •E]
[E → •E + T]
[E → •T]
[T → •T * F]
[T → •F]
[F → •(E)]
[F → •id]
```

From I₀:

- GOTO(I₀, E) = I₁: {[S' → E•], [E → E•+T]}
- GOTO(I₀, T) = I₂: {[E → T•], [T → T•*F]}
- GOTO(I₀, F) = I₃: {[T → F•]}
- GOTO(I₀, () = I₄: {[F → (•E)], [E → •E+T], [E → •T], [T → •T*F], [T → •F], [F → •(E)], [F → •id]}
- GOTO(I₀, id) = I₅: {[F → id•]}

**State I₁**:

```
[S' → E•]
[E → E•+T]
```

- GOTO(I₁, +) = I₆: {[E → E+•T], [T → •T*F], [T → •F], [F → •(E)], [F → •id]}

**State I₂**:

```
[E → T•]
[T → T•*F]
```

- Reduce on FOLLOW(E) = {$, +, )} for production E → T
- GOTO(I₂, _) = I₇: {[T → T_•F], [F → •(E)], [F → •id]}

**State I₃**:

```
[T → F•]
```

- Reduce on FOLLOW(T) = {$, +, \*, )} for production T → F

**State I₄**:

```
[F → (•E)]
[E → •E+T]
[E → •T]
[T → •T*F]
[T → •F]
[F → •(E)]
[F → •id]
```

- GOTO(I₄, E) = I₈: {[F → (E•)], [E → E•+T]}
- GOTO(I₄, T) = I₂
- GOTO(I₄, F) = I₃
- GOTO(I₄, () = I₄
- GOTO(I₄, id) = I₅

**State I₅**:

```
[F → id•]
```

- Reduce on FOLLOW(F) = {$, +, \*, )} for production F → id

**State I₆**:

```
[E → E+•T]
[T → •T*F]
[T → •F]
[F → •(E)]
[F → •id]
```

- GOTO(I₆, T) = I₉: {[E → E+T•], [T → T•*F]}
- GOTO(I₆, F) = I₃
- GOTO(I₆, () = I₄
- GOTO(I₆, id) = I₅

**State I₇**:

```
[T → T*•F]
[F → •(E)]
[F → •id]
```

- GOTO(I₇, F) = I₁₀: {[T → T*F•]}
- GOTO(I₇, () = I₄
- GOTO(I₇, id) = I₅

**State I₈**:

```
[F → (E•)]
[E → E•+T]
```

- GOTO(I₈, )) = I₁₁: {[F → (E)•]}
- GOTO(I₈, +) = I₆

**State I₉**:

```
[E → E+T•]
[T → T•*F]
```

- Reduce on FOLLOW(E) = {$, +, )} for production E → E+T
- GOTO(I₉, \*) = I₇

**State I₁₀**:

```
[T → T*F•]
```

- Reduce on FOLLOW(T) = {$, +, *, )} for production T → T*F

**State I₁₁**:

```
[F → (E)•]
```

- Reduce on FOLLOW(F) = {$, +, \*, )} for production F → (E)

**SLR Parsing Table**:

| State | ACTION |     |     |     |     | GOTO |     |     |
| ----- | ------ | --- | --- | --- | --- | ---- | --- | --- | --- |
|       | id     | +   | \*  | (   | )   | $    | E   | T   | F   |
| 0     | s5     |     |     | s4  |     |      | 1   | 2   | 3   |
| 1     |        | s6  |     |     |     | acc  |     |     |     |
| 2     |        | r2  | s7  |     | r2  | r2   |     |     |     |
| 3     |        | r4  | r4  |     | r4  | r4   |     |     |     |
| 4     | s5     |     |     | s4  |     |      | 8   | 2   | 3   |
| 5     |        | r6  | r6  |     | r6  | r6   |     |     |     |
| 6     | s5     |     |     | s4  |     |      |     | 9   | 3   |
| 7     | s5     |     |     | s4  |     |      |     |     | 10  |
| 8     |        | s6  |     |     | s11 |      |     |     |     |
| 9     |        | r1  | s7  |     | r1  | r1   |     |     |     |
| 10    |        | r3  | r3  |     | r3  | r3   |     |     |     |
| 11    |        | r5  | r5  |     | r5  | r5   |     |     |     |

## Handling Conflicts

SLR parsing may encounter two types of conflicts:

1. **Shift-Reduce Conflict**: When a state has both a shift and a reduce action for the same input symbol.
2. **Reduce-Reduce Conflict**: When a state has multiple reduce actions for the same input symbol.

SLR attempts to resolve these conflicts using FOLLOW sets, but this approach is not always sufficient, leading to the development of more powerful methods like LALR and canonical LR parsing.

## Comparison with Other LR Methods

| Method       | Power  | Table Size | Construction Complexity |
| ------------ | ------ | ---------- | ----------------------- |
| SLR          | Low    | Small      | Simple                  |
| LALR         | Medium | Small      | Moderate                |
| Canonical LR | High   | Large      | Complex                 |

## Exam Tips

1. **Memorize the steps**: Remember the sequence: augment grammar → construct collection → compute FOLLOW → build table.
2. **Practice with examples**: Work through multiple grammar examples to build intuition.
3. **Understand FOLLOW sets**: These are critical for reduce actions in SLR parsing.
4. **Watch for conflicts**: Be able to identify and explain shift-reduce and reduce-reduce conflicts.
5. **Compare methods**: Understand the differences between SLR, LALR, and canonical LR parsing.
6. **Draw state diagrams**: Visualizing the state transitions can help understand the parsing process.
7. **Check your work**: Always verify that your parsing table can correctly parse simple input strings.
