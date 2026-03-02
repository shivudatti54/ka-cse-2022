# Language Models and N-grams

## Introduction
Language models are fundamental components in natural language processing (NLP) that assign probabilities to sequences of words. N-gram models, which use contiguous sequences of n items (typically words), form the basis of traditional statistical language modeling. These models are crucial for tasks like speech recognition, machine translation, and predictive text input.

The importance of n-gram models lies in their simplicity and effectiveness in capturing local linguistic patterns. While modern neural language models have surpassed their performance, n-grams remain essential for understanding foundational concepts in probability estimation, smoothing techniques, and the challenges of sparse data. Current research explores hybrid approaches combining n-grams with neural architectures for improved efficiency in resource-constrained environments.

## Key Concepts
1. **N-grams**: Contiguous sequences of n words
   - Unigram (1-gram), Bigram (2-gram), Trigram (3-gram)
   - Markov assumption: Probability of word depends only on previous n-1 words

2. **Probability Estimation**:
   - Maximum Likelihood Estimation (MLE): P(w_i | w_{i-n+1}^{i-1}) = count(w_{i-n+1}^i) / count(w_{i-n+1}^{i-1})
   - Smoothing Techniques:
     - Laplace (Add-one) Smoothing
     - Lidstone (Add-k) Smoothing
     - Good-Turing Estimation
     - Kneser-Ney Smoothing

3. **Evaluation Metrics**:
   - Perplexity: 2^H where H is cross-entropy
   - Cross-Entropy: H(p,q) = -1/N Σ log_2 q(w_i | context)

4. **Sparsity Problem**:
   - Zipf's Law: Most n-grams occur rarely
   - Handling Out-of-Vocabulary (OOV) words

## Examples

**Example 1: Bigram Probability Calculation**
Corpus: "The cat sat on the mat. The cat slept."
Calculate P("mat" | "the") with MLE

Solution:
1. Count("the mat") = 1
2. Count("the") = 2
3. P("mat"|"the") = 1/2 = 0.5

**Example 2: Laplace Smoothing**
Same corpus, calculate P("dog"|"the") with add-1 smoothing (V=6 vocabulary size)

Solution:
1. Count("the dog") = 0
2. Smoothed count = 0 + 1 = 1
3. Smoothed denominator = 2 + 6 = 8
4. P("dog"|"the") = 1/8 = 0.125

**Example 3: Perplexity Calculation**
Test sentence: "the cat sat"
Bigram probabilities:
P(the|<s>) = 0.5, P(cat|the) = 0.4, P(sat|cat) = 0.3, P(</s>|sat) = 0.6

Perplexity = (0.5 * 0.4 * 0.3 * 0.6)^(-1/4) ≈ 2.45

## Exam Tips
1. Focus on smoothing techniques - be prepared to compare Laplace vs Kneser-Ney
2. Understand the trade-off between n-gram order and data sparsity
3. Practice perplexity calculations with logarithms to avoid underflow
4. Remember evaluation metrics require separate training and test sets
5. Study the connection between n-grams and Hidden Markov Models
6. Be prepared to discuss limitations: long-distance dependencies, context capture
7. Know current research applications like n-gram features in transformer models

Length: 2500 words