# Textbook Chapter 3: 3.1-3.6

### Key Points

- **Classic IR Models**
  - Definition: IR model that uses mathematical techniques (e.g., vector space model, term frequency-inverse document frequency) to calculate document similarity.
  - Types:
    - Vector Space Model (VSM)
    - Term Frequency-Inverse Document Frequency (TF-IDF)
- **Alternative Set Theoretic Models**
  - Definition: IR model that uses set theory to calculate document similarity (e.g., Jaccard similarity, cosine similarity).
  - Types:
    - Jaccard Similarity
    - Cosine Similarity
- **Definition of Similarity Measures**
  - Cosine Similarity: measures similarity between two vectors as the dot product of the vectors divided by the product of their magnitudes.
  - Jaccard Similarity: measures similarity between two sets as the size of their intersection divided by the size of their union.
- **Important Formulas and Theorems**
  - Cosine Similarity: $sim(x, y) = \frac{x \cdot y}{\|x\| \|y\|}$
  - Jaccard Similarity: $sim(x, y) = \frac{|x \cap y|}{|x \cup y|}$
  - Vector Space Model: $sim(x, y) = \sum_{i=1}^n \frac{t_i x_i y_i}{\|x\| \|y\|}$
- **Key Concepts**
  - Document representation: vector or set that represents a document.
  - Term frequency: frequency of a term in a document.
  - Inverse document frequency: rarity of a term across all documents.

### Quick Revision Checklist

- Classic IR models (VSM, TF-IDF)
- Alternative set theoretic models (Jaccard, cosine)
- Similarity measures (cosine, Jaccard)
- Formulas and theorems (cosine, Jaccard)
- Key concepts (document representation, term frequency, inverse document frequency)
