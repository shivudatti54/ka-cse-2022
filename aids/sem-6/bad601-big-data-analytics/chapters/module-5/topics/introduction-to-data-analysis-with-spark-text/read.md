python
    # Using PySpark (Spark's Python API)
    sc = SparkContext()  # SparkContext is the entry point
    lines_rdd = sc.textFile("hdfs://path/to/large_text_file.txt")