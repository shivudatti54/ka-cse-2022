# KMP String Matching Algorithm - Summary

## Key Definitions and Concepts

- **String Matching**: Finding occurrences of a pattern string within a larger text string
- **Failure Function (π array)**: An array where π[i] stores the length of the longest proper prefix of pattern[0...i] that is also a suffix of this substring
- **Proper Prefix**: A prefix that is not equal to the entire string (e.g., "A", "AB", "ABA" are proper prefixes of "ABAB")
- **LPS (Longest Proper Prefix which is also Suffix)**: Another name for the failure function values

## Important Formulas and Theorems

- **Preprocessing Time**: O(m) where m is the pattern length
- **Search Time**: O(n) where n is the text length
- **Total Time Complexity**: O(n + m)
- **Space Complexity**: O(m) for storing the failure function
- **π[0] = 0**: Always true for any pattern
- **Failure function update**: If pattern[i] == pattern[j], then π[i] = j + 1; else j = π[j-1] and repeat

## Key Points

- KMP achieves linear time complexity by preprocessing the pattern to create a failure function
- When a mismatch occurs, instead of restarting from the beginning, KMP uses the failure function to skip characters
- The failure function contains information about self-overlapping portions of the pattern
- KMP never re-examines characters in the text that have already been matched
- The algorithm finds all non-overlapping and overlapping occurrences of the pattern
- Both preprocessing and search phases can be performed in a single pass through the text
- KMP is optimal for worst-case scenarios, unlike brute-force which can degrade severely

## Common Mistakes to Avoid

- Forgetting that π[0] is always 0 (single character has no proper prefix)
- Confusing "prefix" with "proper prefix" - the entire string is NOT a proper prefix
- When computing failure function, not updating the index j correctly after a mismatch
- Attempting to use the failure function value for the current position j, rather than j-1 when shifting after mismatch
- Believing KMP requires backtracking in the text - it only shifts the pattern

## Revision Tips

1. Practice computing failure functions for at least 5 different patterns before the exam
2. Hand-trace one complete example showing both preprocessing and search phases
3. Memorize that the answer after a mismatch at position j is π[j-1], not π[j]
4. Compare KMP with brute force: understand why KMP doesn't re-examine text characters
5. Remember the worst-case O(n×m) scenario for brute force occurs with patterns like "AAA" in "AAAAAAA"