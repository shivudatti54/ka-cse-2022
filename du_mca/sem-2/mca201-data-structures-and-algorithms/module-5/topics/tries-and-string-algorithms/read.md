# Tries and String Algorithms

## Introduction
Tries (pronounced "trys") and string algorithms form the backbone of modern text processing systems. A trie is a tree-like data structure that stores dynamic sets with string keys, enabling efficient prefix-based searches. Combined with advanced string algorithms like Knuth-Morris-Pratt (KMP) and Rabin-Karp, these techniques power critical applications ranging from search engine autocomplete to DNA sequence analysis.

The importance of tries lies in their O(L) time complexity for insertion, search, and deletion operations where L is the string length. When combined with suffix trees/arrays and pattern matching algorithms, they enable efficient solutions for complex problems like longest common substring, plagiarism detection, and genome sequencing. Modern applications include Google's search suggestions, antivirus signature detection, and bioinformatics databases.

## Key Concepts
1. **Trie Structure**: 
   - Nodes represent characters (not stored explicitly)
   - Path from root to leaf spells a string
   - End-of-word markers for valid words
   - Space complexity: O(N*L) where N=number of strings, L=avg length

2. **Compressed Tries**:
   - Radix Tree (Patricia Trie): Merge single-child nodes
   - Suffix Tree: Contains all suffixes of a text with O(n) construction (Ukkonen's algorithm)

3. **String Matching Algorithms**:
   - **KMP Algorithm**: Uses prefix function to avoid backtracking (O(n+m))
   - **Rabin-Karp**: Rolling hash function for pattern matching (avg O(n+m))
   - **Boyer-Moore**: Bad character heuristic for practical efficiency

4. **Suffix Arrays**:
   - Lexicographically sorted array of all suffixes
   - Can replicate suffix tree functionality with O(n log n) construction

## Examples

**Example 1: Trie Insertion**
Insert "apple", "app", and "apply" into a trie:

1. Root → 'a' → 'p' → 'p'
2. Create 'l' branch from second 'p'
3. 'l' → 'e' (mark end for "apple")
4. 'l' → 'y' (mark end for "apply")
5. Existing 'p' node marked as end for "app"

**Example 2: KMP Prefix Function**
Pattern = "ABABC":
1. Compute prefix array [0,0,1,2,0]
2. When mismatch occurs at index 4, shift by (4 - prefix[3]) = 2 positions

**Example 3: Rabin-Karp Hashing**
Text = "314159265", pattern "4159" (mod 13):
1. Hash("4159") = (4*1000 + 1*100 + 5*10 + 9) mod 13 = 8
2. Rolling hash of first 4 digits "3141" = 7
3. Next window "1415": (7 - 3*1000) *10 +5 mod13 = 8 → match found

## Exam Tips
1. Always draw trie structures with clear end-of-word markers
2. For compressed tries, show node merging with combined edge labels
3. KMP: Memorize prefix function calculation steps
4. Rabin-Karp: Demonstrate hash recalculation formula
5. Compare suffix trees vs arrays in time/space tradeoffs
6. Practice constructing suffix arrays using DC3 algorithm
7. Remember real-world applications: search engines (tries), virus scanning (Aho-Corasick), DNA sequencing (suffix trees)