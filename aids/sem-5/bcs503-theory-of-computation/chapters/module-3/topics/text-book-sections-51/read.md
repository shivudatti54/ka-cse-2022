# **Theory of Computation**

## **Module: 10 Hours**

## **Topic: TEXT BOOK: Sections 5.1**

## **Introduction**

In this module, we will explore the basics of the Theory of Computation, which is the foundation of computer science. Specifically, we will delve into the concept of Formal Languages, which are sets of strings that are accepted by a given algorithm.

## **Formal Languages**

A Formal Language is a set of strings that is defined by a set of production rules. These production rules are used to generate all possible strings in the language.

### Definition

A Formal Language L is defined as a set of strings S over an alphabet Σ such that:

- L is non-empty
- L is closed under the operation of taking substrings
- L is closed under the operation of concatenation

### Examples

- {a, b, aa}
- {a, b, ab, ba}
- {a^n | n ∈ N}

## **Types of Formal Languages**

There are several types of Formal Languages, including:

- **Regular Languages**: These are languages that can be recognized by a finite automaton.
- **Context-Free Languages**: These are languages that can be recognized by a pushdown automaton.
- **Recursively Enumerable Languages**: These are languages that can be recognized by a Turing machine.
- **Undecidable Languages**: These are languages that cannot be recognized by any algorithm.

### Regular Languages

Regular Languages are the simplest type of Formal Language. They can be recognized by a finite automaton.

### Definition

A Regular Language L is defined as a set of strings S over an alphabet Σ such that:

- L is non-empty
- L is closed under the operation of taking substrings
- L is closed under the operation of concatenation
- L can be recognized by a finite automaton

### Example

- L = {a^n | n ∈ N}

### Regular Expression

Regular Expressions are used to describe Regular Languages. They are a way of specifying a language using a set of rules.

### Example

- L = {a^n | n ∈ N} can be described by the regular expression "a*", where "*" represents zero or more occurrences of "a".

## **Key Concepts**

- Formal Language
- Production Rules
- Finite Automaton
- Regular Language
- Context-Free Language
- Pushdown Automaton
- Recursively Enumerable Language
- Turing Machine
- Undecidable Language
- Regular Expression

## **Practice Problems**

1.  Write a Regular Expression to describe the language {a^n | n ∈ N}.
2.  Write a Formal Language that can be recognized by a pushdown automaton.
3.  Classify the following language as Regular, Context-Free, or Undecidable: {a, b, ab, ba}
