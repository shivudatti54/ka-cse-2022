Of course. Here is a comprehensive educational module on N-gram models, specifically the Unigram model, tailored for  engineering students.

# Module 1: Statistical Language Models - The Unigram Model

## 1. Introduction

In Natural Language Processing (NLP), a fundamental question is: **How can we get a machine to understand, generate, and process human language?** One of the most successful and foundational approaches is through **Statistical Language Models (SLMs)**. An SLM is a probabilistic model that predicts the likelihood of a sequence of words occurring in a language. Think of it as teaching a machine the "probability" of a sentence being well-formed and natural. The simplest building block of these models is the **Unigram Model**.

## 2. Core Concepts

### What is a Language Model?
A Language Model assigns a probability $P(W)$ to a sequence of words $W = (w_1, w_2, w_3, ..., w_n)$. This probability represents how likely that sequence is to be a valid sentence in a given language.

### The N-gram Assumption
Calculating the probability of a full sentence, considering all previous words, is computationally impossible. To simplify, we use the **Markov Assumption**: the probability of a word depends only on a limited number of previous words.

An **N-gram** is a contiguous sequence of `N` items (words) from a given text. The `N` defines the context window for the model.

*   **Unigram (1-gram):** `N=1`. A single word. No context.
*   **Bigram (2-gram):** `N=2`. A pair of words. Context is the immediate previous word.
*   **Trigram (3-gram):** `N=3`. Context is the two previous words.

### The Unigram Model
The Unigram model is the simplest N-gram model. It makes a strong (and often incorrect) assumption: **each word in a sentence occurs independently of all other words**. There is no notion of word order or context.

The probability of a sentence $W$ is simply the product of the probabilities of each individual word:
$$P(W) = P(w_1, w_2, ..., w_n) \approx P(w_1) \cdot P(w_2) \cdot \ ... \ \cdot P(w_n)$$

### How do we calculate these probabilities? Maximum Likelihood Estimation (MLE)
We estimate the probability of a word from a large corpus of text (our training data).

The probability of a word $w_i$ is its **relative frequency** in the corpus:
$$P(w_i) = \frac{\text{Count}(w_i)}{N}$$
where:
*   $\text{Count}(w_i)$ is the number of times word $w_i$ appears in the corpus.
*   $N$ is the total number of **word tokens** (i.e., the total size) of the corpus.

## 3. Example

Let's train a simple Unigram model on a tiny corpus:
> "I love NLP. I love ."

**Step 1: Preprocessing & Vocabulary Creation**
First, we normalize the text (convert to lowercase, remove punctuation) and split into words (tokens). Our corpus becomes:
`["i", "love", "nlp", "i", "love", ""]`

Our vocabulary (unique words) is: `{i, love, nlp, }`

**Step 2: Count Word Frequencies**
*   Count(i) = 2
*   Count(love) = 2
*   Count(nlp) = 1
*   Count() = 1
Total number of word tokens, $N = 6$.

**Step 3: Calculate Unigram Probabilities**
Using the formula $P(w_i) = \frac{\text{Count}(w_i)}{N}$:
*   $P(i) = 2/6 = 1/3$
*   $P(love) = 2/6 = 1/3$
*   $P(nlp) = 1/6$
*   $P() = 1/6$

**Step 4: Calculate Sentence Probability**
Now, let's find the probability of a new sentence: **"love "**.

$$P(\text{"love "}) = P(\text{love}) \cdot P(\text{}) = \frac{2}{6} \cdot \frac{1}{6} = \frac{2}{36} = \frac{1}{18}$$

Notice that the model assigns the **same probability** to the sentences "love " and " love" because it ignores word order:
$$P(\text{" love"}) = P(\text{}) \cdot P(\text{love}) = \frac{1}{6} \cdot \frac{2}{6} = \frac{1}{18}$$

This highlights a major weakness of the Unigram model: it has no understanding of syntax or word order.

## 4. Key Points & Summary

| Aspect | Description |
| :--- | :--- |
| **Core Idea** | Models language by calculating the probability of a sequence of words based on the independent probability of each word. |
| **Assumption** | **Bag-of-Words**: Words are independent events. The order of words does not matter. |
| **Probability Formula** | $P(W) = \prod_{i=1}^{n} P(w_i)$ |
| **Parameter Estimation** | $P(w_i) = \frac{\text{Count}(w_i)}{\text{Total Words in Corpus}}$ (Maximum Likelihood Estimation) |
| **Advantages** | • Extremely simple to implement and compute.<br>• Requires minimal data storage (just a vocabulary and counts).<br>• Serves as a strong baseline for more complex models. |
| **Disadvantages** | • **Fails to capture context or word order.** "cat eats fish" and "fish eats cat" have the same probability.<br>• Prone to the **sparsity problem** (gives zero probability to words not seen in the training corpus).<br>• Often performs poorly as a standalone model for tasks like text generation. |
| **Typical Use Cases** | • **Text Classification** (e.g., Naive Bayes classifiers), where word order is often secondary to word presence.<br>• As a component in more complex models (e.g., for smoothing). |

**In summary,** the Unigram model is the foundational, albeit naive, statistical approach to language modeling. Its strength lies in its simplicity, but its inability to model context makes it unsuitable for advanced NLP tasks on its own. It is a crucial first step in understanding the more powerful Bigram and N-gram models that follow.