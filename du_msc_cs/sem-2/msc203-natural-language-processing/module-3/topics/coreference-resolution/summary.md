# Coreference Resolution - Summary

## Key Definitions and Concepts
- **Coreference**: Multiple expressions referring to same entity
- **Mention**: Text span that refers to an entity (e.g., "she", "the research team")
- **Cluster**: Group of coreferent mentions
- **Antecedent**: Earlier mention that subsequent expressions refer to

## Important Formulas and Theorems
- **MUC Score**: |Links System| / |Links Gold|
- **B³ Precision**: Σ [|S ∩ G|² / |S|] / N
- **CEAF-φ4**: Entity-based alignment using Kuhn-Munkres algorithm
- **Hobbs Algorithm**: Tree-search method for pronoun resolution

## Key Points
- Coreference chains maintain discourse coherence
- Neural models outperform rule-based systems but require large training data
- Cross-lingual coreference remains challenging due to pronoun drop languages
- Recent work uses attention mechanisms for mention ranking
- Winograd schemas test commonsense reasoning in coreference
- Coreference impacts performance in QA and summarization tasks
- Zero-shot approaches reduce annotation costs

## Common Mistakes to Avoid
- Confusing coreference with mere co-occurrence
- Ignoring world knowledge requirements
- Overlooking split antecedents ("John and Mary argued. *They* left.")
- Assuming all pronouns have explicit antecedents
- Misapplying metrics (e.g., using MUC for singleton mentions)

## Revision Tips
1. Create coreference chains for news articles
2. Implement B³ metric from scratch in Python
3. Study ablation studies in Lee et al. (2017) end-to-end paper
4. Practice resolving cataphoric references in literary texts
5. Explore OntoNotes 5.0 corpus annotation guidelines