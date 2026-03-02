# Module 5: Web Retrieval

## Introduction

Web Retrieval is a specialized sub-field of Information Retrieval (IR) that deals with the unique challenges of searching and indexing the vast, decentralized, and ever-evolving collection of documents known as the World Wide Web. Unlike searching a controlled, static corpus like a digital library, web retrieval must handle an enormous scale, heterogeneous content, and a web structure where hyperlinks connect pages. This module explores the core concepts and algorithms that power modern search engines.

## Core Concepts

### 1. The Web as a Graph

The fundamental shift in thinking for web retrieval is to view the web not just as a collection of texts, but as a directed graph.
*   **Nodes:** Web pages.
*   **Edges:** Hyperlinks from one page to another.

This graph structure provides crucial information beyond the text on a page. A link from page A to page B can be interpreted as a vote of confidence or an endorsement from A to B. This insight is the foundation for the most famous web retrieval algorithm: PageRank.

### 2. PageRank

Developed by Larry Page and Sergey Brin at Stanford, PageRank is a link analysis algorithm that assigns a numerical weight (a "PageRank score") to each document on the web, measuring its relative importance.

**How it works (Simplified):**
Imagine a surfer randomly clicking on links. The PageRank of a page is the probability that this "random surfer" will be on that page at any given time. A page has high rank if:
*   Many other important pages link to it.
*   The pages that link to it do not link to many other pages (i.e., the vote isn't diluted).

**The Algorithm:**
The PageRank value for a page $P_i$ is calculated as:

$$PR(P_i) = \frac{1-d}{N} + d \sum_{P_j \in L(P_i)} \frac{PR(P_j)}{C(P_j)}$$

Where:
*   $PR(P_i)$ is the PageRank of page $P_i$.
*   $N$ is the total number of pages in the index.
*   $L(P_i)$ is the set of pages that link to $P_i$.
*   $C(P_j)$ is the number of outbound links on page $P_j$.
*   $d$ is a damping factor (usually set to ~0.85), representing the probability that the surfer will continue clicking links.

**Example:**
Consider a tiny web of three pages: A, B, and C.
*   Page B links to A and C.
*   Page C links to A.
*   Page A links to B.

Initially, all pages have a rank of 1/3. Using the formula iteratively, we would see Page A's rank increase because it receives votes from both B and C, while B only receives a vote from A (and shares its vote with C).

### 3. HITS (Hyperlink-Induced Topic Search)

Another important algorithm, HITS, was developed by Jon Kleinberg. It identifies two types of pages for a given query topic:
*   **Hubs:** Pages that act as directories or link lists, pointing to many good, authoritative pages on a topic. (e.g., "Top 10 Machine Learning Blogs")
*   **Authorities:** Pages that are high-quality, trusted sources of information on the topic, linked to by many hubs. (e.g., the official TensorFlow documentation)

**How it works:**
1.  A root set of pages relevant to the query is retrieved via a text-based IR system.
2.  A base set is expanded by including pages that link to or are linked from the root set.
3.  Two scores are iteratively calculated for each page in the base set:
    *   **Authority Score:** Sum of the hub scores of pages that point to it.
    *   **Hub Score:** Sum of the authority scores of pages it points to.
4.  After convergence, the top authorities and hubs are returned.

### 4. The "Crawler" and Indexing

A web crawler (or spider) is a software bot that systematically browses the web to build the index. It starts from a seed set of URLs, downloads the pages, extracts all the links within them, and adds those new URLs to a queue to be visited next. This process of discovering and fetching web pages is the first and most critical step before any ranking can be applied.

## Summary of Key Points

| Concept | Description | Key Idea |
| :--- | :--- | :--- |
| **Web as a Graph** | Views web pages as nodes and hyperlinks as edges. | Structure provides information beyond text content. |
| **PageRank** | Algorithm to measure page importance based on link structure. | A page is important if important pages link to it. Uses the "random surfer" model. |
| **HITS Algorithm** | Identifies **Hubs** (good link lists) and **Authorities** (trusted content sources) for a topic. | Authority and hub scores reinforce each other iteratively. |
| **Web Crawler** | Software that automatically traverses the web to discover and download pages for indexing. | The foundational process for building a search engine's database. |

**Conclusion:** Web retrieval moves beyond simple text matching by leveraging the graph structure of the web. Algorithms like PageRank and HITS use the collective wisdom embedded in hyperlinks to rank pages by quality and authority, which is essential for sorting the trillions of documents on the web into a useful result list.