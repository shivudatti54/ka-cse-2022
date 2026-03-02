# Naive Bayes Classifiers for Text Classification

## Introduction to Naive Bayes

Naive Bayes classifiers are a family of simple probabilistic classifiers based on applying Bayes' theorem with strong (naive) independence assumptions between the features. They are particularly well-suited for text classification tasks such as sentiment analysis, spam detection, and document categorization.

The "naive" aspect refers to the assumption that all features (words in text classification) are conditionally independent given the class label. While this assumption is rarely true in real-world text data (where words often appear in correlated patterns), Naive Bayes classifiers still perform remarkably well in practice.

### Mathematical Foundation: Bayes' Theorem

Bayes' theorem forms the foundation of Naive Bayes classifiers:

```
P(C|X) = [P(X|C) × P(C)] / P(X)
```

Where:
- `P(C|X)` is the posterior probability: probability of class C given features X
- `P(X|C)` is the likelihood: probability of features X given class C
- `P(C)` is the prior probability: probability of class C
- `P(X)` is the evidence: probability of features X

In text classification:
- C represents a class (e.g., "spam" or "not spam")
- X represents the features (words in a document)

## How Naive Bayes Works for Text Classification

### Text Representation: The Bag-of-Words Model

Naive Bayes classifiers typically use a bag-of-words representation, where:
- The order of words is ignored
- Only word frequencies matter
- Each document is represented as a vector of word counts

```
Document: "The quick brown fox jumps over the lazy dog"

Bag-of-words representation:
{"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}
```

### The Naive Bayes Algorithm

For text classification, we want to find the most probable class given a document:

```
argmax_c P(C=c|D=d)
```

Using Bayes' theorem:

```
argmax_c [P(D=d|C=c) × P(C=c)] / P(D=d)
```

Since P(D=d) is constant for all classes, we can simplify to:

```
argmax_c P(D=d|C=c) × P(C=c)
```

### The "Naive" Independence Assumption

The key assumption is that all words are conditionally independent given the class:

```
P(D=d|C=c) = P(w₁, w₂, ..., wₙ|C=c) = ∏ P(wᵢ|C=c)
```

This allows us to compute the probability as:

```
P(C=c|D=d) ∝ P(C=c) × ∏ P(wᵢ|C=c)
```

## Types of Naive Bayes Classifiers

### 1. Multinomial Naive Bayes

Most commonly used for text classification. It models word counts and is suitable for discrete features.

```
P(D|C) ∝ P(C) × ∏ P(wᵢ|C)^(count(wᵢ in D))
```

### 2. Bernoulli Naive Bayes

Models binary word presence (1 if word appears, 0 otherwise). Better for shorter documents.

```
P(D|C) ∝ P(C) × ∏ [P(wᵢ|C) if wᵢ in D else (1 - P(wᵢ|C))]
```

### 3. Gaussian Naive Bayes

Used for continuous features, less common in text classification.

## Training a Naive Bayes Classifier

### Step 1: Data Preparation

1. Tokenization: Split text into words/tokens
2. Lowercasing: Convert all text to lowercase
3. Stopword removal: Remove common words (the, and, etc.)
4. Stemming/Lemmatization: Reduce words to their root form

### Step 2: Feature Extraction

Create a vocabulary from all training documents and represent each document as a feature vector.

### Step 3: Calculate Priors and Likelihoods

```
P(C=c) = (Number of documents in class c) / (Total number of documents)

P(wᵢ|C=c) = (Count of wᵢ in class c + α) / (Total word count in class c + α × |V|)
```

Where α is the smoothing parameter (Laplace smoothing) and |V| is the vocabulary size.

### Step 4: Make Predictions

For a new document, calculate:

```
argmax_c [log(P(C=c)) + ∑ count(wᵢ) × log(P(wᵢ|C=c))]
```

Using log probabilities prevents underflow with small numbers.

## Example: Sentiment Analysis

Let's consider a simple sentiment analysis example with two classes: Positive and Negative.

Training data:
- Positive: "Great movie" → {"great": 1, "movie": 1}
- Negative: "Bad movie" → {"bad": 1, "movie": 1}

Calculate probabilities:
```
P(Positive) = 1/2 = 0.5
P(Negative) = 1/2 = 0.5

With Laplace smoothing (α=1):
P(great|Positive) = (1 + 1)/(2 + 1×4) = 2/6 ≈ 0.333
P(movie|Positive) = (1 + 1)/(2 + 1×4) = 2/6 ≈ 0.333
P(bad|Positive) = (0 + 1)/(2 + 1×4) = 1/6 ≈ 0.167

P(great|Negative) = (0 + 1)/(2 + 1×4) = 1/6 ≈ 0.167
P(movie|Negative) = (1 + 1)/(2 + 1×4) = 2/6 ≈ 0.333
P(bad|Negative) = (1 + 1)/(2 + 1×4) = 2/6 ≈ 0.333
```

Test document: "Great story"
```
P(Positive|"great story") ∝ log(0.5) + log(0.333) + log(P(story|Positive))
P(Negative|"great story") ∝ log(0.5) + log(0.167) + log(P(story|Negative))
```

## Handling Zero Probabilities: Smoothing Techniques

### Laplace Smoothing (Add-α Smoothing)

Adds a small constant α to all counts to avoid zero probabilities:

```
P(wᵢ|C) = (count(wᵢ, C) + α) / (∑ count(w, C) + α × |V|)
```

### Lidstone Smoothing

Generalization of Laplace smoothing with parameter λ:

```
P(wᵢ|C) = (count(wᵢ, C) + λ) / (∑ count(w, C) + λ × |V|)
```

## Advantages and Limitations

### Advantages of Naive Bayes

| Advantage | Description |
|-----------|-------------|
| Simple and fast | Easy to implement and computationally efficient |
| Works well with high dimensions | Handles large feature spaces well |
| Good baseline | Provides a strong benchmark for text classification |
| Handles irrelevant features | Robust to irrelevant features |
| Probabilistic outputs | Provides probability estimates for predictions |

### Limitations of Naive Bayes

| Limitation | Description |
|-----------|-------------|
| Independence assumption | Words are not actually independent in text |
| Zero-frequency problem | Requires smoothing for unseen words |
| Feature correlation | Cannot capture relationships between words |
| Data scarcity | Performance degrades with insufficient training data |

## Applications in NLP

1. **Spam Detection**: Classify emails as spam or not spam
2. **Sentiment Analysis**: Determine positive/negative sentiment in text
3. **Topic Classification**: Categorize documents into topics
4. **Language Identification**: Identify the language of a text
5. **Author Attribution**: Identify the author of a text

## Implementation Considerations

### Feature Engineering

- N-grams: Consider word sequences instead of single words
- TF-IDF: Use term frequency-inverse document frequency weighting
- Word embeddings: Incorporate semantic information

### Handling Imbalanced Data

- Class weighting: Adjust priors based on class distribution
- Sampling techniques: Oversample minority classes or undersample majority classes

## Comparison with Other Text Classification Methods

| Method | Strengths | Weaknesses | Best For |
|--------|-----------|------------|----------|
| Naive Bayes | Fast, simple, works with small data | Strong independence assumption | Baseline, quick prototypes |
| Logistic Regression | Probabilistic, feature importance | Requires more data | Well-balanced datasets |
| SVM | Handles high dimensions, robust | Computationally expensive, black box | Small to medium datasets |
| Neural Networks | Captures complex patterns | Requires lots of data, compute | Large datasets with resources |

## Exam Tips

1. **Understand Bayes' Theorem**: Be able to write and explain the formula
2. **Know the independence assumption**: Explain why it's "naive" and its implications
3. **Practice calculations**: Work through examples with Laplace smoothing
4. **Compare variants**: Understand differences between Multinomial and Bernoulli Naive Bayes
5. **Recognize applications**: Be prepared to suggest where Naive Bayes would be appropriate
6. **Explain smoothing**: Understand why it's necessary and how it works
7. **Discuss limitations**: Be able to critique the method and suggest alternatives

Remember that despite its simplicity, Naive Bayes often performs surprisingly well in text classification tasks and serves as an excellent baseline before trying more complex methods.