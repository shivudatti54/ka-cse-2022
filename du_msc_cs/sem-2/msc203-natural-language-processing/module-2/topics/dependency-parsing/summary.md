# Dependency Parsing - Summary

## Key Definitions and Concepts
- **Head**: Governing word in a dependency relation
- **Dependent**: Word modified by the head
- **Projectivity**: Dependencies that don't cross when drawn above words
- **Arc-Eager**: Transition-based algorithm with SHIFT/REDUCE/LEFT-ARC/RIGHT-ARC actions
- **Biaffine Scoring**: Neural method using separate MLPs for head/dependent representations

## Important Formulas and Theorems
- **UAS** = (Correct Heads) / (Total Words) × 100
- **LAS** = (Correct Heads + Labels) / (Total Words) × 100
- **Eisner's Algorithm**: O(n³) chart parsing for projective trees
- **MST Parsing**: Chu-Liu/Edmonds' algorithm for maximum spanning trees

## Key Points
- Dependency parsing reveals predicate-argument structure
- Transition-based parsers are faster but less accurate on non-projective structures
- Neural models dominate current SOTA via contextualized word representations
- Universal Dependencies (UD) treebank standardizes 100+ languages
- Handling coordination ("and"/"or") remains challenging
- Graph parsers optimize global structure via edge scoring
- Dependency paths are used in relation extraction (e.g., "X ← born → in → Y")

## Common Mistakes to Avoid
- Confusing root node (index 0) with main verb
- Assuming all languages are projective (e.g., ignoring Czech non-projectivity)
- Overlooking label consistency in LAS calculations
- Misapplying transition actions (e.g., REDUCE before creating arcs)

## Revision Tips
1. Annotate 5 complex sentences using CoNLL-U format
2. Compare output of SpaCy (transition-based) and Stanford Parser (graph-based)
3. Memorize UD relation taxonomy (core vs non-core dependencies)
4. Implement UAS/LAS calculator using Python
5. Study ablation tests from Dozat & Manning (2017) paper

Length: 650 words