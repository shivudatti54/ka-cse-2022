# Introduction to Map Reduce Programming

=====================================

### Introduction

- Map Reduce programming is a processing model used in Big Data analytics
- It's a popular algorithm for processing large datasets in parallel
- It's designed to handle massive amounts of data and perform complex computations

### Key Concepts

- **Mapper**: A program that takes input data, breaks it down into smaller chunks (calls), and produces output (key-value pairs)
- **Reducer**: A program that takes output from multiple Mappers and reduces it into a single output ( aggregated values)
- **Combiner**: A program that combines output from multiple Reducers, improving performance and reducing data transfer
- **Partitioner**: A program that divides input data into smaller chunks (partitions) for processing
- **Searching**: Finding specific data within a large dataset
- **Sorting**: Organizing data in a specific order
- **Compression**: Reducing the size of data to improve storage and transfer efficiency

### Important Formulas and Definitions

- **Map Reduce Formula**: `Output = Map(In) + Reduce(Map(In))`
- **Mapper Formula**: `Mapper(In) -> (Key, Value)`
- **Reducer Formula**: `Reducer(In) -> (Key, Aggregate)`

### Theorems and Concepts

- **Weak Consistency**: Map Reduce ensures weak consistency, where output is eventually consistent across all nodes
- **Fault Tolerance**: Map Reduce is designed to handle node failures and recover from errors

### Why Map Reduce?

- Handles massive amounts of data
- Scalable and parallel processing
- Fault-tolerant and reliable
