# Question Answering Systems - Summary

## Key Definitions and Concepts
- Open-domain QA: Answers arbitrary questions using diverse sources
- Reading Comprehension: Extracting answers from given context
- Multi-hop Reasoning: Combining information from multiple documents
- Dense Passage Retrieval: Vector-based document search

## Important Formulas and Theorems
- F1 Score: 2*(Precision*Recall)/(Precision+Recall)
- BLEU: Brevity penalty * exp(∑ wn log pn)
- Transformer Self-Attention: QK^T/√d
- BERT Objective: Masked LM + Next Sentence Prediction

## Key Points
- Modern QA combines neural networks with knowledge bases
- Retrieval-reader architectures dominate current systems
- Pretrained language models enable zero-shot QA
- Multi-modal QA (text+images) is emerging research area
- Evaluation requires both automatic metrics and human judgment
- Efficient deployment needs model distillation techniques
- Ethical QA requires bias mitigation and provenance tracking

## Common Mistakes to Avoid
- Confusing document retrieval with answer extraction phases
- Overlooking temperature scaling in generative models
- Ignoring context window limitations in transformer models
- Mishandling negations and ambiguous questions

## Revision Tips
1. Memorize SQuAD 2.0 evaluation protocol
2. Practice attention matrix visualization
3. Compare different reader architectures (BiDAF vs BERT)
4. Study error analysis from HotpotQA leaderboard
5. Implement simple QA pipeline using HuggingFace

Length: 600 words