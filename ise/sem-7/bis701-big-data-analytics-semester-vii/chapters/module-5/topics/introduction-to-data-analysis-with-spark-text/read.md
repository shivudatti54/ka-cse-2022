python
# 1. Import and initialize a SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("VTUExample").getOrCreate()

# 2. Load data from a text file into an RDD
lines_rdd = spark.sparkContext.textFile("hdfs://path/to/sample_data.txt")

# 3. Perform transformations on the RDD
#    - Split each line into words
#    - Filter out empty lines
words_rdd = lines_rdd.flatMap(lambda line: line.split(" "))
non_empty_words_rdd = words_rdd.filter(lambda word: word != "")

# 4. Perform an Action: Count the total number of words
total_words = non_empty_words_rdd.count()
print(f"Total words: {total_words}")

# 5. Working with DataFrames for more structured analysis
#    - Convert RDD to a DataFrame with a column named 'word'
words_df = non_empty_words_rdd.map(lambda word: (word,)).toDF(["word"])

# 6. Use DataFrame API for a word count (more efficient)
from pyspark.sql.functions import count
word_count_df = words_df.groupBy("word").agg(count("word").alias("count"))
word_count_df.show(10)  # Show top 10 words

# 7. Alternatively, use SQL
words_df.createOrReplaceTempView("words_table")
result_df = spark.sql("SELECT word, COUNT(*) as count FROM words_table GROUP BY word ORDER BY count DESC")
result_df.show(10)