# Context-Free Grammar and Parsing

## Introduction to Syntactic Analysis
Syntactic analysis, or parsing, is the process of analyzing a string of symbols (words) to determine its grammatical structure with respect to a given formal grammar. It is a fundamental step in Natural Language Processing (NLP) that bridges morphological analysis (word-level) and semantic analysis (meaning-level). Context-Free Grammars (CFGs) provide the formal foundation for describing the syntactic structure of most programming languages and many aspects of natural languages.

## What is a Context-Free Grammar (CFG)?
A Context-Free Grammar is a 4-tuple (N, Σ, R, S) where:
- **N** is a finite set of non-terminal symbols (syntactic categories)
- **Σ** is a finite set of terminal symbols (words/vocabulary)
- **R** is a finite set of production rules of the form A → β, where A ∈ N and β ∈ (N ∪ Σ)*
- **S** is the start symbol (S ∈ N)

### CFG Components Explained
**Terminal Symbols**: The actual words in the language (e.g., "cat", "dog", "the").
**Non-terminal Symbols**: Abstract syntactic categories that represent groups of words (e.g., NP for noun phrase, VP for verb phrase).
**Production Rules**: Rules that define how non-terminals can be rewritten as sequences of terminals and non-terminals.
**Start Symbol**: The root non-terminal from which all derivations begin.

## CFG Notation and Examples
### Basic CFG for English
```
S → NP VP
NP → Det N | Det Adj N | N
VP → V | V NP
Det → 'the' | 'a'
N → 'cat' | 'dog' | 'mouse'
V → 'chases' | 'eats'
Adj → 'big' | 'small'
```

### Derivation Example
Let's derive the sentence "the big cat chases the mouse":
1. S → NP VP
2. NP → Det Adj N
3. Det → 'the'
4. Adj → 'big'
5. N → 'cat'
6. VP → V NP
7. V → 'chases'
8. NP → Det N
9. Det → 'the'
10. N → 'mouse'

## Parse Trees
A parse tree represents the syntactic structure of a sentence according to the grammar. It is a rooted, ordered tree where:
- Root node is labeled S (start symbol)
- Internal nodes are labeled by non-terminals
- Leaf nodes are labeled by terminals
- The children of each node represent the application of a production rule

### Parse Tree for "the big cat chases the mouse"
```
            S
        ____|____
       |         |
       NP        VP
  ____|____      |____
 |    |    |     |    |
Det  Adj   N     V    NP
 |    |    |     |    |___
the  big  cat chases Det  N
                     |    |
                     the mouse
```

## Ambiguity in CFGs
A grammar is ambiguous if it can generate the same sentence with multiple different parse trees. This is a significant challenge in NLP.

### Types of Ambiguity
1. **Structural Ambiguity**: Multiple parse trees for the same sentence.
   Example: "I saw the man with the telescope" - who has the telescope?
2. **Attachment Ambiguity**: Where to attach a prepositional phrase.
3. **Coordination Ambiguity**: How conjunctions group constituents.

### Example of Structural Ambiguity
Sentence: "Old men and women"
```
Interpretation 1: [Old men] and [women]          Interpretation 2: [Old] [men and women]
         S                                       S
        / \                                     / \
      NP   VP                                 NP   VP
     /  |  \                                /  |  \
   Adj  N  Conj NP                       Adj  NP  ...
    |   |   |   |                         |  / | \
   Old men and women                      Old N Conj N
                                          |  | |   |
                                         men and women
```

## Parsing Algorithms
Parsing algorithms determine whether a string belongs to the language of a grammar and build the corresponding parse tree(s).

### Top-Down Parsing
Top-down parsers start with the start symbol and apply production rules to expand non-terminals until they match the input string.

```
Start: S
Goal: Match input "the cat eats"
Step 1: S → NP VP
Step 2: NP → Det N → the N → the cat
Step 3: VP → V → eats
Success: Input matched
```

### Bottom-Up Parsing
Bottom-up parsers start with the input words and work upward, applying production rules in reverse until they reach the start symbol.

```
Input: "the cat eats"
Step 1: the → Det
Step 2: cat → N
Step 3: Det N → NP
Step 4: eats → V
Step 5: V → VP
Step 6: NP VP → S
Success: Reached start symbol S
```

## The CYK Parsing Algorithm
The Cocke-Younger-Kasami (CYK) algorithm is a dynamic programming approach for parsing strings with context-free grammars. It requires the grammar to be in Chomsky Normal Form (CNF).

### Chomsky Normal Form (CNF)
A CFG is in CNF if all production rules are of one of two forms:
1. A → BC (where B and C are non-terminals)
2. A → a (where a is a terminal)

### CYK Algorithm Steps
1. Convert grammar to CNF
2. Create a 2D table where table[i][j] contains all non-terminals that can generate the substring from position i to j
3. Fill the table bottom-up:
   - Initialize diagonal with rules that produce terminals
   - For longer substrings, combine smaller constituents

### CYK Table Visualization
For sentence "the cat eats" and grammar in CNF:
```
Length 1: Positions [0,1]: Det, [1,2]: N, [2,3]: V
Length 2: [0,2]: NP (from Det N), [1,3]: VP (from N V)* *if grammar allows
Length 3: [0,3]: S (from NP VP)
```

```
    j=1    j=2    j=3
i=1 Det    NP     S
i=2        N     VP
i=3              V
```

### CYK Pseudocode
```
let n = length of input string
let table be 2D array of sets of non-terminals (n x n)

for i from 1 to n:
    table[i][1] = {A | A → input[i] is a rule}
    
for length from 2 to n:
    for i from 1 to n - length + 1:
        j = i + length - 1
        for k from i to j-1:
            for each rule A → B C:
                if B ∈ table[i][k] and C ∈ table[k+1][j]:
                    add A to table[i][j]
                    
return S ∈ table[1][n]
```

## CFG Limitations for Natural Language
While CFGs are powerful, they have limitations for modeling natural language:

1. **Lack of agreement features**: CFGs cannot easily handle subject-verb agreement
2. **No shared references**: CFGs cannot represent co-reference relationships
3. **Fixed constituency**: Some linguistic phenomena don't fit neat constituency patterns
4. **Cross-serial dependencies**: Some dependencies span across the sentence

### Comparison: CFG vs Other Grammars
| Feature | CFG | Regular Grammar | Context-Sensitive Grammar |
|---------|-----|-----------------|--------------------------|
| Expressiveness | Moderate | Limited | High |
| Parsing Complexity | O(n³) | O(n) | Undecidable |
| Handles Natural Language | Partially | No | Yes |
| Implementation Difficulty | Moderate | Easy | Very Hard |

## Practical Applications of CFG Parsing
1. **Compiler Design**: Parsing programming languages
2. **Information Extraction**: Identifying syntactic relationships
3. **Question Answering**: Understanding sentence structure
4. **Grammar Checking**: Identifying ungrammatical sentences
5. **Semantic Analysis**: Providing structure for meaning interpretation

## Exam Tips
1. **Remember the 4-tuple definition**: N, Σ, R, S - this is frequently tested
2. **Practice derivation**: Be able to derive sentences step-by-step with given grammars
3. **Draw parse trees**: Clearly label nodes and show the complete structure
4. **Understand ambiguity**: Be prepared to explain and demonstrate different types of ambiguity
5. **CYK algorithm**: Memorize the steps and practice with CNF grammars
6. **Know the limitations**: Understand why CFGs are insufficient for full natural language processing
7. **Compare algorithms**: Be able to contrast top-down, bottom-up, and CYK parsing approaches