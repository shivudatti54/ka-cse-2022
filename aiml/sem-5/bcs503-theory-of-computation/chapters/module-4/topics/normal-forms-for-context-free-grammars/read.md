# Context-Free Grammars (CFGs)

## 1. Introduction to Context-Free Grammars

In the previous chapter on Lexical Analysis, we used **Regular Expressions** to define the structure of tokens (keywords, identifiers, operators, etc.). However, regular expressions are insufficient to describe the nested, recursive structures inherent in programming languages, such as balanced parentheses, nested if-else statements, or the hierarchical structure of arithmetic expressions.

A **Context-Free Grammar (CFG)** is a formal grammar that is powerful enough to describe the syntax of most programming languages. It provides a set of recursive rules to define the structure of a language, making it the fundamental tool for **Syntax Analysis** (or **Parsing**).

### 1.1. Why "Context-Free"?

The term "context-free" means that the production rules can be applied regardless of the context (the symbols surrounding the non-terminal). If a non-terminal `A` appears on the left-hand side of a rule `A -> α`, you can always replace `A` with `α`, no matter where `A` appears in a derivation.

## 2. Formal Definition of a CFG

A Context-Free Grammar `G` is a 4-tuple, `(V, T, P, S)` where:

1.  **`V`** is a finite set of **Non-terminal Symbols** (or variables). These represent syntactic categories, e.g., `〈expression〉`, `〈statement〉`.
2.  **`T`** is a finite set of **Terminal Symbols** (tokens). These are the basic symbols from which strings are formed, e.g., `id`, `+`, `if`.
3.  **`P`** is a finite set of **Production Rules** (or productions). Each production is of the form:
    `A -> β`
    where:
    - `A` is a non-terminal (`A ∈ V`).
    - `β` is a string of symbols from `(V ∪ T)*` (a string of terminals and/or non-terminals).
4.  **`S`** is a special non-terminal called the **Start Symbol** (`S ∈ V`). It represents the main syntactic category of the language, e.g., `〈program〉`.

## 3. Components of a CFG

### 3.1. Terminals and Non-Terminals

| Feature            | Terminal Symbols                          | Non-Terminal Symbols                   |
| :----------------- | :---------------------------------------- | :------------------------------------- |
| **Representation** | Tokens from the lexer (leaf nodes)        | Syntactic variables (non-leaf nodes)   |
| **Purpose**        | Basic alphabet of the language            | Represent phrases and structures       |
| **Example**        | `id`, `+`, `number`, `(`                  | `expr`, `stmt`, `term`, `factor`       |
| **Convention**     | Lowercase letters, operators, punctuation | Enclosed in `< >` or uppercase letters |

### 3.2. Production Rules

Productions define how non-terminals can be rewritten. For example:

- `<expr> -> <expr> + <term>`
- `<if_stmt> -> if ( <expr> ) <stmt> else <stmt>`

### 3.3. Start Symbol

The start symbol is the root from which all derivations begin. Every valid program in the language must be derivable from this symbol.

## 4. Derivations

A derivation is a sequence of rewriting steps that transforms the start symbol into a string of terminals. We use the `=>` symbol to denote a derivation step.

### 4.1. Example Grammar

Let's define a simple grammar `G` for arithmetic expressions:

```
V = {E, T, F}
T = {id, +, *, (, )}
S = E
P:
E -> E + T | T
T -> T * F | F
F -> ( E ) | id
```

_(Note: `\|` denotes an alternative production rule)_

### 4.2. Leftmost Derivation

In a leftmost derivation, the leftmost non-terminal is always replaced first. This is the standard derivation for top-down parsers.

**Deriving `id + id * id`:**

1.  E => E + T
2.  => T + T (using E -> T)
3.  => F + T (using T -> F)
4.  => id + T (using F -> id)
5.  => id + T _ F (using T -> T _ F)
6.  => id + F \* F (using T -> F)
7.  => id + id \* F (using F -> id)
8.  => id + id \* id (using F -> id)

### 4.3. Rightmost Derivation

In a rightmost derivation, the rightmost non-terminal is always replaced first. This is the standard derivation for bottom-up parsers (e.g., LR parsers).

**Deriving `id + id * id`:**

1.  E => E + T
2.  => E + T \* F
3.  => E + T \* id
4.  => E + F \* id
5.  => E + id \* id
6.  => T + id \* id
7.  => F + id \* id
8.  => id + id \* id

The **parse tree** graphically represents the derivation, showing the hierarchical structure without being concerned with the order of replacements.

## 5. Parse Trees

A parse tree is a graphical representation of a derivation.

- **Root Node:** Labeled with the start symbol.
- **Internal Nodes:** Labeled with non-terminals.
- **Leaf Nodes:** Labeled with terminals.
- **Children of a Node:** The symbols on the right-hand side of a production used to rewrite that node.

**Parse Tree for `id + id * id` (using our grammar G):**

```
                E
               /|\
              / | \
             E  +  T
             |    /|\
             T   T * F
             |   |   |
             F   F   id
             |   |
             id  id
```

This tree shows that the expression is an `E` (`E + T`), where the first `E` is just a `T` which is an `F` which is an `id`. The `T` on the right is `T * F`, which is `F * id`, which is `id * id`. This correctly captures the operator precedence: `*` binds tighter than `+`.

## 6. Ambiguity in Grammars

A grammar is **ambiguous** if it can generate more than one parse tree for the same input string. Ambiguity is a critical problem for parsers because a compiler must uniquely determine the meaning (and thus the structure) of a program.

### 6.1. Example of an Ambiguous Grammar

Consider this simpler, but ambiguous, grammar for expressions:

```
E -> E + E | E * E | ( E ) | id
```

For the string `id + id * id`, this grammar can produce two different parse trees, leading to two different interpretations of the expression's meaning.

**Tree 1: `(id + id) * id`**

```
        E
       /|\
      E * E
     /|\   \
    E + E   id
    |   |
    id  id
```

**Tree 2: `id + (id * id)`**

```
        E
       /|\
      E + E
     /   /|\
    id  E * E
        |   |
        id  id
```

Since `*` typically has higher precedence than `+`, we want our grammar to **force** the second interpretation. The first grammar in Section 4.1 is **unambiguous** and enforces the correct precedence.

### 6.2. Resolving Ambiguity

Ambiguity is not a property of the language but of the grammar. We can often resolve ambiguity by:

1.  **Refactoring the Grammar:** Introducing new non-terminals to enforce precedence and associativity, as seen in the first grammar (`E`, `T`, `F`).
2.  **Using Parser Directives:** Specifying precedence and associativity rules for tokens (as done in tools like YACC or Bison), which allows the use of a more natural but ambiguous grammar.

## 7. Role of CFG in Syntax Analysis

The parser (syntax analyzer) uses the CFG to guide its analysis.

- **Top-Down Parsers (LL):** Attempt to construct a parse tree from the root (start symbol) down to the leaves. They follow a leftmost derivation.
- **Bottom-Up Parsers (LR):** Attempt to construct a parse tree from the leaves (input tokens) up to the root. They follow a reverse of a rightmost derivation.

The grammar's structure directly determines which parsing technique can be used and the complexity of the parser.

## 8. Writing a Good Grammar

When designing a CFG for a programming language, consider:

1.  **Clarity:** The grammar should be easy to read and understand.
2.  **Unambiguity:** It should be unambiguous, or ambiguity must be resolvable by the parser.
3.  **Precedence and Associativity:** The grammar should correctly encode operator precedence (`*` > `+`) and associativity (most operators are left-associative: `a+b+c` is `(a+b)+c`).
4.  **Suitability for Parsing:** The grammar should be compatible with the chosen parsing algorithm (e.g., not left-recursive for top-down parsers).

---

**Exam Tips:**

1.  **Memorize the 4-tuple definition:** `(V, T, P, S)`. You will almost certainly be asked to define a CFG.
2.  **Practice Derivations:** Be comfortable performing both leftmost and rightmost derivations for a given string and grammar. Clearly number your steps.
3.  **Draw Parse Trees:** For a given string, be able to draw its parse tree. This is a common question.
4.  **Identify Ambiguity:** If asked, demonstrate ambiguity by showing two different parse trees for the same string. The "dangling else" problem is a classic example.
5.  **Refactor Grammars:** Be prepared to take an ambiguous grammar (e.g., for expressions) and rewrite it to be unambiguous, enforcing standard precedence and associativity rules.
