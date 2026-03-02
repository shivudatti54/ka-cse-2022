# **Textbook 1: Ch - Natural Language Processing**

### Key Concepts

- **Regular Expressions**
  - Definition: A pattern used to match character combinations in strings
  - Examples:
    - Matching strings containing a specific word: `word`
    - Matching strings containing a specific word with a specific prefix: `prefix-word`
    - Matching strings containing a specific word with a specific suffix: `word-suffix`
- **Finite-State Automata**
  - Definition: A mathematical model for recognizing patterns in strings
  - Key concepts:
    - States: Representing different stages of the pattern recognition process
    - Transitions: Moving from one state to another based on input characters
    - Accepting states: States that indicate a match has been found
- **Morphological Parsing**
  - Definition: Analyzing words into their constituent parts (morphemes)
  - Key concepts:
    - Parts of speech: Identifying the grammatical category of each morpheme (e.g. noun, verb, adjective)
    - Morphological rules: Applying rules to combine morphemes into words
- **Spelling**
  - Definition: Verifying whether a word is spelled correctly
  - Key concepts:
    - Dictionary-based spell checking
    - N-gram based spell checking

### Important Formulas and Definitions

- **Regular Expression Patterns**
  - `.`: Matches any single character
  - `^` and `$`: Match the start and end of a string, respectively
  - `|`: Alternation operator (e.g. `a|b` matches either `a` or `b`)
  - `*`: Matches 0 or more of the preceding pattern
  - `+`: Matches 1 or more of the preceding pattern
  - `{n}`: Matches exactly `n` of the preceding pattern
- **Finite-State Automata Transition Function**
  - `Δ(q, a)`: Returns the next state `q'` after reading input character `a` from state `q`
- **Morphological Parsing Algorithm**
  - `Parse(word)`: Returns a parse tree representing the constituent morphemes of `word`
- **Spelling Correction Algorithm**
  - `Correct(word)`: Returns the corrected spelling of `word` if it is misspelled, or the original word if it is spelled correctly

### Theorems and Results

- **Glasher's Theorem**: States that every regular language can be recognized by a finite-state automaton.
- **Chomsky's Hierarchy**: Classifies regular languages, context-free languages, and recursively enumerable languages according to their computational complexity.
