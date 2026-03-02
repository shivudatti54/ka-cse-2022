### Language Modeling: Statistical Language Model

#### N-gram Model (Unigram, Bigram)

- **Unigram Model (N-gram 1):** A statistical model that predicts the next word in a sequence based on the previous word.
  - Formula: P(w) = C(w) / T
  - Where P(w) = Probability of the word w, C(w) = Count of word w, and T = Total number of words
- **Bigram Model (N-gram 2):** A statistical model that predicts the next word in a sequence based on the previous word and the word before that.
  - Formula: P(w|w-1) = C(ww-1) / C(w-1)
  - Where P(w|w-1) = Probability of the word w given the word w-1

#### Paninion Framework

- A framework for constructing statistical language models
- Consists of:
  1.  **Unigram Model:** Predicts the next word based on the previous word
  2.  **Bigram Model:** Predicts the next word based on the previous two words
  3.  **Trigram Model:** Predicts the next word based on the previous three words

#### Karaka Theory

- A theory that explains the properties of statistical language models
- States that the probability of a word is determined by the context in which it appears
- Theorems:
  1.  **Karaka's Law:** The probability of a word is inversely proportional to the number of times it appears in the text
  2.  **Karaka's Corollary:** The probability of a word is directly proportional to the number of times it appears in the same context as the word that follows it
