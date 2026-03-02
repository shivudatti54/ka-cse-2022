# **Implementing a Word Count Program in Hadoop and Spark**

### Overview

This topic focuses on implementing a word count program in two popular big data processing frameworks: Hadoop and Spark. Word count is a basic data processing task that involves counting the frequency of each word in a given text dataset.

### Key Points

#### Hadoop:

- **Word Count Program:**
  - Uses MapReduce programming model
  - Consists of two phases: Map and Reduce
  - Map phase: splits input text into words, creates key-value pairs (word, frequency), and sends them to the reducer
  - Reduce phase: combines key-value pairs, calculates the frequency of each word, and outputs the word-count pairs
- **Hadoop Word Count Example:**
  ```bash
  mapreduce word-count -input input.txt -output output

````

#### Spark:

*   **Word Count Program:**
    *   Uses Resilient Distributed Datasets (RDDs) and DataFrames APIs
    *   Consists of two main steps: data loading, filtering, and aggregation
    *   Data loading: loads input text data into an RDD
    *   Filtering: filters the text data to extract words
    *   Aggregation: counts the frequency of each word using Spark's built-in aggregation functions
*   **Spark Word Count Example:**
    ```python
from pyspark import SparkContext

sc = SparkContext()

textData = sc.textFile('input.txt')
wordData = textData.flatMap(lambda line: line.split())
wordCount = wordData.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

wordCount.saveAsTextFile('output')
````

### Important Formulas, Definitions, and Theorems

- **MapReduce Formula:**
  - `Output = (Map \* Reduce)`
- **Word Count Formula:**
  - `word-count = (number_of_words_in_text) / (number_of_documents)`
- **RDD (Resilient Distributed Dataset) Definition:**
  - A distributed collection of data that can be split across multiple nodes in a cluster

### Quick Revision Tips

- Focus on understanding the programming models and APIs used in Hadoop and Spark for word count programs
- Practice implementing word count programs in both frameworks to solidify your understanding
- Review the key formulas, definitions, and theorems related to word count programs
