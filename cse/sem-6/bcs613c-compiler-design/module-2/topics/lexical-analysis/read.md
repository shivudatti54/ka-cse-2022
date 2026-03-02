# Lexical Analysis

Lexical analysis is the first phase of a compiler, also known as **scanning**. Its primary job is to read the stream of characters that make up the source program and group them into meaningful sequences called **lexemes**. For each lexeme, the lexical analyzer produces a **token** of the form `<token-name, attribute-value>` that it passes to the subsequent phase, syntax analysis (parsing).

## The Role of Lexical Analysis in Compilation

In the compilation pipeline, the lexical analyzer sits between the source program input and the syntax analyzer. It acts as the interface that shields the parser from the complexities of the raw character stream. The interaction typically works as follows:

1. The **parser** calls the lexical analyzer with a `getNextToken` command.
2. The **lexical analyzer** reads input characters until it can identify the next token.
3. It returns the token to the parser.

This demand-driven approach means the lexical analyzer produces one token at a time, as requested by the parser.

## Tokens, Patterns, and Lexemes

Understanding lexical analysis requires clarity on three fundamental concepts:

### Token

A token is a pair consisting of a **token name** and an optional **attribute value**. The token name is an abstract symbol representing a kind of lexical unit. Examples include keywords like `if`, `while`, `return`; operators like `+`, `*`, `<=`; identifiers; and literal constants.

### Pattern

A pattern is a description of the form that the lexemes of a token may take. For keywords, the pattern is simply the sequence of characters that form the keyword. For identifiers, the pattern is a more complex description, typically expressed using regular expressions, such as: a letter followed by zero or more letters or digits.

### Lexeme

A lexeme is the actual sequence of characters in the source program that matches the pattern for a token. For instance, in the statement:

```c
int result = x + 10;
```

The lexemes and their corresponding tokens are:

| Lexeme   | Token                                 |
| -------- | ------------------------------------- |
| `int`    | `<keyword, int>`                      |
| `result` | `<id, pointer to symbol table entry>` |
| `=`      | `<assign_op>`                         |
| `x`      | `<id, pointer to symbol table entry>` |
| `+`      | `<add_op>`                            |
| `10`     | `<number, 10>`                        |
| `;`      | `<semicolon>`                         |

## How Lexical Analysis Works

The lexical analyzer performs several tasks:

### 1. Reading the Input

The scanner reads the source program character by character. Since reading individual characters from disk is slow, **input buffering** techniques are employed. A common approach is the **two-buffer scheme**, where two halves of a buffer are alternately filled from the input, and two pointers (`lexemeBegin` and `forward`) track the current lexeme being processed.

### 2. Removing White Space and Comments

Before identifying tokens, the lexical analyzer strips out whitespace characters (spaces, tabs, newlines) and comments. These have no significance to the syntax of the program and are discarded.

### 3. Identifying Tokens

The core task is recognizing tokens. The scanner uses the patterns defined for each token to identify lexemes in the input. This is done using one of two primary techniques:

- **Hand-coded scanners**: Programmers write explicit code (often using switch-case statements or if-else chains) to recognize each token. This approach gives fine-grained control but is tedious and error-prone.
- **Automata-based scanners**: Regular expressions are used to specify token patterns, which are then converted to deterministic finite automata (DFA) for efficient recognition. Tools like **Lex** and **Flex** automate this process.

### 4. Tracking Line Numbers

The lexical analyzer keeps track of the current line number in the source file so that error messages from later phases can reference the correct source location.

### 5. Interacting with the Symbol Table

When the scanner encounters an identifier, it looks it up in the **symbol table**. If the identifier is new, an entry is created. The token for an identifier typically carries an attribute that is a pointer to the corresponding symbol table entry.

## Specification of Tokens Using Regular Expressions

Tokens are formally specified using **regular expressions**. The key operations are:

- **Union (|)**: `r | s` matches a string matched by either `r` or `s`.
- **Concatenation**: `rs` matches a string formed by concatenating a string matched by `r` with a string matched by `s`.
- **Kleene closure (\*)**: `r*` matches zero or more concatenations of strings matched by `r`.
- **Positive closure (+)**: `r+` matches one or more concatenations of strings matched by `r`.

### Examples of Token Definitions

```
digit -> [0-9]
digits -> digit+
letter -> [a-zA-Z_]
id -> letter (letter | digit)*
number -> digits (. digits)? (E [+-]? digits)?
```

## Finite Automata in Lexical Analysis

The recognition engine behind a lexical analyzer is a **finite automaton**. There are two types:

### Nondeterministic Finite Automata (NFA)

An NFA can have multiple transitions from a state on the same input symbol and can have transitions on the empty string (epsilon). NFAs are easy to construct from regular expressions using **Thompson's construction** but are less efficient to simulate directly.

### Deterministic Finite Automata (DFA)

A DFA has exactly one transition from each state on each input symbol and no epsilon transitions. DFAs are more efficient for simulation (each input character requires exactly one state transition) but can have many more states than the corresponding NFA.

The standard pipeline is:

1. Write **regular expressions** for each token.
2. Convert regular expressions to an **NFA** (Thompson's construction).
3. Convert NFA to a **DFA** (subset construction).
4. **Minimize the DFA** to reduce the number of states.

## Lexical Errors and Recovery

Lexical errors occur when the scanner encounters a character sequence that does not match any token pattern. Common strategies for error recovery include:

- **Panic mode recovery**: Delete successive characters from the remaining input until the scanner finds a well-formed token.
- **Deleting an extraneous character**.
- **Inserting a missing character**.
- **Replacing an incorrect character**.
- **Transposing two adjacent characters**.

The scanner typically generates an error message with the line number and the offending character(s).

## Lexical Analyzer Generators

Tools like **Lex** (or its modern variant **Flex**) automate the construction of lexical analyzers:

1. The programmer writes a **Lex specification file** containing regular expressions and associated actions.
2. Lex compiles this specification into a C program that implements a DFA-based scanner.
3. The generated scanner is compiled and linked with the rest of the compiler.

A typical Lex specification has three sections separated by `%%`:

```
{definitions}
%%
{rules}
%%
{user code}
```

Each rule consists of a regular expression pattern and an associated action (C code) to execute when the pattern is matched.

## Why Separate Lexical Analysis from Parsing?

There are several important reasons for separating lexical analysis from syntax analysis:

1. **Simplicity of design**: The separation allows each phase to focus on a specific task, making both the scanner and the parser simpler.
2. **Compiler efficiency**: Specialized buffering techniques for reading input characters can significantly speed up the compiler.
3. **Compiler portability**: Input-device-specific peculiarities can be restricted to the lexical analyzer, making the rest of the compiler platform-independent.
4. **Use of specialized tools**: Tools like Lex and Flex can automate scanner construction, while parser generators like Yacc handle the more complex grammar-based parsing.

## Key Takeaways

- Lexical analysis transforms a character stream into a token stream.
- Tokens are specified using regular expressions.
- Recognition is performed using finite automata (typically DFAs for efficiency).
- The lexical analyzer handles whitespace removal, comment stripping, and line tracking.
- Separating scanning from parsing leads to a cleaner, more efficient, and more portable compiler design.
- Tools like Lex/Flex automate the construction of efficient lexical analyzers.
