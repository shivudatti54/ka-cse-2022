# Introduction to Map Reduce Programming

=====================================================

MapReduce is a programming model used for processing large data sets in parallel across a cluster of computers. It is the core component of the Hadoop distributed computing framework. In this section, we will delve into the details of MapReduce programming, exploring its history, key components, and applications.

## History of MapReduce

---

The MapReduce programming model was first introduced in 2004 by Google, and later adopted by Yahoo! and Microsoft. The original goal was to provide a simple and efficient way to process large data sets using distributed computing techniques.

In 2005, the Apache Software Foundation (ASF) released the first version of Hadoop, which included the MapReduce framework. Since then, MapReduce has become a widely adopted standard for big data processing.

## Why MapReduce?

---

MapReduce is an ideal choice for processing large data sets due to its ability to scale horizontally, which means that it can handle increasing amounts of data by simply adding more nodes to the cluster.

Here are some reasons why MapReduce is preferred over traditional relational databases (RDBMS):

- **Scalability**: MapReduce can handle massive amounts of data, whereas RDBMS has limitations on data size and scalability.
- **Flexibility**: MapReduce can process various data formats, including text, image, and video data, whereas RDBMS is primarily designed for structured data.
- **Cost-Effective**: MapReduce can process data at a lower cost compared to RDBMS, especially for large-scale data processing.

## Why Not RDBMS?

---

While RDBMS is suitable for small-scale data processing, it has limitations when it comes to handling large amounts of data. Here are some reasons why RDBMS may not be the best choice for big data processing:

- **Performance**: RDBMS can become slow and unresponsive when handling large amounts of data, leading to decreased performance.
- **Storage**: RDBMS requires a significant amount of storage space, which can become expensive and impractical for large-scale data storage.
- **Scalability**: RDBMS has limitations on scalability, making it challenging to add more nodes to the cluster without compromising performance.

## RDBMS Vs Hadoop

---

RDBMS and Hadoop serve different purposes and have different strengths:

- **RDBMS**:
  - Suitable for small-scale to medium-scale data processing
  - Ideal for structured data, such as transactional data
  - Provides strong consistency and ACID compliance
- **Hadoop**:
  - Suitable for large-scale data processing
  - Ideal for unstructured and semi-structured data, such as text and image data
  - Provides high scalability and flexibility

## MapReduce Components

---

MapReduce consists of the following components:

### 1. **Mapper**

A mapper is responsible for breaking down the data into smaller chunks and processing each chunk in parallel. The mapper takes input data, applies a mapping function, and produces an output key-value pair.

### 2. **Reducer**

A reducer is responsible for aggregating the output from the mappers and producing the final output. The reducer takes the output from the mappers, applies a reduction function, and produces the final output.

### 3. **Combiner**

A combiner is an optional component that is used to reduce the output from the mappers before it reaches the reducer. This can improve performance by reducing the amount of data that needs to be processed.

### 4. **Partitioner**

A partitioner is responsible for dividing the output from the mappers into smaller chunks, known as partitions. This allows the reducer to process each partition independently.

### 5. **JobTracker**

The JobTracker is responsible for managing the job and keeping track of the progress. It receives the input data, schedules the jobs, and monitors the execution.

### 6. **TaskTracker**

The TaskTracker is responsible for executing the tasks. It receives the task assignments, executes the tasks, and reports back to the JobTracker.

## MapReduce Workflow

---

Here is an overview of the MapReduce workflow:

1.  **Input**: The input data is processed by the mapper, producing an output key-value pair.
2.  **Mapper**: The mapper is executed in parallel, producing multiple output key-value pairs.
3.  **Shuffle**: The output from the mappers is shuffled and sorted based on the key.
4.  **Reducer**: The reducer is executed in parallel, producing the final output.
5.  **Output**: The final output is produced and stored in the output directory.

## Searching and Sorting

---

MapReduce provides built-in support for searching and sorting data:

- **Sorting**: MapReduce can sort the output based on the key or value.
- **Searching**: MapReduce can search for specific keys or values in the output.

## Compression

---

MapReduce provides built-in support for compressing data:

- **Gzip**: MapReduce can compress data using gzip.
- **Snappy**: MapReduce can compress data using snappy.

## Case Study: Word Count

---

Here is a case study of using MapReduce to perform a word count:

- **Input**: A text file containing a list of words.
- **Mapper**: The mapper breaks down the text into individual words and produces an output key-value pair for each word.
- **Reducer**: The reducer aggregates the output from the mappers and produces the final output, which is the word count.

## Example Code

---

Here is an example code in Java that demonstrates how to use MapReduce to perform a word count:

```java
// Mapper
public class WordCountMapper extends Mapper<String, IntWritable, String, IntWritable> {
    @Override
    public void map(String key, IntWritable value, Context context) {
        context.write(key, value);
    }
}

// Reducer
public class WordCountReducer extends Reducer<String, IntWritable, String, IntWritable> {
    @Override
    public void reduce(String key, Iterable<IntWritable> values, Context context) {
        int sum = 0;
        for (IntWritable value : values) {
            sum += value.get();
        }
        context.write(key, new IntWritable(sum));
    }
}
```

## Further Reading

---

Here are some further reading resources:

- [Hadoop Official Documentation](https://hadoop.apache.org/docs/)
- [Apache Hadoop MapReduce Guide](https://hadoop.apache.org/docs/r2.3.0/hadoop-mapreduce-programming-guide.html)
- [MapReduce Programming Model](https://www.coursera.org/specializations/big-data-with-hadoop)
- [Word Count Example](https://github.com/hadoop/hadoop/blob/master/hadoop-mapreduce-project/hadoop-mapreduce-examples/src/main/java/WordCount.java)
