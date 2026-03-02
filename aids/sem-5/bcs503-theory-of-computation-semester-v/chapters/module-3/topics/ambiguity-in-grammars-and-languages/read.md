# Ambiguity in Grammars and Languages
## Introduction
Ambiguity in grammars and languages is a fundamental concept in the field of computer science, particularly in the context of context-free grammars and pushdown automata. In this chapter, we will delve into the concept of ambiguity, its types, and its implications on the design and analysis of grammars and languages.

## What is Ambiguity?
Ambiguity in a grammar refers to the situation where a single string can be parsed in more than one way, resulting in multiple parse trees. This can lead to confusion and inconsistencies in the interpretation of the language.

### Types of Ambiguity
There are two types of ambiguity:

* **Inherent Ambiguity**: This occurs when a language is inherently ambiguous, meaning that it is impossible to design an unambiguous grammar for the language.
* **Grammar Ambiguity**: This occurs when a particular grammar is ambiguous, but the language itself is not inherently ambiguous.

## Causes of Ambiguity
Ambiguity can arise from several sources, including:

* **Common Prefixes**: When two or more productions have a common prefix, it can lead to ambiguity.
* **Common Suffixes**: Similarly, when two or more productions have a common suffix, it can lead to ambiguity.
* **Left Recursion**: Left recursion can also lead to ambiguity, as it can create multiple parse trees for the same string.

## Examples
Consider the following grammar:
```
E -> E + E
E -> E * E
E -> id
```
This grammar is ambiguous because the string `id + id * id` can be parsed in two different ways:

```
E -> E + E
  -> id + E
  -> id + id * id

E -> E * E
  -> E + id
  -> id + id * id
```
## Resolving Ambiguity
There are several techniques to resolve ambiguity in grammars, including:

* **Left Factoring**: This involves factoring out the common prefix from two or more productions.
* **Right Factoring**: This involves factoring out the common suffix from two or more productions.
* **Eliminating Left Recursion**: This involves transforming the grammar to eliminate left recursion.

## Comparison of Ambiguity Resolution Techniques
| Technique | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Left Factoring | Factors out common prefix | Easy to apply | May not always resolve ambiguity |
| Right Factoring | Factors out common suffix | Easy to apply | May not always resolve ambiguity |
| Eliminating Left Recursion | Transforms grammar to eliminate left recursion | Always resolves ambiguity | Can be complex to apply |

## Exam Tips
* Make sure to understand the concept of ambiguity and its types.
* Practice resolving ambiguity using left factoring, right factoring, and eliminating left recursion.
* Be able to identify the causes of ambiguity and explain how to resolve them.