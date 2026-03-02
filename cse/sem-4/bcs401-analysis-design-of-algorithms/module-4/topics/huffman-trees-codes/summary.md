# Huffman Trees And Codes - Summary

## Key Definitions

- **Prefix Code**: A coding system where no codeword is a prefix of any other codeword, ensuring unique decodability
- **Huffman Tree**: A binary tree constructed bottom-up using greedy approach where leaves represent characters
- **Codeword**: The sequence of bits (0 for left edge, 1 for right edge) from root to a leaf
- **Optimal Code**: A prefix code with minimum average code length for given symbol frequencies

## Important Formulas

- **Total Cost**: Σ(frequency_i × depth_i) for all characters
- **Average Code Length**: Total Cost / Total Frequency
- **Time Complexity**: O(n log n) where n = number of unique characters
- **Space Complexity**: O(n)

## Key Points

- Huffman coding uses greedy approach: always combine the two minimum frequency symbols first
- The algorithm produces optimal prefix codes (proven via exchange argument)
- Characters with higher frequencies get shorter codewords
- Huffman codes are uniquely decodable without needing delimiters
- Decoding: traverse from root, following 0 (left) and 1 (right) until leaf is reached
- Huffman coding is foundational for many compression formats (JPEG, MP3, ZIP)
- Average code length approaches entropy when frequencies follow power law distribution

## Common Mistakes

- Forgetting to reset to root after reaching a leaf during decoding
- Assigning wrong bit values to left/right edges (must be consistent)
- Not considering that multiple optimal trees may exist for certain frequency distributions
- Confusing the number of iterations (n-1 merges for n characters)
- Calculating compression ratio incorrectly—remember to account for variable codeword lengths
