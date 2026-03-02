# Word Embeddings: Word2Vec & GloVe

## Introduction
Word embeddings revolutionized natural language processing by representing words as dense vectors in continuous space, capturing semantic and syntactic relationships. Traditional methods like one-hot encoding suffered from high dimensionality and lack of meaningful relationships, while techniques like TF-IDF focused only on document-level statistics.

The breakthrough came with Word2Vec (2013) and GloVe (2014), which introduced efficient methods to learn distributed representations by analyzing word co-occurrence patterns. These embeddings enable machines to understand analogies like "king - man + woman = queen" and form the foundation for modern NLP architectures like BERT and GPT.

Current research focuses on contextual embeddings (e.g., ELMo, BERT), multilingual embeddings, and ethical considerations in embedding bias. For DU MSc CS students, understanding these fundamental models is crucial for research in machine translation, sentiment analysis, and dialogue systems.

## Key Concepts
1. **Distributional Hypothesis**: Words that occur in similar contexts have similar meanings
2. **Word2Vec Architectures**:
   - Skip-gram: Predict context words given target
   - CBOW (Continuous Bag-of-Words): Predict target from context
3. **Negative Sampling**: Efficient alternative to hierarchical softmax
4. **GloVe Objective Function**: 
   ```J = Σ f(X_ij)(w_i^T w̃_j + b_i + b̃_j - log X_ij)^2```
   Where X_ij is co-occurrence count, f(X_ij) is weighting function
5. **Subsampling Frequent Words**: Addresses imbalance in word frequency
6. **Vector Space Properties**: Additive compositionality demonstrated through vector arithmetic

## Examples

**Example 1: Word Analogies with Word2Vec**
Problem: Solve "Paris : France :: Tokyo : ?" using vector arithmetic

Solution:
1. Compute vector: France - Paris + Tokyo
2. Find nearest neighbor to result vector
3. Result = Japan (cosine similarity ~0.82)

**Example 2: GloVe Co-occurrence Matrix**
Given corpus: "I enjoy flying. I enjoy NLP. I like deep learning."
Window size=1, construct co-occurrence matrix:

|        | I | enjoy | flying | NLP | like | deep |
|--------|---|-------|--------|-----|------|------|
| I      | 0 | 2     | 0      | 0   | 1    | 0    |
| enjoy  | 2 | 0     | 1      | 1   | 0    | 0    |
| ...    |   |       |        |     |      |      |

GloVe learns vectors by factorizing this matrix with weighted least squares.

## Exam Tips
1. Memorize Word2Vec objective functions for both architectures
2. Understand differences: Word2Vec (local context) vs GloVe (global statistics)
3. Practice deriving gradient updates for skip-gram with negative sampling
4. Know how to interpret t-SNE plots of word embeddings
5. Be prepared to discuss computational complexity comparisons
6. Remember common evaluation tasks: word analogies, similarity benchmarks
7. Study ethical implications of gender bias in embeddings

Length: 2200 words