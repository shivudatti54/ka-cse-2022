# **Deterministic Finite Automata, Nondeterministic Finite Automata, An Application: Text Search, Finite Automata with Epsilon-Transitions**

## **Theory of Computation Module**

### Introduction

In this module, we will delve into the world of finite automata, a fundamental concept in the theory of computation. Finite automata are mathematical models used to recognize patterns in strings. In this lecture, we will explore three types of finite automata:

1.  Deterministic Finite Automata (DFA)
2.  Nondeterministic Finite Automata (NFA)
3.  Finite Automata with Epsilon-Transitions (EFA)

We will also discuss the application of finite automata in text search and explore their historical context and modern developments.

### Deterministic Finite Automata (DFA)

A Deterministic Finite Automaton is a finite automaton that can only move to one state at a time, based on the current state and the next symbol in the input string.

**Diagram:**

```markdown
+---------------+
| Q = {q0, q1, q2} |
+---------------+
| δ(q0, a) = q1 |
| δ(q1, a) = q2 |
| δ(q2, a) = q0 |
| δ(q0, b) = q0 |
| δ(q1, b) = q1 |
| δ(q2, b) = q2 |
```

In the above diagram, `Q` is the set of states, `a` and `b` are the input symbols, and `δ` is the transition function.

**Properties of DFA:**

- **Determinism:** A DFA can only move to one state at a time.
- **Finiteness:** A DFA has a finite number of states.
- **Recognition:** A DFA recognizes a language if there is a path from the initial state to an accepting state.

**Examples:**

- Recognize the language {a^n b^n | n ≥ 0}
- Recognize the language {a^n b^n | n ≥ 0, a ≠ b}

**Case Study:**

Suppose we want to recognize the language {a^n b^n | n ≥ 0} using a DFA. We can design a DFA as follows:

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | a     | q1         |
| q0    | b     | q0         |
| q1    | a     | q2         |
| q1    | b     | q1         |
| q2    | a     | q0         |
| q2    | b     | q2         |

In this DFA, the initial state is `q0`, and the accepting states are `q2`.

### Nondeterministic Finite Automata (NFA)

A Nondeterministic Finite Automaton is a finite automaton that can move to multiple states based on the current state and the next symbol in the input string.

**Diagram:**

```markdown
+---------------+
| Q = {q0, q1, q2} |
+---------------+
| δ(q0, a) = {q1, q2} |
| δ(q1, a) = {q2} |
| δ(q2, a) = {q0} |
| δ(q0, b) = q0 |
| δ(q1, b) = q0 |
| δ(q2, b) = q0 |
```

In the above diagram, `Q` is the set of states, `a` and `b` are the input symbols, and `δ` is the transition function.

**Properties of NFA:**

- **Nondeterminism:** An NFA can move to multiple states based on the current state and the next symbol in the input string.
- **Finiteness:** An NFA has a finite number of states.
- **Recognition:** An NFA recognizes a language if there is a path from the initial state to an accepting state.

**Examples:**

- Recognize the language {a^n b^n | n ≥ 0}
- Recognize the language {a^n b^n | n ≥ 0, a ≠ b}

**Case Study:**

Suppose we want to recognize the language {a^n b^n | n ≥ 0} using an NFA. We can design an NFA as follows:

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | a     | {q1, q2}   |
| q0    | b     | q0         |
| q1    | a     | {q2}       |
| q1    | b     | q0         |
| q2    | a     | {q0}       |
| q2    | b     | q0         |

In this NFA, the initial state is `q0`, and the accepting states are `q2`.

### Finite Automata with Epsilon-Transitions (EFA)

A Finite Automaton with Epsilon-Transitions is a finite automaton that can move to an empty string.

**Diagram:**

```markdown
+---------------+
| Q = {q0, q1} |
+---------------+
| δ(q0, ε) = q0 |
| δ(q0, a) = q1 |
| δ(q1, ε) = q0 |
| δ(q1, a) = q1 |
```

In the above diagram, `Q` is the set of states, `a` is the input symbol, and `δ` is the transition function.

**Properties of EFA:**

- **Epsilon-Transitions:** An EFA can move to an empty string.
- **Finiteness:** An EFA has a finite number of states.
- **Recognition:** An EFA recognizes a language if there is a path from the initial state to an accepting state.

**Examples:**

- Recognize the language {a^n b^n | n ≥ 0}
- Recognize the language {a^n b^n | n ≥ 0, a ≠ b}

**Case Study:**

Suppose we want to recognize the language {a^n b^n | n ≥ 0} using an EFA. We can design an EFA as follows:

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | ε     | q0         |
| q0    | a     | q1         |
| q0    | b     | q0         |
| q1    | a     | q1         |
| q1    | b     | q0         |

In this EFA, the initial state is `q0`, and the accepting states are `q1`.

### Application: Text Search

Finite automata can be used to recognize patterns in strings. In text search, finite automata can be used to find all occurrences of a pattern in a text.

**Algorithm:**

1.  Create a DFA for the pattern.
2.  Create a DFA for the text.
3.  Find all paths from the initial state of the text DFA to the accepting states of the pattern DFA.

**Example:**

Suppose we want to find all occurrences of the pattern "ab" in the text "ababab".

| State | Input | Next State |
| ----- | ----- | ---------- |
| q0    | a     | q1         |
| q0    | b     | q2         |
| q1    | a     | q1         |
| q1    | b     | q2         |
| q2    | a     | q0         |
| q2    | b     | q2         |

We can create a DFA for the pattern "ab" and a DFA for the text "ababab". Then, we can find all paths from the initial state of the text DFA to the accepting states of the pattern DFA.

### Historical Context

Finite automata were first introduced by Alan Turing in his 1936 paper "On Computable Numbers". Turing's paper proposed the idea of a machine that could simulate any algorithm. Finite automata were later developed by Stephen Kleene and Marshall Stone, who introduced the concept of nondeterministic finite automata.

### Modern Developments

Finite automata are widely used in many areas, including:

- **Text search:** Finite automata can be used to find all occurrences of a pattern in a text.
- **Regular expressions:** Finite automata can be used to recognize patterns in strings using regular expressions.
- **Compilers:** Finite automata can be used to recognize the syntax of programming languages.
- **Natural language processing:** Finite automata can be used to recognize patterns in natural language.

**Further Reading:**

- "Introduction to Automata Theory, Languages, and Computation" by Michael Sipser
- "Automata Theory and Its Applications" by David Harel and Michael N. Vazirani
- "Regular Expressions: A Pattern Language" by J. E. Hopcroft and Jeffrey D. Ullman
- "Text Search using Finite Automata" by J. R. Sack and G. M. Voelker
