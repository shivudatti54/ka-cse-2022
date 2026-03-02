# Introduction to Searching

## What is Searching?

**Searching** is the process of finding a specific element or determining whether a particular element exists within a collection of data. It is one of the most fundamental operations in computer science and is used extensively in databases, file systems, and algorithms.

## Why is Searching Important?

1. **Data Retrieval**: Quick access to specific information from large datasets
2. **Database Operations**: Core operation in database management systems
3. **Decision Making**: Basis for conditional logic in programs
4. **Optimization**: Finding optimal solutions in problem-solving
5. **Real-world Applications**: Contact lookup, web search, inventory management

## Types of Searching Algorithms

Searching algorithms can be broadly classified into:

### 1. Sequential/Linear Search

- Checks each element one by one from beginning to end
- Works on both sorted and unsorted data
- Time Complexity: O(n)
- Simple but inefficient for large datasets

### 2. Interval/Divide-and-Conquer Search

- Divides the search space to eliminate portions
- Requires sorted data
- Example: Binary Search - Time Complexity: O(log n)
- Efficient for large sorted datasets

## Linear Search Overview

**How it works:**

1. Start from the first element
2. Compare each element with the search key
3. If a match is found, return the position
4. If the end is reached without a match, return "not found"

```c
int linearSearch(int arr[], int n, int key) {
 for (int i = 0; i < n; i++) {
 if (arr[i] == key)
 return i; // Element found at index i
 }
 return -1; // Element not found
}
```

**Complexity Analysis:**

- Best Case: O(1) - element is at the first position
- Worst Case: O(n) - element is at the last position or not present
- Average Case: O(n/2) = O(n)
- Space Complexity: O(1)

## Binary Search Overview

**Prerequisites:** The array must be sorted

**How it works:**

1. Find the middle element of the array
2. If middle element equals the key, search is complete
3. If key is less than middle, search the left half
4. If key is greater than middle, search the right half
5. Repeat until found or search space is exhausted

```c
int binarySearch(int arr[], int low, int high, int key) {
 while (low <= high) {
 int mid = (low + high) / 2;
 if (arr[mid] == key)
 return mid;
 else if (arr[mid] < key)
 low = mid + 1;
 else
 high = mid - 1;
 }
 return -1; // Element not found
}
```

**Complexity Analysis:**

- Best Case: O(1) - element is at the middle
- Worst Case: O(log n) - element is at the extreme or not present
- Average Case: O(log n)
- Space Complexity: O(1) iterative, O(log n) recursive

## Comparison of Searching Techniques

| Feature          | Linear Search         | Binary Search         |
| ---------------- | --------------------- | --------------------- |
| Data Requirement | Any (sorted/unsorted) | Sorted only           |
| Time Complexity  | O(n)                  | O(log n)              |
| Space Complexity | O(1)                  | O(1) iterative        |
| Approach         | Sequential            | Divide and conquer    |
| Best for         | Small/unsorted data   | Large sorted data     |
| Data Structure   | Array or Linked List  | Array (random access) |

## Key Concepts

### Search Key

The value being searched for in the collection. The algorithm compares each element against this key.

### Successful vs Unsuccessful Search

- **Successful**: The key is found in the collection
- **Unsuccessful**: The key is not present in the collection

### Number of Comparisons

The efficiency of a searching algorithm is measured by the number of comparisons it makes. Fewer comparisons mean better performance.

## Applications of Searching

1. **Databases**: Finding records matching a query
2. **Spell Checkers**: Looking up words in a dictionary
3. **Phone Directories**: Finding contact information
4. **Search Engines**: Retrieving relevant web pages
5. **Operating Systems**: Finding files and processes
6. **E-commerce**: Product search and filtering

## Exam Tips

1. Know the difference between linear and binary search clearly
2. Be able to write code for both algorithms
3. Understand time complexity analysis for best, worst, and average cases
4. Remember that binary search requires sorted data
5. Practice tracing through examples step by step
6. Know when to use each algorithm based on the situation
