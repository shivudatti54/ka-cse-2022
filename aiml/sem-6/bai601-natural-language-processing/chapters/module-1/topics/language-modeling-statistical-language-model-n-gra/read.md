# **Language Modeling: Statistical Language Model**

## **Introduction**

Language modeling is a fundamental aspect of Natural Language Processing (NLP) that aims to predict the next word in a sequence of words based on the context provided by the preceding words. In this study material, we will focus on the Statistical Language Model, specifically the N-gram model (unigram, bigram), the Paninion Framework, and Karaka theory.

## **N-gram Model**

The N-gram model is a statistical language model that predicts the next word in a sequence based on the N most recent words. The model is based on the assumption that the probability of each word is dependent on the words that have come before it.

### Types of N-gram Models

- **Unigram Model**: A unigram model is an N-gram model where the probability of each word is independent of the other words. The probability of each word is calculated based on its frequency in the training data.
- **Bigram Model**: A bigram model is an N-gram model where the probability of each word is dependent on the previous word. The probability of each word is calculated based on its frequency and the frequency of the word that comes before it.

### Example

Suppose we have a sequence of words: "the cat sat on the mat". We want to predict the next word in the sequence.

- **Unigram Model**: The probability of each word is independent, so we calculate the probability of each word based on its frequency in the training data. Assume that the word "cat" appears 10 times, "sat" appears 5 times, "on" appears 3 times, and "the" appears 20 times.
- **Bigram Model**: The probability of each word is dependent on the previous word. We calculate the probability of each word based on its frequency and the frequency of the word that comes before it. Assume that the word "cat" appears 10 times, "sat" appears 5 times, "on" appears 3 times, and "the" appears 20 times.

### Code

```python
import numpy as np

def ngram_model(sequence):
    # Unigram Model
    word_freq = {}
    for word in sequence:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Bigram Model
    bigram_freq = {}
    for i in range(len(sequence) - 1):
        word = sequence[i]
        next_word = sequence[i + 1]
        if word not in bigram_freq:
            bigram_freq[word] = {}
        if next_word not in bigram_freq[word]:
            bigram_freq[word][next_word] = 0
        bigram_freq[word][next_word] += 1

    return word_freq, bigram_freq

def predict_next_word(word_freq, bigram_freq, sequence):
    # Unigram Model
    probabilities = {}
    for word in word_freq:
        probabilities[word] = word_freq[word] / len(sequence)

    # Bigram Model
    probabilities = {}
    for word in bigram_freq:
        probabilities[word] = {}
        for next_word in bigram_freq[word]:
            probabilities[word][next_word] = bigram_freq[word][next_word] / bigram_freq[word][word]

    # Predict the next word
    next_word = max(probabilities, key=probabilities.get)
    return next_word

# Example usage
sequence = ["the", "cat", "sat", "on", "the", "mat"]
word_freq, bigram_freq = ngram_model(sequence)
next_word = predict_next_word(word_freq, bigram_freq, sequence)
print("Next word:", next_word)
```

## **Paninion Framework**

The Paninion Framework is a statistical language model that extends the N-gram model by considering the entire sentence as a whole. The model predicts the next word in a sequence based on the probability of the entire sentence.

### Example

Suppose we have a sequence of words: "the cat sat on the mat". We want to predict the next word in the sequence.

- **Paninion Framework**: The model calculates the probability of the entire sentence and predicts the next word based on that probability. Assume that the sentence "the cat sat on the mat" appears 10 times in the training data.

### Code

```python
import numpy as np

def paninion_framework(sequence):
    # Calculate the probability of the entire sentence
    sentence_prob = 1
    for i in range(len(sequence) - 1):
        word = sequence[i]
        next_word = sequence[i + 1]
        sentence_prob *= (word_freq[word] + bigram_freq[word][next_word]) / (len(sequence) - i)

    # Predict the next word
    next_word = max(probabilities, key=probabilities.get)
    return next_word

# Example usage
sequence = ["the", "cat", "sat", "on", "the", "mat"]
sentence_prob = paninion_framework(sequence)
next_word = max(probabilities, key=probabilities.get)
print("Next word:", next_word)
```

## **Karaka Theory**

Karaka theory is a statistical language model that extends the N-gram model by considering the grammatical structure of the sentence. The model predicts the next word in a sequence based on the probability of the previous words and the grammatical structure of the sentence.

### Example

Suppose we have a sequence of words: "the cat sat on the mat". We want to predict the next word in the sequence.

- **Karaka Theory**: The model calculates the probability of the previous words and the grammatical structure of the sentence, and predicts the next word based on that probability. Assume that the sentence "the cat sat on the mat" appears 10 times in the training data.

### Code

```python
import numpy as np

def karaka_theory(sequence):
    # Calculate the probability of the previous words
    prev_words_prob = {}
    for i in range(len(sequence) - 1):
        word = sequence[i]
        next_word = sequence[i + 1]
        if word not in prev_words_prob:
            prev_words_prob[word] = {}
        if next_word not in prev_words_prob[word]:
            prev_words_prob[word][next_word] = 0
        prev_words_prob[word][next_word] += 1

    # Calculate the probability of the grammatical structure
    grammatical_prob = {}
    for i in range(len(sequence) - 1):
        word = sequence[i]
        next_word = sequence[i + 1]
        if word not in grammatical_prob:
            grammatical_prob[word] = {}
        if next_word not in grammatical_prob[word]:
            grammatical_prob[word][next_word] = 0
        grammatical_prob[word][next_word] += 1

    # Predict the next word
    next_word = max(probabilities, key=probabilities.get)
    return next_word

# Example usage
sequence = ["the", "cat", "sat", "on", "the", "mat"]
prev_words_prob = karaka_theory(sequence)
next_word = max(probabilities, key=probabilities.get)
print("Next word:", next_word)
```

## **Conclusion**

Language modeling is a crucial aspect of Natural Language Processing that aims to predict the next word in a sequence of words based on the context provided by the preceding words. The N-gram model, Paninion Framework, and Karaka theory are statistical language models that extend the basic N-gram model to consider the entire sentence, grammatical structure, and context-dependent probability of each word. These models have been widely used in NLP applications, including language translation, text summarization, and sentiment analysis.
