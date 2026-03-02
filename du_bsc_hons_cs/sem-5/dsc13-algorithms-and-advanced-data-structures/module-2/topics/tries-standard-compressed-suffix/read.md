# Tries: Standard and Compressed Suffix Tries

## Introduction

Tries, also known as prefix trees, are fundamental tree-based data structures specifically designed for efficient string operations. Unlike traditional binary search trees that store keys at nodes, tries store characters along the paths from the root to the leaf nodes, making them exceptionally powerful for applications involving prefix matching, auto-completion, and IP routing. The name "trie" originates from the word "retrieval," highlighting its primary purpose of efficient data retrieval.

In the context of the University of Delhi's Computer Science curriculum, understanding tries is crucial because they represent a fundamental departure from conventional tree structures. While BSTs, AVL trees, and B-trees organize data based on total ordering, tries organize data based on the lexicographic ordering of string prefixes. This makes tries the data structure of choice for problems involving dictionary lookups, text prediction, and most importantly, string algorithms in computational biology.

This module explores two critical variants of tries: the standard trie and the compressed suffix trie. The standard trie forms the foundation by storing all characters explicitly, while the compressed suffix trie optimizes space usage through path compression. These structures play a vital role in suffix tree construction, pattern matching algorithms, and various bioinformatics applications where efficient string processing is paramount.

## Key Concepts

### Standard Trie Structure

A standard trie is an ordered tree data structure where each node represents a single character, and the complete path from the root to any node represents a prefix of one or more strings stored in the trie. The root node corresponds to an empty string, and each node may have multiple children, one for each possible next character.

**Formal Definition:** A trie T for an alphabet Σ is a rooted tree where:
- Each node represents a prefix of some string in the set
- Each edge is labeled with a character from Σ
- The path from root to any node spells out the prefix represented by that node
- A special marker (often a $ symbol) indicates the end of a complete string

**Node Structure:** Each node in a standard trie contains:
- An array or hash map of children (typically 26 for lowercase English letters, or dynamic for variable alphabets)
- A boolean flag indicating whether this node marks the end of a word
- Optionally, a count of how many words pass through this node (useful for prefix counting)

The time complexity for insertion, search, and deletion in a standard trie is O(m) where m is the length of the string being operated upon, independent of the total number of strings stored. This makes tries extraordinarily efficient for string operations compared to balanced search trees.

### Suffix Trie

A suffix trie is a specialized variant that contains all suffixes of a given string. For a string S of length n, the suffix trie contains all n(n+1)/2 suffixes. The suffix trie is essentially a trie of all suffixes of the original string.

**Construction:** To build a suffix trie for string S = "banana", we insert all suffixes: "banana", "anana", "nana", "ana", "na", "a" into a standard trie structure.

The suffix trie provides O(m) pattern matching where m is the pattern length, making it powerful for substring searches. However, it requires O(n²) space in the worst case, which led to the development of more space-efficient structures like suffix trees and compressed tries.

### Compressed Trie (Radix Trie)

A compressed trie addresses the space inefficiency of standard tries by compressing paths that contain only single-child nodes into single edges with concatenated labels. This compression technique is also known as radix trie or Patricia trie.

**Path Compression:** If a sequence of nodes each has exactly one child, these nodes can be merged into a single node with an edge label containing the concatenated characters. For example, the path root → 's' → 't' → 'u' → 'd' → 'e' → 'n' 't' can be compressed to a single edge from root labeled "student".

**Compression Rules:**
- A node is compressed if it has exactly one child and is not an end-of-word marker
- The edge label becomes a string instead of a single character
- Decompression occurs during traversal by matching edge labels character by character

The compressed trie maintains the same O(m) query time while significantly reducing space requirements. In practice, compressed tries can reduce space by a factor of 2-10x for typical datasets.

### Suffix Array and LCP Array

While not tries directly, suffix arrays and LCP (Longest Common Prefix) arrays are closely related structures often studied alongside tries. A suffix array is a sorted array of all suffixes of a string, and the LCP array stores the lengths of the longest common prefixes between consecutive suffixes in the sorted order.

These structures, combined with the RMQ (Range Minimum Query) data structure, can answer substring queries in O(m + log n) time, making them competitive alternatives to suffix trees and tries in many applications.

## Examples

### Example 1: Building a Standard Trie

**Problem:** Insert the words "cat", "car", "card", "care", "career" into a standard trie and show the resulting structure.

**Solution:**

Step 1: Insert "cat"
- Create root → 'c' → 'a' → 't' (mark end of word)

Step 2: Insert "car"
- From root, follow 'c' → 'a' (already exists)
- Create new edge from 'a' to 'r' (mark end of word)
- Result: root → 'c' → 'a' → 't' and 'r'

Step 3: Insert "card"
- From 'r', create edge 'd' (mark end of word)
- Structure now has: root → 'c' → 'a' → 'r' → 'd'

Step 4: Insert "care"
- From 'r', create edge 'e' (mark end of word)
- Structure now has branch at 'r': 'd' and 'e'

Step 5: Insert "career"
- From 'e', create edges 'r' (not marked) → (end marker at 'r')
- Final structure shows shared prefixes "c", "ca", "car", "care"

**Visual Representation:**
```
root
 └── c
      └── a
           └── t (end)
           └── r
                ├── d (end)
                └── e
                     └── r (end)
```

**Key Observation:** The trie efficiently stores 5 words using only 9 nodes (compared to 5 × 3.4 = 17 characters if stored separately), demonstrating significant prefix sharing.

### Example 2: Pattern Matching with Standard Trie

**Problem:** Given a trie containing words "apple", "application", "apply", "apt", "bat", "batch", find if the pattern "appl" exists and count words with prefix "bat".

**Solution:**

**Part A: Finding "appl"**
- Start at root
- Follow edge 'a' → node for "a"
- Follow edge 'p' → node for "ap"
- Follow edge 'p' → node for "app"
- Follow edge 'l' → node for "appl"
- Node exists! Pattern "appl" is found as a prefix.

**Part B: Counting words with prefix "bat"**
- Follow path: root → 'b' → 'a' → 't'
- At node for "bat", check: Is this marked as end of word? (Assuming "bat" is a word, yes)
- Count = 1 (for "bat" itself)
- Explore all descendants: found "batch"
- Total count = 2 words with prefix "bat"

**Time Complexity:** O(length of pattern) = O(4) for part A, O(length of prefix + number of matching words) for part B.

### Example 3: Compressed Trie Construction

**Problem:** Convert the following standard trie path into a compressed trie:
- Path: root → 's' → 't' → 'u' → 'd' → 'e' → 'n' → 't' (representing "student")

**Solution:**

**Standard Trie:** 7 nodes with single-character edges
```
root -s- node1 -t- node2 -u- node3 -d- node4 -e- node5 -n- node6 -t- node7
```

**Compression Process:**
- All nodes from node1 to node6 have exactly one child
- Node7 is the end-of-word marker
- Compress nodes 1-6 into a single edge

**Compressed Trie:**
```
root --"student"--> node7(end)
```

**Space Comparison:**
- Standard: 7 nodes + 7 edges = 14 components
- Compressed: 1 node + 1 edge label = 2 components + storage for string "student"
- Net savings: 5 nodes eliminated

**Important Note:** If "study" also exists in the trie, the compression would only apply up to the branching point:
- root → 's' → 't' → 'u' (shared)
- From 'u': "d" → "dent" and "y" → "dy"

## Exam Tips

1. **Understand the fundamental difference:** Remember that tries organize strings by prefixes (lexicographic order) while BSTs organize by total key ordering. This distinction is frequently tested in conceptual questions.

2. **Time and space complexity:** Master the complexities: Standard trie operations are O(m) where m is string length. Space is O(Σ × m × n) in worst case, but compressed tries reduce this significantly.

3. **Suffix vs. Prefix:** Don't confuse suffix tries with standard tries. A suffix trie contains all suffixes of a single string, while a standard trie can contain multiple unrelated strings.

4. **Compression criterion:** For the exam, remember that path compression in compressed tries only occurs when a node has exactly one child and is not marked as end-of-word.

5. **Real-world applications:** Be prepared to explain applications like autocomplete systems, IP routing (tries used in longest prefix matching), and bioinformatics (DNA sequence matching).

6. **Memory representation:** Know how to represent tries using arrays (for small alphabets) vs. linked structures (for large alphabets). This affects both space complexity and implementation choices.

7. **Comparison with other structures:** Understand when to use tries vs. hash tables (tries provide ordered iteration and prefix search) vs. suffix arrays (for pattern matching in large texts).

8. **Edge cases:** Handle empty strings, single characters, and strings that are prefixes of other strings carefully in your implementations and conceptual answers.