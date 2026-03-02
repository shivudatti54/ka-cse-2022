# **Top-Down Parsing: Recursive Descent Parsing, First and Follow, LL(1) Grammars Bottom Up Parsing: Reductions, Handle Pruning, Shift Reduce Parsing Chap**

## **Table of Contents**

1. [Introduction to Top-Down Parsing](#introduction-to-top-down-parsing)
2. [Recursive Descent Parsing](#recursive-descent-parsing)
   - [Definition](#definition)
   - [How it Works](#how-it-works)
   - [Example](#example)
3. [First and Follow Sets](#first-and-follow-sets)
   - [Definition](#definition)
   - [Calculating First and Follow Sets](#calculating-first-and-follow-sets)
   - [Example](#example)
4. [LL(1) Grammars](#ll-1-grammars)
   - [Definition](#definition)
   - [Characteristics](#characteristics)
   - [Example](#example)
5. [Bottom-Up Parsing](#bottom-up-parsing)
   - [Reductions](#reductions)
   - [Handle Pruning](#handle-pruning)
   - [Shift Reduce Parsing](#shift-reduce-parsing)

## **Introduction to Top-Down Parsing**

Top-Down Parsing is a parsing technique used to analyze the structure of a programming language. It works by starting with the overall structure of the program and breaking it down into smaller components. This approach is in contrast to Bottom-Up Parsing, which starts with the individual components and builds up to the overall structure.

## **Recursive Descent Parsing**

### Definition

Recursive Descent Parsing is a top-down parsing technique that uses a set of production rules to parse the structure of a programming language. It is called "recursive descent" because the parser uses recursive functions to parse the language.

### How it Works

The parser starts with the overall structure of the program and uses a set of production rules to break it down into smaller components. Each production rule is used to parse a specific component of the program, and the process is repeated until the entire program has been parsed.

### Example

Consider the following example of a recursive descent parser for the language `E -> E + T | T`, where `E` represents the expression and `T` represents the term.

```
E -> E + T | T
E -> (
    E
    )
T -> T * F | F
F -> ( E ) | id
```

In this example, the parser starts with the overall structure of the program and uses the production rule `E -> E + T | T` to break it down into smaller components. It then uses the production rule `T -> T * F | F` to parse the term, and finally uses the production rule `F -> ( E ) | id` to parse the factor.

## **First and Follow Sets**

### Definition

The first and follow sets are used to keep track of the sets of symbols that appear before and after a non-terminal symbol during the parsing process.

### Calculating First and Follow Sets

The first set of a non-terminal symbol `A` is the set of symbols that appear before `A` during the parsing process. The follow set of `A` is the set of symbols that appear after `A` during the parsing process.

### Example

Consider the following example of a first and follow set for the non-terminal symbol `A` in the language `A -> aB | b`.

```
A -> aB | b
B -> aC | c
C -> a | b
```

The first set of `A` is `{a}`, and the follow set of `A` is `{B}`.

## **LL(1) Grammars**

### Definition

An LL(1) grammar is a grammar that can be parsed using a top-down parser that uses a single token at a time. LL(1) grammars are also known as "unambiguous" grammars because they can be parsed unambiguously using a top-down parser.

### Characteristics

LL(1) grammars have the following characteristics:

- They can be parsed using a top-down parser that uses a single token at a time.
- They are unambiguous because they can be parsed unambiguously using a top-down parser.

### Example

Consider the following example of an LL(1) grammar for the language `E -> E + T | T`, where `E` represents the expression and `T` represents the term.

```
E -> E + T | T
T -> T * F | F
F -> ( E ) | id
```

This grammar is LL(1) because it can be parsed using a top-down parser that uses a single token at a time.

## **Bottom-Up Parsing**

### Reductions

In bottom-up parsing, the parser starts with the individual components of the program and builds up to the overall structure. The parser uses a set of reduction rules to reduce the components to smaller and smaller components until the entire program has been parsed.

### Handle Pruning

Handle pruning is a technique used in bottom-up parsing to reduce the number of reduction rules required to parse a program. Handle pruning involves removing the handles of reduction rules that do not contribute to the parsing process.

### Shift Reduce Parsing

---

Shift reduce parsing is a bottom-up parsing technique that uses a table to keep track of the parsing process. The table is used to determine which reduction rule to apply to reduce the components of the program.

In shift reduce parsing, the parser starts with the individual components of the program and builds up to the overall structure. The parser uses the table to determine which reduction rule to apply to reduce the components to smaller and smaller components until the entire program has been parsed.

## **Conclusion**

In this study material, we have covered the topics of top-down parsing, recursive descent parsing, first and follow sets, LL(1) grammars, bottom-up parsing, reductions, handle pruning, and shift reduce parsing. We have also included examples and explanations to help illustrate these concepts.
