# Simple LR (SLR) Parsing

## 1. Introduction to Bottom-Up Parsing and LR Parsing

Bottom-up parsing is a fundamental technique in compiler design where the parser constructs a parse tree for an input string by beginning at the leaves (the terminals) and working its way up towards the root (the start symbol). The most general and powerful class of bottom-up parsers are the **LR parsers**. The "L" stands for scanning the input from left to right, and the "R" stands for constructing a rightmost derivation in reverse.

LR parsers are table-driven, meaning their operation is guided by two large tables: an **ACTION** table and a **GOTO** table. The parser uses a stack to hold states and grammar symbols. The ACTION table tells the parser whether to **shift** a new terminal onto the stack or **reduce** a handle on the stack to a non-terminal. The GOTO table is used after a reduction to decide which state to push onto the stack.

There are several types of LR parsers, differing in the size of their parsing tables and the class of grammars they can handle:

- **LR(0):** The simplest but least powerful. It uses no lookahead.
- **SLR(1):** Simple LR. A more powerful method that uses a simple form of lookahead (Follow sets).
- **CLR(1) or LR(1):** Canonical LR. The most powerful but has very large tables.
- **LALR(1):** Look-Ahead LR. A practical compromise between SLR and CLR, with power close to CLR but table sizes close to SLR.

**SLR(1)** parsing is a popular choice because it is more powerful than LR(0) and much easier to implement than full LR(1), making it a great introduction to the concepts of LR parsing.

## 2. Core Concepts: Items, Closure, and Goto

### LR(0) Items

An **LR(0) item** (or simply an _item_) is a production of the grammar with a dot (•) at some position in the right-hand side (RHS). The dot indicates how much of the production has been seen (parsed) so far.

For a production `A -> XYZ`, the possible items are:

- `A -> •XYZ` (Nothing of the RHS has been seen)
- `A -> X•YZ` (X has been seen and matched)
- `A -> XY•Z` (X and Y have been seen and matched)
- `A -> XYZ•` (The entire RHS has been seen and is ready for reduction)

An item of the form `A -> α•` is called a **complete item** (or a _reduce item_). Items where the dot is followed by a non-terminal (`A -> α•Bβ`) are crucial for predicting what might come next.

### The Closure Operation

The **closure** of a set of items _I_ is formed by applying two rules until no new items can be added:

1. Add every item in _I_ to _closure(I)_.
2. If _closure(I)_ contains an item of the form `[A -> α•Bβ]`, and the grammar has a production `B -> γ`, then add the item `[B -> •γ]` to _closure(I)_.

This operation essentially "pushes" the lookahead requirement one step forward. If we expect to see a `B` next, we must also be prepared to see the beginning of any production that derives a `B`.

**Example:**
Grammar:

1. `S -> CC`
2. `C -> cC`
3. `C -> d`

Let I = { `[S -> •CC]` }
closure(I) is calculated as:

- Initial item: `[S -> •CC]`
- Dot is before non-terminal `C`, so we add all productions of `C`: `[C -> •cC]` and `[C -> •d]`.
- Dot in `[C -> •cC]` is before terminal `c`, so we stop. No new non-terminals to expand.
- Dot in `[C -> •d]` is before terminal `d`, so we stop.
  ∴ closure(I) = { `[S -> •CC]`, `[C -> •cC]`, `[C -> •d]` }

### The Goto Operation

The **goto** operation is used to define the transitions between states in the LR automaton. Given a set of items _I_ and a grammar symbol _X_ (terminal or non-terminal), `goto(I, X)` is defined as the closure of the set of all items `[A -> αX•β]` such that `[A -> α•Xβ]` is in _I_.

In simpler terms, it represents the movement of the dot across the symbol _X_ in all items in _I_ where the dot is immediately before _X_.

**Example:**
Continuing from the previous `closure(I)`:
I = { `[S -> •CC]`, `[C -> •cC]`, `[C -> •d]` }
Let's compute `goto(I, C)`:

- Look for items where the dot is before `C`. We find `[S -> •CC]`.
- Move the dot past the `C`: `[S -> C•C]`.
- Now, take the closure of this new set { `[S -> C•C]` }. - Dot is before non-terminal `C`, so we add `[C -> •cC]` and `[C -> •d]`.
  ∴ goto(I, C) = closure( { `[S -> C•C]` } ) = { `[S -> C•C]`, `[C -> •cC]`, `[C -> •d]` }

## 3. Constructing the SLR Parsing Table

The SLR parsing table has two parts: the **ACTION** table and the **GOTO** table.

- The **ACTION** table is indexed by state _i_ and a terminal _a_ (or the end marker `$`). It can contain four values: `shift j`, `reduce A -> β`, `accept`, or `error`.
- The **GOTO** table is indexed by state _i_ and a non-terminal _A_. It indicates which state to go to after reducing to non-terminal _A_.

### The Canonical Collection of LR(0) Items

The first step is to create states for the parser. Each state is a set of LR(0) items. The collection of states, _C_, is built as follows:

1. Start with the initial state: `I₀ = closure( { [S' -> •S] } )`. (`S'` is a new start symbol added to the grammar).
2. For each state _I_ in _C_ and each grammar symbol _X_ (terminal or non-terminal), if `goto(I, X)` is not empty and not already in _C_, add it as a new state.
3. Repeat step 2 until no new states can be added.

### Filling the ACTION and GOTO Tables

For each state _I_i_ in the collection _C_:

1. **Shift Actions:** If `[A -> α•aβ]` is in _I_i_ and `goto(I_i, a) = I_j`, then set `ACTION[i, a] = shift j`. (Here, `a` is a terminal).
2. **Reduce Actions:** If `[A -> α•]` is in _I_i_ (a complete item), then set `ACTION[i, a] = reduce A -> α` **for every terminal `a` in `FOLLOW(A)`**. This is the crucial "Simple" lookahead that gives SLR its name.
3. **Accept Action:** If `[S' -> S•]` is in _I_i_, then set `ACTION[i, $] = accept`.
4. **Goto Table:** For all non-terminals _A_, if `goto(I_i, A) = I_j`, then set `GOTO[i, A] = j`.
5. Set any undefined entry in the ACTION table to `error`.

## 4. The SLR Parsing Algorithm

The SLR parser uses a stack that holds states and grammar symbols. The algorithm is as follows:

Let `s` be the current state (on top of the stack).
Let `a` be the current input token.

```
Initialize stack to state 0.
Repeat forever:
 s = top of stack
 if ACTION[s, a] = shift s':
 push a onto the stack
 push s' onto the stack
 advance input to next token
 a = new current token
 else if ACTION[s, a] = reduce A -> β (where |β| = r):
 pop 2*r symbols (r states and r grammar symbols)
 s' = top of stack after pop
 push A onto the stack
 push GOTO[s', A] onto the stack
 output the reduction "A -> β"
 else if ACTION[s, a] = accept:
 break (parsing is done successfully)
 else:
 call error recovery routine
```

**ASCII Diagram of Parser Operation:**

```
+------------------------+ +-----------------------+
| STACK | | INPUT |
|------------------------| |-----------------------|
| State | Symbol | | c c d d $ |
| 0 | | ^ |
+------------------------+ Pointer |
 || |
 \/ Shift 'c' |
+------------------------+ +-----------------------+
| State | Symbol | | INPUT |
|------------------------| |-----------------------|
| 2 | c | | c d d $ |
| 0 | | ^ ^ |
+------------------------+ New Pointer |
 || |
 \/ Reduce 'd' to C |
+------------------------+ +-----------------------+
| State | Symbol | | INPUT |
|------------------------| |-----------------------|
| 5 | C | | c c d d $ |
| 2 | c | ^ |
| 0 | | Pointer is here |
+------------------------+ |
```

## 5. A Complete SLR(1) Example

Let's build the SLR parsing table for a simple grammar.

**Grammar G:**

1. `E -> E + T`
2. `E -> T`
3. `T -> id`

**Augmented Grammar G':** 0. `S -> E`

1. `E -> E + T`
2. `E -> T`
3. `T -> id`

**First and Follow Sets:**

- `FIRST(E) = FIRST(T) = { id }`
- `FOLLOW(E) = { $, + }`
- `FOLLOW(T) = { $, + }`

**Canonical Collection of LR(0) Items:**

- **I0:** closure({[S -> •E]})
  = { [S -> •E], [E -> •E+T], [E -> •T], [T -> •id] }
- **I1:** goto(I0, E) = closure({[S -> E•], [E -> E•+T]}) = { [S -> E•], [E -> E•+T] }
- **I2:** goto(I0, T) = closure({[E -> T•]}) = { [E -> T•] }
- **I3:** goto(I0, id) = closure({[T -> id•]}) = { [T -> id•] }
- **I4:** goto(I1, +) = closure({[E -> E+•T]}) = { [E -> E+•T], [T -> •id] }
- **I5:** goto(I4, T) = closure({[E -> E+T•]}) = { [E -> E+T•] }
- `goto(I4, id)` leads back to I3.

**SLR Parsing Table:**
| State | ACTION | | GOTO |
| | id | + | $ | E | T |
|-------|--------|------|----------|-----|-----|
| 0 | s3 | | | 1 | 2 |
| 1 | | s4 | accept | | |
| 2 | | r2 | r2 | | |
| 3 | | r3 | r3 | | |
| 4 | s3 | | | | 5 |
| 5 | | r1 | r1 | | |

_Explanation of Table Entries:_

- **State 0:** On `id`, shift to state 3. Goto on E is state 1, on T is state 2.
- **State 1:** On `+`, shift to state 4. On `$`, accept.
- **State 2:** This state contains `[E -> T•]` (a reduce item). `FOLLOW(E) = {+, $}`, so we put `reduce E -> T` on `+` and `$`.
- **State 3:** Contains `[T -> id•]`. `FOLLOW(T) = {+, $}`, so we put `reduce T -> id` on `+` and `$`.
- **State 4:** On `id`, shift to state 3.
- **State 5:** Contains `[E -> E+T•]`. `FOLLOW(E) = {+, $}`, so we put `reduce E -> E+T` on `+` and `$`.

## 6. SLR vs. Other LR Parsing Methods

| Feature                     | LR(0)            | SLR(1)                       | LR(1) / LALR(1)                                              |
| --------------------------- | ---------------- | ---------------------------- | ------------------------------------------------------------ |
| **Lookahead**               | None             | Uses `FOLLOW` sets           | Uses state-specific lookahead                                |
| **Power**                   | Weakest          | More powerful than LR(0)     | Most powerful (LR(1))                                        |
| **Table Size**              | Smallest         | Same as LR(0)                | Much larger (LR(1)), similar to LR(0) (LALR(1))              |
| **Reduce-Reduce Conflicts** | Resolved blindly | Resolved using `FOLLOW` sets | Resolved precisely with lookahead                            |
| **Practical Use**           | Rarely used      | Commonly used for teaching   | LR(1): rarely; LALR(1): industry standard (e.g., YACC/Bison) |

## 7. Syntax Directed Definitions (SDD) with LR Parsing

A Syntax Directed Definition is a context-free grammar where attributes are associated with the grammar symbols, and semantic rules are associated with the productions. These rules define how to compute the values of attributes.

SDDs are classified based on when the semantic rules are evaluated:

- **S-attributed definitions:** All attributes are synthesized (computed from children to parent). These can be evaluated easily during bottom-up parsing by storing attribute values on the parser stack alongside state/symbol information. An SLR parser can naturally handle S-attributed SDDs.
- **L-attributed definitions:** A more general class that includes both synthesized and inherited attributes, with restrictions that allow evaluation in a single left-to-right pass. These are more suited to top-down parsing but can also be implemented in bottom-up parsers with careful design.

When an SLR parser performs a reduction using production `A -> XYZ`, it can simultaneously execute the semantic rule associated with that production, e.g., `A.syn = f(X.syn, Y.syn, Z.syn)`.

## Exam Tips and Common Pitfalls

1. **Always Augment the Grammar:** The first step is _always_ to add a new start production `S' -> S`. This ensures there is exactly one accept action.
2. **Closure is Key:** Most errors in building the canonical collection come from incorrect calculation of the `closure` operation. Remember to add items for _every_ production of a non-terminal that appears after a dot.
3. **SLR Reduce Lookahead:** The defining characteristic of SLR is using `FOLLOW(A)` for reduce actions. Don't put a reduce action for `A -> α` in state `i` on a terminal `a` unless `a` is truly in `FOLLOW(A)`.
4. **Conflict Identification:** If a state has a shift item `[A -> α•aβ]` and a reduce item `[B -> γ•]` and `a` is in `FOLLOW(B)`, you have an **shift/reduce conflict**. SLR's use of `FOLLOW` sets is often too weak to resolve this, necessitating a more powerful parser like LALR.
5. **Practice:** The best way to learn SLR parsing is to manually work through several examples from start to finish (grammar -> items -> table -> parse input).
