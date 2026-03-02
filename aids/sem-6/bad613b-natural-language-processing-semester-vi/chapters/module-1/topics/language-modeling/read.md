# Statistical Language Modeling

## Introduction to Language Modeling

A **Language Model (LM)** is a fundamental concept in Natural Language Processing (NLP) that assigns a probability to a sequence of words. It answers the question: "How likely is this sequence of words to appear in a given language?" This probability, P(w₁, w₂, ..., wₙ), helps machines understand, generate, and predict human language.

The core idea is to learn the structure and patterns of a language from a large corpus of text. For example, an LM trained on English text would assign a higher probability to the phrase "the cat sat on the mat" than to the nonsensical "mat the on sat cat the."

## The Challenge of Modeling Language

Modeling language is challenging due to its **combinatorial explosion**. Consider a sentence with 20 words chosen from a vocabulary of 20,000. The number of possible sequences is 20,000²⁰, which is astronomically large. It's impossible to observe all these sequences in any corpus. Therefore, LMs must use clever simplifications and approximations to estimate probabilities for unseen sequences.

## The N-Gram Language Model

The most common simplification is the **N-gram model**. It makes a crucial assumption about language: the probability of a word depends only on the previous **N-1** words. This is known as the **Markov Assumption**.

### From Sequence Probability to N-Grams

The probability of a sequence of words P(w₁, w₂, ..., wₙ) can be broken down using the **chain rule of probability**:
`P(w₁, w₂, ..., wₙ) = P(w₁) * P(w₂|w₁) * P(w₃|w₁,w₂) * ... * P(wₙ|w₁, w₂, ..., wₙ₋₁)`

However, calculating P(wₙ|w₁, w₂, ..., wₙ₋₁) requires seeing the entire previous context, which is impractical. The N-gram model approximates this by assuming a word's probability depends only on its immediate history.

*   **Unigram (1-gram)**: `P(wₙ)` - The probability of a word is independent of context.
    `P("the cat sat") ≈ P("the") * P("cat") * P("sat")`
*   **Bigram (2-gram)**: `P(wₙ|wₙ₋₁)` - The probability of a word depends on the previous one word.
    `P("the cat sat") ≈ P("the") * P("cat"|"the") * P("sat"|"cat")`
*   **Trigram (3-gram)**: `P(wₙ|wₙ₋₂, wₙ₋₁)` - The probability of a word depends on the previous two words.
    `P("the cat sat") ≈ P("the") * P("cat"|"the") * P("sat"|"the cat")`
*   **N-gram (N-gram)**: `P(wₙ|wₙ₋ₙ₊₁, ..., wₙ₋₁)` - General case.

### Calculating N-Gram Probabilities

Probabilities are calculated from a corpus using **Maximum Likelihood Estimation (MLE)**. The probability of a word given its history is the count of that sequence divided by the count of the history.

`P(wₙ|wₙ₋₁) = count(wₙ₋₁, wₙ) / count(wₙ₋₁)`

**Example:**
Consider a tiny corpus: "the cat sat on the mat. the dog sat on the cat."

*   `P(cat | the) = count(the cat) / count(the) = 2 / 4 = 0.5`
*   `P(sat | cat) = count(cat sat) / count(cat) = 1 / 2 = 0.5`
*   `P(mat | the) = count(the mat) / count(the) = 1 / 4 = 0.25`
*   `P(dog | the) = count(the dog) / count(the) = 1 / 4 = 0.25`

The probability of the sentence "the cat sat" is:
`P("the cat sat") = P(the) * P(cat|the) * P(sat|cat) = (4/11) * (2/4) * (1/2) ≈ 0.036`

### The Sparsity Problem and Smoothing

A major issue with MLE is **sparsity**. Many valid N-grams will have a count of zero in the training corpus, leading to zero probabilities and breaking the model. For example, `P(dog|cat)` would be 0 in our corpus, making any sentence containing "cat dog" impossible.

The solution is **smoothing** (or discounting), which redistributes probability mass from seen events to unseen events. Common techniques include:

*   **Add-One (Laplace) Smoothing**: Add 1 to every count.
    `P(wₙ|wₙ₋₁) = (count(wₙ₋₁, wₙ) + 1) / (count(wₙ₋₁) + V)` where V is the vocabulary size.
    Simple but often performs poorly.

*   **Add-K Smoothing**: Add a fractional k (e.g., 0.5) instead of 1.
    `P(wₙ|wₙ₋₁) = (count(wₙ₋₁, wₙ) + k) / (count(wₙ₋₁) + k*V)`

*   **Backoff**: If a high-order N-gram (e.g., trigram) has a count of zero, use a lower-order N-gram (e.g., bigram) instead.

*   **Interpolation**: Mix the probability estimates of all N-gram models (e.g., trigram, bigram, unigram), weighted by a λ parameter.
    `Pₗᵢₙₑₐᵣ(wₙ|wₙ₋₂, wₙ₋₁) = λ₁P(wₙ|wₙ₋₂, wₙ₋₁) + λ₂P(wₙ|wₙ₋₁) + λ₃P(wₙ)`

### Perplexity: Evaluating Language Models

**Perplexity** is the standard metric for evaluating a language model's quality. It measures how surprised the model is by unseen text. A lower perplexity indicates a better model.

Perplexity is defined as the inverse probability of the test set, normalized by the number of words.
`PP(W) = P(w₁, w₂, ..., wₙ)^{-1/N}`

Think of it as the weighted average branching factor—the number of equally likely words the model considers at each point. A perplexity of 50 means the model is as confused as if it had to choose uniformly from 50 words at each step.

## The Paninian Framework: An Indian Linguistic Perspective

The syllabus mentions the "Paninian Framework." This refers to the grammatical tradition established by the ancient Indian linguist **Pāṇini** in his work **Aṣṭādhyāyī**. His framework is remarkably formal and computational.

*   **Morphology-Driven**: Pāṇini's grammar is heavily based on word morphology (structure) and uses a system of affixes (prefixes, suffixes, infixes) to derive word forms and meanings.
*   **Rule-Based and Generative**: It uses a set of meta-rules (sutras) that are applied in a specific order to generate correct word forms and sentences. This is analogous to a modern context-free grammar but is often more compact and elegant.
*   **Relevance to NLP**: For Indian languages, which are highly inflectional (words change form based on tense, gender, number, case), a morphology-based approach like Pāṇini's is highly relevant. Statistical models for these languages must account for this rich morphology to avoid extreme data sparsity. Modern systems often combine statistical methods with rule-based morphological analyzers inspired by this framework.

## Applications of Language Models

Language models are the backbone of numerous NLP applications:
1.  **Speech Recognition:** Resolving ambiguity (e.g., "recognize speech" vs. "wreck a nice beach").
2.  **Machine Translation:** Evaluating the fluency of candidate translations.
3.  **Spell Checking and Autocorrect:** Identifying and suggesting corrections for misspelled words.
4.  **Automatic Text Generation:** Powering predictive text (e.g., smartphone keyboards) and generative AI (e.g., ChatGPT).
5.  **Information Retrieval:** Improving search query understanding and result ranking.

## Comparison of N-Gram Models

| Feature | Unigram | Bigram | Trigram | Higher-Order (N>3) |
| :--- | :--- | :--- | :--- | :--- |
| **Context Window** | 0 words | 1 word | 2 words | N-1 words |
| **Model Quality** | Poor (no context) | Fair | Good | Better |
| **Data Sparsity** | Low | Medium | High | Very High |
| **Storage Needs** | Small | Medium | Large | Very Large |
| **Example** | `P("the")` | `P("cat"\|"the")` | `P("sat"\|"the cat")` | `P("on"\|"the cat sat")` |

## Exam Tips

*   **Memorize the Formulas:** Be able to write down the MLE formula for bigram/trigram probability `P(wₙ|wₙ₋₁) = count(...)/count(...)` and the chain rule.
*   **Understand Sparsity:** Always mention the sparsity problem (zero probability for unseen N-grams) when discussing limitations of MLE.
*   **Know Smoothing Techniques:** Be prepared to define and contrast at least two smoothing techniques (e.g., Add-One vs. Backoff). Explain *why* smoothing is necessary.
*   **Calculate Perplexity:** You might be asked to interpret perplexity. Remember: **lower perplexity = better model**.
*   **Panini's Relevance:** For a short note, connect Pāṇini's framework to the morphological complexity of Indian languages and why it presents a challenge/opportunity for statistical LMs.