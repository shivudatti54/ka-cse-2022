# **Input Enhancement in String Matching: Horspool’s Algorithm**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Horspool’s Algorithm](#horspools-algorithm)
3. [How Horspool’s Algorithm Works](#how-horspools-algorithm-works)
4. [Advantages of Horspool’s Algorithm](#advantages-of-horspools-algorithm)
5. [Implementation](#implementation)
6. [Example Use Case](#example-use-case)
7. [Conclusion](#conclusion)

## **Introduction**

String searching is a fundamental problem in computer science, where we need to find a pattern within a larger string. Horspool’s algorithm is a popular string matching algorithm that uses input enhancement to improve its performance.

## **Horspool’s Algorithm**

Horspool’s algorithm is a linear-time string matching algorithm that uses a combination of hashing and shifting to find a pattern within a larger string. It was first proposed by David Horspool in 1977.

## **How Horspool’s Algorithm Works**

Here's a step-by-step explanation of how Horspool’s algorithm works:

- Initialize a hash table (or a lookup table) that stores the last occurrence of each character in the pattern.
- Initialize a variable `shift` to 0, which represents the shift amount.
- Iterate through the text string, starting from the first character.
- For each character in the text string, calculate the hash value using the current shift amount.
- Compare the hash value with the corresponding character in the pattern.
- If the characters match, increment the `shift` amount and continue the search.
- If the characters don't match, update the hash table with the current character and the corresponding shift amount.
- Repeat the process until the end of the text string is reached.

## **Key Concepts**

- **Hash Table**: A data structure that stores the last occurrence of each character in the pattern.
- **Shift Amount**: A variable that represents the amount by which the hash value is shifted.
- **Hash Value**: A numerical representation of the character in the pattern.

## **Advantages of Horspool’s Algorithm**

- **Linear Time Complexity**: Horspool’s algorithm has a linear time complexity of O(n), where n is the length of the text string.
- **Good Performance**: Horspool’s algorithm performs well even for large text strings and patterns.
- **Simple Implementation**: The algorithm is relatively simple to implement and understand.

## **Implementation**

Here's a simple implementation of Horspool’s algorithm in Python:

```python
def horsepool(text, pattern):
    # Initialize the hash table
    hash_table = {}
    for i in range(len(pattern)):
        hash_table[pattern[i]] = i

    # Initialize the shift amount
    shift = 0

    # Iterate through the text string
    for i in range(len(text)):
        # Calculate the hash value
        hash_value = (ord(text[i + shift]) - ord(pattern[0])) % 256

        # Compare the hash value with the corresponding character
        if text[i] == pattern[0]:
            # If the characters match, increment the shift amount
            while hash_value == 0 and i + shift < len(text):
                hash_value = (ord(text[i + shift + 1]) - ord(pattern[0])) % 256
                shift += 1

            # If the characters don't match, update the hash table
            if hash_value != 0:
                hash_table[text[i]] = i
        else:
            # Update the hash table with the current character
            hash_table[text[i]] = i

    # Find the first occurrence of the pattern
    for key, value in hash_table.items():
        if value == 0:
            return -1
        elif value < len(text) - len(pattern):
            return value

    # If the pattern is not found, return -1
    return -1

# Example usage
text = "banana"
pattern = "ana"
result = horsepool(text, pattern)
print(result)
```

## **Example Use Case**

Horspool’s algorithm is commonly used in various applications, including:

- **Text Search**: Horspool’s algorithm can be used to search for patterns within a large text string.
- **Data Compression**: Horspool’s algorithm can be used to compress data by finding repeated patterns and replacing them with a single occurrence.
- **Cryptography**: Horspool’s algorithm can be used in cryptographic applications, such as data encryption and decryption.

## **Conclusion**

In conclusion, Horspool’s algorithm is a popular string matching algorithm that uses input enhancement to improve its performance. Its advantages include linear time complexity, good performance, and simple implementation. The algorithm can be used in various applications, including text search, data compression, and cryptography.
