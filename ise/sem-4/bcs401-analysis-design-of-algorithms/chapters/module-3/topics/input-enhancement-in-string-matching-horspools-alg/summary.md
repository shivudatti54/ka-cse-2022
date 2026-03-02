# Input Enhancement in String Matching: Horspool’s Algorithm

## Summary

Horspool's Algorithm is an efficient string searching algorithm that takes advantage of the input to enhance its performance.

### Key Points

- **Problem Statement:** Given a text and a pattern, find the first occurrence of the pattern in the text.
- **Input Enhancement:** The algorithm uses the input to shift the pattern along the text, reducing the number of comparisons required.
- **Key Idea:** The shift is based on the last character of the pattern and its position in the alphabet.
- **Formula:** `shift = (c - 'a') mod 256`, where `c` is the last character of the pattern and `'a'` is the ASCII value of 'a'.
- **Theorem:** The algorithm has a time complexity of O(n + m), where n is the length of the text and m is the length of the pattern.
- **Key Steps:**
  - Preprocess the pattern to create a lookup table.
  - Iterate through the text, comparing the pattern with the text using the lookup table.
  - Shift the pattern based on the comparison result.
- **Advantages:**
  - Fast and efficient for short patterns.
  - Uses the input to reduce the number of comparisons required.
- **Disadvantages:**
  - May not be suitable for long patterns or large texts.

### Important Definitions

- **Shift:** The number of positions to shift the pattern along the text.
- **Lookup Table:** A table used to store the comparisons between the pattern and the text.
- **Pattern:** The string to be searched for in the text.
- **Text:** The string in which the pattern is to be searched.

### Important Formulas and Theorems

- **Shift formula:** `shift = (c - 'a') mod 256`, where `c` is the last character of the pattern and `'a'` is the ASCII value of 'a'.
- **Time complexity:** O(n + m), where n is the length of the text and m is the length of the pattern.
