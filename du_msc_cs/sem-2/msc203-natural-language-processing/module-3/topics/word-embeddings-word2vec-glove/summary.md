# Word Embeddings: Word2Vec & GloVe - Summary

## Key Definitions and Concepts
- **Word Embedding**: Dense vector representation capturing semantic meaning
- **Skip-gram**: Predict context words from target (inside-out)
- **CBOW**: Predict target word from context (outside-in)
- **GloVe**: Global Vectors combining matrix factorization with context window

## Important Formulas and Theorems
- Word2Vec Skip-gram Objective:
  ```J(θ) = -1/T Σ Σ log p(w_{t+j}|w_t)```
- Negative Sampling Approximation:
  ```log σ(v_{w_o}'^T v_{w_I}) + Σ_{i=1}^k 𝔼_{w_i∼P_n(w)}[log σ(-v_{w_i}'^T v_{w_I})]```
- GloVe Weighting Function:
  ```f(X_{ij}) = (X_{ij}/x_max)^α if X_{ij} < x_max else 1```

## Key Points
- Word2Vec uses local context windows, GloVe uses global co-occurrence statistics
- Subsampling improves training efficiency on frequent words
- Dimensionality (300d) balances computational cost and representational capacity
- Additive compositionality enables analogy reasoning
- Intrinsic evaluation: word similarity tasks, analogy solving
- Extrinsic evaluation: downstream NLP task performance
- Popular implementations: Gensim (Word2Vec), spaCy (GloVe)

## Common Mistakes to Avoid
- Confusing skip-gram with CBOW architecture
- Ignoring the impact of hyperparameters (window size, negative samples)
- Assuming embeddings capture all linguistic aspects (e.g., polysemy)
- Overlooking the need for proper text preprocessing

## Revision Tips
1. Practice deriving gradient updates for both models
2. Use visualization tools (t-SNE, PCA) on real embedding data
3. Implement a simple version from scratch using NumPy
4. Study original papers (Mikolov 2013, Pennington 2014)
5. Explore bias detection using WEAT (Word Embedding Association Test)

Length: 650 words