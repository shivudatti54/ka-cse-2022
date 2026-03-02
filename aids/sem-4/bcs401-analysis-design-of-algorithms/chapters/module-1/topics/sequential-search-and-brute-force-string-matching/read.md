# Sequential Search and Brute Force String Matching

### Introduction

String matching is a fundamental problem in computer science that deals with finding a substring within a larger string. This topic is crucial in algorithmic problem solving, as it has numerous applications in text processing, data compression, and cryptography. In this study material, we will cover two common algorithms for string matching: Sequential Search and Brute Force.

### Definitions

- **String**: A sequence of characters, such as "hello" or "world".
- **Substring**: A portion of a string, such as "he" or "worlds".
- **Matching**: Finding a substring within a larger string.

### Sequential Search

Sequential search is a simple algorithm that checks each character of the target string against the characters of the substring. It starts from the first character of the target string and compares it with the first character of the substring. If they match, it moves on to the next character in the target string and compares it with the next character in the substring.

**Algorithm:**

- Initialize two pointers, `target` and `substring`, to point to the first character of the target string and the substring respectively.
- Compare the characters at the current positions of `target` and `substring`.
- If they match, move the `substring` pointer forward by one character.
- If they do not match, move the `target` pointer forward by one character.
- Repeat steps 2-4 until the `target` pointer reaches the end of the target string.

**Example:**

Suppose we want to find the substring "hello" within the string "hello world".

| Target String | Substring | Position |
| ------------- | --------- | -------- |
| h             | h         | 0        |
| e             | e         | 1        |
| l             | l         | 2        |
| l             | l         | 3        |
| o             | o         | 4        |
|               |           |          |

As we can see, the substring "hello" is found at position 0.

**Time Complexity:** O(n), where n is the length of the target string.

**Space Complexity:** O(1), as we only use a constant amount of space.

### Brute Force String Matching

Brute force string matching is a more complex algorithm that tries all possible substrings of the target string and checks if they match the given string. It is called "brute force" because it uses a systematic approach to try all possible solutions.

**Algorithm:**

- Generate all possible substrings of the target string.
- For each substring, compare it with the given string.
- If a match is found, return the position of the match.

**Example:**

Suppose we want to find the substring "hello" within the string "hello world".

| Substring | Position |
| --------- | -------- |
| hello     | 0        |
| ello      | 1        |
| llo       | 2        |
| lo        | 3        |
| o         | 4        |
| world     | 6        |

As we can see, the substring "hello" is found at position 0.

**Time Complexity:** O(n^2), where n is the length of the target string. This is because we generate all possible substrings of the target string, which has a time complexity of O(n).

**Space Complexity:** O(n), as we need to store all possible substrings of the target string.

### Key Concepts

- **Sequential Search**: A simple algorithm that checks each character of the target string against the characters of the substring.
- **Brute Force String Matching**: A more complex algorithm that tries all possible substrings of the target string and checks if they match the given string.
- **Time Complexity**: The amount of time an algorithm takes to complete.
- **Space Complexity**: The amount of space an algorithm uses.

### Conclusion

Sequential search and brute force string matching are two common algorithms for string matching. While sequential search is simple and efficient, brute force string matching is more complex but can handle larger strings. Understanding these algorithms is crucial for solving string matching problems in algorithmic problem solving.

### Practice Problems

1.  Implement the sequential search algorithm in Python to find the substring "hello" within the string "hello world".
2.  Implement the brute force string matching algorithm in Python to find the substring "hello" within the string "hello world".
3.  Compare the time and space complexities of the two algorithms.

### References

- "Introduction to Algorithms" by Thomas H. Cormen
- "Algorithms" by Robert Sedgewick and Kevin Wayne
- "String Matching" by Donald E. Knuth
