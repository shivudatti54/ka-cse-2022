# **Revision Notes: Chapter 9.2-9.6 - Information Retrieval**

### 9.2 Inverted Indexes

- An inverted index is a data structure that maps keywords to documents containing those keywords.
- It is used for fast retrieval of documents based on search queries.
- Advantages: efficient search, fast lookup.
- Disadvantages: high storage requirements, complex construction.

### 9.3 Signature Files

- A signature file is a data structure that maps a set of keywords to a document's signature (a unique string identifying the document).
- It is used for fast retrieval of documents based on a set of keywords.
- Advantages: efficient search, fast lookup.
- Disadvantages: high storage requirements, complex construction.

### 9.4 Suffix Trees

- A suffix tree is a data structure that presents all the suffixes of a given string in a tree-like format.
- It is used for matching patterns in strings.
- Advantages: efficient matching, fast lookup.
- Disadvantages: high construction time, high space complexity.

### 9.5 Suffix Arrays

- A suffix array is an array that contains the starting positions of all the suffixes of a given string.
- It is used for efficient matching of patterns in strings.
- Advantages: efficient matching, fast lookup.
- Disadvantages: high construction time, high space complexity.

## **Important Formulas and Definitions**

- **Inverted Index Construction Formula**: `I = (T \* K) / (K + 1)`, where `I` is the number of unique keywords, `T` is the total number of documents, and `K` is the number of unique keywords in each document.
- **Signature File Construction Formula**: `S = (T \* K) / (K + 1)`, where `S` is the number of unique signatures, `T` is the total number of documents, and `K` is the number of unique keywords in each document.
- **Suffix Tree Construction Formula**: `T = O(n \* m)`, where `n` is the length of the string and `m` is the maximum length of a suffix.
- **Suffix Array Construction Formula**: `A = O(n \* m)`, where `n` is the length of the string and `m` is the maximum length of a suffix.

## **Theorems**

- **Inverted Index Theorem**: An inverted index can be constructed in `O(n \* m)` time, where `n` is the number of documents and `m` is the maximum number of unique keywords in each document.
- **Signature File Theorem**: A signature file can be constructed in `O(n \* m)` time, where `n` is the number of documents and `m` is the maximum number of unique keywords in each document.
