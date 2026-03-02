# **Textbook 1: Ch**

## **Natural Language Processing**

### Word Level Analysis

#### Regular Expressions

Regular expressions (regex) are a powerful tool for pattern matching in strings. They are used to search for specific patterns in text, validate input, and extract data.

**Definition:** A regular expression is a string that defines a search pattern used to match character combinations.

**Example:** `hello` matches the string "hello"

**Key Concepts:**

- **Character Classes:** `[a-z]` matches any lowercase letter
- **Quantifiers:** `*` matches 0 or more occurrences of the preceding element, `+` matches 1 or more occurrences
- **Escaping:** `\` is used to escape special characters, e.g. `\.` matches a literal period
- **Groups:** `(` and `)` are used to group elements for capturing, e.g. `(hello|world)` matches either "hello" or "world"

**Regex Patterns:**

- `^[a-zA-Z]+$` matches a string that consists only of letters
- `^\d+$` matches a string that consists only of digits
- `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` matches an email address

#### Finite-State Automata

Finite-state automata (FSA) is a mathematical model for recognizing patterns in strings. It consists of a set of states, a transition function, and an acceptance function.

**Definition:** A finite-state automaton is a 5-tuple `(Q, Σ, δ, q0, F)`, where:

- `Q` is the set of states
- `Σ` is the input alphabet
- `δ` is the transition function
- `q0` is the initial state
- `F` is the set of accepting states

**Example:** Consider the automaton that recognizes the language `L = {ab, bb}`

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | a     | q1         |
| q0    | b     | q2         |
| q1    | a     | q2         |
| q2    | b     | q2         |
| q2    | b     | q3         |
| q3    | b     | q3         |

**Key Concepts:**

- **States:** The set of possible states in the automaton
- **Transitions:** The function that specifies the next state given the current state and input
- **Acceptance:** The set of states that indicate the end of a valid string

**FSAs:**

- `NFA` (Non-Deterministic Finite State Automaton): An automaton where the transition function is non-deterministic
- `DFA` (Deterministic Finite State Automaton): An automaton where the transition function is deterministic

### Morphological Parsing

Morphological parsing is the process of breaking down words into their constituent morphemes.

**Definition:** A morpheme is the smallest unit of language that carries meaning.

**Example:** The word "unbreakable" can be broken down into its constituent morphemes: "un-" (prefix), "-break-" (root), "-able" (suffix)

**Key Concepts:**

- **Morphemes:** The smallest units of language that carry meaning
- **Morphological Analysis:** The process of breaking down words into their constituent morphemes
- **Part-of-Speech Tagging:** The process of identifying the part of speech (such as noun, verb, adjective, etc.) of each word in a sentence

**Morphological Parsing Techniques:**

- **Rule-Based Approach:** Uses predefined rules to break down words into their constituent morphemes
- **Machine Learning Approach:** Uses machine learning algorithms to learn patterns in language and break down words into their constituent morphemes

#### Morphological Parsing Algorithms

- **N-gram Algorithm:** Uses N-grams (sequences of N items) to break down words into their constituent morphemes
- **Hidden Markov Model (HMM) Algorithm:** Uses HMMs to model the probability of morphological parsing

**Code Example (Python):**

```python
import re

def morphological_parsing(word):
    # Use regular expressions to break down the word into its constituent morphemes
    prefixes = re.findall(r'^([a-z]+)-', word)
    roots = re.findall(r'-([a-z]+)-', word)
    suffixes = re.findall(r'([a-z]+)-$', word)
    return prefixes, roots, suffixes

# Test the function
word = "unbreakable"
prefixes, roots, suffixes = morphological_parsing(word)
print(f"Prefixes: {prefixes}")
print(f"Roots: {roots}")
print(f"Suffixes: {suffixes}")
```

This code example uses regular expressions to break down the word "unbreakable" into its constituent morphemes. The `morphological_parsing` function returns three lists: `prefixes`, `roots`, and `suffixes`.
