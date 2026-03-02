# Recognition of Tokens

## Introduction to Token Recognition

Token recognition is a fundamental process in the lexical analysis phase of compilation. The **lexical analyzer** (or lexer) scans the source code character by character, grouping these characters into meaningful sequences called **tokens**. Each token is a syntactic category that represents a basic building block of the programming language, such as keywords, identifiers, operators, and constants.

The process of recognizing tokens involves:

1. **Reading** the input stream of characters
2. **Identifying** patterns that form valid tokens
3. **Classifying** these patterns into token types
4. **Producing** output (token streams) for the syntax analyzer

## The Role of the Lexical Analyzer

The lexical analyzer serves as the first front-end phase of a compiler. Its primary responsibilities include:

- **Removing Whitespace and Comments:** Strips out characters that are irrelevant to syntactic analysis, such as spaces, tabs, newlines, and comments.
- **Tokenization:** Breaks the preprocessed input string into a sequence of tokens.
- **Symbol Table Management:** Enters identifiers (variable names, function names, etc.) into the symbol table upon first encounter.
- **Error Reporting:** Detects and reports lexical errors, such as the presence of invalid characters or malformed tokens.

### Interaction with the Parser

The lexer and parser work in a tightly coupled producer-consumer relationship. The parser, which performs syntax analysis, requests tokens from the lexer as needed. This is often implemented via a `getNextToken()` function.

```
 Source Code
 |
 v
+---------------------+
| Lexical Analyzer | getNextToken() +----------------+
| (Scanner/Lexer) |----------------->| Syntax Analyzer|
| | | (Parser) |
+---------------------+ +----------------+
 | |
 v v
 Sequence of Tokens Parse Tree / AST
```

## Specification of Tokens

Before recognition can occur, tokens must be formally specified. This is done using **regular expressions**, which provide a concise and precise notation for defining patterns of strings.

### Common Token Patterns

| Token Type          | Regular Expression Pattern Example         | Sample Matches               |
| :------------------ | :----------------------------------------- | :--------------------------- |
| Keyword             | `if` \| `else` \| `while` \| `for`         | `if`, `while`                |
| Identifier          | `[a-zA-Z_][a-zA-Z0-9_]*`                   | `count`, `index`, `temp_var` |
| Integer Literal     | `[0-9]+`                                   | `0`, `42`, `1000`            |
| Float Literal       | `[0-9]+\.[0-9]+`                           | `3.14`, `0.5`                |
| Relational Operator | `==` \| `!=` \| `<` \| `<=` \| `>` \| `>=` | `==`, `<=`                   |
| Assignment          | `=`                                        | `=`                          |

These regular expressions form the **lexical specification** of the language.

## The Process of Token Recognition

The core algorithm for recognizing tokens is based on **finite automata**. A finite automaton can be either a **Deterministic Finite Automaton (DFA)** or a **Nondeterministic Finite Automaton (NFA)**. Lexical analyzers typically use DFAs for efficiency, as they can process input in linear time.

### Steps in the Recognition Process

1. **Pattern Specification:** Define all tokens using regular expressions.
2. **Conversion to NFA:** Convert each regular expression into an equivalent NFA (e.g., using Thompson's Construction).
3. **Conversion to DFA:** Convert the collection of NFAs into a single, more efficient DFA (e.g., using Subset Construction).
4. **Minimization:** Minimize the DFA to reduce its state count, optimizing the recognizer.
5. **Simulation:** Implement the transition table of the final DFA in code to simulate the automaton and recognize tokens.

### Example: Recognizing Identifiers and Keywords

Consider the input `if (count < 10)`. The lexer must distinguish the keyword `if` from an identifier.

1. The lexer starts in an initial state.
2. It reads character `'i'`. This could be the start of keyword `if` or an identifier.
3. It reads next character `'f'`. The sequence "if" matches a keyword pattern.
4. It reads the next character `' '` (a space). Since no keyword pattern continues after "if", the lexer recognizes "if" as a keyword token. It then returns this token to the parser and resets to the initial state for the next token.
5. It continues, recognizing `'('`, then the identifier `'count'`, the operator `'<'`, the integer `'10'`, and finally `')'`.

## Transition Diagrams

A transition diagram is a graphical representation of a finite automaton. It is a directed graph where nodes represent states and edges represent transitions on input characters.

### Diagram for an Identifier Token

```
 [a-zA-Z_] [a-zA-Z0-9_]*
Start --------> State 1 ---------------> State 2 (Final)
 | ^
 | |
 +-----------------------+
 [a-zA-Z0-9_]
```

- **Start:** Initial state.
- **State 1:** The automaton moves here after reading the first valid identifier character (a letter or underscore).
- **State 2 (Final):** This is an accepting state. The automaton moves here and remains here for every subsequent valid identifier character (letter, digit, or underscore). Once a non-matching character (e.g., `+`, ` `, `;`) is encountered, the lexer retracts the input pointer, recognizes the lexeme, and emits the token.

### Diagram for an Integer Literal Token

```
 [0-9] [0-9]*
Start --------> State 3 -----------> State 4 (Final)
 | ^
 | |
 +-------------------+
 [0-9]
```

## Implementation: Buffering and Techniques

Reading input character-by-character from secondary storage is inefficient. To optimize, lexical analyzers use **input buffering**.

### Double Buffer Scheme

A common approach is to use two buffers (each typically the size of a disk block, e.g., 4096 bytes). The lexer loads data into these buffers alternately.

```
+-------------------------+-------------------------+
| Buffer 1 | Buffer 2 |
+-------------------------+-------------------------+
^ ^ ^
| | |
lexemeBegin forward Buffer End
Pointer Pointer
```

- `lexemeBegin`: Points to the start of the current lexeme being scanned.
- `forward`: Scans ahead until a pattern is matched.
- When `forward` reaches the end of one buffer, it loads the next block into the other buffer and continues scanning seamlessly. This handles lexemes that span disk blocks.

### Lookahead and Retraction

Sometimes, the automaton cannot determine the end of a token until it reads one character too far. For example, seeing `>` could be the end of a greater-than operator, but seeing `>=` forms a different operator. The `forward` pointer scans ahead, and if no rule matches, it may need to **retract** (back up) to the end of the previous valid token. Sentinels (a special character like `EOF` at the end of each buffer) simplify the check for buffer ends.

## Lexical Errors

Although lexical error recovery is simpler than syntactic or semantic error recovery, it is still important. Common lexical errors include:

- **Illegal characters:** e.g., `@`, `$` in a language that doesn't support them.
- **Unterminated comments or strings.**
- **Malformed constants:** e.g., `123.45.67`

### Error Recovery Strategies

- **Panic Mode Recovery:** The most common strategy. The lexer skips characters until a well-defined _synchronizing token_ (like a semicolon, space, or keyword) is found, then continues processing.
- **Delete one character:** Sometimes, deleting the offending character allows processing to continue.
- **Insert a missing character:** A hypothesized repair, less common in lexers.

## The `lex` Tool

The `lex` (or `flex`) tool is a **lexical analyzer generator**. Developers specify tokens using regular expressions and associate them with corresponding C/C++ code fragments (actions). `lex` then generates the actual C code for a state machine that implements the lexer.

**Basic structure of a `lex` input file:**

```
%{
/* C declarations and #includes */
%}
/* Definitions: e.g., DIGIT [0-9] */
%%
/* Rules: Regex { Action } */
{DIGIT}+ { printf("Integer: %s\n", yytext); }
"if" { return(IF); }
%%
/* Auxiliary C functions */
```

## Exam Tips

1. **Understand the Conversion Pipeline:** Be able to explain the steps from regular expression -> NFA -> DFA -> minimized DFA. Practice these conversions.
2. **Draw Transition Diagrams:** For common tokens like identifiers, integers, and simple operators, practice drawing precise transition diagrams, clearly marking start and final states.
3. **Trace the Algorithm:** Given a sample input string (e.g., `"sum=42+val;"`), trace the steps the lexer would take, showing the value of pointers `lexemeBegin` and `forward` and the tokens produced.
4. **Know the Role:** Be prepared to contrast the roles of the lexical analyzer and the syntax analyzer. The lexer deals with regular grammar; the parser deals with context-free grammar.
5. **Focus on Buffering:** Understand why buffering is necessary and how the two-buffer scheme works with pointers. This is a common exam question.
6. **Error Handling:** Remember the simple strategies for lexical error recovery, with "panic mode" being the most critical.
