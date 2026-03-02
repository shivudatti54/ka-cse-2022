# Sequential Searching in Information Retrieval

## Introduction

In the domain of Information Retrieval (IR), searching refers to the process of scanning a collection of documents to identify those that match a user's query. **Sequential Searching**, also known as linear search, is the most fundamental and straightforward search algorithm. It forms the baseline against which more complex and efficient IR techniques are measured. For  engineering students, understanding sequential search is crucial as it provides a clear foundation for grasping the need for and the workings of advanced indexing and retrieval methods.

## Core Concepts

Sequential search operates on a simple principle: it examines every document in the collection one after the other, in sequence, and checks it against the query criteria. There is no pre-built index or sophisticated data structure to expedite the process. The entire collection is treated as a linear list.

The algorithm can be broken down into the following steps:

1.  **Input:** A collection of `N` documents (`D1, D2, D3, ..., Dn`) and a user Query `Q`.
2.  **Initialization:** Start from the first document in the collection (`i = 1`).
3.  **Matching:** For the current document `Di`, check if it satisfies the query `Q`. This typically involves scanning the entire text of the document for the presence of query terms.
4.  **Result Collection:** If document `Di` matches the query, add it to the result set.
5.  **Iteration:** Move to the next document (`i = i + 1`).
6.  **Termination:** Repeat steps 3-5 until all `N` documents have been examined (`i > N`).
7.  **Output:** Return the complete set of matching documents.

### Time Complexity

The computational cost of a sequential search is directly proportional to the size of the collection. If there are `N` documents and the average length of a document is `L`, the time complexity is **O(N*L)**. This means the time taken to complete the search grows linearly with the size of the dataset. For very large collections like the web or digital libraries, this linear growth becomes a significant performance bottleneck.

### Pros and Cons

| Aspect | Description |
| :--- | :--- |
| **Advantages** | • **Simplicity:** Extremely easy to understand and implement. <br> • **No Overhead:** Requires no additional memory for storing an index structure. <br> • **Dynamic Collections:** It handles dynamic collections effortlessly. New documents can be added to the end without any need for index updates. <br> • **Always Correct:** It is guaranteed to find all matching documents. |
| **Disadvantages** | • **Inefficiency:** Painfully slow for large collections as every document must be examined. <br> • **Scalability:** Does not scale well. Performance degrades linearly as the collection grows. |

## Example

Imagine a collection of 5 simple documents:
*   `D1`: "The quick brown fox"
*   `D2`: "Jumps over the lazy dog"
*   `D3`: "The dog is lazy"
*   `D4`: "The fox is quick"
*   `D5`: "A quick brown fox jumps"

And a user query: `Q: "quick fox"`

A sequential search would process this as follows:
1.  **Check D1:** Contains both "quick" and "fox" -> **Match**. Add to results.
2.  **Check D2:** Contains neither "quick" nor "fox" -> Skip.
3.  **Check D3:** Contains neither "quick" nor "fox" -> Skip.
4.  **Check D4:** Contains both "fox" and "quick" -> **Match**. Add to results.
5.  **Check D5:** Contains both "quick" and "fox" -> **Match**. Add to results.

**Final Result Set:** `{D1, D4, D5}`

This example required examining all 5 documents. For a collection of millions of documents, this process would be prohibitively time-consuming.

## Key Points / Summary

*   **Fundamental Algorithm:** Sequential search is the simplest search method where each document is checked sequentially against a query.
*   **No Index Required:** It operates directly on the raw document collection without any pre-processing or index building.
*   **Linear Time Complexity:** Its performance is O(N), making it inefficient for large-scale information retrieval systems.
*   **Baseline for Comparison:** It serves as a benchmark for evaluating the efficiency of more advanced indexed retrieval systems (like those using inverted indexes).
*   **Practical Use:** While too slow for large databases, it can be practical for very small, static, or frequently updated collections where the overhead of maintaining an index is not justified.
*   **Trade-off:** It trades off computational efficiency for implementation simplicity and zero storage overhead.