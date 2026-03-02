# Normal Forms for Context-Free Grammars

## Introduction to Normal Forms

Normal forms are standardized ways of writing context-free grammars (CFGs) that simplify analysis and manipulation while preserving the language generated. They are essential for proving properties of context-free languages and for practical applications like parsing.

**Why Use Normal Forms?**
- Simplify the structure of grammars
- Enable easier proofs (e.g., Pumping Lemma)
- Facilitate parser design and implementation
- Eliminate ambiguity and redundancy
- Provide canonical forms for equivalence testing

## Key Concepts and Definitions

### Formal Definition of CFG
A context-free grammar is a 4-tuple G = (V, Σ, R, S) where:
- V is a finite set of variables (non-terminals)
- Σ is a finite set of terminals (V ∩ Σ = ∅)
- R is a finite set of production rules (V → (V ∪ Σ)*)
- S ∈ V is the start symbol

### Useful Productions vs Problematic Productions
Some production types complicate grammar analysis:
- ε-productions (A → ε)
- Unit productions (A → B)
- Useless symbols (non-generating or unreachable)
- Mixed productions (excessive terminals/non-terminals)

## Chomsky Normal Form (CNF)

### Definition
A CFG is in Chomsky Normal Form if all production rules are of one of two forms:
1. A → BC (where B and C are variables)
2. A → a (where a is a terminal)

Additionally, the grammar cannot contain ε-productions (except possibly S → ε, and if so, S cannot appear on any right-hand side).

### Conversion to CNF

#### Step 1: Eliminate ε-Productions
A variable A is **nullable** if A ⇒* ε.

Algorithm:
1. Identify all nullable variables
2. For each production A → X₁X₂...Xₙ, add new productions where nullable symbols are omitted in all possible combinations
3. Remove all ε-productions (except possibly S → ε)

**Example:**
Original: S → aSb | ε
Nullable: S
New productions: S → aSb | ab
After ε-elimination: S → aSb | ab

#### Step 2: Eliminate Unit Productions
Unit productions are of the form A → B where B is a variable.

Algorithm:
1. Find all pairs (A, B) such that A ⇒* B using unit productions
2. For each such pair, add A → α for every production B → α
3. Remove all unit productions

**Example:**
Original: S → A | a, A → B | b, B → C | c, C → d
Unit pairs: (S, A), (S, B), (S, C), (A, B), (A, C), (B, C)
New productions: S → a | b | c | d, A → b | c | d, B → c | d
After elimination: S → a | b | c | d, A → b | c | d, B → c | d, C → d

#### Step 3: Eliminate Useless Symbols
A symbol is **useless** if it:
- Cannot generate any terminal string (non-generating)
- Cannot be reached from the start symbol (unreachable)

Algorithm:
1. Eliminate non-generating symbols
2. Eliminate unreachable symbols

**Example:**
Grammar: S → AB | a, A → a, B → b, C → c
Non-generating: None
Unreachable: C
After elimination: S → AB | a, A → a, B → b

#### Step 4: Convert to Proper Form
Finally, convert remaining productions to CNF form:

For productions with more than 2 symbols: A → X₁X₂...Xₙ (n > 2)
Introduce new variables: A → X₁A₁, A₁ → X₂A₂, ..., Aₙ₋₂ → Xₙ₋₁Xₙ

For productions with mixed terminals/non-terminals: A → aB
Introduce new variable: A → CₐB, Cₐ → a

**Complete Example Conversion:**
Original: S → aSb | ε

After ε-elimination: S → aSb | ab
After unit elimination: (No unit productions)
After useless elimination: (No useless symbols)
Final CNF:
S → AC | AB
A → a
B → b
C → SB

## Greibach Normal Form (GNF)

### Definition
A CFG is in Greibach Normal Form if all production rules are of the form:
A → aα (where a is a terminal and α is a string of zero or more variables)

No ε-productions are allowed (except possibly S → ε, with S not on any right-hand side).

### Conversion to GNF

Conversion to GNF is more complex and typically involves:
1. Eliminating left recursion
2. Ensuring productions begin with terminals
3. Using substitution to achieve the proper form

**Left Recursion Elimination:**
For immediate left recursion: A → Aα | β
Replace with: A → βA', A' → αA' | ε

**Example:**
Original: S → Sa | b
After elimination: S → bS', S' → aS' | ε

## Comparison of Normal Forms

| Feature | Chomsky Normal Form | Greibach Normal Form |
|---------|---------------------|----------------------|
| **Production Form** | A → BC or A → a | A → aα (α ∈ V*) |
| **ε-productions** | Not allowed (except S → ε) | Not allowed (except S → ε) |
| **Parse Tree Height** | Relates to string length | Relates to derivation length |
| **Use in Parsing** | CYK algorithm | Top-down parsing |
| **Conversion Complexity** | Moderate | More complex |
| **Theoretical Applications** | Pumping lemma proofs | Automation theory |

## Practical Applications

### CYK Parsing Algorithm
The Cocke-Younger-Kasami algorithm uses CNF to parse strings in O(n³) time:

```
Algorithm CYK(w, G in CNF)
1. Let n = length(w)
2. Create table T[i,j] for all substrings
3. For i = 1 to n:
      For each production A → a:
          if a = w_i then add A to T[i,1]
4. For l = 2 to n:
      For i = 1 to n-l+1:
          For k = 1 to l-1:
              For each production A → BC:
                  if B ∈ T[i,k] and C ∈ T[i+k,l-k] then
                      add A to T[i,l]
5. Return true if S ∈ T[1,n]
```

**Example Parse Table for "aab" and grammar S → AB, A → a, B → b:**
```
    1     2     3
1: {A}   {S}   ∅
2: ∅     {B}   ∅  
3: ∅     ∅     ∅
```

## Exam Tips

1. **Conversion Order Matters**: Always follow the sequence: ε-elimination → unit elimination → useless elimination → final conversion
2. **Watch for Special Cases**: The start symbol may need special handling for ε-productions
3. **Minimize New Variables**: While converting, try to reuse existing variables when possible
4. **Verify Results**: Always check that your converted grammar generates the same language
5. **Practice Common Patterns**: Familiarize yourself with common grammar structures and their normal form equivalents
6. **Time Management**: CNF conversion questions can be time-consuming; practice to build speed