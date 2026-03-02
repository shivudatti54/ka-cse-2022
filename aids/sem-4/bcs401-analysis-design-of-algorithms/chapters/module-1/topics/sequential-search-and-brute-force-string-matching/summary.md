# Sequential Search and Brute Force String Matching

**Definitions and Notations**

- **String Matching**: The process of finding a substring (pattern) within a larger string.
- **Pattern**: The substring to be searched within the larger string.
- **Text**: The larger string in which the pattern is to be searched.
- **Match**: A location of the pattern within the text.

**Brute Force String Matching**

- **Brute Force Algorithm**: A simple, yet inefficient algorithm that tries all possible substrings of the text as the pattern.
- **Time Complexity**: O(n\*m), where n is the length of the text and m is the length of the pattern.

**Sequential Search (Linear Search) String Matching**

- **Sequential Search Algorithm**: A modified brute force algorithm that starts from the first character of the text and compares it with the pattern.
- **Time Complexity**: O(n), where n is the length of the text.

**Key Formulas and Theorems**

- **Rabin-Karp Algorithm**: A more efficient algorithm that uses hashing to find the pattern in the text.
- **Knuth-Morris-Pratt (KMP) Algorithm**: A more efficient algorithm that uses the lps (longest proper prefix which is also a suffix) array to find the pattern in the text.
- **Boyer-Moore Algorithm**: A more efficient algorithm that uses the bad character heuristic to find the pattern in the text.

**Important Steps**

- Initialize the pattern and text.
- Preprocess the pattern to create the lps array (if KMP algorithm is used).
- Compare the first character of the text with the first character of the pattern.
- Shift the text by one character and compare the next character with the next character of the pattern.
- Repeat the process until the end of the text is reached.

**Revision Tips**

- Understand the time and space complexities of each algorithm.
- Learn the different algorithms and their applications.
- Practice solving string matching problems using different algorithms.
