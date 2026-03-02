# Strings

## Overview

A string is a finite sequence of characters drawn from a character set. In the context of data structures, strings are a formal Abstract Data Type (ADT) with well-defined operations, multiple possible representations, and algorithms with measurable time complexity.

## Key Points

- String ADT operations include StrLen, StrConcat, SubStr, StrCompare, StrInsert, StrDelete, and StrIndex.
- Three major string representations: fixed-length array, variable-length with dynamic allocation, and linked list.
- Naive pattern matching has O(n \* m) worst-case time complexity.
- KMP algorithm has O(n + m) time complexity and uses a failure function to avoid redundant comparisons.

## Important Definitions

- **Abstract Data Type (ADT)**: A high-level description of a data structure that defines its operations without specifying implementation details.
- **String**: A finite sequence of characters drawn from a character set.
- **Null string**: The string of length zero.
- **Failure function**: A function used in the KMP algorithm to determine the next position to compare in the text.

## Key Formulas / Syntax

- `StrLen(S)`: Returns the length of string S.
- `StrConcat(S, T)`: Returns a new string by appending T after S.
- `SubStr(S, i, j)`: Returns substring of S starting at position i with length j.
- `StrCompare(S, T)`: Compares S and T lexicographically.

## Comparisons

| Criterion            | Fixed Array          | Dynamic Array       | Linked List             |
| -------------------- | -------------------- | ------------------- | ----------------------- |
| Random access        | O(1)                 | O(1)                | O(n)                    |
| Insert at position i | O(n)                 | O(n)                | O(1) after traversal    |
| Delete at position i | O(n)                 | O(n)                | O(1) after traversal    |
| Concatenation        | O(n+m), may overflow | O(n+m), may realloc | O(1)                    |
| Space efficiency     | Wastes space         | Good                | Poor (pointer overhead) |

## Exam Tips

- Be prepared to write the naive pattern matching algorithm and trace its execution.
- Understand how to compute the failure function for the KMP algorithm.
- Know the trade-offs between different string representations.
- Be able to implement string operations in C, accounting for null terminators and buffer bounds.
- Practice computing the failure function by hand and tracing the KMP search.
- Focus on understanding the String ADT operations and their time complexities.
- Review the C string essentials, including null-terminated arrays and common string functions.
