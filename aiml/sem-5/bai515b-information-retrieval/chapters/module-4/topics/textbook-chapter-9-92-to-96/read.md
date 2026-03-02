# **Indexing and Searching: Inverted Indexes, Signature Files, Suffix Trees and Suffix Arrays**

## **9.2 Inverted Indexes**

### Definition

An inverted index is a data structure used in information retrieval systems to store the index of words or phrases in a document, along with their locations in the document.

### Properties

- Stores word or phrase occurrences in documents
- Allows for fast lookup and retrieval of documents containing a given word or phrase
- Typically implemented as a collection of arrays or lists, where each array or list represents a word or phrase and its corresponding document IDs

### Example

Suppose we have the following documents:

| Document ID | Document Content                            |
| ----------- | ------------------------------------------- |
| 1           | The quick brown fox jumps over the lazy dog |
| 2           | The sun rises over the hills in the east    |
| 3           | Foxes are fast and agile animals            |

Inverted index for the words "fox" and "the":

| Word | Document IDs |
| ---- | ------------ |
| fox  | 1, 3         |
| the  | 1, 2         |

### Advantages

- Fast lookup and retrieval of documents containing a given word or phrase
- Allows for efficient ranking of documents based on relevance

### Disadvantages

- Requires additional storage space for the inverted index
- Can be computationally expensive to build and maintain

## **9.3 Signature Files**

### Definition

A signature file is a data structure used in information retrieval systems to store a compact representation of a document, allowing for efficient matching between documents.

### Properties

- Stores a unique signature for each document, based on its contents
- Typically implemented as a collection of one-bit or byte arrays, where each array represents a document and its corresponding signature
- Allows for fast matching between documents based on their signatures

### Example

Suppose we have the following documents:

| Document ID | Document Content                            |
| ----------- | ------------------------------------------- |
| 1           | The quick brown fox jumps over the lazy dog |
| 2           | The sun rises over the hills in the east    |
| 3           | Foxes are fast and agile animals            |

Signature file for the documents:

| Document ID | Signature |
| ----------- | --------- |
| 1           | 10101010  |
| 2           | 01010101  |
| 3           | 11001100  |

### Advantages

- Fast matching between documents based on their signatures
- Compact representation of documents

### Disadvantages

- Requires additional storage space for the signature file
- Can be computationally expensive to build and maintain

## **9.4 Suffix Trees**

### Definition

A suffix tree is a data structure used in information retrieval systems to store the suffixes of a document, allowing for efficient matching between documents.

### Properties

- Stores the suffixes of a document in a tree-like structure
- Typically implemented as a collection of nodes, where each node represents a suffix and its corresponding parent
- Allows for fast matching between documents based on their suffixes

### Example

Suppose we have the following documents:

| Document ID | Document Content                            |
| ----------- | ------------------------------------------- |
| 1           | The quick brown fox jumps over the lazy dog |
| 2           | The sun rises over the hills in the east    |

Suffix tree for the documents:

        *
       / \
      E E E
     / \   / \
    n E r s o o

/ \ / \
 u x i m p s

### Advantages

- Fast matching between documents based on their suffixes
- Allows for efficient retrieval of substrings

### Disadvantages

- Requires additional storage space for the suffix tree
- Can be computationally expensive to build and maintain

## **9.5 Suffix Arrays**

### Definition

A suffix array is a data structure used in information retrieval systems to store the sorted suffixes of a document, allowing for efficient matching between documents.

### Properties

- Stores the sorted suffixes of a document in an array
- Typically implemented as a collection of integers, where each integer represents a suffix and its corresponding position in the array
- Allows for fast matching between documents based on their suffixes

### Example

Suppose we have the following documents:

| Document ID | Document Content                            |
| ----------- | ------------------------------------------- |
| 1           | The quick brown fox jumps over the lazy dog |
| 2           | The sun rises over the hills in the east    |

Suffix array for the documents:

| Suffix | Position |
| ------ | -------- |
| east   | 2        |
| dog    | 1        |
| fox    | 3        |
| hills  | 4        |
| jumps  | 5        |
| lazy   | 6        |
| over   | 7        |
| quick  | 8        |
| rises  | 9        |
| sun    | 10       |
| the    | 11       |

### Advantages

- Fast matching between documents based on their suffixes
- Allows for efficient retrieval of substrings

### Disadvantages

- Requires additional storage space for the suffix array
- Can be computationally expensive to build and maintain

### Comparison of Indexing and Searching Techniques

---

|                              | Inverted Index    | Signature File    | Suffix Tree       | Suffix Array      |
| ---------------------------- | ----------------- | ----------------- | ----------------- | ----------------- |
| **Matching Time**            | O(m)              | O(n)              | O(m)              | O(n)              |
| **Matching Space**           | O(m)              | O(n)              | O(n)              | O(n)              |
| **Document Representation**  | Document-specific | Document-specific | Document-specific | Document-specific |
| **Computational Complexity** | High              | High              | High              | High              |

Note: m and n represent the number of words or phrases in the document and the number of documents in the system, respectively.
