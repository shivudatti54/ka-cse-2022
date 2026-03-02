# Information Retrieval Fundamentals

## Introduction to Information Retrieval (IR)

**Information Retrieval (IR)** is the scientific field concerned with the structure, analysis, organization, storage, searching, and retrieval of information, particularly from large collections of unstructured text. At its core, IR addresses a fundamental human need: finding the most relevant information to satisfy a specific need from a vast corpus of data.

A classic IR system, like a web search engine, does not return "answers" but rather *documents* (web pages, articles, etc.) that are predicted to contain the information relevant to a user's **query**. The effectiveness of an IR system is measured by its ability to retrieve **all** the relevant documents (**recall**) and **only** the relevant documents (**precision**).

## Key Components of an IR System

An IR system is typically composed of several key components that work in tandem.

```
+-------------------+    +---------------------+    +-------------------+
|   Document Corpus |--->|   Indexing Module   |--->|   Search Index    |
+-------------------+    +---------------------+    +-------------------+
                                                             |
                                                             v
+-------------------+    +---------------------+    +-------------------+
|   User Query      |--->|   Ranking Module    |<---|   Retrieval Module|
+-------------------+    +---------------------+    +-------------------+
                                                             |
                                                             v
                                                     +-------------------+
                                                     |   Results (Ranked |
                                                     |   List of Docs)   |
                                                     +-------------------+
```

1.  **Document Corpus:** The collection of documents to be searched (e.g., all web pages, a library of scientific articles).
2.  **Indexing Module:** This module processes the raw text of the documents. It performs tasks like tokenization, stop-word removal, and stemming (discussed later) to create a normalized representation of the content. The output is a **search index**, a data structure (like an **inverted index**) that allows for fast lookup of which documents contain which terms.
3.  **User Query:** The input from the user expressing their information need.
4.  **Retrieval Module:** This module takes the user's query, processes it similarly to the documents, and uses the search index to quickly find all documents that contain at least one of the query terms.
5.  **Ranking Module:** This is the intelligent core of the system. It scores and ranks the retrieved documents based on how well they match the query. Different IR models (e.g., Boolean, Vector Space, Probabilistic) use different algorithms for this ranking.
6.  **Results:** The final output is an ordered list of documents, presented to the user from most to least relevant.

## The Inverted Index

The **inverted index** is the fundamental data structure that makes large-scale IR efficient. Instead of storing a list of words for each document (the forward index), it stores a list of documents for each word.

**Example Corpus:**
*   Doc1: "the cat sat on the mat"
*   Doc2: "the dog sat on the log"

**Building the Index:**
1.  **Tokenization:** Split text into terms (words).
    *   Doc1: ["the", "cat", "sat", "on", "the", "mat"]
    *   Doc2: ["the", "dog", "sat", "on", "the", "log"]
2.  **Normalization:** Convert to lowercase and apply stemming (e.g., "sat" -> "sat", "log" -> "log").
    *   Doc1: ["the", "cat", "sat", "on", "the", "mat"]
    *   Doc2: ["the", "dog", "sat", "on", "the", "log"]
3.  **Stop-word Removal:** Remove extremely common words (e.g., "the", "on").
    *   Doc1: ["cat", "sat", "mat"]
    *   Doc2: ["dog", "sat", "log"]
4.  **Create Postings Lists:** For each unique term, list the documents it appears in.
    *   `cat -> [Doc1]`
    *   `dog -> [Doc2]`
    *   `sat -> [Doc1, Doc2]`
    *   `mat -> [Doc1]`
    *   `log -> [Doc2]`

This structure allows a query for "sat" to instantly return `[Doc1, Doc2]` without scanning every document.

## Classical IR Models

### 1. Boolean Model
The Boolean model is one of the oldest and simplest IR models. It treats retrieval as a logical operation. Documents are represented as sets of terms, and queries are constructed using the logical operators AND, OR, and NOT.

*   **Query:** `cat AND mat`
*   **Execution:** Find the intersection of the postings lists for "cat" (`[Doc1]`) and "mat" (`[Doc1]`). Result: `[Doc1]`.
*   **Query:** `cat OR dog`
*   **Execution:** Find the union of the postings lists for "cat" (`[Doc1]`) and "dog" (`[Doc2]`). Result: `[Doc1, Doc2]`.
*   **Pros:** Simple to implement and understand; precise for well-defined queries.
*   **Cons:** No notion of partial match or ranking; everything is either a match or not. A document with one occurrence of "cat" is treated the same as a document with one hundred. This binary outcome often leads to poor user experience.

### 2. Vector Space Model (VSM)
The Vector Space Model addresses the ranking limitation of the Boolean model. Both documents and queries are represented as vectors in a high-dimensional space, where each dimension corresponds to a unique term in the vocabulary.

*   **Term Frequency (TF):** How often a term appears in a document. `tf(t,d)`. More frequent terms are more important to the document's meaning.
*   **Inverse Document Frequency (IDF):** How rare a term is across the entire collection. `idf(t) = log(N / df(t))`, where `N` is the total number of documents and `df(t)` is the number of documents containing the term `t`. Common terms (e.g., "the") are penalized.
*   **TF-IDF Weight:** The combined weight for a term in a document is `tf-idf(t,d) = tf(t,d) * idf(t)`.

The similarity between a query vector `q` and a document vector `d` is calculated using the **Cosine Similarity**:
`sim(q, d) = (q • d) / (||q|| * ||d||)`

This measures the cosine of the angle between the two vectors. A value of 1 means identical orientation (very similar), 0 means orthogonal (no similarity).

**Example:**
Imagine a vocabulary: [cat, dog, sat, mat, log]. Let's calculate simple TF vectors (ignoring IDF for clarity).

*   Doc1: "cat sat mat" -> Vector: [1, 0, 1, 1, 0]
*   Doc2: "dog sat log" -> Vector: [0, 1, 1, 0, 1]
*   Query: "cat dog" -> Vector: [1, 1, 0, 0, 0]

`sim(Query, Doc1) = ([1,1,0,0,0] • [1,0,1,1,0]) / (√2 * √3) = (1*1 + 1*0) / (√2 * √3) = 1 / (√6) ≈ 0.41`
`sim(Query, Doc2) = ([1,1,0,0,0] • [0,1,1,0,1]) / (√2 * √3) = (1*0 + 1*1) / (√2 * √3) = 1 / (√6) ≈ 0.41`

In this simple case, both scores are equal. Adding IDF would change the weights and likely break the tie.

*   **Pros:** Allows partial matching and ranking; simple and effective.
*   **Cons:** Assumes terms are independent (which is not true; "hot" and "dog" vs. "hot dog"), can be computationally heavy for very large vocabularies.

### 3. Probabilistic Models
Probabilistic models, like the **BM25** algorithm, rank documents based on the *probability* that they are relevant to a given query. BM25 is a bag-of-words retrieval function that combines TF, IDF, and document length normalization in a probabilistic framework. It is considered a state-of-the classical baseline and is highly effective.

The core idea is to score a document based on how well its term frequencies match the frequencies one would expect to see in a relevant document. It has tunable parameters to control the saturation of term frequency (how quickly more occurrences stop adding value) and the impact of document length.

*   **Pros:** Very strong empirical performance; theoretical foundation.
*   **Cons:** More complex to understand and implement than VSM.

| Model | Ranking | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Boolean** | No (Binary) | Simple, precise | No ranking, poor user experience |
| **Vector Space (VSM)** | Yes (Cosine Similarity) | Effective ranking, simple | Assumes term independence |
| **Probabilistic (BM25)** | Yes (Probability of Relevance) | Strong performance, theoretical basis | More complex |

## Lexical Resources for IR

### Stemmers and Lemmatizers
These are crucial for **term normalization** during indexing and query processing. They reduce inflected words to a common base form.

*   **Stemming:** A crude heuristic process that chops off word endings. (e.g., "running" -> "run", "cats" -> "cat", "universal" -> "univers"). The **Porter Stemmer** is a common algorithm for English.
*   **Lemmatization:** A more sophisticated process that uses vocabulary and morphological analysis to return the base or dictionary form (lemma) of a word. (e.g., "better" -> "good", "is"/"are" -> "be").

Stemming is faster and simpler, while lemmatization is more accurate but requires more linguistic knowledge. For IR, stemming is often sufficient.

### WordNet
**WordNet** is a large lexical database of English. Nouns, verbs, adjectives, and adverbs are grouped into sets of cognitive synonyms (**synsets**), each expressing a distinct concept. It is a critical resource for tackling the issue of **vocabulary mismatch** (where a document uses different words than the query to describe the same concept).

*   **Synonymy:** Finding synonyms (e.g., "car" and "automobile").
*   **Hypernymy/Hyponymy:** Finding more general (hypernym) or more specific (hyponym) terms. (e.g., "dog" is a hyponym of "animal"; "animal" is a hypernym of "dog").
*   **Use in IR:** Query expansion. A search for "car" can be automatically expanded to include documents containing "automobile", "vehicle", "sedan", etc., potentially improving recall.

### FrameNet
**FrameNet** is a resource based on **Frame Semantics**. It defines semantic frames, which are schematic representations of situations involving various participants, props, and other conceptual roles. For example, the `Commerce_buy` frame involves a **Buyer**, a **Seller**, **Goods**, and **Money**.

*   **Use in IR:** Allows for deeper semantic search beyond just keywords. A query like "buy a book" could be matched with documents describing someone "purchasing a novel" or "paying for a textbook", even if the word "buy" is never used, because they evoke the same semantic frame.

### Research Corpora
Large, annotated text corpora are essential for training and evaluating modern IR and NLP systems.
*   **TREC Collections:** A series of standard text corpora and evaluation tasks run by the Text Retrieval Conference (TREC). They provide datasets, queries, and human-judged relevance assessments, allowing researchers to compare the performance of different IR algorithms objectively.

## Alternative/Modern Models

The classical models are **term-based**. Modern approaches, often used in web search, incorporate many additional signals:
*   **PageRank:** Analyzes the link structure between web pages to determine their importance or authority.
*   **Learning to Rank (LTR):** Uses machine learning models to combine hundreds of features (e.g., TF-IDF score, PageRank, document freshness, user click-through data) to rank documents.
*   **Neural IR Models:** Use deep learning (e.g., transformers like BERT) to create dense vector representations of queries and documents, capturing semantic meaning much more effectively than sparse TF-IDF vectors. These models can understand context and paraphrase much better.

## Exam Tips

1.  **Understand the Components:** Be able to draw and explain the diagram of an IR system's architecture. Know the role of each module.
2.  **Master the Inverted Index:** You should be able to walk through the steps of creating a simple inverted index from a small corpus. This is a common exam question.
3.  **Compare and Contrast Models:** Focus on the differences between the Boolean, Vector Space, and Probabilistic models. Create a table for yourself to memorize their characteristics. Be prepared to explain the TF-IDF weighting scheme and cosine similarity.
4.  **Know Your Resources:** Understand what WordNet and FrameNet are and how they can be used to improve IR (e.g., query expansion vs. semantic search). Be able to differentiate between stemming and lemmatization.
5.  **Think About Evaluation:** Remember that IR is evaluated on the trade-off between **Precision** (fraction of retrieved documents that are relevant) and **Recall** (fraction of relevant documents that are retrieved). A perfect system gets 1.0 for both.