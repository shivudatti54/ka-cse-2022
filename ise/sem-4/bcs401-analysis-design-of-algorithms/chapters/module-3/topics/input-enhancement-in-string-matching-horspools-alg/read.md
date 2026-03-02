# Input Enhancement in String Matching: Horspool’s Algorithm

=====================================================

## Overview

---

String matching is a fundamental problem in computer science, where we need to find a substring within a given text. One approach to improve the efficiency of string matching is to enhance the input data. Horspool's algorithm is a popular string matching algorithm that uses input enhancement to reduce the number of comparisons required.

## What is Input Enhancement?

---

Input enhancement is a technique used to modify the input data to make it more efficient for the algorithm to process. In the context of string matching, input enhancement involves modifying the input text to reduce the number of comparisons required.

## Horspool’s Algorithm

---

Horspool's algorithm is a string matching algorithm that uses input enhancement to reduce the number of comparisons required. The algorithm works by using a hashing function to map the characters of the text to a range of indices in a table. The table is used to store the maximum number of characters that can be shifted without causing a collision.

### How Horspool’s Algorithm Works

The algorithm works as follows:

1.  Create a hash table of size `m`, where `m` is the length of the pattern.
2.  For each character `c` in the text, calculate the hash value `h = (b \* p + c) mod m`, where `b` is the current index and `p` is the pattern length.
3.  Compare the hash value `h` with the hash values in the table. If a match is found, return the starting index of the match.
4.  If no match is found, shift the window by one character and repeat the process.

### Example Use Case

Suppose we want to search for the pattern "abc" in the text "banana":

|     | a   | b   | a   | n   | a   | n   | a   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b   | 2   | 5   | 8   | 11  | 14  | 17  | 20  |
| a   | 11  | 14  | 17  | 20  | 23  | 26  | 29  |
| c   | 20  | 23  | 26  | 29  | 32  | 35  | 38  |

In this example, the hash table is created based on the pattern "abc". The hash values are calculated as follows:

|     | a   | b   | c   | p   | h   |
| --- | --- | --- | --- | --- | --- |
| 2   | 0   | 2   | 2   | 2   | 4   |
| 5   | 2   | 1   | 3   | 2   | 7   |
| 8   | 2   | 3   | 0   | 2   | 12  |
| 11  | 1   | 4   | 2   | 2   | 18  |
| 14  | 4   | 1   | 0   | 2   | 26  |
| 17  | 0   | 5   | 2   | 2   | 36  |
| 20  | 5   | 2   | 0   | 2   | 48  |
| 23  | 2   | 1   | 1   | 2   | 60  |
| 26  | 1   | 6   | 2   | 2   | 74  |
| 29  | 6   | 3   | 0   | 2   | 88  |
| 32  | 3   | 0   | 1   | 2   | 104 |
| 35  | 0   | 7   | 2   | 2   | 120 |
| 38  | 7   | 4   | 1   | 2   | 136 |

The algorithm compares the hash values in the table with the hash value of the current character in the text. If a match is found, the algorithm returns the starting index of the match.

### Key Concepts

- **Hash table**: A data structure used to store the hash values of the pattern.
- **Hashing function**: A function that maps the characters of the text to a range of indices in the table.
- **Collision**: A situation where two different characters in the text produce the same hash value.
- **Shift**: The process of shifting the window by one character to reduce the number of comparisons required.

## Advantages of Horspool’s Algorithm

---

Horspool's algorithm has several advantages over other string matching algorithms:

- **Efficient**: Horspool's algorithm has a time complexity of O(n/m), where n is the length of the text and m is the length of the pattern.
- **Space-efficient**: The algorithm uses a hash table of size m, which is relatively small compared to the length of the text.
- **Fast**: Horspool's algorithm is faster than other string matching algorithms because it uses a hashing function to reduce the number of comparisons required.

## Disadvantages of Horspool’s Algorithm

---

While Horspool's algorithm has several advantages, it also has some disadvantages:

- **Complexity**: The algorithm is relatively complex because it uses a hashing function to map the characters of the text to a range of indices in the table.
- **Overhead**: The algorithm requires additional memory to store the hash table, which can be a significant overhead for large texts.
- **Limited flexibility**: The algorithm is designed to work with a specific pattern and text, which can limit its flexibility and adaptability.

### Best Practices for Implementing Horspool’s Algorithm

To get the most out of Horspool’s algorithm, follow these best practices:

- **Use a good hashing function**: The hashing function should be designed to minimize collisions and maximize the range of possible hash values.
- **Use a suitable table size**: The table size should be chosen based on the length of the pattern and the complexity of the text.
- **Optimize the algorithm**: The algorithm can be optimized by using techniques such as caching and parallel processing.

## Example Code

---

Here is an example implementation of Horspool’s algorithm in Python:

```python
def horspool_algorithm(text, pattern):
    m = len(pattern)
    table = {}
    for i in range(m):
        table[pattern[i]] = i

    j = 0
    for i in range(len(text)):
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i - j + 1
        table[text[i + j]] = table.get(text[i + j], -1)
        j = min(table.get(text[i + j], m), j - 1)

    return -1

# Example usage
text = "banana"
pattern = "abc"
index = horspool_algorithm(text, pattern)
if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found")
```

This code implements the Horspool’s algorithm using a hash table to store the hash values of the pattern. The algorithm iterates through the text and compares the hash values with the hash values in the table. If a match is found, the algorithm returns the starting index of the match.
