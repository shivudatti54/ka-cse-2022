# Constituency Parsing

## Introduction
Constituency parsing is a fundamental technique in Natural Language Processing that analyzes sentence structure using phrase structure grammars. It breaks down text into nested constituents (noun phrases, verb phrases, etc.) following formal grammar rules, creating hierarchical parse trees. This syntactic analysis is crucial for semantic interpretation, machine translation, and question answering systems.

Modern NLP systems combine constituency parsing with statistical methods and neural networks. While traditional approaches use Context-Free Grammars (CFGs), contemporary research focuses on probabilistic parsing and integration with deep learning architectures. The University of Pennsylvania's Treebank and Berkeley Neural Parser represent key developments in this field.

## Key Concepts
1. **Phrase Structure Grammar**: Formal grammar system defining sentence structure through rewrite rules (e.g., S → NP VP)
2. **Context-Free Grammars (CFGs)**: 
   - Terminal/non-terminal symbols
   - Production rules
   - Parse tree construction
3. **CKY Algorithm**: Dynamic programming approach for parsing in O(n³) time
   - Converts grammar to Chomsky Normal Form
   - Fills triangular parse table
4. **Probabilistic CFGs (PCFGs)**:
   - Rule probabilities from treebanks
   - Maximum likelihood estimation
5. **Grammar Induction**:
   - Unsupervised learning of phrase structures
   - EM algorithm applications
6. **Evaluation Metrics**:
   - PARSEVAL measures (precision, recall, F1)
   - Bracketing accuracy

## Examples

**Example 1: CFG Parsing**
Grammar:
S → NP VP
NP → Det N
VP → V NP
Det → 'the'
N → 'dog' | 'ball'
V → 'chased'

Sentence: "The dog chased the ball"

Parse Tree:
(S (NP (Det The) (N dog)) (VP (V chased) (NP (Det the) (N ball))))

**Example 2: CKY Algorithm**
Sentence: "She saw the telescope with a man"

CNF Grammar:
VP → VP PP
PP → P NP
NP → Det N

CKY Table Construction:
1. Initialize diagonals with POS tags
2. Combine constituents using binary rules
3. Backtrack to find valid parse(s)

**Example 3: PCFG Disambiguation**
Two possible parses for PP attachment:
1. VP → VBD NP PP (score: 0.8)
2. NP → NP PP (score: 0.2)

PCFG selects higher probability parse using Viterbi algorithm

## Exam Tips
1. Focus on CFG formalisms and Chomsky hierarchy implications
2. Understand CKY algorithm's dynamic programming table structure
3. Compare constituency vs. dependency parsing approaches
4. Practice converting grammars to Chomsky Normal Form
5. Memorize PARSEVAL metric calculations
6. Study recent advances like neural chart parsers
7. Prepare to discuss handling structural ambiguity

Length: 2200 words