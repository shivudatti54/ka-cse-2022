# Text Search Algorithms - Summary

## Key Definitions and Concepts

- **Pattern Matching**: Finding occurrences of a pattern string within a larger text string
- **Prefix Function (lps)**: In KMP, an array storing the length of the longest proper prefix that is also a suffix for each position
- **Rolling Hash**: Hash technique allowing O(1) computation of hash for consecutive substrings
- **Bad Character Rule**: Boyer-Moore heuristic shifting pattern based on mismatched text character
- **Good Suffix Rule**: Boyer-Moore heuristic shifting pattern based on matched suffix information

## Important Formulas and Theorems

- Naive Algorithm: Time O(n × m), Space O(1)
- KMP Algorithm: Time O(n + m), Space O(m)
- Boyer-Moore: Time O(n × m) worst, O(n/m) average, Space O(m + σ)
- Rabin-Karp: Time O(n + m) average, Space O(1)
- Finite Automata: Time O(n) search, Space O(m × σ)

## Key Points

- Naive approach compares pattern at every position, performing redundant work
- KMP uses pre-computed prefix function to skip characters after mismatches
- Boyer-Moore scans pattern from right to left, often skipping large portions
- Rabin-Karp uses hashing to find potential matches quickly
- Finite automata guarantee linear search time after preprocessing
- Choice of algorithm depends on pattern length, alphabet size, and text characteristics

## Common Mistakes to Avoid

- Confusing proper prefix with prefix (proper prefix cannot be the entire string)
- Forgetting that Boyer-Moore scans right-to-left while most algorithms scan left-to-right
- Assuming hash matches in Rabin-Karp are always correct (must verify with direct comparison)
- Incorrectly computing prefix function values for overlapping patterns

## Revision Tips

1. Practice prefix function computation for at least 5 different patterns
2. Trace through KMP and Boyer-Moore manually on small examples
3. Remember the worst-case vs average-case trade-offs between algorithms
4. Focus on understanding when to apply each algorithm in practical scenarios
