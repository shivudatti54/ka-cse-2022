# Parse Trees

## Introduction

Parse trees, also known as concrete syntax trees (CST), constitute a fundamental data structure in compiler design and formal language theory. A parse tree provides a hierarchical representation of the syntactic structure of a string derived from a formal grammar, capturing the application of production rules in a tree data structure. When the lexical analyzer processes source code, it produces a stream of tokens; the parser then analyzes this token stream and constructs a parse tree that reflects the grammatical structure of the input according to the defined context-free grammar (CFG).

The significance of parse trees in compiler design is multifaceted. They serve as an essential intermediate representation between lexical analysis and semantic analysis, enabling the compiler to perform type checking, symbol table construction, and subsequent code generation phases. Furthermore, parse trees facilitate syntax error detection and recovery mechanisms. In the broader context of theoretical computer science, parse trees establish a concrete connection between formal grammars and derivations, providing a visual and structural representation of how strings are generated or recognized.

This topic forms the foundation for understanding more advanced parsing techniques, including top-down parsing (recursive descent, LL(k)), bottom-up parsing (LR(0), SLR(1), LALR), abstract syntax trees (AST), and syntax-directed translation schemes. A thorough comprehension of parse trees is therefore essential for students pursuing courses in compiler design, theory of computation, and formal languages.

## Formal Definitions and Properties

### Definition of Parse Tree

A parse tree is an ordered, rooted tree that represents the syntactic structure of a string according to a context-free grammar G = (V, T, P, S), where V is the set of non-terminals, T is the set of terminals, P is the set of production rules, and S is the start symbol.

**Definition**: Let G = (V, T, P, S) be a context-free grammar. A parse tree for a string w ∈ T\* is an ordered tree T such that:

1. Every node in T is labeled by a symbol from V ∪ T ∪ {ε}
2. The root node is labeled with the start symbol S
3. If a node labeled A ∈ V has children labeled X₁, X₂, ..., Xₙ (from left to right), then A → X₁X₂...Xₙ must be a production rule in P
4. If a node is labeled with ε, that node is a leaf and has exactly one child
5. The yield (frontier) of the tree, obtained by reading leaf nodes from left to right, equals the string w

**Theorem (Parse Tree ↔ Derivation Equivalence)**: For a context-free grammar G, there exists a one-to-one correspondence between parse trees for a string w and leftmost (or rightmost) derivations of w from the start symbol S.

_Proof_: We prove this by demonstrating the bidirectional mapping:

(_Derivation → Parse Tree_) Given a leftmost derivation S ⇒\* w, we can construct the parse tree by induction on the number of derivation steps. At each step, when a non-terminal A is expanded to α = X₁X₂...Xₙ using production A → α, we create children X₁, X₂, ..., Xₙ under the node labeled A in the partially constructed tree. Since leftmost derivation expands the leftmost non-terminal first, the tree construction proceeds unambiguously, yielding a unique parse tree.

(_Parse Tree → Derivation_) Given a parse tree, we obtain a leftmost derivation by repeatedly replacing the leftmost non-terminal leaf with its production rule RHS. Since each internal node corresponds to exactly one production application, this process yields a unique leftmost derivation.

Therefore, there is a bijective relationship between parse trees and leftmost derivations. ∎

### Properties of Parse Trees

Let T be a parse tree constructed from grammar G = (V, T, P, S). The following properties hold:

1. **Root Property**: The root node of every parse tree is labeled with the start symbol S ∈ V.

2. **Node Label Property**: Every internal node (including root) must be labeled with a non-terminal symbol A ∈ V. Every leaf node must be labeled with either a terminal symbol a ∈ T or ε.

3. **Production Rule Property**: If a node labeled A ∈ V has children labeled X₁, X₂, ..., Xₙ (read from left to right), then the production rule A → X₁X₂...Xₙ must exist in the grammar's production set P.

4. **Yield Property**: The string obtained by reading all leaf labels from left to right is called the **yield** or **frontier** of the parse tree. For a valid parse tree representing string w, the yield must equal w.

5. **Subtree Property**: Every subtree of a parse tree corresponds to a derivation of its yield from the label of the subtree's root node.

### Relationship Between Derivations and Parse Trees

Consider a context-free grammar G and a string w. Let S ⇒\* w be a derivation. The parse tree representing this derivation has the following characteristics:

- **Leftmost Derivation**: A leftmost derivation replaces the leftmost non-terminal at each step. For example, given grammar E → E + T | T, T → T _ F | F, F → (E) | id, the string id + id _ id has the following leftmost derivation:

E ⇒ E + T ⇒ T + T ⇒ F + T ⇒ id + T ⇒ id + T _ F ⇒ id + F _ F ⇒ id + id _ F ⇒ id + id _ id

- **Rightmost Derivation**: A rightmost derivation replaces the rightmost non-terminal at each step. For the same string, the rightmost derivation proceeds as:

E ⇒ E + T ⇒ E + T _ F ⇒ E + T _ id ⇒ E + F _ id ⇒ E + id _ id ⇒ T + id _ id ⇒ F + id _ id ⇒ id + id \* id

_Note_: Both leftmost and rightmost derivations yield the same parse tree structure; they differ only in the order of production applications.

## Ambiguity in Grammars

### Definition and Implications

**Definition**: A context-free grammar G is said to be **ambiguous** if there exists at least one string w ∈ L(G) that has two or more distinct parse trees. Equivalently, there exist two or more distinct leftmost (or rightmost) derivations for the same string.

**Theorem**: If a grammar is ambiguous, then it is not inherently suitable for parsing because the syntactic structure of certain strings becomes non-deterministic.

_Proof_: Suppose string w has two distinct parse trees T₁ and T₂. Since parse trees correspond bijectively to leftmost derivations, w must have two distinct leftmost derivations D₁ and D₂. During semantic analysis, these different parse trees may lead to different semantic interpretations (e.g., different operator precedence), making deterministic semantic analysis impossible without additional disambiguation rules. ∎

### Example of Ambiguous Grammar

Consider the classic dangling-else ambiguity in the grammar:

```
S → if E then S | if E then S else S | other
```

The string `if a then if b then c else d` has two valid parse trees:

**Parse Tree 1** (associating else with nearest if):

```
      S
   /  |  \
if  E   S
 |      /|\
 a   if E S else d
     |  |  |
     b  c
```

**Parse Tree 2** (associating else with outer if):

```
       S
   /   |   \
if  E     S
 |      / | \
 a   if E S else d
     |  |  |
     b  c
```

The ambiguity arises because the grammar does not specify whether the `else` clause binds to the inner or outer `if` statement. This is typically resolved in programming languages by adopting the rule that `else` associates with the nearest unmatched `then`.

## Construction of Parse Trees

### Algorithm

Given a context-free grammar G = (V, T, P, S) and an input string w, the parse tree construction proceeds as follows:

**Step 1**: Begin with root node labeled S.

**Step 2**: At each internal node labeled with non-terminal A, select a production rule A → α ∈ P and create children labeled with symbols of α from left to right.

**Step 3**: Continue until all leaf nodes are labeled with terminals from T ∪ {ε}.

**Step 4**: Verify that the yield equals w. If so, a valid parse tree exists; otherwise, parsing fails.

### Worked Example

**Problem**: Construct the parse tree for string `id + id * id` using grammar:

```
E → E + T | T
T → T * F | F
F → ( E ) | id
```

**Solution Using Leftmost Derivation**:

Step 1: E → E + T

Step 2: E → T + T

Step 3: E → F + T

Step 4: E → id + T

Step 5: E → id + T \* F

Step 6: E → id + F \* F

Step 7: E → id + id \* F

Step 8: E → id + id \* id

**Parse Tree**:

```
           E
        /  |  \
       E   +   T
       |      /|\
       T     T * F
       |     |   |
       F    F   F
       |    |   |
      id   id  id
```

**Verification**: Reading the leaves from left to right yields: id + id \* id, which matches the input string.

## Parse Trees vs. Abstract Syntax Trees

While parse trees capture every detail of the grammar including all intermediate non-terminals and production steps, **Abstract Syntax Trees (AST)** represent only the essential syntactic structure relevant for semantic analysis and code generation.

| Feature    | Parse Tree                        | Abstract Syntax Tree               |
| ---------- | --------------------------------- | ---------------------------------- |
| Node Types | All non-terminals preserved       | Only operators and operands        |
| Size       | Larger (includes all productions) | More compact                       |
| Structure  | Concrete syntax                   | Abstract syntax                    |
| Use Case   | Parsing verification              | Semantic analysis, code generation |
| Precedence | Implicit through structure        | Must be encoded separately         |

## Conclusion

Parse trees provide a fundamental bridge between formal grammar theory and practical compiler implementation. The one-to-one correspondence between parse trees and derivations establishes their theoretical importance, while their role in syntax analysis makes them indispensable in compiler design. Understanding parse trees, their properties, and their construction is essential for grasping more advanced topics in parsing theory and compiler construction.
