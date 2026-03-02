# Apache Spark Streaming

## Introduction
Apache Spark Streaming is a scalable, high-throughput fault-tolerant streaming processing system that enables real-time data processing. As part of the Apache Spark ecosystem, it extends Spark's core API to process live data streams from sources like Kafka, Flume, and HDFS. 

In the era of IoT and real-time analytics, Spark Streaming addresses critical needs for:
- Fraud detection in financial transactions
- Real-time recommendations in e-commerce
- Social media sentiment analysis
- Network intrusion detection

Unlike traditional batch processing, Spark Streaming uses micro-batch architecture to provide near-real-time processing (latency as low as 500ms). Its integration with Spark's machine learning libraries (MLlib) and graph processing (GraphX) makes it uniquely positioned for complex streaming pipelines.

## Key Concepts
1. **DStream (Discretized Stream)**: 
   - Fundamental abstraction representing continuous data stream
   - Internally divided into RDDs (Resilient Distributed Datasets)
   - Created from input sources or transformations

2. **Micro-Batch Architecture**:
   - Processes data in small batches (configurable duration: 0.5-10 seconds)
   - Combines benefits of real-time and batch processing

3. **Window Operations**:
   - Sliding Window: Overlapping time intervals
   - Tumbling Window: Fixed non-overlapping intervals
   - Used for aggregations over time ranges

4. **Stateful vs Stateless Processing**:
   - Stateful: Maintains context across batches (e.g., sessionization)
   - Stateless: Each batch processed independently

5. **Checkpointing**:
   - Two types: Metadata (configuration) and Data (RDD)
   - Essential for fault recovery in long-running applications

6. **Integration with Kafka**:
   - Direct API for Kafka (no receiver needed)
   - Exactly-once semantics support

## Examples

**Example 1: Word Count Stream**
```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 5)  # 5-second batch

lines = ssc.socketTextStream("localhost", 9999)
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
word_counts = pairs.reduceByKey(lambda x,y: x+y)
word_counts.pprint()

ssc.start()
ssc.awaitTermination()
```

**Example 2: Sliding Window (Trending Hashtags)**
```python
hashtags = tweets.flatMap(lambda tweet: tweet.split())\
                 .filter(lambda word: word.startswith('#'))\
                 .map(lambda hashtag: (hashtag, 1))

# 30-second window sliding every 10 seconds
trending = hashtags.reduceByKeyAndWindow(
    lambda x,y: x+y, lambda x,y: x-y, 30, 10)
```

**Example 3: Stateful Processing (Fraud Detection)**
```python
def updateFunc(new_values, running_count):
    return sum(new_values) + (running_count or 0)

transaction_counts = transactions.map(lambda t: (t.user_id, 1))\
    .updateStateByKey(updateFunc)\
    .filter(lambda (user, count): count > 100)  # Alert threshold
```

## Exam Tips
1. Understand the difference between Spark Streaming's micro-batch vs true streaming (like Flink)
2. Always mention checkpointing when discussing fault tolerance
3. For window operations, remember to specify both window and slide durations
4. Know the differences between DStream API and Structured Streaming
5. When asked about Kafka integration, explain the advantages of direct stream approach
6. Be prepared to compare stateful vs stateless transformations with examples
7. Practice writing transformation chains using map, reduceByKey, and window functions