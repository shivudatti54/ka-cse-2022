# Recursive Descent Parsing

## Introduction to Top-Down Parsing

Recursive Descent Parsing (RDP) is a fundamental **top-down parsing** technique widely used in compiler design. It is called "top-down" because the parser begins with the start symbol of the grammar and attempts to recursively rewrite it into the sequence of tokens (the input string), building a parse tree from the root down to the leaves.

The "recursive descent" name comes from the fact that the parsing process is guided by the grammar's production rules and is implemented by a set of mutually recursive procedures, each corresponding to a non-terminal in the grammar. The parser conceptually "descends" through the levels of the grammar's structure.

## Key Concepts and How It Works

### The Basic Algorithm

At its core, a recursive descent parser is a collection of functions (or procedures). For each non-terminal `A` in the grammar, there is a function `parseA()`. The job of this function is to read a sequence of tokens from the input that can be derived from `A`.

The function examines the next input token (often called the "lookahead" token) and chooses which production rule for `A` to apply. It then executes the right-hand side of that production:

- For a terminal symbol: It checks if the current lookahead token matches that terminal. If it does, it consumes the token (reads the next one). If not, it reports a syntax error.
- For a non-terminal symbol: It makes a recursive call to the corresponding function for that non-terminal.

```ascii
Flow of a parseX() function:

+-----------------------+
|   Start parseX()      |
+-----------------------+
           |
           v
+-----------------------------------------+
| Look at the current token (lookahead)   |
| to decide which production for X to use  |
+-----------------------------------------+
           |
           v
+-----------------------+
| For each symbol in the  |
| chosen production:     |
|   - If terminal: match & consume |
|   - If non-terminal: call its parse function |
+-----------------------+
           |
           v
+-----------------------+
|   Return (success)     |
+-----------------------+
```

### Example Grammar and Parser

Consider a simple grammar for arithmetic expressions with addition and multiplication:

```
E  -> T E'
E' -> '+' T E' | ε
T  -> F T'
T' -> '*' F T' | ε
F  -> '(' E ')' | id
```

This grammar is **left-recursion-free** and is a prerequisite for basic recursive descent parsing. A recursive descent parser for this grammar would have functions: `parseE()`, `parseEPrime()`, `parseT()`, `parseTPrime()`, and `parseF()`.

**Snippet of pseudo-code for `parseE()` and `parseEPrime()`:**

```pseudo
function parseE() {
    parseT();   // E -> T E'
    parseEPrime();
}

function parseEPrime() {
    if (lookahead == '+') {
        match('+');    // Consume the '+' token
        parseT();      // E' -> '+' T E'
        parseEPrime();
    } else {
        // Do nothing, apply E' -> ε
    }
}
```

The `match(expectedToken)` function checks if the current lookahead is the `expectedToken`. If it is, it consumes it and advances the input; if not, it raises an error.

## Handling Choice: Using FIRST Sets

The parser decides which production to use based on the current lookahead token. The set of tokens that can begin a string derived from a non-terminal is called its **FIRST** set.

- For the production `E' -> '+' T E'`, `FIRST('+' T E') = { '+' }`.
- For the production `E' -> ε`, we must also consider the **FOLLOW** set of `E'` (the tokens that can legally appear after `E'`). If the lookahead is in `FOLLOW(E')`, we can apply the epsilon production.

A well-designed recursive descent parser encodes these decisions into `if-else` or `switch` statements.

```ascii
Decision making in parseEPrime():

                          +-----------------+
                          | Enter parseE'() |
                          +-----------------+
                                     |
                                     v
                    +--------------------------------+
                    | Is lookahead == '+' ?          |
                    +--------------------------------+
                     /                           \
                    / Yes                         \ No
                   v                               v
    +--------------------------+        +-------------------------+
    | match('+');               |        |                         |
    | parseT();                 |        | Check if lookahead is   |
    | parseEPrime();            |        | in FOLLOW(E')? If yes,  |
    | return;                   |        | apply ε. If no, error.  |
    +--------------------------+        +-------------------------+
```

## Limitations and Challenges

### 1. Left Recursion

A grammar is left-recursive if a non-terminal `A` derives a sentential form that starts with `A` itself (e.g., `A -> Aα | β`). A recursive descent parser for such a grammar would enter an infinite loop, as `parseA()` would immediately call `parseA()` again without consuming any input.

**Solution:** Left recursion must be eliminated from the grammar before implementing a recursive descent parser. This is typically done by transforming the grammar into an equivalent form that uses right recursion and iteration.

**Original (Left-Recursive):**
`A -> Aα | β`

**Transformed (Right-Recursive):**
`A -> βA'`
`A' -> αA' | ε`

### 2. Backtracking and Predictive Parsing

A naive recursive descent parser might involve backtracking: if a production choice leads to a dead end, the parser rewinds the input and tries another production. This is inefficient.

**Solution:** Most modern recursive descent parsers are **predictive parsers**. They use lookahead (often just one token, hence LL(1)) to uniquely determine which production to take, eliminating the need for backtracking. The grammar must be crafted to be LL(1), meaning the FIRST and FOLLOW sets of alternative productions for a non-terminal must be disjoint.

### 3. Grammar Factorisation

A common issue is when two productions for the same non-terminal start with the same symbols, making the choice ambiguous based on a single lookahead token.
Example: `S -> if E then S | if E then S else S`

**Solution:** The grammar must be refactored (or "factored") to pull the common prefix out. This often resolves the ambiguity and makes the grammar suitable for predictive parsing.

## Recursive Descent vs. Other Parsers

| Feature                    | Recursive Descent Parser                                 | LR Parser (e.g., SLR, LALR)                               |
| :------------------------- | :------------------------------------------------------- | :-------------------------------------------------------- |
| **Type**                   | Top-Down                                                 | Bottom-Up                                                 |
| **Construction**           | Manual (or generated from functions)                     | Automated (via parsing table construction)                |
| **Grammar Class**          | LL(1), often requires transformation                     | LR(1), handles more grammars (e.g., left-recursive)       |
| **Control**                | Explicit in code (procedural)                            | Driven by a state machine and stack                       |
| **Error Reporting**        | Often easier to customize and make meaningful            | Can be more complex                                       |
| **Efficiency**             | Highly efficient (predictive)                            | Highly efficient (table-driven)                           |
| **Ease of Implementation** | Relatively easy to implement by hand for small languages | Difficult to implement by hand, relies on generator tools |

## Advantages and Disadvantages

**Advantages:**

- **Conceptual Simplicity:** The code structure directly mirrors the grammar, making it intuitive.
- **Ease of Implementation:** It is straightforward to code by hand for simple grammars.
- **Excellent Error Reporting:** Since the parser is hand-coded, it can be designed to produce very clear and informative error messages tailored to the context.
- **No Parser Generator Needed:** You can write it in a general-purpose programming language without extra tools.

**Disadvantages:**

- **Grammar Restrictions:** Cannot directly handle left-recursive or ambiguous grammars. The grammar must often be massaged into an LL(1) form, which can be less natural.
- **Manual Labor:** For large grammars, writing all the functions by hand can be tedious and error-prone.
- **Limited Power:** The class of grammars parsable by predictive recursive descent (LL(1)) is smaller than those parsable by LR techniques.

## Exam Tips

1.  **Know the Transformation:** Be prepared to eliminate left recursion and factor a grammar to make it suitable for recursive descent parsing. This is a very common exam question.
2.  **FIRST and FOLLOW are Crucial:** You must understand how to compute FIRST and FOLLOW sets, as they are the basis for the decision logic (`if`/`switch` statements) in the parser functions.
3.  **Trace the Parser:** Be able to manually trace through a recursive descent parser's function calls for a given input string and grammar. Show the sequence of function calls and token consumption.
4.  **Contrast with LR:** Expect questions that ask you to compare and contrast recursive descent (top-down) with shift-reduce (bottom-up) parsing. Highlight the differences in approach, grammar compatibility, and implementation.
5.  **Code Snippets:** If asked to write code, focus on clarity. Clearly show the function structure, the check of the lookahead token, the call to `match()`, and the recursive calls to other parsing functions. Don't forget to handle epsilon productions by checking the FOLLOW set.
