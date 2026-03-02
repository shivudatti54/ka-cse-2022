# Introduction to Map Reduce Programming

=====================================

### Introduction

- Map Reduce is a programming model used for processing large data sets in parallel across a cluster of nodes.
- It's a key component of the Hadoop framework, designed to handle big data.

### Key Components

- **Mapper**: Transforms input data into a set of key-value pairs.
  - Formula: `key = key_input, value = value_input`
- **Reducer**: Combines the output from multiple Mappers to produce the final result.
  - Formula: `output = combine(key, values)`
- **Combiner**: An optional component that combines the output from Mappers before it reaches the Reducer.
  - Formula: `output = combine(key, values)`
- **Partitioner**: Divides the output from Mappers into smaller chunks for the Reducer to process.
  - Formula: `partition(key, value) -> partition_id`
- **Search**: Not a standard Map Reduce component, but can be achieved using the output of the Reducer.
- **Sorting**: Not a standard Map Reduce component, but can be achieved using the output of the Reducer.
- **Compression**: Not a standard Map Reduce component, but can be achieved using the output of the Reducer.

### Important Formulas and Definitions

- **Map Reduce Formula**: `output = map_input + reduce_input`
- **Partitioner Formula**: `partition(key, value) -> partition_id`

### Theorems

- **Map Reduce Theorem**: If a function `f(x)` is applied to each element of a dataset, and a function `g(x)` is applied to the output, then the result can be computed in parallel using Map Reduce.
- **Shannon's Source Coding Theorem**: The entropy of a source is equal to the log of the number of possible codes.
