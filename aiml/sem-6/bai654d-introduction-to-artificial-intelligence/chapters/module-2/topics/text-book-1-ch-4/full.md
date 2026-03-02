# Text Book 1: Ch 4

## Introduction to Artificial Intelligence

=====================================================

### Overview

Artificial Intelligence (AI) is a broad field that aims to create intelligent machines capable of performing tasks that typically require human intelligence. In this chapter, we will delve into the fundamental concepts of AI, focusing on knowledge representation issues and using predicate logic.

### Historical Context

The term "Artificial Intelligence" was first coined in 1956 by John McCarthy, a computer scientist and cognitive scientist, at the Dartmouth Summer Research Project on Artificial Intelligence. However, the concept of creating intelligent machines dates back to ancient Greece, where myths about automatons and robots were common.

In the early 20th century, pioneers like Alan Turing and Marvin Minsky laid the groundwork for modern AI research. Turing's 1950 paper "Computing Machinery and Intelligence" proposed the Turing Test, a measure of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.

### Knowledge Representation Issues

Knowledge representation is a crucial aspect of AI, as it enables machines to reason, learn, and make decisions based on the information they have acquired. The goal of knowledge representation is to encode knowledge in a way that allows machines to process, manipulate, and reason about it.

### Predicate Logic

Predicate logic is a formal system used to represent knowledge and reason about it. It consists of a set of predicates (functions that take arguments) and a set of axioms (statements that are assumed to be true without proof).

### Representing Knowledge using Predicate Logic

Predicate logic provides a formal framework for representing knowledge using logical statements. A predicate logic statement consists of a predicate, arguments, and a logical operator.

#### Example 1: Simple Predicate Logic Statement

Suppose we want to represent the statement "John likes reading" using predicate logic. We can define the predicate `likes` as follows:

```
likes(X, Y) :- author(X), enjoys(Y).
```

where `X` represents the person who likes, `Y` represents the book they like, `author(X)` represents the statement that `X` is an author, and `enjoys(Y)` represents the statement that `Y` is a book that `X` enjoys.

#### Example 2: Compound Predicate Logic Statement

Suppose we want to represent the statement "All books written by John are fiction" using predicate logic. We can define the predicate `writes` as follows:

```
writes(X, Y) :- author(X), writes(Y).
writes(X, Y) :- fiction(Y), author(X).
```

where `writes(X, Y)` represents the statement that `X` writes `Y`. The first clause states that `X` writes `Y` if `X` is an author and `Y` is a book written by `X`. The second clause states that `X` writes `Y` if `Y` is a fiction book and `X` is an author.

### Applications of Predicate Logic

Predicate logic has numerous applications in AI, including:

- Expert systems: Predicate logic can be used to represent knowledge and reason about it in expert systems, which mimic the decision-making process of a human expert.
- Natural Language Processing (NLP): Predicate logic can be used to represent the meaning of sentences and reason about them in NLP applications.
- Computer Vision: Predicate logic can be used to represent knowledge about images and reason about them in computer vision applications.

### Case Study: Rule-Based Expert System

Suppose we want to build an expert system that diagnoses diseases based on symptoms. We can use predicate logic to represent the knowledge of the doctor and reason about the diagnosis.

```
diagnose(X) :- symptom(X, F).
diagnose(X) :- symptom(X, T).
```

where `diagnose(X)` represents the statement that `X` is a disease, `symptom(X, F)` represents the statement that `X` is a disease characterized by fever, and `symptom(X, T)` represents the statement that `X` is a disease characterized by headache.

We can add more rules to reason about the diagnosis:

```
diagnose(Cancer) :- symptom(Cancer, F), !.
diagnose(Malaria) :- symptom(Malaria, T), !.
```

where `Cancer` and `Malaria` are diseases, and `!` represents the "fail" operator, which indicates that the rule is non-grounded.

### Further Reading

- "Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig
- "Knowledge Representation" by Edward Feigenbaum
- "Predicate Logic" by Patrick Suppes
- "Expert Systems: Principles and Practice" by Edward Feigenbaum and Joshua Lederberg

### Diagrams

#### Figure 1: Predicate Logic Statement

```
likes(X, Y) :- author(X), enjoys(Y)
```

This diagram represents a simple predicate logic statement that states "X likes Y" if X is an author and Y is a book that X enjoys.

#### Figure 2: Compound Predicate Logic Statement

```
writes(X, Y) :- author(X), writes(Y)
writes(X, Y) :- fiction(Y), author(X)
```

This diagram represents a compound predicate logic statement that states "X writes Y" if X is an author and Y is a book written by X, or if Y is a fiction book and X is an author.

Note: The diagrams are not included in this text-based format, but you can create them using graphing software or online tools.
