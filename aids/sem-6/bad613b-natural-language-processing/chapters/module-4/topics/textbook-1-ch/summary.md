# Textbook 1: Ch

## Natural Language Processing: Information Retrieval

### Design Features of Information Retrieval Systems

- **Query-Document Intersection**: The intersection of the query terms and the document terms, which is used to compute the relevance of a document to the query.
- **Term Frequency-Inverse Document Frequency (TF-IDF)**: A weighting scheme that takes into account the frequency of a term in a document and its rarity across the entire corpus.
- **Document Vector Space Model**: A mathematical representation of a document as a vector of TF-IDF values, which can be used for similarity calculations.

### Information Retrieval Theories

- **Bayes' Theorem**: A mathematical formula used to compute the probability of a document being relevant to a query, given the probability of the query terms occurring in the document.
- **Probabilistic Model**: A model that assumes that the relevance of a document to a query is a probabilistic event, and uses Bayes' Theorem to compute the probability.

### Important Formulas

- **Maximum Marginal Relevance (MMR)**: A formula used to compute the relevance of a document to a query, based on the intersection of query terms and document terms.
- **Diversify**: A formula used to compute the diversity of a set of documents, which is used to avoid over-representation of similar documents.

### Important Definitions

- **Relevance**: The degree to which a document is relevant to a query.
- **Precision**: The degree to which a set of documents retrieved by an IR system are relevant to the query.
- **Recall**: The degree to which an IR system has retrieved all relevant documents for a query.

### Important Theorems

- **Zipf's Law**: A mathematical law that states that the frequency of a term in a document is inversely proportional to its rank in the frequency distribution of all terms in the corpus.
- **Laplacian Smoothing**: A smoothing technique used to reduce the impact of rare terms in a document on its TF-IDF value.
