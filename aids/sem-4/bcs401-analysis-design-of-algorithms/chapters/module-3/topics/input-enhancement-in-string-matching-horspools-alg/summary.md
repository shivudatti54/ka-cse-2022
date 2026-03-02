# **Input Enhancement in String Matching: Horspool’s Algorithm**

## **Definition and Notation**

- **Horspool’s Algorithm**: A string searching algorithm that uses a preprocessing step to enhance input strings for faster matching.
- **String Matching**: Finding occurrences of a pattern within a text.
- **Shift**: The number of characters to shift the pattern when a mismatch occurs.
- **Failure Function**: A table that stores the last occurrence of a substring in the text.

## **Key Points**

- **Preprocessing Step**:
  - Create a failure function table to store the last occurrence of each substring.
  - Calculate the shift value for each substring based on the failure function.
- **Main Loop**:
  - Compare characters between the pattern and the text.
  - If a mismatch occurs, shift the pattern by the calculated shift value.
  - If a match occurs, mark the occurrence in the table.
- **Time Complexity**: O(n + m) where n is the length of the text and m is the length of the pattern.
- **Space Complexity**: O(m) for the failure function table.

## **Important Formulas and Definitions**

- **Failure Function**: f[i] = last(i, text) where last(i, text) is the last occurrence of substring i in text.
- **Shift Value**: s[i] = max(1, len(pattern) - 1 - (f[i] - i)) where len(pattern) is the length of the pattern.
- **Horspool’s Algorithm**: A(1 ... n) = pattern[1 ... m] \* (m - 1)

## **Important Theorems**

- **Horspool’s Algorithm**: A string matching algorithm that uses a preprocessing step to enhance input strings for faster matching.

## **Revision Notes**

- Horspool’s Algorithm uses a preprocessing step to create a failure function table.
- The main loop compares characters between the pattern and the text, shifting the pattern by the calculated shift value when a mismatch occurs.
- The algorithm has a time complexity of O(n + m) and a space complexity of O(m).
