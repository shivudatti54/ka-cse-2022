# Training Word2Vec Models

## Introduction to Word2Vec

Word2Vec is a groundbreaking technique in Natural Language Processing (NLP) that learns distributed vector representations of words from large amounts of text. These vector representations, often called word embeddings, capture semantic and syntactic relationships between words. Words with similar meanings are mapped to nearby points in the vector space.

The key insight behind Word2Vec is the **Distributional Hypothesis**: words that appear in similar contexts tend to have similar meanings. Word2Vec operationalizes this hypothesis by training a model to predict either a target word from its context (Continuous Bag of Words, CBOW) or the context from a target word (Skip-Gram).

## Core Architectures

Word2Vec offers two main architectural approaches for training word embeddings:

### 1. Continuous Bag of Words (CBOW)

The CBOW model predicts a target word based on its surrounding context words. It takes the context words as input and tries to predict the target word at the center.

```
Input Context Words: [The, cat, on, mat]
                  ↓
              CBOW Model
                  ↓
        Predicted Target Word: sat
```

The architecture can be visualized as:

```
Context Words → Input Layer → Hidden Layer → Output Layer → Target Word
      (One-hot)      (V-dim)     (N-dim)      (V-dim)     (One-hot)
```

Where:
- V = Vocabulary size
- N = Embedding dimension (typically 100-300)

### 2. Skip-Gram Model

The Skip-Gram model does the opposite of CBOW: it predicts context words given a target word. This approach often works better with larger datasets and captures more fine-grained relationships.

```
Input Target Word: sat
            ↓
        Skip-Gram Model
            ↓
Predicted Context Words: [The, cat, on, mat]
```

The architecture can be visualized as:

```
Target Word → Input Layer → Hidden Layer → Output Layer → Context Words
 (One-hot)      (V-dim)     (N-dim)      (V-dim)       (One-hot)
```

## Training Process

### Neural Network Structure

Both CBOW and Skip-Gram use a shallow neural network with one hidden layer:

```
Input Layer (V neurons) → Hidden Layer (N neurons) → Output Layer (V neurons)
```

The weight matrix between the input and hidden layer (W₁) becomes our word embeddings after training.

### Objective Function

Word2Vec uses a softmax function to calculate the probability of a word given its context:

P(wₜ|w_c) = exp(vₜ · v_c) / Σᵢ exp(vᵢ · v_c)

Where:
- wₜ = target word
- w_c = context word
- vₜ, v_c = vector representations

The model is trained to maximize the log probability of observed word-context pairs.

### Negative Sampling

Since calculating the full softmax over a large vocabulary is computationally expensive, Word2Vec uses Negative Sampling as an optimization technique. Instead of updating all weights in the output layer, we only update:
1. The weights for the positive example (actual context word)
2. The weights for a small number of "negative" examples (randomly sampled words)

The modified objective function becomes:

log σ(vₜ · v_c) + Σᵢᴺ 𝔼wᵢ~Pₙ(w)[log σ(-vᵢ · v_c)]

Where:
- σ = sigmoid function
- N = number of negative samples
- Pₙ(w) = noise distribution (typically unigram distribution raised to 3/4 power)

### Hierarchical Softmax

An alternative to negative sampling is Hierarchical Softmax, which uses a binary Huffman tree to reduce computation from O(V) to O(log V). Frequent words are assigned shorter paths in the tree.

## Implementation Details

### Training Parameters

| Parameter | Typical Value | Description |
|-----------|---------------|-------------|
| Embedding Dimension | 100-300 | Size of word vectors |
| Window Size | 5-10 | Context window around target word |
| Negative Samples | 5-25 | Number of negative examples per positive |
| Learning Rate | 0.025→0.0001 | Often decreased during training |
| Minimum Word Count | 5-10 | Ignore rare words |
| Subsampling | 10⁻³-10⁻⁵ | Discard frequent words probabilistically |

### Subsampling Frequent Words

To counter the imbalance between frequent and rare words, Word2Vec uses subsampling:

P(discard wᵢ) = 1 - √(t / f(wᵢ))

Where:
- t = threshold (typically 10⁻⁵)
- f(wᵢ) = frequency of word wᵢ

This helps improve both quality of representations and training speed.

## Mathematical Foundations

### Word Similarity Calculation

The cosine similarity between word vectors is commonly used:

similarity(A, B) = (A · B) / (‖A‖ ‖B‖)

This measures the cosine of the angle between vectors, with values ranging from -1 to 1.

### Vector Space Properties

Word2Vec embeddings exhibit interesting mathematical properties:

```
v(king) - v(man) + v(woman) ≈ v(queen)
v(Paris) - v(France) + v(Italy) ≈ v(Rome)
```

These analogies demonstrate that the vector space captures semantic relationships.

## Practical Implementation

### Data Preprocessing

Proper preprocessing is crucial for training effective Word2Vec models:

1. **Tokenization**: Split text into words or subwords
2. **Lowercasing**: Convert all text to lowercase (usually)
3. **Stopword Removal**: Optionally remove common words
4. **Rare Word Filtering**: Remove words below frequency threshold

### Training Code Example (Python with Gensim)

```python
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# Preprocessed sentences
sentences = [["the", "cat", "sat", "on", "mat"], 
             ["the", "dog", "ran", "in", "park"]]

# Train Word2Vec model
model = Word2Vec(
    sentences=sentences,
    vector_size=100,      # Embedding dimension
    window=5,            # Context window size
    min_count=5,         # Minimum word frequency
    negative=15,         # Number of negative samples
    workers=4,           # Number of threads
    epochs=10           # Number of iterations
)

# Get word vector
vector = model.wv['cat']

# Find similar words
similar_words = model.wv.most_similar('cat', topn=5)
```

## Evaluation Methods

### Intrinsic Evaluation

1. **Word Similarity Tasks**: Compare model similarity scores with human judgments
2. **Analogy Tasks**: Test semantic and syntactic relationships (e.g., "man is to woman as king is to ?")
3. **Concept Categorization**: Group words into semantic categories

### Extrinsic Evaluation

1. **Downstream NLP Tasks**: Use embeddings as features in text classification, named entity recognition, etc.
2. **Performance Comparison**: Compare with other embedding techniques on specific applications

## Comparison with Other Methods

| Method | Training Objective | Advantages | Limitations |
|--------|-------------------|------------|-------------|
| **Word2Vec** | Predict context/target words | Fast training, captures semantic relationships | Cannot handle out-of-vocabulary words |
| **GloVe** | Factorize word-context matrix | Captures global statistics | Less effective for rare words |
| **FastText** | Predict context/target with subwords | Handles OOV words, better for morph-rich languages | Larger model size |
| **ELMo** | Language model objective | Contextualized embeddings, captures polysemy | Computationally expensive |

## Advanced Variations

### Paragraph Vector (Doc2Vec)

An extension of Word2Vec that learns embeddings for entire documents or paragraphs by adding a paragraph token that gets updated during training.

### Subword Information (FastText)

Facebook's FastText extends Word2Vec by representing words as bags of character n-grams, allowing it to handle out-of-vocabulary words and capture morphological information.

## Applications of Word2Vec

1. **Text Classification**: Use as features for sentiment analysis, topic labeling
2. **Information Retrieval**: Improve search relevance with semantic matching
3. **Recommendation Systems**: Represent items and users in shared embedding space
4. **Named Entity Recognition**: Enhance feature representations for entity detection

## Limitations and Challenges

1. **Polysemy**: Cannot handle multiple meanings of words (addressed by contextual embeddings)
2. **Out-of-Vocabulary Words**: Cannot generate embeddings for unseen words
3. **Domain Specificity**: Embeddings trained on one domain may not transfer well to others
4. **Bias**: Can capture and amplify biases present in training data

## Recent Developments

While Word2Vec was groundbreaking, it has been largely superseded by contextual embedding approaches like:

1. **BERT**: Bidirectional Encoder Representations from Transformers
2. **GPT**: Generative Pre-trained Transformer
3. **ELMo**: Embeddings from Language Models

These models generate context-dependent embeddings that capture polysemy and perform better on most NLP tasks.

## Exam Tips

1. **Understand the difference between CBOW and Skip-Gram**: CBOW is faster and works better with frequent words, while Skip-Gram performs better with larger datasets and rare words.

2. **Remember the purpose of negative sampling**: It's an optimization technique that approximates the softmax function by sampling negative examples instead of computing over the entire vocabulary.

3. **Know the mathematical properties**: Word embeddings should capture analogical relationships (e.g., king - man + woman ≈ queen).

4. **Be familiar with evaluation methods**: Both intrinsic (word similarity, analogies) and extrinsic (downstream task performance) evaluations are important.

5. **Understand limitations**: Word2Vec cannot handle polysemy or out-of-vocabulary words, which led to the development of contextual embeddings.

6. **Practice with code examples**: Be able to write simple Word2Vec training code using libraries like Gensim.

7. **Compare with alternatives**: Be prepared to contrast Word2Vec with GloVe, FastText, and contextual embedding methods.