# Input Enhancement in String Matching

**Subject:** Analysis & Design of Algorithms
**Module:** Module 3

## 1. Introduction

In the string matching problem, we aim to find all occurrences of a pattern `P[0..m-1]` within a larger text `T[0..n-1]`. A naive brute-force approach would check for the pattern starting at every possible position in the text, leading to a worst-case time complexity of **O(n*m)**. Input enhancement is a powerful technique used to improve the efficiency of algorithms by **preprocessing** the input—either the pattern or the text—to gather valuable information. This precomputed data is then used to skip unnecessary comparisons during the actual search phase, significantly speeding up the process. This note explores two fundamental input enhancement techniques: the use of the **Horspool's Algorithm** and the **Boyer-Moore Algorithm**.

## 2. Core Concepts

The core idea behind input enhancement for string matching is to preprocess the pattern to create a "shift table." This table tells us, upon a mismatch, how far we can safely shift the pattern to the right without missing any potential matches.

### 2.1. Horspool's Algorithm

Horspool's algorithm is a simplification of the Boyer-Moore algorithm. It preprocesses the pattern to create a **bad-symbol shift table**. The algorithm aligns the pattern with the text and compares characters from right to left.

*   **Preprocessing:** Create a shift table `ST[]` for all possible characters in the alphabet.
    *   For every character `c` in the alphabet, the shift value is calculated as:
        `shift(c) = { m, if c is not in the last m-1 characters of P; m - 1 - j, otherwise }`
    where `j` is the index of the *rightmost occurrence* of `c` in `P[0..m-2]`.

*   **Matching:** For each alignment of `P` against `T`:
    1.  Compare `P` with the current text window from right to left.
    2.  If all characters match, record the occurrence.
    3.  If a mismatch occurs at `T[i] = c`:
        *   The shift distance is determined by the table value for the character `c` in the text that was aligned with the *last character* of the pattern, i.e., `ST[T[i + m - 1]]`.
        *   Shift the pattern to the right by this value.

**Example:** Let `P = "BARBER"` (`m=6`).
Precomputed Shift Table (for last `m-1=5` characters):
*   `B` is at index 0 -> shift = 6-1-0 = **5**
*   `A` is at index 1 -> shift = 6-1-1 = **4**
*   `R` is at index 3 -> shift = 6-1-3 = **2**
*   `E` is at index 4 -> shift = 6-1-4 = **1**
*   All other chars (e.g., `Z`, `X`) -> shift = **6**

Searching in `T = "JIM_SAW_ME_IN_A_BARBERSHOP"`:
*   First alignment: `JIM_SAW_ME_IN_A_BARBERSHOP`
                      `BARBER` (mismatch at `S` vs `R`)
*   The last char in the current window is `S`. `ST['S'] = 6`. Shift by **6**.
*   Next alignment: `JIM_SAW_ME_IN_A_BARBERSHOP`
                            `BARBER` (mismatch at `space` vs `R`)
*   The last char is `R`. `ST['R'] = 2`. Shift by **2**.
*   This process continues, skipping large portions of the text.

### 2.2. Boyer-Moore Algorithm

The Boyer-Moore algorithm enhances Horspool's approach by using two heuristics instead of one: the **bad-symbol shift** (same as Horspool's) and the more powerful **good-suffix shift**.

*   **Bad-Symbol Shift:** Functions identically to Horspool's shift table. It's effective for large alphabets (e.g., natural language).

*   **Good-Suffix Shift:** This heuristic comes into play when a suffix of the pattern has matched the text, but then a mismatch occurs.
    *   Preprocessing: The algorithm precomputes a table that, for each possible suffix `k` of `P` that has matched, determines how far to shift the pattern to align with the next occurrence of that same suffix preceded by a *different* character.
    *   During matching, if a suffix of length `k` matches before a mismatch, the pattern is shifted according to the good-suffix rule. The algorithm then uses the **maximum shift** suggested by the bad-symbol and good-suffix heuristics to ensure efficiency.

The good-suffix rule allows for even larger shifts than the bad-symbol rule alone, especially when the pattern contains repeated substrings. While its preprocessing is more complex, the Boyer-Moore algorithm is often **sub-linear** in practice, meaning it doesn't need to check every character of the text.

## 3. Key Points & Summary

| Feature | Horspool's Algorithm | Boyer-Moore Algorithm |
| :--- | :--- | :--- |
| **Core Idea** | Input enhancement via preprocessing a bad-symbol shift table. | Enhances Horspool by adding a good-suffix shift heuristic. |
| **Preprocessing** | Simple. Creates a table based on the rightmost occurrence of each char in the pattern (excluding last). | More complex. Precomputes both a bad-symbol table and a good-suffix table. |
| **Matching** | Compares right-to-left. Shifts based on the text character aligned with the pattern's last character. | Compares right-to-left. Shifts by the maximum of the bad-symbol and good-suffix values. |
| **Efficiency** | Worst-case: **O(n*m)**<br>Average-case: **Θ(n)** | Worst-case: **O(n+m)** (with full Galil rule)<br>Often sub-linear in practice. |
| **Use Case** | Excellent and efficient practical algorithm for most applications. | The gold standard for efficient string matching, especially with large alphabets. |

*   **Input Enhancement** is the strategy of preprocessing the input to make the subsequent search phase faster.
*   Both algorithms use a **right-to-left** comparison strategy, which is key to enabling large shifts.
*   The shift tables allow the algorithms to **skip alignments** (portions of the text) that are guaranteed not to yield a match, drastically reducing the number of comparisons.
*   While Horspool is simpler and very effective, the Boyer-Moore algorithm can provide superior performance by leveraging the good-suffix rule for larger shifts.