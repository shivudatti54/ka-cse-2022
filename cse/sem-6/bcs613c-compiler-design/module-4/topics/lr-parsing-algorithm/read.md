# LR Parsing Algorithm

## Introduction to LR Parsing

**LR parsing** is a powerful bottom-up parsing technique used in compiler design. The "L" stands for scanning the input from **Left to right**, and the "R" stands for producing a **Rightmost derivation** in reverse. LR parsers are widely used in practice because they can handle a larger class of grammars than top-down parsers like LL parsers.

**Key Properties of LR Parsers:**

- They scan input left to right
- They produce a rightmost derivation in reverse
- They use a stack and parsing table for decisions
- They can detect syntax errors as soon as possible (at the earliest point where no valid continuation exists)

## Components of an LR Parser

An LR parser consists of three main components:

### 1. Input Buffer

Contains the string to be parsed, followed by the end-of-input marker `$`.

### 2. Stack

Stores a sequence of states and grammar symbols. The stack contents are of the form: `s0 X1 s1 X2 s2 ... Xm sm`, where `si` are states and `Xi` are grammar symbols.

### 3. Parsing Table

The parsing table has two parts:

- **ACTION table**: `ACTION[s, a]` specifies the action to take when the parser is in state `s` and the current input symbol is `a`. Actions can be:
- **Shift s**: Push the current input symbol and state `s` onto the stack
- **Reduce A -> beta**: Pop `|beta|` symbols and states from the stack, then push `A` and `GOTO[s', A]`
- **Accept**: Parsing is successful
- **Error**: Syntax error detected

- **GOTO table**: `GOTO[s, A]` specifies the state to transition to when non-terminal `A` is pushed onto the stack after a reduction, and the current top state is `s`.

## The LR Parsing Algorithm

```
Input: An input string w and an LR parsing table
Output: If w is in L(G), a bottom-up parse; otherwise, an error

Initialize: Push state s0 onto the stack
Set ip (input pointer) to the first symbol of w$

repeat:
 Let s be the state on top of the stack
 Let a be the symbol pointed to by ip

 if ACTION[s, a] = shift s' then
 Push a and then s' onto the stack
 Advance ip to the next input symbol

 else if ACTION[s, a] = reduce A -> beta then
 Pop 2 * |beta| symbols from the stack
 Let s' be the state now on top of the stack
 Push A and then GOTO[s', A] onto the stack
 Output the production A -> beta

 else if ACTION[s, a] = accept then
 return success (parsing complete)

 else
 call error-recovery routine
```

## LR(0) Items

An **LR(0) item** (or simply "item") of a grammar G is a production of G with a dot (.) at some position of the right-hand side. The dot indicates how much of the production has been seen so far.

**Example:** For the production `A -> X Y Z`, the LR(0) items are:

- `A -> .X Y Z` (nothing has been matched yet)
- `A -> X.Y Z` (X has been matched)
- `A -> X Y.Z` (X and Y have been matched)
- `A -> X Y Z.` (the entire right side has been matched, ready to reduce)

For the production `A -> epsilon`, the only item is:

- `A -> .`

### Closure of Item Sets

The **CLOSURE** operation computes the complete set of items for a given state:

```
CLOSURE(I):
 repeat
 for each item [A -> alpha . B beta] in I
 for each production B -> gamma in G
 add [B -> .gamma] to I
 until no more items can be added to I
 return I
```

### GOTO Function

The **GOTO** function computes transitions between states:

```
GOTO(I, X):
 Let J be the set of items [A -> alpha X . beta]
 such that [A -> alpha . X beta] is in I
 return CLOSURE(J)
```

## Shift-Reduce Parsing

LR parsing is a form of **shift-reduce parsing**, which uses two main operations:

### Shift

- Move the next input symbol onto the top of the stack
- The parser "shifts" the input symbol and a new state onto the stack

### Reduce

- Replace the top symbols on the stack (matching the right side of a production) with the left side of the production
- The parser "reduces" a handle to a non-terminal

### Example: Parsing `id * id + id`

Using the grammar:

```
E -> E + T
E -> T
T -> T * F
T -> F
F -> (E)
F -> id
```

| Stack           | Input           | Action             |
| --------------- | --------------- | ------------------ |
| 0               | id \* id + id $ | Shift              |
| 0 id 5          | \* id + id $    | Reduce F -> id     |
| 0 F 3           | \* id + id $    | Reduce T -> F      |
| 0 T 2           | \* id + id $    | Shift              |
| 0 T 2 \* 7      | id + id $       | Shift              |
| 0 T 2 \* 7 id 5 | + id $          | Reduce F -> id     |
| 0 T 2 \* 7 F 10 | + id $          | Reduce T -> T \* F |
| 0 T 2           | + id $          | Reduce E -> T      |
| 0 E 1           | + id $          | Shift              |
| 0 E 1 + 6       | id $            | Shift              |
| 0 E 1 + 6 id 5  | $               | Reduce F -> id     |
| 0 E 1 + 6 F 3   | $               | Reduce T -> F      |
| 0 E 1 + 6 T 9   | $               | Reduce E -> E + T  |
| 0 E 1           | $               | Accept             |

## Parser Actions and Conflicts

### Shift-Reduce Conflict

Occurs when the parser cannot decide whether to shift the next input symbol or reduce the current handle on the stack. This happens when a state contains both a shift item and a complete (reduce) item for the same lookahead.

### Reduce-Reduce Conflict

Occurs when the parser cannot decide which of two (or more) possible reductions to apply. This happens when a state contains complete items for two different productions for the same lookahead.

## Types of LR Parsers

| Type    | Lookahead | Table Size | Power                     |
| ------- | --------- | ---------- | ------------------------- |
| LR(0)   | 0 symbols | Smallest   | Weakest, many conflicts   |
| SLR(1)  | 1 symbol  | Small      | More powerful than LR(0)  |
| LALR(1) | 1 symbol  | Small      | More powerful than SLR(1) |
| CLR(1)  | 1 symbol  | Largest    | Most powerful             |

- **SLR (Simple LR)**: Uses FOLLOW sets to resolve some conflicts
- **LALR (Look-Ahead LR)**: Merges states with same core items; basis of most parser generators like YACC
- **CLR (Canonical LR)**: Most powerful but largest tables; uses explicit lookahead in items

## Summary

- LR parsing is a bottom-up technique that scans left-to-right and produces rightmost derivation in reverse
- The parser uses a stack, input buffer, and a two-part parsing table (ACTION and GOTO)
- Four possible actions: Shift, Reduce, Accept, Error
- LR(0) items track parsing progress with a dot marker in productions
- CLOSURE and GOTO functions are used to construct the parsing automaton
- Shift-reduce and reduce-reduce conflicts indicate grammar ambiguity or parser limitation
- LR parsers are more powerful than LL parsers and can handle a wider class of grammars
