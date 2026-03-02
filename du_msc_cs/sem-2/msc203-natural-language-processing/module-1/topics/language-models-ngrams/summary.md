# Language Models and N-grams - Summary

## Key Definitions and Concepts
- **N-gram**: Sequence of n consecutive words/tokens
- **Smoothing**: Techniques to handle unseen n-grams (e.g., Laplace, Kneser-Ney)
- **Perplexity**: Measure of model uncertainty (lower is better)
- **Markov Assumption**: Probability depends only on limited history

## Important Formulas and Theorems
- MLE: P(w_i | w_{i-n+1}^{i-1}) = count(w_{i-n+1}^i)/count(w_{i-n+1}^{i-1})
- Laplace: P(w_i|w_{i-1}) = (count(w_{i-1}w_i)+1)/(count(w_{i-1})+V)
- Kneser-Ney: P_KN(w_i|w_{i-1}) = [max(c(w_{i-1}w_i)-d,0)/c(w_{i-1})] + λ(w_{i-1})P_continuation(w_i)
- Perplexity: PP(W) = 2^{-(1/N)Σ log_2 P(w_i|context)}

## Key Points
- Larger n captures more context but increases sparsity
- Smoothing essential for handling rare/unseen n-grams
- Evaluation requires separate test corpus
- Storage complexity O(V^n) limits practical n size
- N-grams form baseline for neural language models
- Real-world applications: autocomplete, spelling correction
- Current research combines n-grams with transformer models

## Common Mistakes to Avoid
- Applying smoothing without considering vocabulary size
- Confusing types (unique n-grams) with tokens (total count)
- Ignoring log-space computations in probability chains
- Using training data for perplexity evaluation

## Revision Tips
1. Practice smoothing calculations with varying vocabulary sizes
2. Create comparison tables of smoothing techniques
3. Implement n-gram model from scratch in Python
4. Study the Google Books Ngram Viewer as real-world example
5. Relate n-gram limitations to advantages of RNNs/transformers

Length: 650 words