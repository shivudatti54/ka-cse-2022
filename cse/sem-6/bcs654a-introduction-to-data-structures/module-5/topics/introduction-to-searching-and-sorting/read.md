# Introduction to Searching and Sorting

## Overview

Searching and Sorting are fundamental operations in computer science and data structures. They are among the most frequently performed operations on data and form the basis for many algorithms.

## Searching

### What is Searching?

**Searching** is the process of finding a particular element or checking whether an element exists in a given collection of data.

### Why Searching is Important

1. **Data Retrieval**: Quick access to information
2. **Database Operations**: Core operation in databases
3. **Decision Making**: Basis for conditional logic
4. **Optimization**: Finding best solutions

### Types of Searching

#### 1. Linear Search

- Sequential search through elements
- Works on unsorted data
- Time Complexity: O(n)

#### 2. Binary Search

- Divide and conquer approach
- Requires sorted data
- Time Complexity: O(log n)

### Applications of Searching

- Finding records in database
- Dictionary lookups
- Phone directory
- Web search engines
- File systems

## Sorting

### What is Sorting?

**Sorting** is the process of arranging data in a particular order (ascending or descending).

### Why Sorting is Important

1. **Efficient Searching**: Enables binary search
2. **Data Presentation**: Organized display
3. **Optimization**: Many algorithms work better on sorted data
4. **Database Operations**: Indexing and queries
5. **Data Analysis**: Finding patterns

### Classification of Sorting

#### By Complexity

- **Simple Sorts**: Bubble, Selection, Insertion - O(n²)
- **Efficient Sorts**: Merge, Quick, Heap - O(n log n)
- **Linear Sorts**: Counting, Radix, Bucket - O(n)

#### By Method

- **Comparison-based**: Compare elements
- **Non-comparison**: Use properties of data

#### By Memory Usage

- **In-place**: O(1) extra space
- **Out-of-place**: O(n) extra space

#### By Stability

- **Stable**: Maintains relative order of equal elements
- **Unstable**: May change relative order

### Common Sorting Algorithms

#### 1. Bubble Sort

- Repeatedly swap adjacent elements
- Time: O(n²), Space: O(1)
- Stable

#### 2. Selection Sort

- Select minimum and place at beginning
- Time: O(n²), Space: O(1)
- Unstable

#### 3. Insertion Sort

- Build sorted array one element at a time
- Time: O(n²), Space: O(1)
- Stable

#### 4. Merge Sort

- Divide and conquer
- Time: O(n log n), Space: O(n)
- Stable

#### 5. Quick Sort

- Partition based on pivot
- Time: O(n log n) average, O(n²) worst, Space: O(log n)
- Unstable

#### 6. Heap Sort

- Use heap data structure
- Time: O(n log n), Space: O(1)
- Unstable

### Comparison of Sorting Algorithms

| Algorithm      | Time (Avg) | Time (Worst) | Space    | Stable | In-place |
| -------------- | ---------- | ------------ | -------- | ------ | -------- |
| Bubble Sort    | O(n²)      | O(n²)        | O(1)     | Yes    | Yes      |
| Selection Sort | O(n²)      | O(n²)        | O(1)     | No     | Yes      |
| Insertion Sort | O(n²)      | O(n²)        | O(1)     | Yes    | Yes      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n)     | Yes    | No       |
| Quick Sort     | O(n log n) | O(n²)        | O(log n) | No     | Yes      |
| Heap Sort      | O(n log n) | O(n log n)   | O(1)     | No     | Yes      |

## Applications of Sorting

1. **Databases**: Organizing records
2. **Search Optimization**: Enabling binary search
3. **Data Analysis**: Finding median, percentiles
4. **Graphics**: Rendering order
5. **Compression**: Data compression algorithms
6. **Scheduling**: Job scheduling

## Choosing the Right Algorithm

### For Searching

- **Small data**: Linear search
- **Large sorted data**: Binary search
- **Dynamic data**: Hash tables

### For Sorting

- **Small data (<50)**: Insertion sort
- **Large data**: Quick sort or Merge sort
- **Stability needed**: Merge sort
- **Memory limited**: Heap sort or Quick sort
- **Nearly sorted**: Insertion sort

## Relationship Between Searching and Sorting

1. **Sorted data enables efficient searching**: Binary search requires sorted array
2. **Search during sorting**: Insertion sort searches for position
3. **Combined operations**: Many algorithms use both

## Exam Tips

1. Understand time and space complexity of each algorithm
2. Know which algorithms are stable
3. Remember in-place vs out-of-place sorting
4. Understand when to use which algorithm
5. Practice drawing diagrams for each algorithm
6. Know advantages and disadvantages
7. Understand relationship between sorting and searching
8. Remember real-world applications
