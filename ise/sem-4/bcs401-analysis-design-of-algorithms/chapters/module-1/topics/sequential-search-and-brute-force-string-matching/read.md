# Sequential Search and Brute Force String Matching

## Table of Contents

1. [Definition and Problem Statement](#definition-and-problem-statement)
2. [Sequential Search Algorithm](#sequential-search-algorithm)
3. [Brute Force Algorithm](#brute-force-algorithm)
4. [Time and Space Complexity](#time-and-space-complexity)
5. [Example Use Cases](#example-use-cases)
6. [Code Implementation](#code-implementation)

### Definition and Problem Statement

String matching is a fundamental problem in computer science that involves finding a specific pattern within a larger string. The problem can be classified into two categories:

- **Exact matching**: Find a specific pattern within a string.
- **Substring matching**: Find all occurrences of a specific pattern within a string.

Sequential search and brute force string matching are two approaches to solve these problems.

### Sequential Search Algorithm

The sequential search algorithm is a simple and intuitive approach to find a specific pattern within a string. It works by iterating through each character of the string and comparing it to the corresponding character of the pattern.

**Step-by-Step Process:**

1.  Initialize two pointers, one for the string and one for the pattern.
2.  Compare the characters at the current positions of the string and pattern.
3.  If the characters match, move the pointers one position forward.
4.  If the characters do not match, move the pointer for the string one position forward.
5.  Repeat steps 2-4 until the end of the string or pattern is reached.
6.  If the entire pattern is matched, return the starting position of the match.

**Example:**

Suppose we want to find the pattern "abc" within the string "abcdefg".

| String | Pattern | Pointers |
| ------ | ------- | -------- |
| a      | a       | (0,0)    |
| b      | b       | (0,1)    |
| c      | c       | (0,2)    |
| d      | a       | (1,0)    |
| e      | b       | (2,1)    |
| f      | c       | (3,2)    |
| g      | d       | (4,3)    |

Since the characters at positions (0,2) and (3,3) do not match, we move the pointer for the string one position forward.

### Brute Force Algorithm

The brute force algorithm is an exhaustive approach to find a specific pattern within a string. It works by generating all possible subsequences of the string and comparing them to the pattern.

**Step-by-Step Process:**

1.  Generate all possible subsequences of the string.
2.  Compare each subsequence to the pattern.
3.  If a match is found, return the starting position of the match.

**Example:**

Suppose we want to find the pattern "abc" within the string "abcdefg".

| Subsequence | Pattern |
| ----------- | ------- | -------- |
| a           | a       | Match    |
| bc          | bc      | Match    |
| c           | a       | No match |
| def         | ab      | No match |
| ef          | c       | Match    |
| ...         | ...     | ...      |

The brute force algorithm has a high time complexity due to the generation of all possible subsequences.

### Time and Space Complexity

| Algorithm         | Time Complexity | Space Complexity |
| ----------------- | --------------- | ---------------- |
| Sequential Search | O(n)            | O(1)             |
| Brute Force       | O(n\*m)         | O(n\*m)          |

### Example Use Cases

- **File searching**: Sequential search can be used to find a specific word within a large text file.
- **Text editing**: Brute force algorithm can be used to find all occurrences of a specific word within a large text document.

### Code Implementation

Here is an example implementation of the sequential search algorithm in Python:

```python
def sequential_search(string, pattern):
    for i in range(len(string)):
        if string[i] == pattern[0]:
            for j in range(len(pattern)):
                if string[i + j] != pattern[j]:
                    break
                if j == len(pattern) - 1:
                    return i
    return -1

string = "abcdefg"
pattern = "abc"
match = sequential_search(string, pattern)
if match != -1:
    print("Pattern found at position", match)
else:
    print("Pattern not found")

```

And here is an example implementation of the brute force algorithm in Python:

```python
def brute_force(string, pattern):
    for i in range(len(string) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if string[i + j] != pattern[j]:
                match = False
                break
        if match:
            print("Pattern found at position", i)
    return None

string = "abcdefg"
pattern = "abc"
brute_force(string, pattern)
```

Note that the brute force algorithm has a high time complexity and is not suitable for large strings or patterns.
