# Sequential Search and Brute Force String Matching

### Overview

- **Sequential Search**: A algorithmic technique used to find a specific substring within a larger string.
- **Brute Force String Matching**: A algorithmic technique used to find all occurrences of a substring within a larger string.

### Definitions

- **Substring**: A sequence of characters within a string.
- **Pattern**: The substring to be searched for within the larger string.
- **Text**: The larger string in which the pattern is to be searched for.

### Algorithms

#### Sequential Search

- **Time Complexity**: O(n), where n is the length of the text and pattern.
- **Space Complexity**: O(1), as only a constant amount of space is required.
- **Steps**:
  1. Initialize two pointers, one for the text and one for the pattern.
  2. Compare the characters at the current positions of the two pointers.
  3. If the characters match, move the pointers forward.
  4. If the characters do not match, move the pointer for the pattern forward by one position.
  5. Repeat steps 2-4 until the end of the pattern is reached.

#### Brute Force String Matching

- **Time Complexity**: O(n\*m), where n is the length of the text and m is the length of the pattern.
- **Space Complexity**: O(1), as only a constant amount of space is required.
- **Steps**:
  1. Generate all possible substrings of the text with the same length as the pattern.
  2. Compare each substring with the pattern using the sequential search algorithm.
  3. If a match is found, report the match.

### Important Formulas and Theorems

- **Rabin-Karp Algorithm**: A variation of the brute force algorithm using hashing to reduce the time complexity to O(n+m).
- **Knuth-Morris-Pratt Algorithm**: A variation of the sequential search algorithm using a lookup table to reduce the time complexity to O(n+m).

### Key Points

- Sequential search has a linear time complexity, making it suitable for small patterns and large texts.
- Brute force string matching has a quadratic time complexity, making it unsuitable for large patterns and large texts.
- Rabin-Karp and Knuth-Morris-Pratt algorithms are variations of the brute force and sequential search algorithms, respectively, that reduce the time complexity.
