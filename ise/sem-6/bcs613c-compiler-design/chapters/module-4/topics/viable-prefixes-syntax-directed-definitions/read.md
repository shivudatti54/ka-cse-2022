# Syntax Directed Definitions

## Introduction to Syntax Directed Definitions

Syntax Directed Definitions (SDDs) are a powerful mechanism used in compiler design to specify the translation of programming language constructs. They provide a formal way to associate semantic rules with context-free grammar productions, enabling the computation of attributes during parsing.

SDDs form the foundation for syntax-directed translation, where the translation process is guided by the syntax of the source language. This approach allows compiler writers to specify translations declaratively rather than imperatively, making compiler implementation more systematic and maintainable.

## Basic Concepts

### Attributes and Semantic Rules

In SDDs, we work with two main components:

1. **Attributes**: Values associated with grammar symbols (terminals and non-terminals)
2. **Semantic Rules**: Rules that define how to compute attribute values

There are two types of attributes:

- **Synthesized Attributes**: Computed from children nodes to parent nodes (bottom-up)
- **Inherited Attributes**: Computed from parent and/or siblings nodes (top-down)

```
Example Parse Tree with Attributes:

        E (val=19)
       /|\
      / | \
 (val=3) T (val=19)
     E' /|\
       / | \
 (val=5) F (val=5)
      T' /|\
       / | \
 (val=5) digit (lexval=5)
```

### SDD Notation

An SDD is specified by associating semantic rules with each grammar production. The general form is:

```
Production: X → Y₁ Y₂ ... Yₙ
Semantic Rules: X.a = f(Y₁.b, Y₂.c, ..., Yₙ.d)
```

Where `a`, `b`, `c`, `d` are attributes of the corresponding symbols.

## Types of Syntax Directed Definitions

### S-Attributed Definitions

S-attributed definitions use only synthesized attributes. These are particularly well-suited for bottom-up parsing as they can be evaluated during reduction operations.

**Example: Simple Expression Evaluator**

Grammar:

```
E → E + T     { E.val = E₁.val + T.val }
E → T         { E.val = T.val }
T → T * F     { T.val = T₁.val * F.val }
T → F         { T.val = F.val }
F → ( E )     { F.val = E.val }
F → digit     { F.val = digit.lexval }
```

### L-Attributed Definitions

L-attributed definitions use both synthesized and inherited attributes but with restrictions that make them suitable for top-down parsing. They satisfy:

1. All inherited attributes of a symbol can be computed from attributes of its left siblings and parents
2. Synthesized attributes can be computed in the usual way

**Example: Type Declaration Processing**

Grammar:

```
D → T L       { L.in = T.type }
T → int       { T.type = integer }
T → float     { T.type = float }
L → L₁, id    { L₁.in = L.in; addType(id.entry, L.in) }
L → id        { addType(id.entry, L.in) }
```

## Dependency Graphs

To determine the evaluation order of attributes, we construct dependency graphs that show the flow of information between attributes.

**Example Dependency Graph:**

Consider the production: `S → A B { S.val = A.val + B.val }`

The dependency graph would show:

- A.val → S.val
- B.val → S.val

```
Dependency Graph:

A.val ───┐
         │
         ├─→ S.val
         │
B.val ───┘
```

## Evaluation Orders

The order in which attributes are computed depends on the dependencies between them. Different evaluation strategies include:

### 1. Depth-First Evaluation

Traverse the parse tree and evaluate attributes when all dependencies are satisfied.

### 2. Oblivious Evaluation

Predefine an order regardless of dependencies (less common).

### 3. Rule-Based Evaluation

Evaluate based on the order specified by semantic rules.

## Implementation with Parsing Techniques

### SDDs with LR Parsing

LR parsers can efficiently handle S-attributed definitions. During reduction, the semantic actions are executed, and synthesized attributes are computed.

**SLR Parser with Semantic Actions:**

```
State Stack | Input | Action | Semantic Stack
--------------------------------------------
0          | 3+5*2$| shift  | -
0,3        | +5*2$ | reduce F→digit | push(3)
0,F        | +5*2$ | reduce T→F | push(3)
0,T        | +5*2$ | reduce E→T | push(3)
0,E        | +5*2$ | shift  | 3
0,E,+
```

### SDDs with LL Parsing

LL parsers can handle L-attributed definitions effectively. Inherited attributes are passed down during prediction.

## Applications of SDDs

SDDs are used extensively in various compiler phases:

1. **Abstract Syntax Tree Construction**: Building AST nodes with proper attributes
2. **Type Checking**: Verifying type compatibility using inherited type information
3. **Intermediate Code Generation**: Generating three-address code or other IR
4. **Symbol Table Management**: Propagating declaration information
5. **Code Optimization**: Collecting information for optimization decisions

## Examples and Case Studies

### Example 1: Expression Evaluation

**Grammar with SDD:**

```
Production               Semantic Rule
E → E₁ + T              E.val = E₁.val + T.val
E → T                   E.val = T.val
T → T₁ * F              T.val = T₁.val * F.val
T → F                   T.val = F.val
F → ( E )               F.val = E.val
F → digit               F.val = digit.lexval
```

**Parse Tree for "3 + 5 \* 2":**

```
        E (val=13)
       /|\
      / | \
 (val=3) + (val=10)
     E   T /|\
          / | \
     (val=5) * (val=2)
         T   F /|\
              / | \
         (val=2) digit (2)
```

### Example 2: Type Declaration Processing

**Grammar with SDD:**

```
D → T L                 { L.in = T.type }
T → int                 { T.type = integer }
T → float               { T.type = float }
L → L₁, id              { L₁.in = L.in; addType(id.entry, L.in) }
L → id                  { addType(id.entry, L.in) }
```

**Processing "int x, y":**

```
Parse Tree:

        D
       / \
      /   \
     T     L (in=integer)
     |    /|\
     |   / | \
   int L , id (y)
      /|\
     / | \
    /  |  \
   id (x)  [addType]
```

## Comparison of SDD Types

| Feature                       | S-Attributed SDDs      | L-Attributed SDDs              |
| ----------------------------- | ---------------------- | ------------------------------ |
| **Attributes Used**           | Synthesized only       | Both synthesized and inherited |
| **Parsing Compatibility**     | Bottom-up parsers (LR) | Top-down parsers (LL)          |
| **Evaluation Order**          | Bottom-up              | Left-to-right                  |
| **Implementation Complexity** | Simpler                | More complex                   |
| **Expressiveness**            | Limited                | More powerful                  |

## Common Challenges and Solutions

### 1. Circular Dependencies

Problem: Attributes depending on each other circularly
Solution: Ensure the SDD is non-circular by careful design

### 2. Evaluation Order Determination

Problem: Determining the correct order to evaluate attributes
Solution: Use dependency graphs to find topological orders

### 3. Parser Integration

Problem: Integrating semantic actions with parsing algorithms
Solution: Choose appropriate SDD type for the parsing technique

## Exam Tips

1. **Understand Attribute Types**: Clearly distinguish between synthesized and inherited attributes
2. **Practice Dependency Graphs**: Be able to draw and analyze dependency graphs for given productions
3. **Know Parser Compatibility**: Remember that S-attributed SDDs work with LR parsing, while L-attributed work with LL parsing
4. **Work Through Examples**: Practice evaluating attributes for simple expressions and declarations
5. **Watch for Circularities**: Always check that your SDDs don't have circular dependencies
6. **Focus on Evaluation Order**: Understand how different evaluation strategies work

**Memory Aid**: "Synthesized goes Up, Inherited goes Down" - SUID principle
