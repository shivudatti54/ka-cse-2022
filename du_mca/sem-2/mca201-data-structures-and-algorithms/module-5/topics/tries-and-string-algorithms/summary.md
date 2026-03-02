# Tries and String Algorithms - Summary

## Key Definitions and Concepts

- **Trie (Prefix Tree):** A tree data structure where each node represents a character, paths from root to nodes represent prefixes, and end-of-word markers indicate complete words. Enables O(m) insertion, search, and deletion.

- **Failure Function (LPS Array):** In KMP, this array stores the length of the longest proper prefix that is also a suffix for each position in the pattern, enabling efficient skipping during mismatches.

- **Rolling Hash:** A technique in Rabin-Karp that computes hash values for overlapping substrings in O(1) time by updating the previous hash value rather than recomputing from scratch.

- **Bad-Character Rule (Boyer-Moore):** Heuristic that uses the mismatched character in text to determine pattern shift, aligning the rightmost occurrence in the pattern.

- **Good-Suffix Rule (Boyer-Moore):** Heuristic that uses information about matched suffixes to determine pattern shift after a mismatch.

## Important Formulas and Theorems

- **Naive Pattern Matching:** Time Complexity O(mn), Space O(1)
- **KMP Algorithm:** Time O(m+n), Space O(m) for LPS array
- **Rabin-Karp:** Average Time O(m+n), Worst O(mn), Space O(1)
- **Boyer-Moore:** Average O(n/m), Worst O(mn), Space O(σ) for bad-character table
- **Trie Operations:** Time O(m) per operation, Space O(Σm) where Σ is alphabet size

## Key Points

- Trie provides efficient prefix operations making it ideal for autocomplete and dictionary implementations
- KMP preprocessing builds LPS array in O(m) time, achieving linear search time
- Rabin-Karp uses hashing to reduce character comparisons, with hash collisions handled by verification
- Boyer-Moore's right-to-left scanning often outperforms other algorithms for natural language text
- Space-Time tradeoff is fundamental: faster algorithms typically require more memory
- Rolling hash enables O(1) hash recomputation for sliding windows in Rabin-Karp

## Common Mistakes to Avoid

- Confusing the direction of comparison in Boyer-Moore (right-to-left vs. left-to-right)
- Forgetting to verify hash matches in Rabin-Karp due to potential false positives from collisions
- Incorrectly computing the LPS array in KMP, especially when handling fallback positions
- Not marking end-of-word nodes in trie implementation, leading to prefix-only matches succeeding incorrectly
- Using naive approach when efficient algorithms are expected in exam solutions

## Revision Tips

1. Practice computing LPS arrays manually for various patterns until the process becomes automatic
2. Trace through each algorithm with small examples like searching "ABA" in "ABABABA"
3. Remember the key insight of each algorithm: KMP uses previously matched information, Boyer-Moore uses right-to-left scanning, Rabin-Karp uses hashing
4. Focus on understanding when to use each algorithm based on problem characteristics
5. Review trie implementation code and be able to add features like word frequency counting