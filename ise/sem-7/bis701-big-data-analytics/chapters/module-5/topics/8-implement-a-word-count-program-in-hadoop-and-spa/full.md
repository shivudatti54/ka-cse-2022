# 8 Implement a Word Count Program in Hadoop and Spark

======================================================

## Introduction

---

In this chapter, we will dive into the world of big data analytics and explore how to implement a word count program using two popular tools: Hadoop and Spark. We will cover the historical context of big data, the rise of Hadoop and Spark, and the key concepts and techniques involved in implementing a word count program.

## Historical Context

---

Big data has become an essential aspect of modern business and analytics. The concept of big data emerged in the early 2000s, but it wasn't until around 2010 that it started to gain mainstream attention. The rise of social media, online transactions, and sensor data created an explosion of new data sources that needed to be processed and analyzed.

Hadoop, developed in 2003 by Doug Cutting and Mike Cafarella, was one of the first tools specifically designed to handle big data. It was initially called "Nutch" and was designed to handle the sheer volume of web pages that needed to be crawled and indexed.

Spark, developed in 2009 by Apache, was initially called "Lightning" and was designed to provide in-memory processing for big data. It was later rebranded as Apache Spark, and it has since become one of the most popular big data tools in the world.

## Implementing a Word Count Program in Hadoop

---

### Overview

A word count program is a simple program that takes a text file as input and outputs the frequency of each word in the file. In this section, we will explore how to implement a word count program using Hadoop.

### Hadoop Word Count Program

Here is a simple Hadoop word count program in Java:

```java
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {
  public static void main(String[] args) throws Exception {
    Job job = Job.getInstance(HadoopConfig conf, "wordcount");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(WordMapper.class);
    job.setReducerClass(WordReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path("input.txt"));
    FileOutputFormat.addOutputPath(job, new Path("output.txt"));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }

  public static class WordMapper extends Mapper<Text, Text, Text, IntWritable> {
    @Override
    public void map(Text key, Text value, Context context) throws IOException, InterruptedException {
      String word = value.toString().toLowerCase();
      IntWritable count = new IntWritable(1);
      context.write(key, count);
    }
  }

  public static class WordReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable value : values) {
        sum += value.get();
      }
      IntWritable count = new IntWritable(sum);
      context.write(key, count);
    }
  }
}
```

This program uses the Hadoop MapReduce framework to process the input file `input.txt` and output the frequency of each word in the file to `output.txt`.

### Hadoop Word Count Program (using Pig)

Here is a simple Hadoop word count program using Pig:

```pig
data = load 'input.txt' as (key, value);
group data by key;
generate count = sum($value);
store group into 'output.txt';
```

This program uses the Pig Latin language to process the input file `input.txt` and output the frequency of each word in the file to `output.txt`.

## Implementing a Word Count Program in Spark

---

### Overview

Spark provides a simple and efficient way to process big data using the Resilient Distributed Dataset (RDD) data structure. In this section, we will explore how to implement a word count program using Spark.

### Spark Word Count Program

Here is a simple Spark word count program in Scala:

```scala
import org.apache.spark.SparkConf
import org.apache.spark.api.java.JavaPairRDD
import org.apache.spark.api.java.JavaSparkContext

object WordCount {
  def main(args: Array[String]) {
    val sparkConf = new SparkConf().setAppName("wordcount").setMaster("local")
    val sc = new JavaSparkContext(sparkConf)
    val rdd = sc.textFile("input.txt")
    val wordCounts = rdd.map(_.toLowerCase().split("\\s+")).flatMap(arr => arr.map(word => (word, 1))).reduceByKey(_ + _)
    wordCounts.saveAsTextFile("output.txt")
  }
}
```

This program uses the Spark Scala API to process the input file `input.txt` and output the frequency of each word in the file to `output.txt`.

### Spark Word Count Program (using Python)

Here is a simple Spark word count program using Python:

```python
from pyspark import SparkContext

def word_count(rdd):
    word_counts = rdd.map(lambda x: x.lower().split()).flatMap(lambda x: [[word, 1] for word in x]).collect()
    return word_counts

def main():
    spark_conf = SparkConf().setAppName("wordcount").setMaster("local")
    sc = SparkContext(spark_conf)
    rdd = sc.textFile("input.txt")
    word_counts = word_count(rdd)
    word_counts.saveAsTextFile("output.txt")

if __name__ == "__main__":
    main()
```

This program uses the Spark Python API to process the input file `input.txt` and output the frequency of each word in the file to `output.txt`.

## Case Study: Implementing a Word Count Program for a Large Text File

---

Let's say we have a large text file called `large_text.txt` that contains millions of lines of text. We want to implement a word count program to output the frequency of each word in the file.

Here is an example of how we can implement a word count program using both Hadoop and Spark:

```java
// Hadoop implementation
public class LargeTextWordCount {
  public static void main(String[] args) throws Exception {
    Job job = Job.getInstance(HadoopConfig conf, "large_text_wordcount");
    job.setJarByClass(LargeTextWordCount.class);
    job.setMapperClass(LargeTextWordMapper.class);
    job.setReducerClass(LargeTextWordReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path("large_text.txt"));
    FileOutputFormat.addOutputPath(job, new Path("output.txt"));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }

  public static class LargeTextWordMapper extends Mapper<Text, Text, Text, IntWritable> {
    @Override
    public void map(Text key, Text value, Context context) throws IOException, InterruptedException {
      String word = value.toString().toLowerCase();
      IntWritable count = new IntWritable(1);
      context.write(key, count);
    }
  }

  public static class LargeTextWordReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable value : values) {
        sum += value.get();
      }
      IntWritable count = new IntWritable(sum);
      context.write(key, count);
    }
  }
}
```

```python
# Spark implementation
from pyspark import SparkContext

def large_text_word_count(rdd):
    word_counts = rdd.map(lambda x: x.lower().split()).flatMap(lambda x: [[word, 1] for word in x]).collect()
    return word_counts

def main():
    spark_conf = SparkConf().setAppName("large_text_wordcount").setMaster("local")
    sc = SparkContext(spark_conf)
    rdd = sc.textFile("large_text.txt")
    word_counts = large_text_word_count(rdd)
    word_counts.saveAsTextFile("output.txt")

if __name__ == "__main__":
    main()
```

This program uses both Hadoop and Spark to process the large text file `large_text.txt` and output the frequency of each word in the file to `output.txt`. The Hadoop implementation uses the Hadoop MapReduce framework, while the Spark implementation uses the Spark Scala API.

## Applications of Word Count Programs

---

Word count programs have many applications in real-world scenarios. Here are a few examples:

- Sentiment analysis: Word count programs can be used to analyze the sentiment of customer reviews or social media posts.
- Topic modeling: Word count programs can be used to identify topics or themes in a large corpus of text.
- Text classification: Word count programs can be used to classify text into categories such as spam or non-spam emails.
- Information retrieval: Word count programs can be used to retrieve relevant documents based on the frequency of certain words.

## Further Reading

---

- "Hadoop: The Definitive Guide" by Tom White
- "Spark: The Definitive Guide" by Alex Woodie
- "Natural Language Processing (almost) from Scratch" by Collobert et al.
- "Topic Modeling" by LDA (Latent Dirichlet Allocation) paper by Blei et al.
- "Sentiment Analysis" by VaderSentiment paper by Cho et al.

This concludes our deep dive into implementing a word count program in Hadoop and Spark. We hope that this tutorial has been informative and helpful in understanding the concepts and techniques involved in implementing a word count program.
