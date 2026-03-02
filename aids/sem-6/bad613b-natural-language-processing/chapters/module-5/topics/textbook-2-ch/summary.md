# **Textbook 2: Ch - Natural Language Processing**

# **Machine Translation: Language Divergences and Typology**

### Key Concepts

- **Language Divergence**: The process of languages becoming increasingly different from each other over time.
- **Typological Distance**: A measure of the similarity or difference between two languages.
- **Language Contact**: The interaction between two or more languages, resulting in language change or convergence.

### Important Formulas and Definitions

- **Levenshtein Distance**: A measure of the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another.
  - Formula: `L(i, j) = min(c(i, j) + L(i+1, j), c(i, j+1) + L(i, j+1), L(i+1, j+1) + c(i, j))`
- **Jaro-Winkler Distance**: A measure of the similarity between two strings.
  - Formula: `JW(i, j) = (J(i, j) \* w) / (1 + (1-w) \* (1 - J(i, j)))`
- **Word Embeddings**: A mathematical representation of words as vectors in a high-dimensional space.
  - Definition: Word embeddings capture the semantic meaning of words and their relationships.

### Important Theorems

- **The Typological Distance Theorem**: The typological distance between two languages is a measure of the degree to which they are similar or different.
- **The Language Contact Theorem**: Language contact between two or more languages results in language change or convergence.

### Key Theorems and Results

- **The Levenshtein Distance Theorem**: The Levenshtein distance between two words is a measure of the minimum number of operations required to change one word into another.
- **The Jaro-Winkler Distance Theorem**: The Jaro-Winkler distance between two strings is a measure of the similarity between them.

### Important Text

- **Chapman, H. E. (2005). Computational Lexical Semantics. MIT Press.**
- **Kilgarriff, A. (1996). Dictionary of Word Origins. Oxford University Press.**

### Quick Revision Tips

- Focus on the key concepts and definitions.
- Practice calculating Levenshtein and Jaro-Winkler distances.
- Review the typological distance theorem and language contact theorem.
- Use word embeddings to analyze semantic meaning and relationships between words.
