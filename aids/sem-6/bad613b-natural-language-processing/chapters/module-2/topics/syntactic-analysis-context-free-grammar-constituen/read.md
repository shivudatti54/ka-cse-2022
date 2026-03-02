# **Syntactic Analysis: Context-Free Grammar, Constituency, Top-down and Bottom-up Parsing, CYK Parsing**

### Definition and Overview

---

Syntactic analysis is the process of breaking down a sentence or a sequence of words into smaller components, known as phrases or clauses, based on the grammatical structure of the language. This process involves identifying the relationships between words and phrases, and understanding how they contribute to the overall meaning of the sentence.

### Context-Free Grammar (CFG)

---

A context-free grammar is a formal grammar system that uses a set of production rules to generate an infinite number of strings. Each production rule consists of a left-hand side (LHS) and a right-hand side (RHS), where the LHS is a string of non-terminal symbols, and the RHS is a string of terminal symbols or non-terminal symbols.

**Example CFG:**

```
S → NP VP
NP → Det N
VP → V NP | V
Det → a | an
N → man | woman | city
V → run | jump
```

In this example, `S` is the start symbol, and `NP` and `VP` are non-terminal symbols that represent noun phrases and verb phrases, respectively. The production rules show how these symbols can be combined to generate a sentence.

### Constituency

---

Constituency refers to the way in which the words in a sentence are grouped together to form phrases or clauses. There are two main types of constituency:

- **Semantic constituency**: This refers to the way in which the words in a sentence are grouped together to form meaningful units.
- **Syntactic constituency**: This refers to the way in which the words in a sentence are grouped together to form phrases or clauses based on grammatical rules.

**Example:**

```
The dog chased the cat.
```

In this sentence, "The", "dog", and "chased" form a semantic constituency, while "The", "dog", "chased", and "the" form a syntactic constituency.

### Top-down Parsing

---

Top-down parsing is a parsing technique that starts with the overall sentence and works its way down to the individual words. It involves applying production rules to the entire sentence to identify the relationships between the words.

**Example:**

```
Input: The dog chased the cat.
Parse Tree:
  S
 / \
NP VP
 / \
Det N V NP
 / \
The dog chased
 / \
The cat
```

In this example, the top-down parser identifies the `S` symbol as the start symbol, and then works its way down to the individual words to identify the relationships between them.

### Bottom-up Parsing

---

Bottom-up parsing is a parsing technique that starts with the individual words and works its way up to the overall sentence. It involves identifying the words and phrases that make up the sentence, and then combining them to form the overall sentence.

**Example:**

```
Input: The dog chased the cat.
Parse Tree:
  S
 / \
NP VP
 / \
Det N V NP
  / \
 The dog
  / \
  chased
 / \
The cat
```

In this example, the bottom-up parser identifies the individual words and phrases that make up the sentence, and then combines them to form the overall sentence.

### CYK Parsing

---

CYK (Context-Free Grammar) parsing is a parsing technique that uses a table-based approach to parse sentences. It involves creating a table of cells that represent the possible parses of the sentence, and then filling in the table based on the production rules.

**Example:**

```
Input: The dog chased the cat.
CYK Table:
  | S | NP | VP | Det | N | V
-------------------------
S |  |  |  |  |  |
NP |  |  |  |  |  |
VP |  |  |  |  |  |
Det |  |  |  |  |  |
N |  |  |  |  |  |
V |  |  |  |  |  |
```

In this example, the CYK parser fills in the table based on the production rules, and then identifies the parse tree based on the filled-in table.

### Key Concepts

---

- **Context-free grammar**: A formal grammar system that uses a set of production rules to generate an infinite number of strings.
- **Constituency**: The way in which words are grouped together to form phrases or clauses.
- **Top-down parsing**: A parsing technique that starts with the overall sentence and works its way down to the individual words.
- **Bottom-up parsing**: A parsing technique that starts with the individual words and works its way up to the overall sentence.
- **CYK parsing**: A parsing technique that uses a table-based approach to parse sentences.

### Exercises

---

1. Create a context-free grammar for the following sentence: "The dog chased the cat."
2. Identify the constituency of the following sentence: "The dog chased the cat."
3. Parse the following sentence using top-down parsing: "The dog chased the cat."
4. Parse the following sentence using bottom-up parsing: "The dog chased the cat."
5. Create a CYK table for the following sentence: "The dog chased the cat."
