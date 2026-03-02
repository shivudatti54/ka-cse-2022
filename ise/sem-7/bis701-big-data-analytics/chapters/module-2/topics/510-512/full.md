# 5.10-5.12: Big Data Analytics with Hadoop

=====================================================

## 5.10: Introduction to MapReduce

---

MapReduce is a programming model used for processing large data sets in parallel across a cluster of computers. It is the core component of the Hadoop platform and is used for tasks such as data aggregation, filtering, and sorting.

### Components of MapReduce

- **Mapper**: The mapper is responsible for breaking down the data into smaller chunks, processing each chunk, and producing a set of key-value pairs.
- **Reducer**: The reducer takes the key-value pairs produced by the mapper and aggregates them to produce the final output.

### MapReduce Workflow

1.  **Input**: The input data is divided into smaller chunks, known as splits.
2.  **Mapper**: Each split is processed by a mapper, which produces a set of key-value pairs.
3.  **Shuffle**: The key-value pairs produced by the mapper are shuffled and sorted based on the key.
4.  **Reducer**: The sorted key-value pairs are processed by a reducer, which produces the final output.

### Advantages of MapReduce

- **Parallel Processing**: MapReduce can process large data sets in parallel across a cluster of computers.
- **Flexible**: MapReduce can be used for a variety of tasks, including data aggregation, filtering, and sorting.
- **Scalable**: MapReduce can scale to handle large data sets and complex processing tasks.

### Disadvantages of MapReduce

- **Complexity**: MapReduce can be complex to implement and manage.
- **Limited Expressiveness**: MapReduce has limited expressiveness and requires a significant amount of code to achieve complex processing tasks.

### Example Use Case

Suppose we want to count the number of occurrences of each word in a large text file. We can use MapReduce to achieve this task.

- **Mapper**: The mapper breaks down the text file into smaller chunks, processes each chunk, and produces a set of key-value pairs, where the key is the word and the value is the count.
- **Reducer**: The reducer aggregates the key-value pairs and produces the final output, which is a map of words to their corresponding counts.

### Code Example

Here is an example of how to implement a simple MapReduce program in Java:

```java
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {
    public static class Mapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        @Override
        public void map(LongWritable key, Text value, Context context) {
            String word = value.toString();
            context.write(new Text(word), new IntWritable(1));
        }
    }

    public static class Reducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) {
            int sum = 0;
            for (IntWritable value : values) {
                sum += value.get();
            }
            context.write(key, new IntWritable(sum));
        }
    }

    public static void main(String[] args) throws Exception {
        FileInputFormat.setInputPaths(System.in);
        FileOutputFormat.setOutputLocation(new FileSystem("output"), new Path("wordcount"));
        Job job = Job.getInstance();
        job.setMapperClass(WordCount.Mapper.class);
        job.setReducerClass(WordCount.Reducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

This code example demonstrates how to implement a simple MapReduce program in Java. The mapper breaks down the text file into smaller chunks and produces a set of key-value pairs, where the key is the word and the value is the count. The reducer aggregates the key-value pairs and produces the final output, which is a map of words to their corresponding counts.

## 5.11: Hadoop File System (HDFS)

---

HDFS is a distributed file system that is designed to handle large amounts of data. It is used as the storage component of the Hadoop platform and is responsible for storing and retrieving data.

### Components of HDFS

- **NameNode (NN)**: The NameNode is responsible for maintaining a directory hierarchy of the data stored in HDFS.
- **DataNode (DN)**: The DataNode is responsible for storing and retrieving data from HDFS.
- **Block**: A block is a small chunk of data that is stored in HDFS.

### How HDFS Works

1.  **Client Request**: A client requests data from HDFS.
2.  **NameNode**: The NameNode receives the request and locates the block containing the requested data.
3.  **DataNode**: The DataNode retrieves the block from HDFS and returns the data to the client.

### Advantages of HDFS

- **Scalability**: HDFS can scale to handle large amounts of data.
- **Fault Tolerance**: HDFS provides fault tolerance by storing data in multiple locations.
- **High Throughput**: HDFS provides high throughput by storing data in a distributed manner.

### Disadvantages of HDFS

- **Complexity**: HDFS can be complex to implement and manage.
- **Limited Expressiveness**: HDFS has limited expressiveness and requires a significant amount of configuration to achieve complex data management tasks.

### Example Use Case

Suppose we want to store a large text file in HDFS. We can use HDFS to store the file and retrieve it later.

- **Client Request**: The client requests the text file from HDFS.
- **NameNode**: The NameNode receives the request and locates the block containing the text file.
- **DataNode**: The DataNode retrieves the block from HDFS and returns the text file to the client.

### Code Example

Here is an example of how to implement a simple HDFS client in Java:

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class HDFSClient {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(conf);

        Path input = new Path(args[0]);
        Path output = new Path(args[1]);

        FSDataInputStream in = fs.open(input);
        FSDataOutputStream out = fs.create(output);

        byte[] buffer = new byte[1024];
        int len;
        while ((len = in.read(buffer)) > 0) {
            out.write(buffer, 0, len);
        }

        in.close();
        out.close();
    }
}
```

This code example demonstrates how to implement a simple HDFS client in Java. The client reads the text file from HDFS and writes it to a new file.

## 5.12: Spark SQL

---

Spark SQL is a component of the Apache Spark platform that provides a SQL interface for processing big data. It allows users to write SQL queries and execute them on large data sets.

### Components of Spark SQL

- **DataFrame**: A DataFrame is a data structure that represents a collection of data.
- **Dataset**: A Dataset is a data structure that represents a collection of data with a specific schema.
- **SQLContext**: The SQLContext provides a way to execute SQL queries on DataFrames and Datasets.

### How Spark SQL Works

1.  **Data Source**: A data source is a way to load data into Spark SQL.
2.  **DataFrame/Dataset**: A DataFrame or Dataset is created from the data source.
3.  **SQL Query**: A SQL query is executed on the DataFrame or Dataset.
4.  **Execution**: The SQL query is executed and the results are returned.

### Advantages of Spark SQL

- **High Performance**: Spark SQL provides high performance for big data processing.
- **Flexible**: Spark SQL allows users to write SQL queries and execute them on large data sets.
- **Easy to Use**: Spark SQL provides a simple and intuitive API for processing big data.

### Disadvantages of Spark SQL

- **Steep Learning Curve**: Spark SQL has a steep learning curve.
- **Limited Support for Complex Queries**: Spark SQL has limited support for complex queries.

### Example Use Case

Suppose we want to process a large text file and extract the top 10 words with the highest frequency. We can use Spark SQL to achieve this task.

- **Data Source**: The text file is loaded into Spark SQL as a DataFrame.
- **SQL Query**: The SQL query is executed to extract the top 10 words with the highest frequency.
- **Execution**: The SQL query is executed and the results are returned.

### Code Example

Here is an example of how to implement a simple Spark SQL query in Java:

```java
import org.apache.spark.sql.SparkSession;

public class SparkSQLExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("Spark SQL Example").getOrCreate();

        DataFrame df = spark.read().text("input.txt");

        df.groupBy("word").count().orderBy("count").limit(10).show();

        spark.stop();
    }
}
```

This code example demonstrates how to implement a simple Spark SQL query in Java. The query extracts the top 10 words with the highest frequency from the text file.

## Further Reading

---

- "Hadoop: The Definitive Guide" by Tom White
- "Big Data: The Missing Manual" by Tim O'Reilly and Tim Hill
- "Spark SQL: A Guide to Working with Data in Apache Spark" by O'Reilly Media
- "Hadoop and Spark: Deeper Dive" by Packt Publishing
