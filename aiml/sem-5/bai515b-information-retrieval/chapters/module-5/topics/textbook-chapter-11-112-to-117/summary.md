### Revision Notes: Web Retrieval - Chapter 11.2 to 11.7

#### Introduction to Web Retrieval

- Web retrieval refers to the process of searching and retrieving relevant web pages from the vast amount of information available on the internet.
- It involves searching engines, web crawlers, indexing, and retrieval.

#### Search Engine Architectures

- **Crawlers (Web Crawlers)**
  - Software programs that continuously scan and index web pages.
  - Use URLs to navigate the web and collect relevant data.
- **Indexing**
  - Storage of web pages in a database for efficient retrieval.
  - Typically uses a document-term matrix (DTM) or inverted index.

#### Search Engine Ranking

- **Relevance Ranking**
  - Assigns a ranking score to documents based on their relevance to the search query.
  - Can use various ranking algorithms, such as PageRank or TF-IDF.
- **PageRank**
  - Algorithm developed by Google to rank web pages based on their importance.
  - Uses a matrix equation to compute the PageRank scores.

#### Managing Search Engines

- **Scalability**
  - Techniques to increase the capacity of search engines to handle large volumes of data.
- **Query Expansion**
  - Techniques to expand search queries to retrieve more relevant results.
- **Filtering and Ranking Algorithms**
  - Algorithms used to filter and rank search results.

#### Important Formulas and Definitions

- **PageRank (PR)**
  - PR(A) = (1-d) / N + d \* (PR(T1) / C(T1) + ... + PR(Tn) / C(Tn))
  - d: damping factor (0 < d < 1)
  - N: total number of pages
  - T: number of outgoing links from page A
  - C(T): number of outgoing links from page T
- **Term Frequency-Inverse Document Frequency (TF-IDF)**
  - TF: frequency of term in document
  - IDF: inverse document frequency of term in corpus
  - TF-IDF: TF \* IDF

#### Theorems and Concepts

- **Massey's Law**
  - The number of possible webs is finite and grows exponentially with the number of hyperlinks.
- **Hub-and-Spoke Model**
  - Model representing the structure of the web, with hubs (highly connected pages) and spokes (lowly connected pages).

These notes cover the key concepts and formulas in Chapter 11.2 to 11.7 of the textbook, focusing on web retrieval, search engine architectures, ranking, and management.
