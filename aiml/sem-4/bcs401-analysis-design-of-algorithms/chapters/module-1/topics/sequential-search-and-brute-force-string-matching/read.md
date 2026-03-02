# **Sequential Search and Brute Force String Matching**

## **Introduction**

String matching is a fundamental problem in computer science, where we need to find a specific substring within a larger string. In this section, we will discuss two common approaches to solve this problem: Sequential Search and Brute Force string matching.

## **Sequential Search**

### Definition

Sequential Search is a method of finding a specific substring within a larger string by iterating through the characters of the string one by one.

### Algorithm

1. Initialize two pointers, `i` and `j`, to 0, which will be used to traverse the string and the substring respectively.
2. Compare the characters at the current positions `i` and `j` in the string and the substring.
3. If the characters match, increment both `i` and `j` by 1.
4. If the characters do not match, increment `i` by 1 and reset `j` to 0.
5. Repeat steps 2-4 until `j` reaches the end of the substring.
6. If `j` reaches the end of the substring, return true indicating that the substring was found.
7. If the end of the string is reached without finding the substring, return false.

### Example

Suppose we want to find the substring "abc" in the string "abcdefg".

| i   | j   | chars | result |
| --- | --- | ----- | ------ |
| 0   | 0   | a     |        |
| 0   | 1   | b     |        |
| 0   | 2   | c     |        |
| 0   | 3   | d     |        |
| 0   | 4   | e     |        |
| 0   | 5   | f     |        |
| 0   | 6   | g     |        |
| 1   | 0   | a     |        |
| 1   | 1   | b     |        |
| 1   | 2   | c     |        |
| 1   | 3   |       |        |
| 1   | 4   | d     |        |
| 1   | 5   | e     |        |
| 1   | 6   | f     |        |
| 1   | 7   | g     |        |
| 2   | 0   |       |        |
| 2   | 1   | a     |        |
| 2   | 2   | b     |        |
| 2   | 3   | c     |        |
| 2   | 4   |       |        |
| 2   | 5   | d     |        |
| 2   | 6   | e     |        |
| 2   | 7   | f     |        |
| 2   | 8   | g     |        |

As we can see, the substring "abc" is found at position 0.

### Code

```python
def sequential_search(string, substring):
    i = j = 0
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            j += 1
        else:
            i += 1
    return j == len(substring)
```

## **Brute Force String Matching**

### Definition

Brute Force string matching is a method of finding a specific substring within a larger string by checking all possible substrings of the larger string.

### Algorithm

1. Generate all possible substrings of the larger string.
2. Compare each substring with the target substring.
3. If a match is found, return true.
4. If no match is found, return false.

### Example

Suppose we want to find the substring "abc" in the string "abcdefg".

| substring | chars | result |
| --------- | ----- | ------ |
| a         | a     |        |
| ab        | b     |        |
| abc       | c     |        |
| abcd      | d     |        |
| abce      | e     |        |
| abcdg     | f     |        |
| abcdfg    |       |        |

As we can see, the substring "abc" is found at position 0.

### Code

```python
def brute_force_search(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return True
    return False
```

## **Comparison of Sequential Search and Brute Force**

|                  | Sequential Search           | Brute Force                   |
| ---------------- | --------------------------- | ----------------------------- |
| Time Complexity  | O(n)                        | O(n\*m)                       |
| Space Complexity | O(1)                        | O(1)                          |
| Practicality     | Efficient for large strings | Inefficient for large strings |
| Difficulty       | Easy to implement           | Difficult to implement        |

In conclusion, Sequential Search is a more efficient and practical approach for string matching, especially for large strings. However, Brute Force string matching can be useful in certain situations, such as when the target substring is very short or when the implementation is required for educational purposes.
