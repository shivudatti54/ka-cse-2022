# Regular Expressions and Finite-State Automata

## Introduction

Regular Expressions (Regex) and Finite-State Automata (FSA) are fundamental formalisms in computer science and natural language processing (NLP) for describing patterns in strings. They form the mathematical backbone of many text processing tasks, including tokenization, morphological analysis, spelling error detection, and information extraction. Their importance stems from their simplicity, expressiveness, and computational efficiency.

## 1. Regular Expressions (Regex)

A regular expression is a sequence of characters that defines a search pattern. It is a powerful and concise notation for describing a set of strings that belong to a formal language.

### 1.1 Basic Regex Components

*   **Literals:** Ordinary characters like `a`, `5`, or `@` that match themselves.
*   **Metacharacters:** Characters with special meaning: `. ^ $ * + ? { } [ ] \ | ( )`
*   **Character Classes (`[...]`):** Match any one of a set of characters.
    *   `[aeiou]` matches any single vowel.
    *   `[A-Za-z]` matches any single uppercase or lowercase letter.
    *   `[^0-9]` matches any single character that is *not* a digit (the `^` inside brackets negates the class).
*   **Predefined Character Classes:** Shorthand for common classes.
    *   `\d` matches any digit (`[0-9]`).
    *   `\w` matches any word character (`[A-Za-z0-9_]`).
    *   `\s` matches any whitespace character (space, tab, newline).
    *   Their uppercase versions (`\D`, `\W`, `\S`) match the opposite.
*   **Quantifiers:** Specify how many instances of a character or group are required.
    *   `*` : 0 or more times.
    *   `+` : 1 or more times.
    *   `?` : 0 or 1 time (optional).
    *   `{n}` : Exactly `n` times.
    *   `{n,}` : `n` or more times.
    *   `{n,m}` : Between `n` and `m` times.
*   **Anchors:** Specify the position of the pattern in the string.
    *   `^` : Start of a line.
    *   `$` : End of a line.
    *   `\b` : Word boundary.
*   **Alternation (`|`) and Grouping (`(...)`)**: The pipe `|` acts as a logical OR. Parentheses `(...)` are used to group subpatterns and apply quantifiers to the entire group.
    *   `cat|dog` matches "cat" or "dog".
    *   `(ab)+` matches "ab", "abab", "ababab", etc.

### 1.2 Examples and Use Cases in NLP

Regex is extensively used in the early stages of the NLP pipeline.

*   **Tokenization:** Splitting text into words/tokens.
    *   Simple word splitter: `\w+` (matches sequences of word characters).
*   **Finding Patterns:**
    *   Email: `\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b`
    *   Hashtags: `#\w+`
*   **Morphology:** Finding word stems or variants.
    *   Matching "running", "jumping", "flying": `\w+ing\b`

### 1.3 Limitations of Regex

While powerful, regex has limitations. It cannot, for example:
*   Count and match arbitrary nested structures (e.g., balanced parentheses `((()))`).
*   Remember an arbitrary amount of state (e.g., checking if a string has the same number of 'a's and 'b's).

## 2. Finite-State Automata (FSA)

A Finite-State Automaton (FSA) or Finite-State Machine (FSM) is an abstract mathematical model of computation consisting of a finite number of states, transitions between those states, and an input. It is a graph-based representation of a pattern.

### 2.1 Core Components of an FSA

An FSA is formally defined as a 5-tuple `(Q, Σ, δ, q0, F)`:
*   `Q`: A finite set of **states**.
*   `Σ` (Sigma): A finite **alphabet** (set of input symbols).
*   `δ` (Delta): The **transition function** (`δ: Q × Σ → Q`). It defines the rules for moving from one state to another.
*   `q0`: The **start state** (`q0 ∈ Q`).
*   `F`: A set of **final/accepting states** (`F ⊆ Q`).

### 2.2 How an FSA Works

The automaton starts in the start state `q0`. It reads the input string one symbol at a time. For each symbol, it consults the transition function `δ` to move to a new state. After processing the entire string, if the automaton is in **any one of the accepting states** (`F`), the input string is **accepted** (it matches the pattern). Otherwise, it is **rejected**.

### 2.3 Example: Building an FSA for "cat" and "cot"

Let's build an FSA that accepts the words "cat" and "cot".

*   **Alphabet (Σ):** `{a, c, o, t}`
*   **States (Q):** `q0, q1, q2, q3`
*   **Start State (q0):** `q0`
*   **Accept States (F):** `{q3}`

**Transition Function (δ):**
*   `δ(q0, c) = q1`
*   `δ(q1, a) = q2`
*   `δ(q1, o) = q2`  // This is the key! From q1, we can go to q2 on 'a' OR 'o'
*   `δ(q2, t) = q3`

This can be represented as a state diagram:

```
       a
    /-----\
c  V       | t
q0 --> q1 --> q2 --> q3 (FINAL)
    \->/
       o
```
*(ASCII Art: `q0` has an arrow labeled 'c' to `q1`. `q1` has two arrows: one labeled 'a' to `q2` and one labeled 'o' to `q2`. `q2` has an arrow labeled 't' to the final state `q3`.)*

### 2.4 Types of FSA

*   **Deterministic Finite Automaton (DFA):** For every state and every input symbol, there is **exactly one** transition. The example above is a DFA.
*   **Nondeterministic Finite Automaton (NFA):** For a given state and input symbol, there can be **zero, one, or many** transitions. NFAs can also have **ε-transitions** (transitions that occur without consuming an input symbol). NFAs are often easier to design but are computationally equivalent to DFAs.

## 3. The Fundamental Equivalence

A crucial theorem in formal language theory states that:
**The class of languages that can be described by Regular Expressions is exactly the same as the class of languages that can be recognized by Finite-State Automata (both DFAs and NFAs).**

This means any regex pattern can be converted into an equivalent FSA, and vice-versa. This equivalence is why regex engines are implemented using automata theory.

### 3.1 Conversion Process (Conceptual)

1.  **Regex to NFA:** There are standard algorithms (e.g., Thompson's construction) to build an NFA from a regex. Each regex operation (concatenation, alternation `|`, Kleene star `*`) has a corresponding NFA construction.
2.  **NFA to DFA:** Another algorithm (the subset construction) converts an NFA into an equivalent DFA. The DFA's states represent sets of possible states the NFA could be in. This can sometimes lead to a combinatorial explosion of states but guarantees determinism.
3.  **DFA Minimization:** The resulting DFA can often be minimized to an equivalent DFA with the smallest possible number of states.

This pipeline is often used in lexer generators (like `lex` or `flex`).

## 4. Applications in NLP

The synergy between regex and FSA is vital for NLP tasks outlined in the syllabus.

*   **Morphological Parsing:** FSAs are perfect for modeling simple morphological processes. An FSA can be built to recognize all valid prefixes, stems, and suffixes of a language. For instance, an FSA can recognize "un+system+atic+al+ly" by chaining together morpheme FSAs.
*   **Spelling Error Detection:** A large FSA can be constructed to accept all correctly spelled words in a dictionary. Any input word not accepted by this automaton is a potential spelling error. Furthermore, FSAs can model common errors (insertion, deletion, substitution, transposition) to suggest corrections.
*   **Tokenization and Word Segmentation:** Defining what constitutes a token often uses regex patterns. These patterns are implemented as FSAs for efficient scanning.

### 4.1 Comparison Table: Regex vs. FSA

| Feature | Regular Expressions | Finite-State Automata |
| :--- | :--- | :--- |
| **Representation** | Textual, declarative string | Graphical, state-transition diagram |
| **Formalism** | Algebraic | Computational |
| **Ease of Writing** | **Easier** for simple patterns | Can be more intuitive for complex alternations |
| **Implementation** | Interpreted by a regex engine | Can be directly executed as a state machine |
| **Underlying Theory** | Both are equivalent and describe the class of **Regular Languages** | Both are equivalent and describe the class of **Regular Languages** |

## 5. Implementation and Efficiency

Modern regex engines are highly optimized. While they are based on NFAs/DFAs, they often use sophisticated techniques like backtracking for features not present in pure regular languages (e.g., backreferences `\1`), which make them more powerful but also potentially exponentially slower. For patterns that remain purely regular, DFA-based engines guarantee linear-time processing `O(n)` relative to input length `n`.

## Exam Tips

1.  **Understand Equivalence:** Be able to explain why regex and FSA are two sides of the same coin. This is a key conceptual point.
2.  **Draw FSAs:** Practice converting simple regex patterns (e.g., `a(b|c)*d`, `colou?r`) into their corresponding FSA diagrams. Clearly label start and final states.
3.  **Write Regex:** Practice writing regex for common NLP tasks: finding plurals (`\w+s\b`), finding phone numbers, extracting URLs.
4.  **Know the Limits:** Remember that neither regex nor FSA can handle nested structures or true counting. This is why more powerful models like Context-Free Grammars (CFG) are needed for syntactic parsing, the next topic in your syllabus.
5.  **Link to Applications:** Be prepared to describe how FSA/regex are used in morphological parsing and spelling error detection. Use examples.