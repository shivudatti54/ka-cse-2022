# Sequential Search and Brute Force String Matching

## **Key Concepts**

- **Sequential Search**: A searching algorithm that checks each element in a list one by one.
- **Brute Force String Matching**: A string matching algorithm that checks all possible substrings of the target string against the pattern string.
- **Pattern Matching Problem**: Given a pattern string and a text string, find all occurrences of the pattern in the text.

## **Algorithms**

### Sequential Search (Linear Search) for String Matching

- **Time Complexity**: O(n \* m), where n is the length of the text string and m is the length of the pattern string.
- **Formula**: `text = text[0] + text[1] + ... + text[n-1]`, `pattern = pattern[0] + pattern[1] + ... + pattern[m-1]`.
- **Step-by-Step Solution**:
  1.  Start from the first character of the text string.
  2.  Compare the current character of the text string with the first character of the pattern string.
  3.  If they match, move to the next character in both strings and repeat step 2.
  4.  If they don't match, move to the next character in the text string.

### Brute Force String Matching

- **Time Complexity**: O(n \* m^2), where n is the length of the text string and m is the length of the pattern string.
- **Formula**: `text = text[0] + text[1] + ... + text[n-1]`, `pattern = pattern[0] + pattern[1] + ... + pattern[m-1]`.
- **Step-by-Step Solution**:
  1.  Generate all possible substrings of the text string with the same length as the pattern string.
  2.  Compare each substring with the pattern string using the sequential search algorithm.
  3.  If a match is found, report the starting position of the match.

## **Important Formulas and Definitions**

- **Big O Notation**: A measure of the complexity of an algorithm, expressed as a function of the size of the input.
- **String Matching Problem**: Given a pattern string and a text string, find all occurrences of the pattern in the text.

## **Theorem**

- **Knuth-Morris-Pratt Algorithm**: A linear-time string searching algorithm that uses the lps (longest proper prefix which is also a suffix) array to preprocess the pattern string and improve the efficiency of the sequential search algorithm.

## **Revision Tips**

- Understand the basic concepts of sequential search and brute force string matching.
- Be familiar with the time complexities and formulas of these algorithms.
- Practice implementing these algorithms on different inputs to improve your problem-solving skills.
