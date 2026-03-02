# Words and Word Classes

## Natural Language Processing (NLP) Module

### Word Level Analysis: Regular Expressions, Finite-State Automata, Morphological Parsing

**Definition:** A word class refers to the part of speech (POS) that a word belongs to, such as noun, verb, adjective, adverb, etc.

**Key Points:**

- **Word Classes:** Based on grammatical function:
  - Nouns (N)
  - Verbs (V)
  - Adjectives (Adj)
  - Adverbs (Adv)
  - Prepositions (P)
  - Conjunctions (C)
  - Interjections (I)
- **Part-of-Speech (POS) Tagging:** Assigning a word class to each word in a sentence
- **Morphological Analysis:** Breaking down words into their base form and affixes (prefixes, suffixes, roots)
- **Stemming and Lemmatization:** Reducing words to their base form (e.g., "running" -> "run")

**Important Formulas:**

- **Bigram Formula:** P(word2|word1) = (number of occurrences of word2 following word1) / (total number of word1 occurrences)
- **Trigram Formula:** P(word3|word1, word2) = (number of occurrences of word3 following words1 and word2) / (total number of word1 and word2 occurrences)

**Theorems:**

- **Zipf's Law:** The frequency of a word decreases as its rank in the frequency distribution increases
- **N-gram Theorem:** The probability of a sequence of n items is proportional to the number of possible sequences of length n

**Key Concepts:**

- **Regular Expressions:** Patterns used to match strings in text data
- **Finite-State Automata:** Mathematical models used to recognize patterns in text data
- **Morphological Parsing:** Analyzing the structure of words to identify their parts of speech and relationships between words.
