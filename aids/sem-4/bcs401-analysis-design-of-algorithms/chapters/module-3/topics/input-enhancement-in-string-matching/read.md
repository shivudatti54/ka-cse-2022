# Input Enhancement in String Matching

**Subject:** Analysis & Design of Algorithms
**Module:** Module 3
**Topic:** Input Enhancement in String Matching

## 1. Introduction

String Matching is a fundamental problem in computer science: finding all occurrences of a pattern `P[0..m-1]` within a larger text `T[0..n-1]`. A naive approach checks for the pattern starting at every possible position in the text, leading to a worst-case time complexity of **O(m*n)**. Input Enhancement is a powerful pre-processing technique used to improve the efficiency of string matching algorithms. The core idea is to gather information during a pre-processing phase (of either the pattern or the text) and then use this information to speed up the subsequent search. This note focuses on two seminal algorithms that use this technique: the **Knuth-Morris-Pratt (KMP)** and the **Boyer-Moore (BM)** algorithms.

## 2. Core Concepts

### a) Knuth-Morris-Pratt (KMP) Algorithm

The KMP algorithm pre-processes the pattern `P` to create a **Prefix Function** (often called the `lps` array - longest prefix suffix). This function helps the algorithm avoid unnecessary comparisons by utilizing the information from previous matches.

*   **Prefix Function (`lps` array):** For a pattern `P`, `lps[i]` is defined as the length of the longest proper prefix of the substring `P[0..i]` that is also a proper suffix. A proper prefix/suffix cannot be the entire string itself.
*   **How it works:** The algorithm uses the `lps` array to decide how many characters to skip after a mismatch. Instead of always shifting the pattern by one position after a mismatch, KMP uses the pre-computed `lps` array to shift the pattern by `(j - lps[j-1])` positions, where `j` is the position of the mismatch in the pattern. This allows the algorithm to avoid re-checking known matching characters.

**Example:**
Pattern `P = "ABABC"`, its `lps` array is computed as `[0, 0, 1, 2, 0]`.
*   `lps[3] = 2` for substring "ABAB": The longest prefix that is also a suffix is "AB" (length=2).
*   During a search, if a mismatch occurs at the last character (`P[4] = 'C'`), the pattern can be shifted so that the prefix "AB" (which we know matches) aligns with the corresponding suffix in the text.

**Time Complexity:**
*   Pre-processing (building `lps`): **O(m)**
*   Searching: **O(n)**
*   **Total: O(m + n)**

### b) Boyer-Moore (BM) Algorithm

The Boyer-Moore algorithm is often more efficient in practice because it often allows shifts larger than the KMP algorithm. It pre-processes the pattern to create two different heuristics: the **Bad Character Shift** and the **Good Suffix Shift**.

*   **1. Bad Character Heuristic:** When a mismatch occurs between a character in the text `T[i]` and a pattern character `P[j]`, the heuristic shifts the pattern to align the last occurrence of the bad character `T[i]` in the pattern with this text position. If the character doesn't exist in the pattern, the pattern is shifted completely past this point.
    *   This requires precomputing a `badchar` table that stores the last occurrence index of every character in the pattern.

*   **2. Good Suffix Heuristic:** When a mismatch occurs, but a suffix of the pattern has already matched successfully with the text, this heuristic shifts the pattern to align the next occurrence of that matched suffix (or a prefix of it) within the pattern.
    *   This requires precomputing shift tables based on the pattern's suffixes.

The algorithm uses the **maximum shift** suggested by these two heuristics to achieve larger skips through the text.

**Example:**
Text `T = "THIS IS A SIMPLE TEST"`, Pattern `P = "TEST"`.
The algorithm starts comparing from the *end* of the pattern.
*   Compare `T[3] ('S')` with `P[3] ('T')`. Mismatch.
*   The bad character is `'S'` in the text. The last occurrence of `'S'` in the pattern is at index `2`.
*   The shift is calculated as `max(1, 3 - 2) = 1`. The pattern shifts right by 1 position.
*   This process continues, often leading to very large skips.

**Time Complexity:**
*   Pre-processing: **O(m + |Σ|)** (where Σ is the alphabet size)
*   Searching: **O(m*n)** in the worst-case, but often **sub-linear** (better than O(n)) in practice.

## 3. Key Points & Summary

| Feature | Knuth-Morris-Pratt (KMP) | Boyer-Moore (BM) |
| :--- | :--- | :--- |
| **Pre-processing** | Pattern (`lps` array) | Pattern (`badchar` table & good suffix tables) |
| **Comparison Order** | Left-to-right | Right-to-left |
| **Key Heuristic** | Longest Prefix-Suffix | Bad Character & Good Suffix |
| **Worst-case Time** | **O(n + m)** | **O(n*m)** (but often much better) |
| **Best Use Case** | Small alphabet, worst-case guarantees needed | Large alphabet, practical speed is critical |

**Summary:**
*   **Input Enhancement** involves pre-processing the input (pattern) to store information that makes the subsequent search phase more efficient.
*   **KMP** ensures that the text pointer `i` never moves backwards, achieving optimal linear worst-case time. Its strength is its predictable performance.
*   **Boyer-Moore** uses the clever strategy of comparing from the end of the pattern and can often skip large portions of the text, making it extremely efficient for natural language texts.
*   The choice between them depends on the application: use KMP for reliable worst-case performance (e.g., in embedded systems) and Boyer-Moore for raw speed in typical applications (e.g., text editors, search engines).