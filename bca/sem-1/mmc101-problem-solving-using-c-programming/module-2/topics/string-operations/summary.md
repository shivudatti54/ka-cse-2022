# String Operations in C - Summary

## Key Definitions and Concepts

- **String in C**: An array of characters terminated by a null character ('\0'), which marks the end of the string and enables functions to determine string boundaries.

- **Null Terminator**: The character '\0' with ASCII value 0, automatically added by the compiler when initializing strings with string literals, but must be manually added for character-by-character initialization.

- **String Literal**: A sequence of characters enclosed in double quotes (e.g., "Hello") that creates a read-only array of characters with an implicit null terminator.

## Important Formulas and Theorems

- **String Length Calculation**: strlen(str) counts characters before '\0', excluding the null terminator. A string of length n requires n+1 bytes.

- **String Comparison**: strcmp(s1, s2) returns 0 if equal, negative if s1 < s2, positive if s1 > s2 based on ASCII values. The comparison stops at first differing character.

- **Array-Pointer Relationship**: Array name acts as a pointer to the first element, enabling pointer arithmetic for string traversal: *(str + i) is equivalent to str[i].

## Key Points

- Always allocate one extra byte for the null terminator when declaring character arrays: char str[11] for a 10-character string.

- Never use gets() - it is removed from C11 due to buffer overflow vulnerabilities. Use fgets() instead.

- String comparison must use strcmp(), not the == operator which compares memory addresses.

- When using scanf() for strings, do NOT use the & operator since the array name is already an address.

- The most efficient way to remove newline from fgets() input: str[strcspn(str, "\n")] = '\0';

- Manual string reversal uses two-pointer technique with O(n/2) swaps.

- Palindrome checking compares characters from both ends moving toward the center.

## Common Mistakes to Avoid

- Forgetting the null terminator when building strings character by character, leading to garbage output.

- Using uninitialized character arrays which contain random garbage values.

- Buffer overflow when copying strings without ensuring destination has sufficient capacity.

- Confusing strcmp() return values - 0 means equal, not 1.

- Using scanf() with %s cannot read strings with spaces; use fgets() for multi-word input.

## Revision Tips

- Practice implementing standard string functions (strlen, strcpy, strcmp) from scratch to understand underlying mechanics.

- Memorize the ASCII value differences: 'a'-'A' = 32, which enables case conversion with addition or subtraction.

- Review previous year question papers to identify frequently asked string operation patterns.

- When stuck on string questions, draw the character array with indices to visualize operations.