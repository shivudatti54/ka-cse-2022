# Context Free Transformational Grammars
## BSc (Hons) Computer Science — Artificial Intelligence (NEP 2024 UGCF, Delhi University)

### Introduction

Context-Free Transformational Grammars (CFTG) represent a foundational concept in Artificial Intelligence, particularly in Natural Language Processing (NLP). Combining **Context-Free Grammars (CFG)** with **Transformational Grammar** theory (proposed by Noam Chomsky), this formalism enables the representation and transformation of syntactic structures in natural and programming languages.

---

### Key Concepts

**1. Context-Free Grammar (CFG)**
- Formal grammar with four components: Terminal symbols (T), Non-terminal symbols (N), Production rules (P), and Start symbol (S)
- Production form: **A → α** (where A ∈ N, α ∈ (N ∪ T)*)
- Named "context-free" because the left-hand side is replaced regardless of surrounding context
- Used to generate and parse sentences in formal languages

**2. Backus-Naur Form (BNF)**
- Standard notation for expressing CFGs
- Uses `< >` for non-terminals and `::=` for production
- Essential for defining programming language syntax

**3. Derivations**
- **Leftmost Derivation**: Expanding leftmost non-terminal at each step
- **Rightmost Derivation**: Expanding rightmost non-terminal at each step
- Derivation tree (Parse Tree): Hierarchical representation of sentence structure

**4. Ambiguity**
- A grammar is **ambiguous** if a sentence has multiple parse trees
- Problematic for NLP; requires disambiguation techniques

**5. Transformational Grammar**
- Chomsky's theory introducing **deep structure** and **surface structure**
- Transformational rules convert one structure to another
- Forms basis for syntax analysis in AI

**6. Context-Free Transformational Grammar (CFTG)**
- Extends CFG with transformational rules
- Enables generation of complex sentences through transformations
- Used for: Parsing, sentence generation, machine translation, semantic analysis

**7. Applications in AI**
- Natural Language Understanding (NLU)
- Programming language compilers
- Machine translation systems
- Speech recognition
- Text summarization and generation

**8. Limitations**
- Cannot handle context-sensitive phenomena
- Ambiguity issues in natural language
- Limited semantic representation

---

### Conclusion

Context-Free Transformational Grammars provide a mathematical framework for analyzing and generating linguistic structures. For AI practitioners, understanding CFTG is essential for building NLP systems, though modern approaches (like Transformers and neural networks) have supplemented traditional grammatical methods for complex language tasks. This topic forms a critical part of the Delhi University AI syllabus under NEP 2024 UGCF.

---

*Quick Revision Tip: Remember CFG components (T, N, P, S) and the difference between derivations and parse trees.*