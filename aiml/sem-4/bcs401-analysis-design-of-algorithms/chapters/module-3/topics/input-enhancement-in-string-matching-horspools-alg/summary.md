# Input Enhancement in String Matching: Horspool's Algorithm

### Overview

Horspool's Algorithm is a string searching algorithm that uses input enhancement to improve the efficiency of the classic Boyer-Moore algorithm.

### Key Points

- **Input Enhancement**: A technique to reduce the number of bad matches by adjusting the starting point of the search in the next iteration.
- **Horspool's Algorithm**: An optimized string searching algorithm that uses input enhancement to achieve a linear time complexity of O(n/m) in the worst case.
- **Signature**: A prefix of the pattern string that is used to determine the starting point of the search.
- **Bad Match**: A mismatch between the pattern and the text that causes the algorithm to move the starting point of the search.
- **Good Match**: A match between the pattern and the text that allows the algorithm to move the starting point of the search.

### Important Formulas and Definitions

- **Bad Match**: A mismatch between the pattern and the text that causes the algorithm to move the starting point of the search. The bad match is defined as the first character that differs between the pattern and the text.
- **Good Match**: A match between the pattern and the text that allows the algorithm to move the starting point of the search.
- **Horspool's Algorithm Formula**: `shift = (pattern[i] - text[shift]) * (26^(n-1-i))`, where `shift` is the starting point of the search, `pattern[i]` is the `i`-th character of the pattern, `text[shift]` is the `shift`-th character of the text, and `n` is the length of the pattern.

### Theorem

- **Horspool's Algorithm Theorem**: If the input is uniformly distributed, then Horspool's Algorithm has a time complexity of O(n/m) in the worst case.

### Important Theorems and Lemmas

- **Boyer-Moore-Horspool Algorithm Theorem**: The Boyer-Moore-Horspool algorithm has a time complexity of O(n/m) in the worst case.
- **Horspool's Algorithm Lemma**: If the input is uniformly distributed, then Horspool's Algorithm has a time complexity of O(n/m) in the worst case.

### Conclusion

Horspool's Algorithm is an efficient string searching algorithm that uses input enhancement to achieve a linear time complexity of O(n/m) in the worst case. It is widely used in many applications, including text searching and pattern matching.
