# Information Retrieval Models - Classical and Alternative

## Introduction to Information Retrieval (IR)

Information Retrieval (IR) is the process of obtaining information resources relevant to an information need from a collection of resources. The fundamental goal of IR systems is to retrieve documents that satisfy a user's information need, typically expressed as a query.

An IR system consists of:
- **Document Collection**: The set of documents to be searched
- **Query**: The user's information need expressed in natural language
- **Retrieval Model**: The mathematical framework that defines how documents are represented, how queries are represented, and how relevance is calculated

## Classical IR Models

### 1. Boolean Model

The Boolean model is one of the oldest and simplest IR models based on set theory and Boolean algebra.

**Key Concepts:**
- Documents are represented as sets of terms
- Queries are Boolean expressions using AND, OR, and NOT operators
- Retrieval is based on exact match of the Boolean conditions

**Example:**
Query: "information AND retrieval NOT boolean"
This would retrieve documents containing both "information" and "retrieval" but excluding those containing "boolean"

```
+----------------+    +----------------+    +----------------+
|   Document 1   |    |   Document 2   |    |   Document 3   |
| - information  |    | - information  |    | - retrieval    |
| - retrieval    |    | - boolean      |    | - system       |
| - system       |    | - system       |    | - evaluation   |
+----------------+    +----------------+    +----------------+

Query: "information AND retrieval NOT boolean"

Result: Document 1 matches (has both terms, no "boolean")
```

**Advantages:**
- Simple to implement and understand
- Precise matching based on Boolean conditions

**Limitations:**
- No ranking of results (all matching documents are equally relevant)
- No partial matching
- Requires users to understand Boolean logic

### 2. Vector Space Model (VSM)

The Vector Space Model represents documents and queries as vectors in a high-dimensional space, where each dimension corresponds to a term in the collection.

**Key Concepts:**
- **Term Frequency (tf)**: How often a term appears in a document
- **Inverse Document Frequency (idf)**: How rare a term is across the collection
- **TF-IDF**: Combination of tf and idf to weight terms
- **Cosine Similarity**: Measures the angle between document and query vectors

**TF-IDF Calculation:**
```
tf(t,d) = frequency of term t in document d
idf(t) = log(N/df(t)) where N = total documents, df(t) = documents containing t
tf-idf(t,d) = tf(t,d) * idf(t)
```

**Example:**
Consider 3 documents and query "information retrieval"

```
Document 1: "information retrieval systems"
Document 2: "information theory"
Document 3: "data retrieval methods"
Query: "information retrieval"

Term weights using tf-idf:

          Doc1   Doc2   Doc3   Query
information  0.5   0.5     0      1
retrieval    0.5     0     0      1
systems      0.5     0     0      0
theory         0   0.5     0      0
data           0     0   0.5      0
methods        0     0   0.5      0

Cosine similarity calculation:
sim(Doc1, Query) = (0.5*1 + 0.5*1 + 0.5*0 + ...) / (||Doc1|| * ||Query||)
```

**Advantages:**
- Provides ranked results
- Handles partial matching
- Intuitive geometric interpretation

**Limitations:**
- Assumes term independence
- Doesn't capture semantic relationships

### 3. Probabilistic Model

The probabilistic model ranks documents based on the probability of relevance to the query.

**Key Concepts:**
- **Probability Ranking Principle**: Documents should be ranked by decreasing probability of relevance
- **Binary Independence Model**: Assumes term presence/absence is independent given relevance
- **Okapi BM25**: Popular probabilistic ranking function

**BM25 Formula:**
```
score(D,Q) = Σ[i=1 to n] IDF(q_i) * (f(q_i,D) * (k_1 + 1)) / (f(q_i,D) + k_1 * (1 - b + b * |D|/avgdl))
Where:
- f(q_i,D) = frequency of term q_i in document D
- |D| = length of document D
- avgdl = average document length
- k_1 and b = tuning parameters
- IDF(q_i) = log((N - n(q_i) + 0.5) / (n(q_i) + 0.5))
```

**Advantages:**
- Strong theoretical foundation
- Excellent empirical performance
- Handles document length normalization

**Limitations:**
- Requires relevance feedback for optimal performance
- Complex parameter tuning

## Alternative IR Models

### 1. Language Modeling Approach

The language modeling approach views both documents and queries as language models and estimates the probability that a document's language model generated the query.

**Key Concepts:**
- **Document Language Model**: Probability distribution over terms for a document
- **Query Likelihood**: P(Q|D) = probability of query given document model
- **Smoothing**: Techniques to handle unseen words (Jelinek-Mercer, Dirichlet)

**Query Likelihood Formula:**
```
P(Q|D) = Π[q in Q] P(q|D)
P(q|D) = (1-λ) * (c(q,D)/|D|) + λ * P(q|Collection)
```

**Example:**
```
Document: "information retrieval systems retrieve information"
Query: "information retrieval"

P("information"|D) = (2/5) = 0.4
P("retrieval"|D) = (1/5) = 0.2
P(Q|D) = 0.4 * 0.2 = 0.08
```

**Advantages:**
- Strong theoretical foundation in statistical language modeling
- Natural handling of term dependencies
- Good empirical performance

**Limitations:**
- Requires smoothing for zero probability terms
- Can be computationally intensive

### 2. Latent Semantic Indexing (LSI)

LSI uses singular value decomposition to project documents and queries into a latent semantic space.

**Key Concepts:**
- **Term-Document Matrix**: Matrix where rows=terms, columns=documents, values=term weights
- **Singular Value Decomposition (SVD)**: Matrix factorization technique
- **Latent Concepts**: Reduced-dimensional representation capturing semantic relationships

**Process:**
1. Create term-document matrix A
2. Apply SVD: A = UΣVᵀ
3. Reduce dimensionality by keeping only top k singular values
4. Project documents and queries into reduced space

```
Original Space:       Reduced Space:
+---+---+---+        +---+---+
| t | d | w |        | c | d |
+---+---+---+        +---+---+
| 1 | 1 | 2 |   SVD  | 1 | 1 |
| 1 | 2 | 1 |  ====> | 1 | 2 |
| 2 | 1 | 1 |        | 2 | 1 |
| 2 | 2 | 2 |        | 2 | 2 |
+---+---+---+        +---+---+
```

**Advantages:**
- Captures semantic relationships between terms
- Handles synonymy and polysemy
- Reduces dimensionality

**Limitations:**
- Computationally expensive for large collections
- Difficult to interpret latent concepts

### 3. Neural IR Models

Neural models use deep learning techniques to learn representations of documents and queries.

**Key Concepts:**
- **Word Embeddings**: Distributed representations of words (Word2Vec, GloVe)
- **Deep Neural Networks**: Multi-layer networks that learn complex representations
- **Attention Mechanisms**: Focus on relevant parts of documents/queries

**Common Architectures:**
- **DSSM**: Deep Structured Semantic Model
- **DRMM**: Deep Relevance Matching Model
- **BERT**: Bidirectional Encoder Representations from Transformers

**Advantages:**
- Captures complex semantic relationships
- Learns representations from data
- State-of-the-art performance

**Limitations:**
- Requires large amounts of training data
- Computationally intensive
- Black box nature makes interpretation difficult

## Comparison of IR Models

| Model | Representation | Ranking Method | Advantages | Limitations |
|-------|----------------|----------------|------------|-------------|
| Boolean | Set of terms | Exact match | Simple, precise | No ranking, no partial match |
| Vector Space | Term vectors | Cosine similarity | Ranking, partial match | Term independence assumption |
| Probabilistic | Probability distributions | Probability of relevance | Theoretical foundation, handles length | Needs relevance feedback |
| Language Model | Language models | Query likelihood | Handles dependencies, good performance | Needs smoothing |
| LSI | Latent concepts | Cosine in reduced space | Handles synonymy, reduces dimension | Computationally expensive |
| Neural | Learned embeddings | Neural similarity | State-of-art, captures semantics | Data hungry, complex |

## Exam Tips

1. **Understand the fundamentals**: Focus on how each model represents documents and queries, and how relevance is calculated.
2. **Compare and contrast**: Be prepared to discuss advantages and limitations of different models.
3. **Mathematical formulations**: Know the key formulas (TF-IDF, BM25, query likelihood).
4. **Practical applications**: Understand which models are suitable for different scenarios.
5. **Evolution of models**: Be able to explain how alternative models address limitations of classical models.
6. **Focus on concepts**: Rather than memorizing formulas, understand the underlying principles and intuitions.