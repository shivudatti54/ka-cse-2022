# **Theory of Computation**

**Section 5.1: Introduction to Formal Language**

### Overview

In this section, we introduce the concept of formal languages, which are used to describe the set of strings that a Turing machine can accept as input. Formal languages are essential in the theory of computation, as they provide a formal framework for describing the properties of a Turing machine's behavior.

### Definition of Formal Language

A formal language is a set of strings over an alphabet, where each string is called a word. A formal language is defined as follows:

- **Alphabet**: A set of symbols, denoted by Σ.
- **Word**: A string of symbols over the alphabet, denoted by s.
- **Formal Language**: A set of words, denoted by L.

For example, let Σ = {0, 1} be the alphabet, and let L = {0, 01, 1001} be a formal language.

### Properties of Formal Language

Formal languages have several important properties:

- **Closure**: A formal language is closed under a particular operation, such as union, intersection, or concatenation.
- **Decidability**: A formal language is decidable if there exists an algorithm that can determine whether a given word is in the language or not.
- **Regularity**: A formal language is regular if it can be described by a regular expression.

### Regular Expressions

Regular expressions are a way to describe formal languages using a formal grammar. A regular expression is a string of symbols that describes a pattern of words. For example, the regular expression `0*1*` describes the formal language L = {0, 01, 1001}, where `*` denotes any number of consecutive symbols.

### Types of Regular Expressions

There are two types of regular expressions:

- **Deterministic regular expressions**: These are regular expressions that describe a formal language by specifying a set of possible words.
- **Nondeterministic regular expressions**: These are regular expressions that describe a formal language by specifying a set of possible strings.

### Conversion to Regular Expressions

There are several algorithms for converting a formal language to a regular expression, including:

- **Kleene's theorem**: This states that a formal language is regular if and only if it can be described by a regular expression.
- **Thue-Muller algorithm**: This is a method for converting a formal language to a regular expression.

### Key Concepts

- **Alphabet**: A set of symbols used to describe a formal language.
- **Word**: A string of symbols over the alphabet.
- **Formal Language**: A set of words over an alphabet.
- **Regular Expression**: A string of symbols that describes a pattern of words.
- **Deterministic Regular Expression**: A regular expression that describes a formal language by specifying a set of possible words.
- **Nondeterministic Regular Expression**: A regular expression that describes a formal language by specifying a set of possible strings.

### Examples

- **Example 1**: Convert the formal language L = {0, 01, 1001} to a regular expression.
- **Answer**: The regular expression `0*1*` describes the formal language L = {0, 01, 1001}.
- **Example 2**: Determine whether the formal language L = {0, 1, 10} is regular or not.
- **Answer**: The formal language L = {0, 1, 10} is not regular, as it cannot be described by a regular expression.

### Practice Problems

1. Convert the formal language L = {0, 01, 1001} to a regular expression.
2. Determine whether the formal language L = {0, 1, 10} is regular or not.
3. Convert the formal language L = {0, 1, 11} to a regular expression.
