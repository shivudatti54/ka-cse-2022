**Chapter 13: Web Retrieval**

**13.2: Web Retrieval Models**

Web retrieval refers to the process of searching and retrieving relevant web pages from a large corpus of web pages. Web retrieval models are algorithms that aim to rank web pages in order of relevance to a query. The goal of web retrieval is to find the most relevant web pages that match the user's query.

**13.2.1: Information Retrieval (IR) Models**

Information retrieval (IR) models are a type of web retrieval model that uses statistical and mathematical techniques to rank web pages. IR models are based on the idea that web pages can be represented as vectors in a high-dimensional space, where each dimension corresponds to a feature of the web page (e.g., keyword frequency, link count, etc.).

**13.2.2: PageRank**

PageRank is a widely used web retrieval model developed by Google's founders, Larry Page and Sergey Brin. It is based on the idea that a page's importance can be measured by the number and quality of links pointing to it. PageRank uses a matrix equation to iterate over the web graph, where each page is represented as a node, and the edges represent links between pages.

**Example:**

Suppose we have a web page with the following links:

- Link 1 -> Page A
- Link 2 -> Page B
- Link 3 -> Page C

PageRank will calculate the PageRank score for each page as follows:

- Page A: 1/3 + 1/3 = 2/3 (because it has two outgoing links)
- Page B: 1/3 (because it has only one outgoing link)
- Page C: 1/3 (because it has only one outgoing link)

**13.2.3: TF-IDF**

Term Frequency-Inverse Document Frequency (TF-IDF) is a technique used to weight the importance of words in a web page. The idea is to count the frequency of each word in the page and divide it by the frequency of the word in the entire document collection. This gives a higher weight to words that are rare in the document collection but appear frequently in the page.

**Example:**

Suppose we have a web page with the following keywords:

- Keyword 1: "machine learning" (frequency: 5)
- Keyword 2: "deep learning" (frequency: 2)
- Keyword 3: "neural networks" (frequency: 1)

The TF-IDF score for each keyword would be:

- Keyword 1: 5/10 = 0.5 (because it appears 5 times in the page and 10 times in the entire document collection)
- Keyword 2: 2/10 = 0.2 (because it appears 2 times in the page and 10 times in the entire document collection)
- Keyword 3: 1/10 = 0.1 (because it appears only 1 time in the page and 10 times in the entire document collection)

**13.3: Web Search Engines**

A web search engine is a software system that searches and retrieves relevant web pages from a large corpus of web pages. Web search engines use web retrieval models to rank web pages in order of relevance to a query.

**13.3.1: Search Engine Architectures**

There are several search engine architectures, including:

- **Crawling-based search engines**: These search engines use web crawlers to crawl the web and index web pages.
- **Index-based search engines**: These search engines use a pre-existing index of web pages to retrieve results.
- **Hybrid search engines**: These search engines use a combination of crawling and indexing to retrieve results.

**Example:**

Google is a crawling-based search engine that uses web crawlers to crawl the web and index web pages.

**13.3.2: Search Engine Ranking**

Search engine ranking refers to the process of ranking web pages in order of relevance to a query. Search engine ranking algorithms use web retrieval models to rank web pages.

**13.3.2.1: PageRank-based ranking**

PageRank is a widely used ranking algorithm that uses PageRank scores to rank web pages.

**13.3.2.2: TF-IDF-based ranking**

TF-IDF is a ranking algorithm that uses TF-IDF scores to rank web pages.

**13.3.2.3: Hybrid ranking**

Hybrid ranking algorithms use a combination of PageRank and TF-IDF to rank web pages.

**Example:**

Suppose we have a query "machine learning". Google would use a combination of PageRank and TF-IDF to rank web pages as follows:

- Page 1: 10 (because it has a high PageRank score and contains the keyword "machine learning" with a high TF-IDF score)
- Page 2: 5 (because it has a lower PageRank score but contains the keyword "machine learning" with a high TF-IDF score)
- Page 3: 1 (because it has a low PageRank score and contains the keyword "machine learning" with a low TF-IDF score)

**13.4: Web Retrieval Techniques**

Web retrieval techniques refer to the methods used to improve the accuracy of web retrieval systems. Web retrieval techniques include:

- **Preprocessing**: Preprocessing techniques are used to preprocess web pages before they are indexed. Examples include stemming and lemmatization.
- **Indexing**: Indexing techniques are used to index web pages before they are retrieved. Examples include inverted indexes and Bloom filters.
- **Ranking**: Ranking techniques are used to rank web pages in order of relevance to a query. Examples include PageRank and TF-IDF.

**13.4.1: Preprocessing Techniques**

Preprocessing techniques are used to preprocess web pages before they are indexed. Examples include:

- **Stemming**: Stemming is a technique that reduces words to their base form.
- **Lemmatization**: Lemmatization is a technique that reduces words to their base form using a dictionary.
- **Stopword removal**: Stopword removal is a technique that removes common words like "the" and "and" from web pages.

**13.4.2: Indexing Techniques**

Indexing techniques are used to index web pages before they are retrieved. Examples include:

- **Inverted indexes**: Inverted indexes are data structures that store the words in a web page and their document IDs.
- **Bloom filters**: Bloom filters are data structures that store a set of words and indicate whether a word is likely to be present in a web page.

**13.4.3: Ranking Techniques**

Ranking techniques are used to rank web pages in order of relevance to a query. Examples include:

- **PageRank**: PageRank is a ranking algorithm that uses PageRank scores to rank web pages.
- **TF-IDF**: TF-IDF is a ranking algorithm that uses TF-IDF scores to rank web pages.

**13.5: Web Retrieval Applications**

Web retrieval applications refer to the ways in which web retrieval systems are used in real-world applications. Web retrieval applications include:

- **Search engines**: Search engines are web retrieval systems that allow users to search for web pages.
- **Information retrieval systems**: Information retrieval systems are web retrieval systems that allow users to retrieve relevant web pages.
- **Recommendation systems**: Recommendation systems are web retrieval systems that recommend web pages to users based on their past behavior.

**Example:**

Suppose we have a search engine that uses PageRank and TF-IDF to rank web pages. The search engine would use this ranking algorithm to rank web pages as follows:

- Page 1: 10 (because it has a high PageRank score and contains the keyword "machine learning" with a high TF-IDF score)
- Page 2: 5 (because it has a lower PageRank score but contains the keyword "machine learning" with a high TF-IDF score)
- Page 3: 1 (because it has a low PageRank score and contains the keyword "machine learning" with a low TF-IDF score)

**Further Reading:**

- **"Information Retrieval" by Edward C. Gildea**
- **"Search Engine Optimization" by Jill Wharton**
- **"Web Search Engines: The Mechanics" by S. S. Srinivasan**
