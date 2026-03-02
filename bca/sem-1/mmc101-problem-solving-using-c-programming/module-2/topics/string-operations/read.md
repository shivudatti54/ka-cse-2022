# String Operations in C Programming


## Table of Contents

- [String Operations in C Programming](#string-operations-in-c-programming)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [String Declaration and Initialization](#string-declaration-and-initialization)
  - [String Input and Output Functions](#string-input-and-output-functions)
  - [Standard Library Functions (string.h)](#standard-library-functions-stringh)
  - [Character-wise String Operations](#character-wise-string-operations)
  - [String Searching Functions](#string-searching-functions)
- [Examples](#examples)
  - [Example 1: Palindrome Checker](#example-1-palindrome-checker)
  - [Example 2: String Reversal](#example-2-string-reversal)
  - [Example 3: Word Count in Sentence](#example-3-word-count-in-sentence)
- [Exam Tips](#exam-tips)

## Introduction

Strings represent one of the most fundamental data types in C programming, serving as the backbone for text processing, file handling, user input management, and numerous real-world applications. In the C programming language, strings are not a built-in data type but rather an array of characters terminated by a null character ('\0'). This unique representation makes string handling both powerful and challenging, requiring a deep understanding of character arrays and memory management.

The importance of string operations in computer science cannot be overstated. From simple console applications to complex text editors, search engines, and data processing systems, strings form the foundation of information representation. In the context of the University of Delhi's Computer Science curriculum, string operations represent a critical skill set that students must master to excel in their programming assignments and end-semester examinations. The CUET-qualified students entering DU's premier colleges bring diverse backgrounds, but string manipulation remains a common challenge that requires systematic practice and conceptual clarity.

This topic builds directly upon the understanding of one-dimensional arrays, as strings are essentially character arrays. The connection between arrays and strings becomes evident when we consider that string functions operate by traversing character arrays element by element. Furthermore, string operations frequently appear in algorithm implementations, including sorting algorithms like Selection Sort and searching algorithms like Linear Search and Binary Search, making this topic essential for overall programming proficiency.

## Key Concepts

### String Declaration and Initialization

In C, a string is declared as a character array. The declaration requires allocating sufficient memory to hold all characters plus the null terminator. There are multiple ways to initialize a string in C:

```c
char str1[] = "Hello";           // Compiler adds '\0' automatically
char str2[10] = "Hello";         // Explicit size with extra space
char str3[] = {'H', 'e', 'l', 'l', 'o', '\0'}; // Character by character
char str4[6] = "World";          // Size matches content exactly
```

The null character '\0' is crucial as it marks the end of the string. Without it, functions traversing the string would not know where to stop, leading to undefined behavior or buffer overflow vulnerabilities.

### String Input and Output Functions

C provides several functions for reading and writing strings. The gets() function, while historically significant, is deprecated due to buffer overflow vulnerabilities. The fgets() function provides safer string input:

```c
char name[50];
printf("Enter your name: ");
fgets(name, 50, stdin);  // Reads up to 49 characters or newline
name[strcspn(name, "\n")] = '\0';  // Remove trailing newline
```

For output, puts() and printf() serve different purposes. puts() automatically adds a newline, while printf() offers formatted output with escape sequences:

```c
puts("Hello");           // Output: Hello\n
printf("Value: %d\n", x); // Formatted output
```

### Standard Library Functions (string.h)

The C standard library provides powerful string manipulation functions through the string.h header. Understanding these functions is essential for efficient string handling:

**strlen() - String Length**: Returns the number of characters before the null terminator.

```c
size_t strlen(const char *s);
// Example
char msg[] = "Programming";
int len = strlen(msg);  // Returns 11
```

**strcpy() - String Copy**: Copies source string to destination. The safer alternative is strncpy():

```c
char dest[20], src[] = "Hello";
strcpy(dest, src);           // dest now contains "Hello"
strncpy(dest, src, 5);       // Copies exactly n characters
```

**strcat() - String Concatenation**: Appends source string to destination:

```c
char str[20] = "Hello";
strcat(str, " World");       // str now contains "Hello World"
```

**strcmp() - String Comparison**: Returns 0 if strings are equal, negative if first < second, positive if first > second (based on ASCII values):

```c
int result = strcmp("apple", "banana");  // Returns negative
int result2 = strcmp("hello", "hello");  // Returns 0
```

### Character-wise String Operations

Beyond library functions, programmers often need to process strings character by character. Common operations include:

**Converting to Uppercase/Lowercase**:
```c
void toUpperCase(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z')
            str[i] = str[i] - 32;  // ASCII adjustment
    }
}
```

**Counting Vowels and Consonants**:
```c
int countVowels(char str[]) {
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        char ch = tolower(str[i]);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count++;
    }
    return count;
}
```

### String Searching Functions

**strchr() - Character Search**: Finds first occurrence of a character:

```c
char *strchr(const char *s, int c);
// Returns pointer to first occurrence or NULL if not found
```

**strstr() - Substring Search**: Finds first occurrence of a substring:

```c
char *strstr(const char *haystack, const char *needle);
// Returns pointer to first occurrence of needle in haystack
```

## Examples

### Example 1: Palindrome Checker

A palindrome reads the same forwards and backwards. This example demonstrates string traversal and comparison techniques.

```c
#include <stdio.h>
#include <string.h>

int isPalindrome(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;
    
    while (left < right) {
        // Skip non-alphanumeric characters if needed
        if (str[left] != str[right])
            return 0;  // Not a palindrome
        left++;
        right--;
    }
    return 1;  // Is a palindrome
}

int main() {
    char word[50];
    printf("Enter a word: ");
    scanf("%s", word);
    
    if (isPalindrome(word))
        printf("%s is a palindrome\n", word);
    else
        printf("%s is not a palindrome\n", word);
    
    return 0;
}
```

**Step-by-step execution for "radar":**
- left = 0 (r), right = 4 (r): Equal, continue
- left = 1 (a), right = 3 (a): Equal, continue
- left = 2 (d), right = 2 (d): Equal, continue
- left becomes 3 which is not < right, loop exits
- Returns 1 (palindrome)

### Example 2: String Reversal

Reversing a string is a fundamental operation used in many algorithms including palindrome checking and anagram detection.

```c
#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;
    char temp;
    
    while (start < end) {
        // Swap characters
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        
        start++;
        end--;
    }
}

int main() {
    char text[] = "Programming";
    printf("Original: %s\n", text);
    
    reverseString(text);
    printf("Reversed: %s\n", text);
    
    return 0;
}
```

**Output:**
```
Original: Programming
Reversed: gnimmargorP
```

### Example 3: Word Count in Sentence

This example demonstrates string parsing and boundary detection.

```c
#include <stdio.h>

int countWords(char sentence[]) {
    int count = 0;
    int inWord = 0;
    
    for (int i = 0; sentence[i] != '\0'; i++) {
        if (sentence[i] == ' ' || sentence[i] == '\n' || sentence[i] == '\t') {
            inWord = 0;  // Found a delimiter
        } else if (inWord == 0) {
            inWord = 1;  // Starting a new word
            count++;
        }
    }
    return count;
}

int main() {
    char text[] = "The quick brown fox jumps over the lazy dog";
    printf("Word count: %d\n", countWords(text));
    return 0;
}
```

**Execution analysis:**
- "The" - first non-space triggers count = 1
- Space after "The" - inWord = 0
- "quick" - non-space with inWord = 0 triggers count = 2
- Continues until all 9 words are counted

## Exam Tips

1. ALWAYS remember the null terminator '\0' when calculating string size. A string of n characters requires n+1 bytes of storage.

2. In exam questions, pay attention to whether strings are compared using == operator (compares addresses) or strcmp() (compares content). Using == for string comparison is a common mistake.

3. When using scanf() for strings, do not use & operator as the array name already represents the base address. Use scanf("%s", str) not scanf("%s", &str).

4. The strcmp() function returns 0 for equal strings, not 1. Many students lose marks by writing if(strcmp(a,b) == 1) instead of if(strcmp(a,b) == 0).

5. For string manipulation questions, always initialize strings properly. Uninitialized character arrays contain garbage values.

6. Remember that gets() is unsafe and removed from C11. Use fgets() instead for reading strings with spaces.

7. When implementing string functions from scratch, the null terminator must be explicitly added at the end of the modified string.

8. In two-dimensional arrays of characters (array of strings), each row represents an individual string with its own null terminator.