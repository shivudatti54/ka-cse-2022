# POS Tagging and Named Entity Recognition (NER)

## Introduction
Part-of-Speech (POS) tagging and Named Entity Recognition (NER) form the foundation of syntactic and semantic analysis in Natural Language Processing. POS tagging involves labeling words with their grammatical categories (nouns, verbs, etc.), while NER identifies and classifies proper nouns into predefined categories (persons, organizations, locations). These tasks are crucial for downstream NLP applications like machine translation, question answering, and information extraction.

In modern NLP pipelines, POS tagging helps resolve syntactic ambiguity ("book" as noun vs verb), while NER enables structured representation of unstructured text. The combination of statistical models and deep learning approaches has revolutionized these tasks, achieving human-level performance in many domains. Current research focuses on cross-lingual tagging, few-shot learning for rare entities, and integration with transformer architectures.

## Key Concepts
1. **POS Tagging Approaches**:
   - Rule-Based: Uses handcrafted linguistic rules (ENGTWOL tagger)
   - Stochastic: HMM-based taggers using Viterbi algorithm
   - Transformation-Based: Brill tagger with error-driven learning
   - Neural: BiLSTM-CRF architectures with word embeddings

2. **NER Techniques**:
   - Dictionary-Based: Gazetteer matching
   - Machine Learning: CRFs with feature engineering
   - Deep Learning: Transformer-based models (BERT) with token classification heads
   - Hybrid: Combining rule-based and statistical methods

3. **Ambiguity Resolution**:
   - Context window analysis
   - Morphological analyzers for unknown words
   - Domain adaptation techniques

4. **Evaluation Metrics**:
   - Accuracy (POS)
   - F1-score (NER)
   - CoNLL-2003 evaluation scheme

5. **Recent Advances**:
   - Cross-lingual transfer learning
   - Few-shot NER using meta-learning
   - Integration with knowledge graphs

## Examples

**Example 1: POS Tagging with HMM**
Problem: Tag the sentence "The bear books a flight" using HMM with given transition/emission probabilities.

Solution:
1. Define states (tags) and observations (words)
2. Calculate transition probabilities P(tag|prev_tag)
3. Calculate emission probabilities P(word|tag)
4. Apply Viterbi algorithm to find optimal path
5. Resolve ambiguity: "books" → VBZ (verb) in this context

**Example 2: NER with CRF**
Problem: Extract entities from "Apple Inc. plans to open a store in Delhi by 2025."

Solution:
1. Feature engineering: word shape, prefixes/suffixes, context words
2. Define label set: B-ORG, I-ORG, B-LOC, B-DATE
3. Train CRF model to maximize sequence probability
4. Predict: [Apple: B-ORG], [Delhi: B-LOC], [2025: B-DATE]

**Example 3: Transformer-based NER**
Problem: Fine-tune BERT for medical entity recognition using BC5CDR corpus.

Steps:
1. Add token classification head to BERT
2. Use BIO tagging scheme
3. Mask non-entity tokens during loss calculation
4. Apply dynamic padding and mixed precision training

## Exam Tips
1. Understand Viterbi algorithm's time complexity (O(N²T))
2. Contrast closed-class vs open-class words in POS tagging
3. Remember exact F1-score formula: 2*(P*R)/(P+R)
4. Analyze tradeoffs: Rule-based vs ML approaches for low-resource languages
5. Study transformer architectures' impact on NER (attention mechanisms)
6. Prepare for diagram questions: HMM trellis diagrams
7. Review latest SOTA models (RoBERTa, ELECTRA) for both tasks