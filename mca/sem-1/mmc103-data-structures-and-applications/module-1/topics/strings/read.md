# Strings


## Table of Contents

- [Strings](#strings)
- [1. Introduction](#1-introduction)
- [2. Formal Definition of String ADT](#2-formal-definition-of-string-adt)
  - [2.1 String ADT Operations](#21-string-adt-operations)
- [3. String Representations](#3-string-representations)
  - [3.1 Fixed-Length Array (Sequential Representation)](#31-fixed-length-array-sequential-representation)
  - [3.2 Dynamic Array Representation (Heap-Based)](#32-dynamic-array-representation-heap-based)
  - [3.3 Linked List Representation](#33-linked-list-representation)
  - [3.4 Representation Comparison](#34-representation-comparison)
- [4. Fundamental String Algorithms](#4-fundamental-string-algorithms)
  - [4.1 Naive Pattern Matching](#41-naive-pattern-matching)
  - [4.2 KMP (Knuth-Morris-Pratt) Algorithm](#42-kmp-knuth-morris-pratt-algorithm)
  - [4.3 Rabin-Karp Algorithm](#43-rabin-karp-algorithm)
- [5. String Operations — Implementation Details](#5-string-operations--implementation-details)
  - [5.1 String Length](#51-string-length)
  - [5.2 String Copy](#52-string-copy)
  - [5.3 String Comparison](#53-string-comparison)
  - [5.4 String Concatenation](#54-string-concatenation)
- [6. Multiple Choice Questions](#6-multiple-choice-questions)

## 1. Introduction

A string is a **finite sequence of characters** drawn from a character set (alphabet). In computer science, strings are treated not merely as primitive data types but as a formal **Abstract Data Type (ADT)** with well-defined operations, multiple memory representations, and algorithms whose time and space complexities can be precisely analyzed.

## 2. Formal Definition of String ADT

A string `S` is formally defined as a sequence:

```
S = s₀s₁s₂...sₙ₋₁
```

where each `sᵢ` is a character from the alphabet Σ, and `n` is the **length** of the string, denoted |S| = n. The string of length zero is called the **null string** or **empty string**, denoted by ε or "".

### 2.1 String ADT Operations

The String ADT provides the following primitive operations:

| Operation            | Description                                                 | Complexity     |
| -------------------- | ----------------------------------------------------------- | -------------- |
| `StrLen(S)`          | Returns the number of characters in S                       | O(1) or O(n)\* |
| `StrConcat(S, T)`    | Returns a new string by appending T after S                 | O(n + m)       |
| `SubStr(S, i, j)`    | Returns substring of S starting at position i with length j | O(j)           |
| `StrCompare(S, T)`   | Compares S and T lexicographically                          | O(min(n, m))   |
| `StrInsert(S, i, T)` | Inserts string T into S at position i                       | O(n + m)       |
| `StrDelete(S, i, j)` | Deletes j characters from S starting at position i          | O(n - i - j)   |
| `StrIndex(S, T)`     | Returns position of first occurrence of T in S, or -1       | O(nm) naive    |

\*O(1) if length is stored, O(n) if computed by traversal

**Theorem 1:** For any two strings S and T, if |S| = n and |T| = m, the time complexity of `StrConcat(S, T)` is Θ(n + m).

_Proof:_ To concatenate S and T, we must copy all n characters of S to the result buffer, then copy all m characters of T. Each character is copied exactly once, so the total operations are proportional to n + m. ∎

## 3. String Representations

### 3.1 Fixed-Length Array (Sequential Representation)

This is the traditional C-style representation where a string is stored in a character array terminated by a null character `'\0'`.

```c
#define MAX_LEN 100
typedef struct {
    char ch[MAX_LEN];
    int length;
} String;
```

**Memory Layout:**

```
String "HELLO":
Index:   0   1   2   3   4   5
Char:   ['H']['E']['L']['L']['O']['\0']
```

**Complexity Analysis:**

| Operation         | Time Complexity        | Space Complexity |
| ----------------- | ---------------------- | ---------------- |
| Access s[i]       | O(1)                   | -                |
| StrLen (stored)   | O(1)                   | O(1) extra       |
| StrLen (computed) | O(n)                   | O(1) extra       |
| StrConcat         | O(n + m), may overflow | O(n + m)         |
| StrInsert         | O(n)                   | O(1) extra       |
| StrDelete         | O(n)                   | O(1) extra       |

**Theorem 2:** In a fixed-length array representation, insertion at position i requires shifting n - i characters.

_Proof:_ When inserting at position i, all characters from position i to n-1 must be moved one position to the right to create a gap. This involves exactly (n - i) character moves. Each move is a constant-time operation, so total time is Θ(n - i). ∎

### 3.2 Dynamic Array Representation (Heap-Based)

Strings grow and shrink using dynamic memory allocation via `malloc` and `realloc`.

```c
typedef struct {
    char *ch;      // dynamically allocated array
    int length;    // current string length
    int capacity;  // allocated memory size
} DynString;

DynString *createString(const char *init) {
    DynString *s = (DynString *)malloc(sizeof(DynString));
    s->length = strlen(init);
    s->capacity = s->length + 1;
    s->ch = (char *)malloc(s->capacity * sizeof(char));
    strcpy(s->ch, init);
    return s;
}
```

**Complexity Analysis:**

| Operation   | Time Complexity    | Notes                   |
| ----------- | ------------------ | ----------------------- |
| Access s[i] | O(1)               | Direct indexing         |
| StrConcat   | O(n + m) amortized | May require realloc     |
| StrInsert   | O(n) amortized     | May require resizing    |
| StrDelete   | O(n) amortized     | May require shrinking   |
| Space       | O(n)               | Proportional to content |

**Theorem 3 (Amortized Analysis):** For a dynamic array that doubles in capacity when full, the amortized cost of inserting n characters is O(1) per insertion.

_Proof:_ When the array is full, we allocate a new array of size 2k and copy k elements. This costs 2k operations. Over the sequence of k insertions that caused the overflow, we amortize the copy cost: 2k/k = 2 operations per insertion. Thus, amortized cost is O(1). ∎

### 3.3 Linked List Representation

Each node stores one character (or a block of characters) and a pointer to the next node.

```c
typedef struct StrNode {
    char ch;
    struct StrNode *next;
} StrNode;
```

**Block-Based Linked List (Space-Efficient):**

```c
#define BLOCK_SIZE 4
typedef struct StrBlock {
    char ch[BLOCK_SIZE];
    int count;
    struct StrBlock *next;
} StrBlock;
```

**Complexity Analysis:**

| Operation   | Time Complexity | Notes                                 |
| ----------- | --------------- | ------------------------------------- |
| Access s[i] | O(n)            | Must traverse from head               |
| StrConcat   | O(1)            | Link last node to T's head            |
| StrInsert   | O(n) + O(1)     | O(n) to find position, O(1) to insert |
| StrDelete   | O(n) + O(1)     | O(n) to find position, O(1) to delete |
| Space       | O(n + k)        | n chars + k pointers overhead         |

### 3.4 Representation Comparison

| Criterion            | Fixed Array      | Dynamic Array    | Linked List             |
| -------------------- | ---------------- | ---------------- | ----------------------- |
| Random access        | O(1)             | O(1)             | O(n)                    |
| Insert at position i | O(n)             | O(n)             | O(n) + O(1)             |
| Delete at position i | O(n)             | O(n)             | O(n) + O(1)             |
| Concatenation        | O(n+m), may fail | O(n+m) amortized | O(1)                    |
| Space efficiency     | Wastes space     | Optimal          | Poor (pointer overhead) |
| Cache friendliness   | Excellent        | Good             | Poor                    |
| Implementation       | Simple           | Moderate         | Complex                 |

## 4. Fundamental String Algorithms

### 4.1 Naive Pattern Matching

Given a text T of length n and pattern P of length m, find all occurrences of P in T.

```c
int naiveMatch(char *text, char *pattern) {
    int n = strlen(text);
    int m = strlen(pattern);
    int count = 0;

    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && pattern[j] == text[i + j]) {
            j++;
        }
        if (j == m) {
            count++;  // Match found at position i
        }
    }
    return count;
}
```

**Time Complexity:**

- **Worst Case:** O(nm) — occurs when pattern like "AAA...A" in text "AAA...AA"
- **Best Case:** O(n) — occurs when first character of pattern doesn't match any character in text
- **Average Case:** O(n + m)

### 4.2 KMP (Knuth-Morris-Pratt) Algorithm

The KMP algorithm achieves O(n + m) time complexity by preprocessing the pattern to compute the **Longest Proper Prefix which is also a Suffix (LPS)** array.

**LPS Array Computation:**

```c
void computeLPS(char *pattern, int *lps, int m) {
    lps[0] = 0;
    int length = 0;
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}
```

**KMP Search:**

```c
int kmpSearch(char *text, char *pattern) {
    int n = strlen(text);
    int m = strlen(pattern);
    int lps[m];
    computeLPS(pattern, lps, m);

    int i = 0, j = 0, count = 0;
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }
        if (j == m) {
            count++;
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return count;
}
```

**Theorem 4:** The KMP algorithm has a time complexity of O(n + m).

_Proof:_ The LPS computation loop runs in O(m) since i always increments and length never exceeds i. In the search phase, we maintain the invariant that in each iteration, either i increments (making progress) or j decreases via lps (reducing the need to re-examine characters). Since i can increment at most n times and j can decrease at most m times total, the total operations are O(n + m). ∎

**Space Complexity:** O(m) for the LPS array.

### 4.3 Rabin-Karp Algorithm

Uses hashing to find pattern matches in O(n + m) average time.

```c
#define d 256  // number of characters in alphabet
#define q 101  // a prime number for modulo

int rabinKarp(char *text, char *pattern) {
    int n = strlen(text);
    int m = strlen(pattern);
    int h = 1;
    int p = 0;  // hash value for pattern
    int t = 0;  // hash value for text window
    int count = 0;

    // Calculate h = d^(m-1) % q
    for (int i = 0; i < m - 1; i++) {
        h = (h * d) % q;
    }

    // Calculate initial hash values
    for (int i = 0; i < m; i++) {
        p = (d * p + pattern[i]) % q;
        t = (d * t + text[i]) % q;
    }

    // Slide pattern over text
    for (int i = 0; i <= n - m; i++) {
        if (p == t) {
            // Verify (to handle hash collisions)
            int j = 0;
            while (j < m && pattern[j] == text[i + j]) {
                j++;
            }
            if (j == m) count++;
        }

        // Calculate hash for next window
        if (i < n - m) {
            t = (d * (t - text[i] * h) + text[i + m]) % q;
            if (t < 0) t += q;
        }
    }
    return count;
}
```

**Complexity:**

- **Time:** O(n + m) average, O(nm) worst case
- **Space:** O(1)

## 5. String Operations — Implementation Details

### 5.1 String Length

```c
int strLen(const char *s) {
    int count = 0;
    while (s[count] != '\0') count++;
    return count;
}
```

**Complexity:** O(n)

### 5.2 String Copy

```c
void strCopy(char *dest, const char *src) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}
```

**Complexity:** O(n)

### 5.3 String Comparison

```c
int strCompare(const char *s, const char *t) {
    int i = 0;
    while (s[i] != '\0' && t[i] != '\0') {
        if (s[i] != t[i]) return s[i] - t[i];
        i++;
    }
    return s[i] - t[i];
}
```

| Return Value | Meaning                   |
| ------------ | ------------------------- |
| 0            | Strings are equal         |
| Negative     | S < T (lexicographically) |
| Positive     | S > T (lexicographically) |

**Complexity:** O(min(n, m))

### 5.4 String Concatenation

```c
void strConcat(char *dest, const char *src) {
    int i = 0, j = 0;
    while (dest[i] != '\0') i++;
    while (src[j] != '\0') {
        dest[i + j] = src[j];
        j++;
    }
    dest[i + j] = '\0';
}
```

**Complexity:** O(n + m)

## 6. Multiple Choice Questions

**Question 1:** Consider a dynamic string implementation that doubles capacity when full. If we insert 1000 characters starting from an empty string, what is the total number of memory reallocations performed?

A) 10  
B) 50  
C) 100  
D) 500

**Answer: A) 10**

_Explanation:_ Starting from initial capacity (typically 1 or small), the capacity doubles: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024. We need 11 thresholds to reach ≥1000, but reallocations occur 10 times (when crossing each threshold).

---

**Question 2:** In the KMP algorithm, for pattern P = "ABABAC", what is the value of LPS[4]?

A) 0  
B) 1  
C) 2  
D) 3

**Answer: C) 2**

_Explanation:_ LPS array for "ABABAC":

- i=0: LPS[0]=0
- i=1 (B): LPS[1]=0
- i=2 (A): matches pattern[0], LPS[2]=1
- i=3 (B): matches pattern[1], LPS[3]=2
- i=4 (A): matches pattern[2], LPS[4]=2 (not 3 because we need proper prefix-suffix)
- i=5 (C): LPS[5]=0

---

**Question 3:** What is the worst-case time complexity of searching a pattern of length m in a text of length n using the Rabin-Karp algorithm?

A) O(n)  
B) O(n + m)  
C) O(nm)  
D) O(n log m)

**Answer: C) O(nm)**

_Explanation:_ While Rabin-Karp has O(n+m) average case, the worst case occurs when there are many hash collisions, forcing verification of each potential match character-by-character, resulting in O(nm).

---

**Question 4:** In a linked list representation of strings, what is the time complexity of inserting a character at the beginning of a string of length n?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

**Answer: A) O(1)**

_Explanation:_ Linked list representation allows O(1) insertion at the head once the head pointer is known. No shifting or traversal is required; we simply create a new node and update the head pointer.

---

**Question 5:** For a text "AAAAAAA" and pattern "AAA", how many character comparisons does the naive pattern matching algorithm perform in the worst case?

A) 3  
B) 12  
C) 15  
D) 21

**Answer: C) 15**

_Explanation:_ With naive matching, we try the pattern at positions 0, 1, 2, 3, 4 (n-m+1 = 5 positions). At each position, we compare up to m=3 characters. Total = 5 × 3 = 15 comparisons. Note: At position 4, only 3 comparisons are needed (matches), so actually it's (n-m+1) × m = 5 × 3 = 15.

---

**Question 6:** Which string representation would be most efficient for a text editor that frequently inserts and deletes characters at arbitrary positions?

A) Fixed-length array  
B) Dynamic array  
C) Linked list  
D) All have equal efficiency

**Answer: C) Linked list**

_Explanation:_ Linked lists provide O(1) insertion and deletion once the position is found (O(n) to find it). Arrays require O(n) shifting. For frequent edits at arbitrary positions, linked lists minimize the movement overhead, making them ideal for text editors.

---

**Question 7:** In a dynamic array string implementation with growth factor 2, what is the amortized cost per insertion operation?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n log n)

**Answer: A) O(1)**

_Explanation:_ As proven in Theorem 3, when a dynamic array doubles its capacity, the amortized cost of n insertions is O(n), giving O(1) per insertion. This is because expensive copy operations are spread across many cheap insertions.
