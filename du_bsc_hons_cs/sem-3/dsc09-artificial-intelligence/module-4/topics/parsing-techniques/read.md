# Parsing Techniques

## Comprehensive Study Material for BSc (Hons) Computer Science

### Delhi University - NEP 2024 UGCF (Artificial Intelligence / Compiler Design)

---

## 1. Introduction to Parsing

**Parsing** (also known as **syntax analysis**) is a fundamental phase in compiler design that analyzes a stream of tokens (lexical units produced by the lexical analyzer) and determines whether the token sequence conforms to the grammatical rules of the source programming language. The parser builds a **parse tree** or **syntax tree** that represents the hierarchical structure of the program.

In the classical compiler architecture, parsing sits between lexical analysis (lexing) and semantic analysis:

```
Source Code → Lexical Analyzer (Lexer) → Parser → Semantic Analyzer → Intermediate Code Generator
```

The parser takes the token stream from the lexer and checks whether the program is syntactically correct according to the language's grammar. If errors are found, the parser must report them accurately and recover gracefully to continue checking the rest of the program.

### Real-World Relevance

Parsing techniques are essential not only in compilers but also in numerous real-world applications:

- **Programming Language Implementation**: Every compiler and interpreter relies on parsers to understand code structure
- **Web Development**: HTML, XML, and JSON parsers process structured documents
- **Database Systems**: SQL queries are parsed to generate execution plans
- **Natural Language Processing (NLP)**: Sentence parsing helps analyze linguistic structure
- **Configuration Files**: Parsers read and validate YAML, TOML, and INI files
- **API Development**: Request/response payloads are parsed in web services

Understanding parsing is crucial for AI students because it forms the foundation of **language processing**, which is central to many AI applications including semantic analysis, code generation, and natural language understanding.

---

## 2. Grammars and Languages

### Formal Grammar Definition

A **context-free grammar (CFG)** is a formal system used to describe the syntax of programming languages. A CFG consists of:

1. **Terminals (T)**: The basic symbols from which strings are formed (token types from the lexer)
2. **Non-terminals (N)**: Syntactic variables representing sets of strings
3. **Production Rules (P)**: Rules that define how non-terminals can be replaced with sequences of terminals and non-terminals
4. **Start Symbol (S)**: A distinguished non-terminal from which derivation begins

### Example Grammar

```
S → E
E → E + T | T
T → T * F | F
F → ( E ) | id
```

Here, `S`, `E`, `T`, `F` are non-terminals; `+`, `*`, `(`, `)`, `id` are terminals.

---

## 3. Classification of Parsing Techniques

Parsers are broadly classified into two categories based on the direction of derivation:

### 3.1 Top-Down Parsing

**Top-down parsing** starts from the root (start symbol) and attempts to derive the input string by successively applying production rules. The parser builds the parse tree from the root down to the leaves (input tokens).

**Advantages:**
- Easier to understand and implement
- Direct construction of parse tree
- Good error messages and recovery

**Disadvantages:**
- Cannot handle left-recursive grammars directly
- May require grammar transformation

#### 3.1.1 Recursive Descent Parsing

**Recursive descent parsing** is a top-down parsing technique where each non-terminal is implemented as a recursive function. The parser attempts to match the input by recursively calling functions corresponding to non-terminals.

**Key Characteristics:**
- No backtracking (in its simple form)
- Easy to implement and debug
- Suitable for small languages
- Requires grammar to be left-factored and non-left-recursive

**Example: Recursive Descent Parser for Simple Arithmetic**

```python
# Recursive Descent Parser for Grammar:
# E → T { (+|-) T }
# T → F { (*|/) F }
# F → ( E ) | number

class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def match(self, token_type):
        if self.current_token() == token_type:
            self.pos += 1
            return True
        return False
    
    # E → T { (+|-) T }
    def parse_E(self):
        self.parse_T()
        while self.current_token() in ['+', '-']:
            self.pos += 1
            self.parse_T()
    
    # T → F { (*|/) F }
    def parse_T(self):
        self.parse_F()
        while self.current_token() in ['*', '/']:
            self.pos += 1
            self.parse_F()
    
    # F → ( E ) | number
    def parse_F(self):
        if self.current_token() == '(':
            self.match('(')
            self.parse_E()
            self.match(')')
        elif self.current_token() == 'number':
            self.match('number')
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token()}")
    
    def parse(self):
        self.parse_E()
        if self.current_token() is not None:
            raise SyntaxError("Unexpected tokens after parsing")

# Usage Example
tokens = ['number', '*', '(', 'number', '+', 'number', ')']
parser = RecursiveDescentParser(tokens)
parser.parse()
print("Parsing successful!")
```

#### 3.1.2 LL(k) Parsing

**LL(k) parsing** is a top-down parsing technique where:
- **L**: Left-to-right scanning of input
- **L**: Leftmost derivation
- **k**: Number of lookahead tokens used for decision making

**LL(1) Parsing** (k=1) is the most common variant, using a single lookahead token to make parsing decisions.

**LL(1) Parsing Table Construction:**

1. **First() and Follow() Sets**: Essential for populating the parsing table
2. **Parsing Table**: Maps (non-terminal, terminal) pairs to production rules

**First() Set Computation:**
- First(α) = {a | α ⇒* aβ, a ∈ Terminal}
- If α ⇒* ε, then ε ∈ First(α)

**Follow() Set Computation:**
- Follow(A) = {a | S ⇒* αAaβ, a ∈ Terminal}
- If S ⇒* αA, then $ (end-of-input) ∈ Follow(A)

**LL(1) Grammar Conditions:**
- No ambiguity
- No left recursion (must be eliminated)
- Grammar must be left-factored

**Example: LL(1) Parsing Table Construction**

Consider the grammar:
```
S → aAS | b
A → a | ε
```

**First Sets:**
- First(S) = {a, b}
- First(A) = {a, ε}
- First(aAS) = {a}
- First(b) = {b}

**Follow Sets:**
- Follow(S) = {$}
- Follow(A) = {a, $} (since S → aAS, a follows A; S → aAS | b, $ follows S)

**LL(1) Parsing Table:**

| Non-Terminal | a | b | $ |
|--------------|---|---|---|
| S | S → aAS | S → b | |
| A | A → a | | A → ε |

---

### 3.2 Bottom-Up Parsing

**Bottom-up parsing** starts from the input tokens (leaves) and attempts to reduce them to the start symbol (root). The parser builds the parse tree from the bottom up by identifying handle reductions.

**Advantages:**
- More powerful than top-down parsing
- Can handle more grammars (including left-recursive grammars)
- Preferred for programming language parsers

**Disadvantages:**
- More complex to implement
- Harder to understand and debug
- Slightly more overhead

#### 3.2.1 LR Parsing

**LR(k) parsing** is a bottom-up parsing technique where:
- **L**: Left-to-right scanning of input
- **R**: Rightmost derivation in reverse
- **k**: Number of lookahead tokens

**LR Parsing Variants:**

1. **LR(0)**: No lookahead (limited power, rarely used)
2. **SLR(1)**: Simple LR, uses Follow sets (simple but limited)
3. **LALR(1)**: Look-Ahead LR, merges states (most practical)
4. **Canonical LR(1)**: Full LR, most powerful (large tables)

**LR Parsing Algorithm:**

```
Initialize: Stack = [0], input = w$
Repeat:
    Let s = state on top of stack
    Let a = current input symbol
    If Action[s, a] = shift t:
        push a, then t onto stack
        advance input
    Else if Action[s, a] = reduce A → β:
        pop 2|β| symbols from stack
        Let s' = new state on top
        push A, then Goto[s', A] onto stack
    Else if Action[s, a] = accept:
        Accept
    Else:
        Error
```

**Example: LR(0) Parser Construction**

Grammar:
```
S → E
E → E + id | id
```

After eliminating left recursion:
```
E → E + id | id
```

**LR(0) Items:**
- I₀: S' → ·E, E → ·E + id, E → ·id
- I₁: S' → E·
- I₂: E → E + ·id
- I₃: E → id·
- I₄: E → E + id·

**LR Parsing Table (Simplified):**

| State | Action | Goto |
|-------|--------|------|
| | id | + | $ | E |
| 0 | s3 | | | 1 |
| 1 | | s2 | accept | |
| 3 | r2 | r2 | r2 | |
| 4 | r1 | r1 | r1 | |

*s = shift, r = reduce*

---

## 4. Handling Ambiguity

### What is Ambiguity?

A grammar is **ambiguous** if it produces more than one parse tree for the same input string. Ambiguity is problematic because it leads to multiple interpretations of the same code.

**Example of Ambiguous Grammar:**

```
E → E + E | E * E | ( E ) | id
```

The expression `id + id * id` can be parsed in two ways:
1. (id + id) * id (left-associative)
2. id + (id * id) (right-associative with multiplication having higher precedence)

### Techniques to Handle Ambiguity

1. **Grammar Transformation**: Rewrite the grammar to enforce precedence and associativity
2. **Disambiguation Rules**: Specify rules (e.g., * binds tighter than +)
3. **Using Parser Generators**: Tools like Yacc allow disambiguation through precedence declarations

**Unambiguous Grammar:**

```
E → E + T | T
T → T * F | F
F → ( E ) | id
```

This grammar enforces:
- * has higher precedence than +
- Both + and * are left-associative

---

## 5. Abstract Syntax Trees (ASTs)

### What is an AST?

An **Abstract Syntax Tree (AST)** is a tree representation of the abstract syntactic structure of source code. Unlike parse trees (concrete syntax trees), ASTs abstract away unnecessary details like punctuation and grouping symbols.

### Differences: Parse Tree vs AST

| Parse Tree (CST) | Abstract Syntax Tree (AST) |
|------------------|---------------------------|
| Contains all tokens | Contains only meaningful nodes |
| Represents concrete syntax | Represents abstract structure |
| Usually binary or n-ary | Usually irregular structure |
| Includes terminals | No terminals (only non-terminals concepts) |

### AST Construction Example

**For the expression: `a + b * c`**

```
Parse Tree:
       E
      /|\
     E + T
     |  /|\
     T * F
    / \  |
   F   F
  |    |
  a    b    c

AST:
       +
      / \
     a   *
        / \
       b   c
```

### Implementation in Python

```python
class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.type = node_type
        self.value = value
        self.children = children or []
    
    def __str__(self, level=0):
        ret = "  " * level + f"{self.type}"
        if self.value:
            ret += f": {self.value}"
        ret += "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

class ASTBuilder:
    def build(self, tokens):
        # Simplified AST builder for expression: E → T { (+|-) T }
        # This builds an AST with proper operator precedence
        pass

# Example AST for 'a + b * c'
ast = ASTNode('+',
    children=[
        ASTNode('id', value='a'),
        ASTNode('*',
            children=[
                ASTNode('id', value='b'),
                ASTNode('id', value='c')
            ]
        )
    ]
)

print(ast)
```

**Output:**
```
+:
  id: a
  *:
    id: b
    id: c
```

---

## 6. Parser Generators

**Parser generators** are software tools that automatically generate parsers from formal grammar specifications. They significantly reduce the effort required to implement parsers for programming languages.

### Popular Parser Generators

| Tool | Language | Type | Description |
|------|----------|------|-------------|
| **Yacc/Bison** | C | LALR(1) | Classic Unix parser generator |
| **ANTLR** | Java/C++/Python | LL(*) | Modern, multi-language support |
| **Lex/Flex** | C | Lexer | Lexical analyzer generator |
| **PLY** | Python | LALR | Python implementation of Yacc |
| **JavaCC** | Java | LL(k) | Java Compiler Compiler |

### Using ANTLR (Example)

**Grammar File (Expr.g4):**

```antlr
grammar Expr;

prog: stat+ ;

stat: expr NEWLINE          # printExpr
    | NEWLINE               # blank
    ;

expr: expr op=('*'|'/') expr  # MulDiv
    | expr op=('+'|'-') expr  # AddSub
    | INT                     # int
    | '(' expr ')'            # parens
    ;

MULDIV: '*' | '/' ;
ADD_SUB: '+' | '-' ;
INT: [0-9]+ ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;
```

**Generating Parser (Python):**

```bash
# Install ANTLR
pip install antlr4-python3-runtime

# Generate parser
antlr4 -Dlanguage=Python3 Expr.g4
```

**Using Generated Parser:**

```python
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(f"Result: {value}")
        return value
    
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        return left - right
    
    def visitInt(self, ctx):
        return int(ctx.INT().getText())

# Usage
input_stream = InputStream("3 + 4 * 2")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.prog()

visitor = EvalVisitor()
visitor.visit(tree)
```

---

## 7. Error Handling and Recovery

Parsers must handle errors gracefully. Common strategies include:

1. **Panic Mode**: Skip tokens until a synchronization point (e.g., semicolon)
2. **Phrase Level Recovery**: Replace or skip individual tokens
3. **Error Productions**: Include common errors in grammar
4. **Global Correction**: Find minimal changes to make input valid

---

## 8. Key Takeaways

1. **Parsing** is the phase that checks whether token sequences conform to the language grammar and builds a parse tree/AST.

2. **Top-down parsing** (recursive descent, LL(k)) starts from the start symbol and derives the input; it's easier to implement but limited to certain grammars.

3. **Bottom-up parsing** (LR parsing) reduces input to the start symbol; more powerful and handles more grammars but more complex.

4. **LL(1) parsers** use one lookahead token and require non-left-recursive, left-factored grammars.

5. **LR parsers** are the preferred choice for programming languages due to their power and ability to handle left recursion.

6. **Ambiguous grammars** must be resolved through transformation or disambiguation rules to ensure unique parsing.

7. **ASTs** provide an abstract, simplified tree representation that focuses on semantic structure rather than concrete syntax.

8. **Parser generators** (Yacc, ANTLR, PLY) automate parser creation from grammar specifications.

9. **Error handling** is crucial for user-friendly compilers; various recovery strategies exist with different trade-offs.

---

## 9. Assessment Questions

### Multiple Choice Questions

**1. Which component of a compiler performs parsing?**
- (a) Lexical Analyzer
- (b) Syntax Analyzer (Parser)
- (c) Semantic Analyzer
- (d) Code Optimizer

**2. What does the first 'L' stand for in LL(1) parsing?**
- (a) Leftmost derivation
- (b) Left-to-right scanning
- (c) Left recursion
- (d) Left factoring

**3. Which parsing technique builds parse tree from top to bottom?**
- (a) Bottom-up parsing
- (b) Top-down parsing
- (c) Shift-reduce parsing
- (d) LR parsing

**4. A grammar with left recursion can be parsed by:**
- (a) LL(1) parser directly
- (b) Recursive descent without modification
- (c) LR parser without modification
- (d) None of the above

**5. What is the main advantage of LR parsing over LL parsing?**
- (a) Simpler implementation
- (b) Can handle left-recursive grammars
- (c) Better error messages
- (d) Faster execution

**6. Which data structure is typically used to implement recursive descent parsing?**
- (a) Stack
- (b) Queue
- (c) Recursive function calls
- (d) Array

**7. In LR parsing, what does the 'R' stand for?**
- (a) Rightmost derivation
- (b) Reverse rightmost derivation
- (c) Reduce parsing
- (d) Recursive parsing

**8. What is an Abstract Syntax Tree (AST)?**
- (a) A parse tree with all tokens
- (b) An abstract representation of syntax without unnecessary details
- (c) A binary tree only
- (d) A linear representation of code

**9. Which parser generator is based on LALR(1) parsing?**
- (a) ANTLR
- (b) Yacc/Bison
- (c) JavaCC
- (d) All of the above

**10. A grammar is called ambiguous if:**
- (a) It has more than one valid parse tree for some string
- (b) It cannot be parsed by any parser
- (c) It contains left recursion
- (d) It has no start symbol

**11. What is the purpose of the Follow set in LL(1) parsing?**
- (a) To compute First sets
- (b) To determine what can appear after a non-terminal
- (c) To handle epsilon productions
- (d) To build the parse tree

**12. Which technique is used to eliminate left recursion?**
- (a) Left factoring
- (b) Substitution
- (c) Transformation to right recursion
- (d) Adding new non-terminals

**13. In bottom-up parsing, the fundamental operation is:**
- (a) Shift
- (b) Reduce
- (c) Both Shift and Reduce
- (d) Accept

**14. What type of grammar can be parsed by an LL(1) parser?**
- (a) Ambiguous grammar
- (b) Left-recursive grammar
- (c) Deterministic context-free grammar
- (d) Any context-free grammar

**15. The output of a parser is typically used by:**
- (a) Lexical analyzer
- (b) Semantic analyzer
- (c) Code generator
- (d) Both (b) and (c)

### Fill in the Blanks

**16.** The process of analyzing a stream of tokens to determine its grammatical structure is called ____________.

**17.** A parser that uses a single lookahead token is called ____________ parser.

**18.** The tree representation that abstracts away punctuation is called ____________.

**19.** Yacc stands for ____________.

**20.** LR parsing uses a ____________ to make parsing decisions.

### Answer Key

1. (b) 2. (b) 3. (b) 4. (c) 5. (b) 6. (c) 7. (b) 8. (b) 9. (b) 10. (a) 11. (b) 12. (c) 13. (c) 14. (c) 15. (d)

16. Parsing / Syntax Analysis
17. LL(1)
18. Abstract Syntax Tree (AST)
19. Yet Another Compiler Compiler
20. Parsing Table / State Machine

---

## References for Further Study

1. Aho, Lam, Sethi, Ullman - "Compilers: Principles, Techniques, and Tools" (The Dragon Book)
2. Delhi University BSc (Hons) Computer Science Syllabus - NEP 2024
3. ANTLR Documentation: antlr.org
4. Python PLY Documentation: dabeaz.com/ply/

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University following the NEP 2024 UGCF curriculum.*