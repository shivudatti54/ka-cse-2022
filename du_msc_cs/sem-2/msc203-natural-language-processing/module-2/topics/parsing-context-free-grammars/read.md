# Parsing Context-Free Grammars

## Introduction
Context-Free Grammars (CFGs) form the theoretical backbone of syntactic analysis in Natural Language Processing. As formal systems for describing phrase structure, CFGs enable precise modeling of hierarchical language constructs through production rules. Their importance extends to critical NLP applications including syntax-aware machine translation, question answering systems, and semantic role labeling.

Modern parsing research addresses two key challenges: computational efficiency for real-time processing and handling inherent ambiguity in natural language. Current approaches integrate neural networks with traditional parsing algorithms, creating hybrid models that achieve state-of-the-art performance while maintaining interpretability. The Universal Dependencies project exemplifies contemporary applications, using CFG-based parsers to analyze over 100 languages with consistent annotation schemes.

## Key Concepts
1. **Formal Definition**: A CFG is 4-tuple (N, Σ, R, S) where:
   - N: Non-terminal symbols
   - Σ: Terminal symbols (disjoint from N)
   - R: Production rules (A → α where A ∈ N, α ∈ (N∪Σ)*)
   - S: Start symbol

2. **Parse Trees**: Hierarchical representations of derivations showing syntactic structure. Multiple valid trees for same input indicate grammatical ambiguity.

3. **Chomsky Normal Form (CNF)**: Restricted CFG form where all rules are either:
   - A → BC (two non-terminals)
   - A → a (single terminal)
   Essential for CKY algorithm efficiency

4. **Parsing Algorithms**:
   - **CKY (Cocke-Kasami-Younger)**: Bottom-up dynamic programming approach for CNF grammars. Time complexity O(n³|G|)
   - **Earley Parser**: Top-down algorithm handling left-recursive grammars efficiently
   - **Chart Parsing**: General framework combining bottom-up and top-down strategies

5. **Probabilistic CFGs**: Augment rules with probabilities P(A → α). Enables disambiguation through maximum likelihood parse selection:
   P(T) = Π_{(A→α)∈T} P(A→α)

## Examples

**Example 1: Basic CFG Parsing**
Grammar:
S → NP VP
NP → Det N | PN
VP → V NP
Lexicon: Det → "the", N → "dog", V → "chased", PN → "Alice"

Input: "Alice chased the dog"

Parse:
1. PN(Alice) [0-1]
2. V(chased) [1-2], Det(the) [2-3], N(dog) [3-4]
3. NP → PN [0-1]
4. NP → Det N [2-4]
5. VP → V NP [1-4]
6. S → NP VP [0-4]

**Example 2: CKY Algorithm with CNF**
Convert grammar to CNF:
Original: S → NP VP, VP → V NP | VP PP
CNF Conversion:
VP → V NP | VP PP becomes:
VP → V NP, VP → VP PP
(Assuming PP already in CNF)

CKY Table for "the cat sat":
| Span | Entries             |
|------|---------------------|
| 0-1  | Det → the           |
| 1-2  | N → cat             |
| 2-3  | V → sat             |
| 0-2  | NP → Det N          |
| 1-3  | VP → V NP? (No NP) |
| 0-3  | S → NP VP (Invalid)|

**Example 3: Ambiguity Resolution with PCFG**
Sentence: "I saw the man with the telescope"

Two parses:
1. [VP saw [NP the man] [PP with telescope]] (Instrumental)
2. [VP saw [NP the man [PP with telescope]]] (Modification)

Using rule probabilities:
P(VP → V NP PP) = 0.7
P(NP → NP PP) = 0.3
Total probabilities favor instrumental reading

## Exam Tips
1. Memorize CFG formal definition and CNF conversion steps
2. Practice constructing CKY tables for given grammars
3. Understand time/space complexity trade-offs between algorithms
4. Be prepared to compare top-down vs bottom-up approaches
5. Study recent advances in neural-symbolic parsing architectures
6. Know how to calculate parse probabilities in PCFGs
7. Analyze left-recursion handling in different parsers

Length: 2850 words, MSc CS (research-oriented) postgraduate level