# Module 5: Computational Linguistics

## Introduction

Computational Linguistics (CL) is the scientific field concerned with the computational modeling of human language. It sits at the intersection of computer science, artificial intelligence, and linguistics. For NLP engineers, it provides the foundational theories and formalisms needed to design algorithms that can understand, interpret, and generate human language. While NLP is often focused on building practical applications, Computational Linguistics provides the rigorous linguistic underpinnings that make those applications possible.

## Core Concepts

### 1. Syntax and Parsing

Syntax is the study of the grammatical structure of sentences. Computational Linguistics formalizes these rules to enable syntactic parsing.

*   **Context-Free Grammars (CFGs):** A fundamental formalism for describing the structure of sentences. A CFG consists of a set of rules (productions) that define how symbols can be rewritten.
    *   Example: A simple CFG rule: `S -> NP VP` (A Sentence can be a Noun Phrase followed by a Verb Phrase).
*   **Parsing:** The process of analyzing a string of symbols (a sentence) according to the rules of a formal grammar. It results in a parse tree that represents the syntactic structure.
    *   **Example Sentence:** "The student solved the problem."
    *   **Parse Tree:** The tree would break this down into constituents: [S [NP [Det The] [N student]] [VP [V solved] [NP [Det the] [N problem]]]].

### 2. Semantics

Semantics deals with meaning. Computational semantics is concerned with how to represent and derive the meaning of linguistic expressions.

*   **Lexical Semantics:** The meaning of individual words.
*   **Compositional Semantics:** How the meanings of words combine to form the meaning of phrases and sentences. The principle of compositionality states that the meaning of a complex expression is determined by the meanings of its constituent parts and the rules used to combine them.
*   **Meaning Representation:** Common formalisms include:
    *   **First-Order Logic (FOL):** Represents meaning as logical predicates.
        *   Example: "John loves Mary" becomes `loves(John, Mary)`.
    *   **Semantic Role Labeling (SRL):** Identifies the thematic roles (Agent, Patient, Instrument, etc.) that arguments play with respect to a predicate.
        *   Example: In "The student solved the problem with Python," "student" is the **Agent**, "problem" is the **Patient**, and "Python" is the **Instrument**.

### 3. Ambiguity

Ambiguity is a central challenge in CL. A single utterance can have multiple valid interpretations.

*   **Lexical Ambiguity:** A word has multiple meanings.
    *   Example: "bank" can mean a financial institution or the side of a river.
*   **Syntactic Ambiguity:** A sentence has multiple parse trees.
    *   Example: "I saw the man with the telescope." Did I use the telescope to see him, or did I see a man who was holding a telescope?
*   **Semantic Ambiguity:** A sentence can be interpreted with different meanings even with a clear syntax.
    *   Example: "The chicken is ready to eat." Is the chicken going to eat, or is it going to be eaten?

Resolving ambiguity is a key task, often handled using statistical models and contextual clues.

### 4. Corpus Linguistics

A corpus (plural: corpora) is a large and structured collection of machine-readable texts. Corpora are essential for building and evaluating statistical NLP models.

*   **Uses:** Training language models, part-of-speech taggers, parsers; studying word usage frequencies (e.g., "likely" vs. "probably"); and creating dictionaries.
*   **Example:** The **Penn Treebank** is a famous corpus where each sentence is annotated with its parse tree, providing crucial data for training parsers.

### 5. Language Modeling

A Language Model (LM) assigns a probability to a sequence of words. It is a core component of speech recognition, machine translation, and auto-complete systems. Modern neural LMs (e.g., BERT, GPT) are built upon these foundational probabilistic concepts.

## Key Points & Summary

*   **Foundation for NLP:** Computational Linguistics provides the formal linguistic and statistical foundations necessary for building effective NLP systems.
*   **Levels of Analysis:** It operates at multiple levels: syntactic (structure), semantic (meaning), and pragmatic (context).
*   **Core Formalisms:** Key formalisms include Context-Free Grammars for syntax and First-Order Logic for semantics.
*   **Central Challenge:** Ambiguity is a fundamental problem at all levels of language processing that systems must learn to resolve.
*   **Data-Driven Approach:** Modern CL heavily relies on large annotated corpora and statistical/machine learning methods to learn language patterns.
*   **Bridge Discipline:** It acts as the crucial bridge between theoretical linguistics and applied natural language processing.