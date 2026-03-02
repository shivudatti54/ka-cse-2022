# Parsing Context-Free Grammars - Summary

## Key Definitions and Concepts
- **CFG**: 4-tuple (Non-terminals, Terminals, Production Rules, Start Symbol)
- **Parse Tree**: Hierarchical derivation structure showing syntactic relationships
- **CNF**: Grammar form allowing only A→BC or A→a rules
- **CKY Algorithm**: Dynamic programming parser for CNF grammars
- **Earley Parser**: Top-down parser efficient for left-recursive grammars

## Important Formulas and Theorems
- **CKY Recurrence**: 
  table[i,j] = ∪_{i<k<j} (table[i,k] × table[k,j])
- **PCFG Probability**:
  P(T) = ∏_{r∈T} P(r)
- **CNF Conversion**:
  A → BCD becomes A → BE, E → CD

## Key Points
- CFGs model phrase structure through recursive rewriting rules
- Parsing complexity ranges from O(n³) to O(n) based on grammar restrictions
- Ambiguity resolution requires probabilistic or semantic methods
- Neural parsers use CFGs as structural constraints in end-to-end models
- Modern research focuses on handling non-projectivity in dependency parsing
- Multilingual parsing requires language-universal grammar designs
- Memory-efficient parsing crucial for real-time NLP applications

## Common Mistakes to Avoid
- Forgetting CNF conversion steps before applying CKY
- Confusing chart parsing with pure bottom-up/top-down approaches
- Mishandling left recursion in recursive descent parsers
- Ignoring ε-rules in grammar normalization

## Revision Tips
1. Practice CNF conversions with complex production rules
2. Implement CKY algorithm from scratch in Python
3. Compare parse outputs of different algorithms on ambiguous sentences
4. Review recent ACL papers on neural CFG parsing hybrids

Length: 650 words