# Information Retrieval

### Chapter 2: 2.1 to 2.5

## Revision Notes

### 2.1 Introduction to Information Retrieval

- Definition: The process of searching, selecting, and retrieving relevant documents from a large collection
- Importance: Facilitates information discovery in complex environments

### 2.2 Information Retrieval Problem

- Definition: The task of finding a specific document or answer in a vast collection of documents
- Characteristics:
  - **High dimensionality**: Large number of features (e.g., words, phrases)
  - **High noise**: Irrelevant documents and noisy information
  - **Scalability**: Handling large collections

### 2.3 IR System

- Definition: A software system designed to retrieve relevant documents based on user queries
- Components:
  - **Query parser**: Breaks down user queries into individual words
  - **Indexing**: Builds a data structure (e.g., inverted index) to store document information
  - **Ranking**: Evaluates relevance of documents based on query terms

### 2.4 The Web as an IR System

- Definition: The web as a vast repository of documents, indexed and searchable
- Challenges:
  - **Diversity**: Wide range of document types and formats
  - **Noise**: Irrelevant content, errors, and spam

### 2.5 Document Representation

- Definitions:
  - **Vector space model**: Represents documents as vectors of words or features
  - **Term frequency-inverse document frequency (TF-IDF)**: Weighted representation of words in documents
- Formulas:
  - TF-IDF: $w_i = t_i \cdot \frac{1}{|D|}$, where $w_i$ is the weight of word $i$, $t_i$ is its frequency, and $|D|$ is the total number of documents

## Important Formulas and Definitions

- **TF-IDF**: $w_i = t_i \cdot \frac{1}{|D|}$, where $w_i$ is the weight of word $i$, $t_i$ is its frequency, and $|D|$ is the total number of documents
- **Vector space model**: Represents documents as vectors of words or features
- **Cosine similarity**: Measures similarity between two vectors using the cosine of the angle between them: $\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$
