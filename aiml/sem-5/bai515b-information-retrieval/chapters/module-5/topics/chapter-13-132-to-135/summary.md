# **Chapter 13: 13.2 to 13.5 - Information Retrieval**

## **13.2: Search Engine Architecture**

- Search engines use a combination of indexing, caching, and query processing
- Common architectures:
  - Distributed architecture
  - Centralized architecture
  - Hybrid architecture
- Important components:
  - Indexing system
  - Query processing system
  - Retrieval system

## **13.3: Search Engine Ranking**

- Ranking algorithms:
  - PageRank (Google's algorithm)
  - TF-IDF (Term Frequency-Inverse Document Frequency)
  - Latent Semantic Analysis (LSA)
  - Collaborative Filtering
- Ranking metrics:
  - PageRank score
  - TF-IDF score
  - Relevance score

## **13.4: Search Engine Query Processing**

- Query types:
  - Boolean queries
  - Phrase queries
  - Natural Language Queries
- Query processing techniques:
  - Tokenization
  - Stopword removal
  - Stemming/Lemmatization
  - Query expansion

## **13.5: Search Engine Retrieval**

- Retrieval models:
  - Document Ranking Model
  - Document Retrieval Model
- Retrieval metrics:
  - Precision
  - Recall
  - F1-score
  - Mean Average Precision (MAP)

## **Important Formulas and Definitions**

- PageRank formula:
  - PR(A) = (1-d) / N + d \* (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))
  - where d is damping factor, N is number of pages, PR(Ti) is PageRank of page Ti, and C(Ti) is number of outgoing links from page Ti
- TF-IDF formula:
  - TF-IDF(Ti, Ti') = TF(Ti) \* IDF(Ti')
  - where TF(Ti) is term frequency of term Ti in document Ti, and IDF(Ti') is inverse document frequency of term Ti'

Note: This summary provides key points and important formulas, definitions, and theorems for the given topic. However, it is not an exhaustive list, and you may need to refer to additional resources for a complete understanding of the subject.
