# Huffman Trees And Codes

## Table of Contents

- [Huffman Trees And Codes](#huffman-trees-and-codes)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Prefix Codes and Code Trees](#prefix-codes-and-code-trees)
  - [The Huffman Greedy Algorithm](#the-huffman-greedy-algorithm)
  - [Optimality Proof](#optimality-proof)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Decoding Procedure](#decoding-procedure)
- [Examples](#examples)
  - [Example 1: Constructing Huffman Tree](#example-1-constructing-huffman-tree)
  - [Example 2: Computing Compression Ratio](#example-2-computing-compression-ratio)
  - [Example 3: Decoding Huffman-Encoded Message](#example-3-decoding-huffman-encoded-message)
- [Exam Tips](#exam-tips)

## Introduction

Huffman coding is a fundamental lossless data compression algorithm developed by David A. Huffman in 1952. It employs a greedy approach to construct an optimal prefix-free code for compressing data based on the frequency of characters. The algorithm assigns variable-length codes to input characters, where characters that occur more frequently receive shorter codes, thereby achieving compression.

The fundamental principle behind Huffman coding lies in constructing a binary tree where leaves represent characters and the path from the root to a leaf defines the codeword. This tree structure ensures that no codeword is a prefix of another, making the code uniquely decodable. Huffman coding achieves near-optimal compression, making it the foundation for many modern compression formats including JPEG, MP3, and ZIP files.

This topic explores the theoretical underpinnings of Huffman coding, its algorithmic implementation, the proof of optimality, and practical considerations for both encoding and decoding procedures.

## Key Concepts

### Prefix Codes and Code Trees

A **prefix code** is a coding system where no codeword is a prefix of any other codeword. This property ensures unique decodability—if we know where each codeword begins and ends, we can decode the message unambiguously without needing delimiters between codewords.

The code tree representation provides a visual and mathematical framework for understanding prefix codes:

- Each internal node has exactly two children (binary tree)
- The left edge represents bit '0' and the right edge represents bit '1'
- Each leaf stores a character and its frequency
- The codeword for a character is the sequence of edge labels on the path from root to leaf

**Theorem (Prefix Code Property):** A code is prefix-free if and only if its code tree has all characters at leaf nodes.

### The Huffman Greedy Algorithm

The Huffman algorithm constructs the optimal prefix code using a bottom-up greedy approach:

```
HUFFMAN(C):
 n = |C|
 Q = C (min-heap based on frequency)
 for i = 1 to n-1:
 z = NEW NODE()
 z.left = x = EXTRACT-MIN(Q)
 z.right = y = EXTRACT-MIN(Q)
 z.freq = x.freq + y.freq
 INSERT(Q, z)
 return EXTRACT-MIN(Q) // Returns root of Huffman tree
```

**Algorithm Explanation:**

1. Create a priority queue containing all characters with their frequencies as keys
2. While more than one node remains in the queue:

- Extract the two nodes with minimum frequencies
- Create a new internal node with these two as children
- Set the new node's frequency as the sum of children's frequencies
- Insert the new node back into the queue

3. The remaining node is the root of the Huffman tree

### Optimality Proof

**Theorem (Optimality of Huffman Coding):** The Huffman algorithm produces an optimal prefix code.

**Proof using Exchange Argument:**

We prove that the greedy choice property holds: there exists an optimal code where the two least frequent characters are siblings (have the same parent in the tree).

_Lemma 1 (Greedy Choice Property):_ Let C be an alphabet with frequencies. Let x and y be the two characters with minimum frequency. There exists an optimal prefix code where x and y have the same parent and are assigned the longest codewords (differing only in the last bit).

_Proof of Lemma 1:_ Consider an optimal code tree T. Let a and b be the two deepest leaves (maximum depth). If x and y are already siblings, we are done. Otherwise, let x be at depth d_x and some character c with higher frequency than x be at a shallower depth. Similarly for y. By swapping subtrees, we can transform T without increasing cost:

- Since freq(x) ≤ freq(c), swapping reduces or maintains total cost
- Since freq(y) ≤ freq(d) (where d is the other deep leaf), the same holds
  After possible swaps, x and y become siblings at the deepest level.

_Lemma 2 (Optimal Substructure):_ If we merge x and y into a single symbol z with frequency freq(x) + freq(y), then an optimal code for the reduced alphabet, when expanded, gives an optimal code for the original alphabet.

_Proof of Lemma 2:_ Any code tree for the reduced alphabet can be expanded by replacing z with internal node having children x and y. The total cost increases by freq(x) + freq(y) for the extra level, but this is unavoidable since x and y must be distinguished.

_Theorem Proof:_ By Lemma 1, there exists an optimal tree where x and y are siblings. By Lemma 2, solving the problem for the reduced alphabet (replacing x and y with z) gives the optimal solution for the full problem. The greedy algorithm makes exactly this choice, and by induction on |C|, produces an optimal code.

### Time Complexity Analysis

The Huffman algorithm runs in **O(n log n)** time where n is the number of unique characters:

- Building the initial min-heap: O(n)
- Each of (n-1) iterations:
- Two extract-min operations: O(log n) each
- One insert operation: O(log n)
- Total: O(n log n)

The space complexity is **O(n)** for storing the priority queue and tree nodes.

### Decoding Procedure

Decoding with a Huffman tree is straightforward:

1. Start at the root node
2. Read one bit at a time
3. If bit is 0, go to left child; if 1, go to right child
4. When a leaf is reached, output the character and return to root
5. Repeat until all bits are processed

**Example:** For the tree with codewords: A=0, B=10, C=11

- Encoded message: 011011
- Decoding: 0→A, 11→C, 10→B → Output: A C B

## Examples

### Example 1: Constructing Huffman Tree

**Problem:** Given characters A, B, C, D, E with frequencies 45, 13, 12, 16, 9, construct the Huffman tree and find codewords.

**Solution:**

_Step 1: Initial Priority Queue_
| Character | Frequency |
|-----------|-----------|
| E | 9 |
| C | 12 |
| B | 13 |
| D | 16 |
| A | 45 |

_Step 2: First Iteration_

- Extract: E(9), C(12) → Merge → Node1: freq = 21
- Insert Node1: Queue now contains {B(13), D(16), Node1(21), A(45)}

_Step 3: Second Iteration_

- Extract: B(13), D(16) → Merge → Node2: freq = 29
- Insert Node2: Queue now contains {Node1(21), Node2(29), A(45)}

_Step 4: Third Iteration_

- Extract: Node1(21), Node2(29) → Merge → Node3: freq = 50
- Insert Node3: Queue now contains {A(45), Node3(50)}

_Step 5: Final Iteration_

- Extract: A(45), Node3(50) → Merge → Root: freq = 95

_Codeword Assignment (left=0, right=1):_

- A: 0
- B: 100
- C: 101
- D: 110
- E: 111

_Verification:_

- Total cost = 45×1 + 13×3 + 12×3 + 16×3 + 9×3 = 45 + 39 + 36 + 48 + 27 = 195
- Average code length = 195/95 ≈ 2.05 bits/symbol
- Fixed-length would require log₂(5) ≈ 2.32 bits/symbol

### Example 2: Computing Compression Ratio

**Problem:** A file contains 100,000 characters from alphabet {A,B,C,D} with frequencies: A=45000, B=13000, C=12000, D=20000. Calculate the compression ratio using Huffman coding versus 8-bit ASCII.

**Solution:**

_Step 1: Build Huffman tree (iterations)_

1. Extract: C(12000), B(13000) → Merge → N1(25000)
2. Extract: D(20000), N1(25000) → Merge → N2(45000)
3. Extract: A(45000), N2(45000) → Root(90000)

_Step 2: Codewords:_

- A: 0
- B: 110
- C: 111
- D: 10

_Step 3: Calculate encoded bits_

- A: 45000 × 1 = 45,000 bits
- B: 13000 × 3 = 39,000 bits
- C: 12000 × 3 = 36,000 bits
- D: 20000 × 2 = 40,000 bits
- Total: 160,000 bits

_Step 4: Compare with ASCII_

- ASCII: 100,000 × 8 = 800,000 bits
- Compression ratio = 160,000 / 800,000 = 0.20 (20%)
- Space savings = 80%

### Example 3: Decoding Huffman-Encoded Message

**Problem:** Given the Huffman tree from Example 1 with codewords A=0, B=100, C=101, D=110, E=111, decode the message: 10011011101110

**Solution:**

Reading bit by bit from left to right:

1. 1 → Right to B? No, need more bits
2. 10 → Right, Right to D? No, continue
3. 100 → Right, Right, Left → B (output B, return to root)
4. 11 → Continue: Right, Right → C (output C)
5. 0 → Left → A (output A)
6. 111 → Right, Right, Right → E (output E)
7. 0 → Left → A (output A)
8. 1110 → After A: Right, Right, Right reaches E (wait - need to reset)

- Actually: After outputting A at step 5, we reset to root
- Remaining: 11011101110
- 110 → Right, Left, Left → D (output D)
- Continue: 11101110
- 111 → E (output E)
- 0 → A (output A)

Final decoded message: **B C A E D E A**

## Exam Tips

1. **Remember the greedy choice**: The two least frequent symbols are always combined first—this is the key step in Huffman coding.

2. **Codeword assignment rule**: After tree construction, assign '0' to left edges and '1' to right edges; codeword is the path from root to leaf.

3. **Proof understanding**: Be able to explain the exchange argument for optimality—swapping deeper high-frequency symbols with shallower low-frequency symbols doesn't increase cost.

4. **Time complexity**: Always O(n log n) due to priority queue operations; space is O(n).

5. **Prefix property**: No codeword is a prefix of another; this ensures unique decodability without separators.

6. **Decoding practice**: Practice tracing through the tree bit-by-bit, resetting to root after each leaf is reached.

7. **Average code length**: Calculated as Σ(frequency_i × depth_i) / Σ(frequency_i); compare with log₂(n) for fixed-length codes.
