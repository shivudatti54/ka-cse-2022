# Constituency Parsing - Summary

## Key Definitions and Concepts
- **Constituent**: Grammatical unit acting as single entity in syntax
- **Phrase Structure Tree**: Hierarchical representation of sentence structure
- **Chomsky Normal Form**: CFG restriction to binary productions
- **Treebank**: Annotated corpus of parse trees

## Important Formulas and Theorems
- **CKY Recurrence**: table[i,j] = ∪_{i<k<j} (table[i,k] × table[k,j])
- **PCFG Probability**: P(T) = Π_{r∈T} P(r)
- **PARSEVAL F1**: 2PR/(P+R) where P=correct constituents/total proposed

## Key Points
- Constituency parsing reveals hierarchical sentence structure
- CFGs provide formal framework but require lexicalization for ambiguity resolution
- Dynamic programming enables efficient exhaustive parsing
- Probabilistic methods handle real-world text ambiguity
- Neural parsers (e.g., RNNG) achieve state-of-the-art performance
- Cross-linguistic parsing requires language-specific grammars
- Syntax-semantics interface remains active research area

## Common Mistakes to Avoid
- Confusing terminal/non-terminal symbols in CFG design
- Missing Chomsky Normal Form conversion steps
- Ignoring lexical category ambiguity
- Misapplying probability multiplication in PCFGs
- Overlooking null elements in treebank annotations

## Revision Tips
1. Practice converting complex sentences to parse trees
2. Memorize CKY algorithm steps with example sentences
3. Review Penn Treebank annotation guidelines
4. Study ablation tests from recent ACL papers on neural parsing
5. Implement basic PCFG parser using NLTK/PyTorch

Length: 650 words