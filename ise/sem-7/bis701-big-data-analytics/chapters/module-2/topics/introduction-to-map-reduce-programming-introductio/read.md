# **Introduction to Map Reduce Programming**

## **What is Map Reduce?**

Map Reduce is a programming model used for processing large data sets in parallel across a cluster of computers. It is designed to handle massive amounts of data, making it suitable for big data analytics.

## **Why Map Reduce?**

- **Scalability**: Map Reduce can handle large data sets by distributing the data across a cluster of computers.
- **Flexibility**: Map Reduce can be used to process various types of data, including structured and unstructured data.
- **Performance**: Map Reduce can process large data sets in parallel, resulting in faster processing times.

## **Why Not RDBMS?**

- **Scalability**: RDBMS (Relational Database Management System) can become slow and inefficient as the data volume increases.
- **Schema Inflexibility**: RDBMS requires a predefined schema, making it difficult to adapt to changing data requirements.
- **Data Size Limitations**: RDBMS has limitations on the maximum size of a single row and column, making it unsuitable for big data.

## **RDBMS vs Hadoop**

| **Characteristics**       | **RDBMS**  | **Hadoop**      |
| ------------------------- | ---------- | --------------- |
| **Scalability**           | Limited    | Highly Scalable |
| **Schema Inflexibility**  | High       | Flexible        |
| **Data Size Limitations** | Yes        | No Limitations  |
| **Data Type**             | Relational | Distributed     |

## **History of Map Reduce**

- **Google's Research Paper (2004)**: The concept of Map Reduce was first introduced by Google's research team.
- **Apache Hadoop (2006)**: The Apache Hadoop project was established to implement the Map Reduce model.
- **Hadoop Ecosystem (2007)**: The Hadoop ecosystem was developed to provide a comprehensive platform for big data analytics.

## **Key Concepts in Map Reduce**

### Mapper

- **Definition**: A mapper is a program that takes input data, breaks it down into smaller chunks, and processes each chunk.
- **Function**: The mapper function applies a transformation to each input key-value pair, producing a new set of key-value pairs.
- **Example**: A simple mapper example might count the number of occurrences of each word in a text file.

```python
mapper = lambda key, value: (key, value.count())
```

### Reducer

- **Definition**: A reducer is a program that takes the output from the mapper and reduces the data into a single output.
- **Function**: The reducer function aggregates the values associated with the same key, producing a single output.
- **Example**: A simple reducer example might count the total number of occurrences of each word in a list of words.

```python
reducer = lambda key, values: sum(values)
```

### Combiner

- **Definition**: A combiner is a program that combines the output from multiple mappers.
- **Function**: The combiner function applies a transformation to the output from each mapper, producing a new set of key-value pairs.
- **Example**: A simple combiner example might count the number of occurrences of each word in two separate text files.

```python
combiner = lambda key, values: (key, sum(values))
```

### Partitioner

- **Definition**: A partitioner is a program that divides the data into smaller chunks for parallel processing.
- **Function**: The partitioner function groups the key-value pairs based on a specified key, producing a subset of the data.
- **Example**: A simple partitioner example might group the data by country.

```python
partitioner = lambda key, value: (key // 10,)
```

### Searching

- **Definition**: Searching is the process of finding specific data within the processed data.
- **Function**: The searching function applies a filter to the data, producing a subset of the data that meets the specified criteria.
- **Example**: A simple searching example might find all words that contain a specific keyword.

```python
searcher = lambda key, value: (key, value for key, value in data if keyword in str(value))
```

### Sorting

- **Definition**: Sorting is the process of arranging the data in a specific order.
- **Function**: The sorting function applies a sorting algorithm to the data, producing a subset of the data that is sorted.
- **Example**: A simple sorting example might sort a list of words by alphabetical order.

```python
sorter = lambda key, value: sorted(data)
```

### Compression

- **Definition**: Compression is the process of reducing the size of the data.
- **Function**: The compression function applies a compression algorithm to the data, producing a subset of the data that is compressed.
- **Example**: A simple compression example might compress a text file using gzip.

```python
compressor = lambda key, value: gzip.open(key + '.gz', 'wb').write(value)
```
