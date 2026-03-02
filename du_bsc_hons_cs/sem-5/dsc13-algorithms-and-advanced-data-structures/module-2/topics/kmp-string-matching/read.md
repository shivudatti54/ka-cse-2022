# KMP String Matching Algorithm

## Introduction

The Knuth-Morris-Pratt (KMP) algorithm is one of the most elegant and efficient string matching algorithms in computer science, designed to find a pattern within a text string in O(n + m) time complexity, where n is the length of the text and m is the length of the pattern. This algorithm was independently discovered by Donald Knuth, James Morris, and Vaughan Pratt in 1977, making it a landmark achievement in the field of algorithm design.

Before KMP, traditional string matching algorithms like the brute-force approach required O(n × m) time in the worst case, which becomes prohibitively slow for large texts and patterns. The KMP algorithm revolutionized this by introducing the revolutionary concept of preprocessing the pattern to create a failure function (also called the longest proper prefix which is also a suffix array), which allows the algorithm to skip characters during matching rather than backtracking.

In the context of the University of Delhi's Computer Science curriculum, understanding KMP is crucial because it demonstrates fundamental algorithmic design techniques like preprocessing, dynamic programming thinking, and space-time tradeoffs. Moreover, KMP finds practical applications in text editors, search engines, DNA sequence matching, plagiarism detection, and network intrusion detection systems.

## Key Concepts

### 1. Brute Force String Matching (Review)

Before understanding KMP, let us briefly review the brute-force approach. In this method, we align the pattern with the text at position 0 and compare character by character. On a mismatch, we shift the pattern by one position to the right and start again from the first character of the pattern. The worst-case time complexity is O(n × m), which occurs in scenarios like searching for pattern "AAA" in text "AAAAAAA...A".

### 2. The Core Idea Behind KMP

The fundamental insight of KMP is that when a mismatch occurs, we already know some characters of the text (the ones we just compared). Instead of discarding all this information and starting from scratch, we can use this knowledge to skip some characters intelligently. The key is to preprocess the pattern to determine how far we can shift the pattern when a mismatch occurs.

### 3. The Failure Function (π array)

The failure function, also known as the prefix function or LPS (Longest Proper Prefix which is also a Suffix) array, is the heart of the KMP algorithm. For each position i in the pattern (0-indexed), π[i] stores the length of the longest proper prefix of pattern[0...i] that is also a suffix of this substring.

A **proper prefix** is a prefix that is not equal to the entire string itself. For example, for the string "ABAB":
- Prefix "A", "AB", "ABA" are proper prefixes
- "ABAB" is not a proper prefix
- Suffixes: "B", "AB", "BAB", "ABAB"

For pattern "ABABC", the failure function would be:
- i=0: π[0] = 0 (single character has no proper prefix)
- i=1: π[1] = 0 ("AB" - no prefix which is also suffix)
- i=2: π[2] = 1 ("ABA" - "A" is both prefix and suffix)
- i=3: π[3] = 2 ("ABAB" - "AB" is both prefix and suffix)
- i=4: π[4] = 0 ("ABABC" - no prefix which is also suffix)

### 4. Computing the Failure Function

The failure function is computed using a dynamic approach:
1. Initialize π[0] = 0
2. For each position i from 1 to m-1:
   - If pattern[i] == pattern[j] (where j = π[i-1]), then π[i] = j + 1
   - Otherwise, if j > 0, set j = π[j-1] and repeat
   - If j becomes 0 and still no match, π[i] = 0

### 5. KMP Search Algorithm

Once we have the failure function, the search phase works as follows:
1. Compare pattern[j] with text[i]
2. If they match, increment both i and j
3. If j reaches m (pattern length), we found a match at position i - j
4. If they don't match:
   - If j > 0, set j = π[j-1] and continue comparing
   - If j == 0, increment i and continue

## Examples

### Example 1: Basic KMP Search

**Problem:** Find all occurrences of pattern "ABA" in text "ABABABC".

**Step 1: Compute failure function for "ABA"**
- Pattern: A B A (indices 0, 1, 2)
- π[0] = 0
- π[1]: compare pattern[1]='B' with pattern[0]='A', no match → π[1] = 0
- π[2]: compare pattern[2]='A' with pattern[0]='A', match → π[2] = 1

So, π = [0, 0, 1]

**Step 2: Search in text**
```
Text:    A B A B A B C
Pattern: A B A
         ↓ mismatch at i=3, j=2
         j = π[2-1] = π[1] = 0
         
Text:    A B A B A B C
Pattern:   A B A
         ↓ mismatch at i=1, j=0
         i++, continue
         
Text:    A B A B A B C
Pattern:     A B A
         ↓ match all, found at position 3
```

**Result:** Pattern found at index 3 (0-indexed)

### Example 2: Overlapping Patterns

**Problem:** Find pattern "AA" in text "AAAA"

**Failure function for "AA":**
- π[0] = 0
- π[1]: pattern[1]='A' == pattern[0]='A', so π[1] = 1

π = [0, 1]

**Search:**
```
i=0, j=0: text[0]='A' == pattern[0]='A' → i=1, j=1
i=1, j=1: text[1]='A' == pattern[1]='A' → i=2, j=2
j==2 (m): Found match at i-j=0, output 0
         j = π[1] = 1 (for overlapping match)

i=2, j=1: text[2]='A' == pattern[1]='A' → i=3, j=2
j==2: Found match at i-j=1, output 1
      j = π[1] = 1

i=3, j=1: text[3]='A' == pattern[1]='A' → i=4, j=2
j==2: Found match at i-j=2, output 2
      j = π[1] = 1

i=4 (end)
```

**Result:** Pattern "AA" found at positions 0, 1, 2 in text "AAAA"

### Example 3: No Match Found

**Problem:** Find pattern "XYZ" in text "ABCDEFG"

**Failure function for "XYZ":** π = [0, 0, 0] (all characters different)

**Search:** Each character mismatch leads to j=0, and we simply advance i. No match is ever found.

**Result:** No occurrence of pattern in text

## Exam Tips

1. **Understand the intuition**: In exams, you may be asked to explain why KMP is better than brute force. Focus on the concept of using previously matched information to avoid redundant comparisons.

2. **Remember the time complexity**: Always state both preprocessing (O(m)) and search (O(n)) phases, giving total O(n + m).

4. **Practice failure function computation**: This is the most common exam question. Given a pattern, compute its π array. Remember that π[0] is always 0.

5. **Hand-trace KMP**: Be able to trace through an example step-by-step, showing how i and j pointers move and when the failure function is used.

6. **Space complexity**: The algorithm requires O(m) extra space for the failure function array.

7. **Key distinction**: Remember that the failure function stores the longest proper prefix that is also a suffix - proper prefix excludes the entire string itself.

8. **Edge cases**: Know how KMP handles edge cases like pattern of length 1, all same characters, and no match scenarios.