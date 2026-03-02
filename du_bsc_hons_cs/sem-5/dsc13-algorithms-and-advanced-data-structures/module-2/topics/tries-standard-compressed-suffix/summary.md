# Tries: Standard and Compressed Suffix Tries - Summary

## Key Definitions and Concepts

- **Trie (Prefix Tree):** An ordered tree data structure where each node represents a character, and paths from root to nodes represent prefixes of stored strings.

- **Standard Trie:** A trie where each edge carries exactly one character, and nodes explicitly store every character in the string.

- **Compressed Trie (Radix Trie):** A space-optimized variant that compresses single-child chains into edges with concatenated character labels.

- **Suffix Trie:** A specialized trie containing all suffixes of a given string; requires O(n²) space for string of length n.

- **End-of-Word Marker:** A special flag in each node indicating whether the path to that node represents a complete stored string.

## Important Formulas and Theorems

- **Search Complexity:** O(m) where m = length of string being searched
- **Insert Complexity:** O(m) time, O(m) new nodes in worst case
- **Space Complexity (Standard):** O(Σ × m × n) where Σ = alphabet size, m = avg string length, n = number of strings
- **Space Complexity (Compressed):** Significantly reduced; typically O(m × n) with compression factor of 2-10x
- **Prefix Query:** O(m + k) where k = number of words with given prefix

## Key Points

- Tries excel at prefix-based operations, providing O(m) lookup regardless of total number of stored strings.

- The root node represents an empty string; each level deeper represents one more character.

- Standard tries use significant memory for alphabets like English (26 characters per node in array representation).

- Compressed tries eliminate single-child chains, reducing nodes and edges proportionally.

- Suffix tries enable O(m) pattern matching but require quadratic space for the original string.

- Tries maintain sorted order inherently (lexicographic), unlike hash tables.

- Applications include autocomplete, spell checkers, IP routing, and bioinformatics.

## Common Mistakes to Avoid

1. **Confusing tries with BSTs:** Tries use character-by-character traversal along edges; BSTs compare entire keys at each node.

2. **Forgetting end-of-word markers:** A node being present doesn't guarantee a complete word ends there (e.g., "car" vs "care").

3. **Ignoring alphabet size:** Using array representation for large alphabets wastes massive space; use hash maps instead.

4. **Over-compressing:** Only compress paths where every node has exactly one non-end-of-word child.

5. **Space calculation errors:** Remember that compressed tries store string slices, not just single characters, affecting memory calculations.

## Revision Tips

1. **Practice building tries by hand:** Draw the trie for {"cat", "car", "care", "career"} to reinforce structure concepts.

2. **Trace operations:** Manually trace insert and search operations to understand the O(m) complexity argument.

3. **Compare with alternatives:** Create a decision matrix for when to use tries vs. hash tables vs. BSTs.

4. **Understand compression mechanics:** Practice converting standard trie paths to compressed form and analyze space savings.

5. **Review suffix tree relationship:** Know that compressed suffix tries are essentially suffix trees with additional constraints.