# Semantic Role Labeling - Summary

## Key Definitions and Concepts
- **Predicate**: Verb/action at sentence core (e.g., "eat")
- **Arguments**: Entities involved (Agent, Patient, Instrument)
- **Adjuncts**: Optional modifiers (Time, Location)
- **PropBank**: Verb-specific role schemas
- **FrameNet**: Event-based role inventories

## Important Formulas and Theorems
- **F1 Score**: 2*(P*R)/(P+R) for argument classification
- **Viterbi Algorithm**: For CRF-based role sequence decoding
- **Attention Weights**: α_ij = softmax(q_i^T k_j/√d) in transformers
- **Cross-Entropy Loss**: L = -Σ y log(ŷ) for role classification

## Key Points
- SRL requires syntactic parsing as preprocessing
- Neural models outperform feature-based methods by 8-12% F1
- Multilingual BERT achieves 74% of monolingual performance in zero-shot
- Hindi SRL faces challenges with null subjects and case markers
- Current research integrates SRL with AMR parsing
- PropBank labels are verb-specific (Arg2 for "give" ≠ Arg2 for "see")
- Adjuncts account for 35% of labeling errors in benchmark tests

## Common Mistakes to Avoid
- Confusing locative arguments (ArgM-LOC) with directional adjuncts
- Ignoring light verb constructions (e.g., "take a walk")
- Overlooking implicit arguments in pro-drop languages
- Misapplying PropBank guidelines to FrameNet data

## Revision Tips
1. Annotate 10 sentences using both PropBank/FrameNet schemes
2. Implement a simple CRF model using sklearn-crfsuite
3. Study the CoNLL-2005 shared task evaluation script
4. Review ACL 2022/2023 papers on SRL+LLMs

Length: 650 words