# Deep Learning for Natural Language Processing (NLP)

## Introduction to NLP and Deep Learning

Natural Language Processing (NLP) is a field of artificial intelligence that focuses on enabling computers to understand, interpret, and generate human language. Traditional NLP approaches relied heavily on rule-based systems and hand-crafted features, which were time-consuming to create and often failed to capture the complexity and nuances of language.

The advent of deep learning has revolutionized NLP by allowing models to automatically learn hierarchical representations of language from raw data. Deep learning approaches have achieved state-of-the-art results in various NLP tasks including machine translation, sentiment analysis, text classification, named entity recognition, and question answering.

## The Challenge of Representing Words

At the core of NLP is the challenge of representing words in a way that computers can process. Unlike images which have natural numerical representations (pixel values), words are categorical symbols that need to be converted into numerical form.

### Traditional Approaches

**One-Hot Encoding:**
- Each word is represented as a vector with length equal to the vocabulary size
- The vector has 1 at the position corresponding to the word and 0 elsewhere
- Example for vocabulary ["cat", "dog", "bird"]:
  - "cat" = [1, 0, 0]
  - "dog" = [0, 1, 0]
  - "bird" = [0, 0, 1]

```
Vocabulary: [apple, banana, cat, dog, elephant]
One-hot for "cat": [0, 0, 1, 0, 0]
One-hot for "dog": [0, 0, 0, 1, 0]
```

**Limitations of One-Hot Encoding:**
- High dimensionality (vectors as long as vocabulary size)
- No semantic relationships between words
- "Cat" and "dog" are equally distant as "cat" and "apple"
- No notion of similarity between related words

## Word Embeddings: The Foundation of Modern NLP

Word embeddings address the limitations of one-hot encoding by representing words as dense, low-dimensional vectors in a continuous space where semantically similar words are located close to each other.

### What are Word Vectors?

Word vectors (or word embeddings) are numerical representations of words in a continuous vector space, typically with dimensions ranging from 50 to 300. These vectors capture semantic and syntactic relationships between words.

**Key Properties:**
- Similar words have similar vector representations
- Vector arithmetic can capture semantic relationships
- Example: king - man + woman ≈ queen

### The Distributional Hypothesis

The fundamental idea behind word embeddings is the distributional hypothesis: "Words that occur in similar contexts tend to have similar meanings." This means we can learn about a word's meaning by examining the words that frequently appear around it.

## word2vec: Efficient Learning of Word Embeddings

The word2vec model, introduced by Mikolov et al. at Google in 2013, revolutionized word embedding learning with its efficiency and effectiveness. word2vec offers two main architectures:

### 1. Continuous Bag-of-Words (CBOW)

CBOW predicts the target word based on its context words. It takes the surrounding words as input and tries to predict the center word.

```
Architecture:
Input Context Words → Hidden Layer → Output (Target Word)

Example:
Context: [the, cat, sat, on]
Target: mat

      [the]  
        │
      [cat] → Hidden Layer → [mat]
        │
      [sat]
        │
       [on]
```

**CBOW Process:**
1. Input context words are converted to one-hot vectors
2. These vectors are multiplied by the weight matrix W (input-hidden)
3. The hidden layer computes the average of these vectors
4. The hidden layer output is multiplied by W' (hidden-output)
5. Softmax produces a probability distribution over vocabulary
6. The model is trained to maximize probability of the target word

### 2. Skip-gram Model

Skip-gram does the opposite of CBOW: it predicts context words given a target word. It takes a center word as input and tries to predict the surrounding words.

```
Architecture:
Input (Target Word) → Hidden Layer → Output (Context Words)

Example:
Target: mat
Context: [the, cat, sat, on]

      [mat] → Hidden Layer → [the]
                 │
                [cat]
                 │
                [sat]
                 │
                 [on]
```

**Skip-gram Process:**
1. Input word is converted to one-hot vector
2. Multiplied by weight matrix W to get hidden layer
3. Hidden layer multiplied by W' to get output vectors for each context position
4. Softmax produces probability distributions
5. Model is trained to maximize probability of context words

### Comparison of CBOW and Skip-gram

| Aspect | CBOW | Skip-gram |
|--------|------|-----------|
| **Input** | Context words | Center word |
| **Output** | Center word | Context words |
| **Training Speed** | Faster | Slower |
| **Performance** | Better on frequent words | Better on rare words |
| **Data Efficiency** | Uses context information efficiently | Needs more data |
| **Common Use** | Larger datasets | Smaller datasets |

## Training word2vec: Technical Details

### Negative Sampling

Instead of computing expensive softmax over entire vocabulary, negative sampling approximates the learning process by:
- Training model to distinguish target word from noise words
- For each positive example (target, context), sample k negative examples
- Much more computationally efficient

```
Original softmax: O(V) complexity per training example
Negative sampling: O(k) complexity per training example
where k << V (typically k = 5-20)
```

### Hierarchical Softmax

An alternative to negative sampling that uses a binary Huffman tree to reduce computation:
- Words are leaves of the tree
- Probability computation follows path from root to leaf
- Reduces complexity from O(V) to O(log V)

## Properties of Learned Word Embeddings

### Semantic and Syntactic Relationships

Word embeddings capture various linguistic regularities:

**Semantic Similarity:**
- king ≈ queen ≈ monarch
- car ≈ vehicle ≈ automobile

**Analogies:**
- man : king :: woman : queen
- Paris : France :: Tokyo : Japan

**Syntactic Relationships:**
- run : running :: walk : walking
- big : bigger :: small : smaller

### Mathematical Operations on Word Vectors

```
vec("king") - vec("man") + vec("woman") ≈ vec("queen")
vec("Paris") - vec("France") + vec("Italy") ≈ vec("Rome")
vec("walked") - vec("walk") + vec("run") ≈ vec("ran")
```

## Visualizing Word Embeddings: word2viz

word2viz refers to techniques for visualizing high-dimensional word embeddings in 2D or 3D space for better understanding and interpretation.

### Dimensionality Reduction Techniques

**t-SNE (t-Distributed Stochastic Neighbor Embedding):**
- Non-linear technique that preserves local neighborhoods
- Good for visualizing clusters of similar words
- Commonly used for word embedding visualization

**PCA (Principal Component Analysis):**
- Linear dimensionality reduction
- Preserves global structure
- Useful for identifying main directions of variation

### Example Visualization

```
After t-SNE reduction of word vectors:

[Animal Cluster]      [Royalty Cluster]     [Verb Cluster]
- cat                 - king                - run
- dog                 - queen               - walk
- bird                - prince              - jump
- horse               - princess            - sit

[Country Cluster]     [City Cluster]
- France              - Paris
- Germany             - Berlin
- Italy               - Rome
```

## Applications of Word Embeddings in NLP

### Transfer Learning

Pre-trained word embeddings can be used as feature inputs for various NLP tasks:
- Sentiment analysis
- Text classification
- Named entity recognition
- Part-of-speech tagging

### Initialization for Deep NLP Models

Word embeddings serve as the first layer in many deep learning architectures for NLP:
- Recurrent Neural Networks (RNNs)
- Long Short-Term Memory networks (LSTMs)
- Convolutional Neural Networks (CNNs) for text

## Limitations and Advancements

### Limitations of word2vec

1. **Static embeddings:** Each word has single representation regardless of context
2. **Out-of-vocabulary words:** Cannot handle words not seen during training
3. **Polysemy:** Cannot capture multiple meanings of words

### Advanced Embedding Techniques

**Contextualized Embeddings:**
- ELMo, BERT, GPT provide context-dependent representations
- Same word has different embeddings based on sentence context

**Subword Embeddings:**
- FastText represents words as sum of character n-grams
- Can handle out-of-vocabulary words

## Practical Considerations

### Hyperparameter Tuning

| Parameter | Typical Values | Effect |
|-----------|----------------|--------|
| **Vector Dimension** | 100-300 | Higher dimensions capture more information but require more data |
| **Window Size** | 5-10 | Larger windows capture more topic information, smaller windows capture syntactic information |
| **Negative Samples** | 5-20 | More negative samples improve quality but slow training |
| **Minimum Word Count** | 5-10 | Filters rare words to reduce noise |

### Implementation Tips

1. Use pre-trained embeddings when available
2. Fine-tune embeddings on domain-specific data if needed
3. Normalize embeddings for certain applications
4. Consider using subword models for morphologically rich languages

## Exam Tips

1. **Understand the difference between CBOW and Skip-gram:** Remember that CBOW uses context to predict center word, while Skip-gram uses center word to predict context.

2. **Know the advantages of negative sampling:** Be prepared to explain how negative sampling makes training efficient compared to full softmax.

3. **Be able to interpret word analogies:** Practice with examples like "man is to king as woman is to queen" and understand the vector arithmetic behind it.

4. **Remember the distributional hypothesis:** This is the fundamental principle behind word embeddings - words with similar distributions have similar meanings.

5. **Understand visualization techniques:** Know the difference between t-SNE and PCA and when each is appropriate.

6. **Be aware of limitations:** Static embeddings cannot handle polysemy or context dependence, which is why contextualized embeddings like BERT were developed.

7. **Practice mathematical operations:** Be comfortable with vector arithmetic examples that demonstrate semantic relationships.