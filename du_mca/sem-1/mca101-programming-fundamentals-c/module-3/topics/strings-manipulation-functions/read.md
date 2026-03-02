# Strings Manipulation Functions in C

## Programming Fundamentals C — MCA Delhi University (Revised June 2024)

---

## 1. Introduction to Strings in C

In the C programming language, strings are not a native data type like in many modern programming languages. Instead, **strings in C are represented as arrays of characters terminated by a null character (`'\0'`)**. This null terminator is crucial as it marks the end of the string and allows C string functions to determine the string's length dynamically.

### What Makes C Strings Unique?

```c
char greeting[] = "Hello";
```

In memory, this string is stored as:

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Char  | H | e | l | l | o | \0 |

The string occupies **6 bytes** (5 characters + 1 null terminator), not 5. This fundamental understanding is essential for mastering string manipulation in C.

### Real-World Relevance

String manipulation is ubiquitous in software development:

- **Text Processing**: Parsing log files, processing user inputs, formatting output
- **Data Parsing**: CSV files, JSON, XML parsing
- **Network Programming**: HTTP headers, URL handling, protocol implementation
- **Database Operations**: SQL query construction, data sanitization
- **System Programming**: File path manipulation, environment variable handling

---

## 2. Header Files for String Manipulation

All string manipulation functions in C are declared in the `<string.h>` header file. Some additional functions for memory operations are in `<stdlib.h>` and `<ctype.h>`.

```c
#include <string.h>  // Primary header for string functions
#include <ctype.h>   // For character classification (isalpha, isdigit, etc.)
#include <stdlib.h>  // For memory allocation functions
```

---

## 3. Comprehensive Coverage of String Manipulation Functions

### 3.1 String Length Functions

#### `strlen()` — Get String Length

The `strlen()` function returns the number of characters in a string, **excluding** the null terminator.

**Function Signature:**
```c
size_t strlen(const char *str);
```

**Parameters:**
- `str`: Pointer to a null-terminated string

**Return Value:**
- Returns the number of characters before the null terminator (type: `size_t`)

**Detailed Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Delhi University";
    char str2[] = "";
    char str3[50] = "MCA";
    
    printf("Length of '%s': %zu\n", str1, strlen(str1));  // Output: 16
    printf("Length of empty string: %zu\n", strlen(str2)); // Output: 0
    printf("Length of '%s': %zu\n", str3, strlen(str3));  // Output: 3
    
    // Common pitfall: sizeof vs strlen
    printf("sizeof str3: %zu\n", sizeof(str3));  // Output: 50
    printf("strlen str3: %zu\n", strlen(str3));  // Output: 3
    
    return 0;
}
```

**Key Insight:** The difference between `sizeof()` and `strlen()` is critical:
- `sizeof()` returns total allocated memory (including uninitialized bytes)
- `strlen()` returns actual string length (excluding `\0`)

---

### 3.2 String Copy Functions

#### `strcpy()` — Copy Entire String

Copies the entire source string (including null terminator) to the destination.

**Function Signature:**
```c
char *strcpy(char *dest, const char *src);
```

**Parameters:**
- `dest`: Destination string (must have sufficient space)
- `src`: Source string to copy from

**Return Value:**
- Returns a pointer to the destination string

**Important Warning:** `strcpy()` does not perform bounds checking. If the destination buffer is smaller than the source, it causes a **buffer overflow** vulnerability.

**Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char source[] = "Programming Fundamentals";
    char destination[50];  // Must be large enough!
    
    strcpy(destination, source);
    
    printf("Source: %s\n", source);
    printf("Destination: %s\n", destination);
    
    return 0;
}
```

#### `strncpy()` — Copy N Characters

A safer alternative that copies at most `n` characters.

**Function Signature:**
```c
char *strncpy(char *dest, const char *src, size_t n);
```

**Behavior:**
- Copies up to `n` characters from `src` to `dest`
- If `src` is shorter than `n`, remaining positions are padded with null bytes
- If `src` is longer than `n`, the result is **not null-terminated**

**Critical Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[10];
    char str2[10];
    
    // Problem: May not null-terminate if n >= length of src
    strncpy(str1, "Programming", 10);
    printf("str1 (no null terminator): %s\n", str1);  // May show garbage!
    printf("Length of str1: %zu\n", strlen(str1));    // Undefined behavior!
    
    // Solution: Always null-terminate
    strncpy(str2, "Programming", 9);
    str2[9] = '\0';
    printf("str2 (properly terminated): %s\n", str2);
    
    return 0;
}
```

---

### 3.3 String Concatenation Functions

#### `strcat()` — Concatenate Strings

Appends a copy of the source string to the destination string.

**Function Signature:**
```c
char *strcat(char *dest, const char *src);
```

**Important:** The destination buffer must have enough space to hold both strings plus the null terminator.

**Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello, ";
    char str2[] = "MCA Students!";
    
    strcat(str1, str2);
    printf("Concatenated: %s\n", str1);  // Output: Hello, MCA Students!
    
    return 0;
}
```

#### `strncat()` — Concatenate N Characters

Appends at most `n` characters from source.

**Function Signature:**
```c
char *strncat(char *dest, const char *src, size_t n);
```

**Key Difference from `strncpy()`:** `strncat()` **always** appends a null terminator, making it safer than `strncpy()`.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello";
    char str2[] = " World Programming";
    
    strncat(str1, str2, 6);  // Only append " World"
    printf("Result: %s\n", str1);  // Output: Hello World
    
    return 0;
}
```

---

### 3.4 String Comparison Functions

#### `strcmp()` — Compare Two Strings

Compares two strings lexicographically (character by character).

**Function Signature:**
```c
int strcmp(const char *str1, const char *str2);
```

**Return Values:**
| Return Value | Meaning |
|--------------|---------|
| 0 | Strings are equal |
| < 0 | `str1` is less than `str2` |
| > 0 | `str1` is greater than `str2` |

**Comparison Logic:** Compares the first differing character's ASCII values. Since uppercase letters (A-Z: 65-90) have lower ASCII values than lowercase (a-z: 97-122), string comparison is **case-sensitive**.

**Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "apple";
    char str3[] = "banana";
    char str4[] = "APPLE";
    
    printf("strcmp(str1, str2): %d\n", strcmp(str1, str2));  // 0 (equal)
    printf("strcmp(str1, str3): %d\n", strcmp(str1, str3));  // negative (< 0)
    printf("strcmp(str3, str1): %d\n", str3, str1);  // positive (> 0)
    printf("strcmp(str1, str4): %d\n", strcmp(str1, str4));  // positive (case-sensitive)
    
    return 0;
}
```

#### `strncmp()` — Compare N Characters

Compares only the first `n` characters of two strings.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "hello world";
    char str2[] = "hello MCA";
    
    int result = strncmp(str1, str2, 5);
    printf("strncmp(str1, str2, 5): %d\n", result);  // 0 (first 5 chars equal)
    
    result = strncmp(str1, str2, 6);
    printf("strncmp(str1, str2, 6): %d\n", result);  // negative (space < M)
    
    return 0;
}
```

---

### 3.5 String Search Functions

#### `strchr()` — Find Character (First Occurrence)

Searches for the first occurrence of a character in a string.

**Function Signature:**
```c
char *strchr(const char *str, int c);
```

**Return Value:**
- Pointer to the first occurrence of `c` in `str`
- Returns `NULL` if character not found

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Delhi University";
    char *result;
    
    result = strchr(str, 'i');
    if (result != NULL) {
        printf("First 'i' found at position: %ld\n", result - str);  // Output: 4
        printf("Substring from 'i': %s\n", result);  // Output: i University
    }
    
    // Searching for null character
    result = strchr(str, '\0');
    printf("Null terminator at end: %s\n", result);  // Outputs empty
    
    return 0;
}
```

#### `strrchr()` — Find Character (Last Occurrence)

Searches for the last occurrence of a character.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Programming";
    char *result;
    
    result = strrchr(str, 'r');
    if (result != NULL) {
        printf("Last 'r' found at position: %ld\n", result - str);  // Output: 5
        printf("From last 'r': %s\n", result);  // Output: ramming
    }
    
    return 0;
}
```

#### `strstr()` — Find Substring

Searches for the first occurrence of a substring within a string.

**Function Signature:**
```c
char *strstr(const char *haystack, const char *needle);
```

**Return Value:**
- Pointer to the beginning of the substring
- Returns `NULL` if substring not found

**Example:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char text[] = "MCA Programming Fundamentals";
    char *substring;
    
    substring = strstr(text, "Programming");
    if (substring != NULL) {
        printf("Found 'Programming' at position: %ld\n", substring - text);
        printf("From 'Programming': %s\n", substring);
        // Output: Programming Fundamentals
    }
    
    // Substring not found
    substring = strstr(text, "Java");
    if (substring == NULL) {
        printf("'Java' not found in the text\n");
    }
    
    return 0;
}
```

---

### 3.6 String Tokenization Function

#### `strtok()` — Tokenize String

Breaks a string into tokens (substrings) based on delimiters.

**Function Signature:**
```c
char *strtok(char *str, const char *delimiters);
```

**Critical Behavior:**
1. The function maintains **static internal state** between calls
2. On first call, pass the string to tokenize
3. On subsequent calls, pass `NULL` to continue tokenizing the same string
4. The delimiter string can contain multiple delimiter characters

**Example — Parsing CSV Data:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char data[] = "MCA,Programming,C,Strings";
    char *token;
    const char delimiter[] = ",";
    
    printf("Tokens in '%s':\n", data);
    
    // First call
    token = strtok(data, delimiter);
    
    // Subsequent calls
    while (token != NULL) {
        printf("  - %s\n", token);
        token = strtok(NULL, delimiter);
    }
    
    /* Output:
     * Tokens in 'MCA,Programming,C,Strings':
     *   - MCA
     *   - Programming
     *   - C
     *   - Strings
     */
    
    return 0;
}
```

**Example — Parsing Space-Separated Words:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char sentence[] = "Delhi University MCA Program";
    char *token;
    const char space[] = " \t\n";  // Space, tab, newline
    
    token = strtok(sentence, space);
    while (token != NULL) {
        printf("Token: %s (length: %zu)\n", token, strlen(token));
        token = strtok(NULL, space);
    }
    
    return 0;
}
```

**Important Caveats:**
1. **String Modification:** `strtok()` modifies the original string by inserting `\0` at delimiter positions
2. **Thread Safety:** Not thread-safe; use `strtok_r()` in multi-threaded applications
3. **Empty Tokens:** Consecutive delimiters create empty tokens

---

### 3.7 Additional String Manipulation Functions

#### `strdup()` — Duplicate String

Allocates memory and copies the string.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char original[] = "MCA Delhi University";
    char *duplicate;
    
    duplicate = strdup(original);
    
    if (duplicate != NULL) {
        printf("Original: %s\n", original);
        printf("Duplicate: %s\n", duplicate);
        
        // Important: Free the allocated memory
        free(duplicate);
    }
    
    return 0;
}
```

#### `strlwr()` and `strupr()` — Case Conversion

Convert string to lowercase/uppercase (non-standard but widely available):

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Delhi University";
    
    // Note: These are non-standard functions
    // Use character-by-character approach for portability
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
    printf("Lowercase: %s\n", str);
    
    // Convert back to uppercase
    for (int i = 0; str[i]; i++) {
        str[i] = toupper(str[i]);
    }
    printf("Uppercase: %s\n", str);
    
    return 0;
}
```

#### `strrev()` — Reverse String

Reverses the string (non-standard):

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Programming";
    int len = strlen(str);
    
    // Manual reversal
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - 1 - i];
        str[len - 1 - i] = temp;
    }
    
    printf("Reversed: %s\n", str);  // gnimmargorP
    
    return 0;
}
```

---

## 4. Practical Example: String Processing Application

This comprehensive example demonstrates multiple string functions working together:

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_LENGTH 1000

void removeExtraSpaces(char *input, char *output);
int countWords(const char *str);
void capitalizeFirstLetter(char *str);

int main() {
    char text[MAX_LENGTH] = "  hello   mca  students  of  delhi  university  ";
    char processed[MAX_LENGTH];
    
    printf("Original: '%s'\n", text);
    printf("Original length: %zu\n\n", strlen(text));
    
    // Step 1: Remove extra spaces
    removeExtraSpaces(text, processed);
    printf("After removing extra spaces: '%s'\n", processed);
    printf("New length: %zu\n\n", strlen(processed));
    
    // Step 2: Capitalize first letter of each word
    capitalizeFirstLetter(processed);
    printf("After capitalization: '%s'\n\n", processed);
    
    // Step 3: Count words
    int wordCount = countWords(processed);
    printf("Word count: %d\n", wordCount);
    
    return 0;
}

void removeExtraSpaces(char *input, char *output) {
    int i, j = 0;
    int inSpace = 0;
    
    for (i = 0; input[i] != '\0'; i++) {
        if (isspace(input[i])) {
            if (!inSpace && j > 0) {
                output[j++] = ' ';
                inSpace = 1;
            }
        } else {
            output[j++] = input[i];
            inSpace = 0;
        }
    }
    
    // Remove trailing space
    if (j > 0 && output[j-1] == ' ') {
        j--;
    }
    
    output[j] = '\0';
}

int countWords(const char *str) {
    int count = 0;
    int inWord = 0;
    
    while (*str) {
        if (isspace(*str)) {
            inWord = 0;
        } else if (!inWord) {
            count++;
            inWord = 1;
        }
        str++;
    }
    
    return count;
}

void capitalizeFirstLetter(char *str) {
    int nextChar = 1;  // Next character should be capitalized
    
    while (*str) {
        if (isspace(*str)) {
            nextChar = 1;
        } else if (nextChar && islower(*str)) {
            *str = toupper(*str);
            nextChar = 0;
        } else {
            nextChar = 0;
        }
        str++;
    }
}

/* Output:
Original: '  hello   mca  students  of  delhi  university  '
Original length: 50

After removing extra spaces: 'hello mca students of delhi university'
New length: 37

After capitalization: 'Hello Mca Students Of Delhi University'

Word count: 5
*/
```

---

## 5. Common Pitfalls and Best Practices

### Common Pitfalls

1. **Buffer Overflow**: Not allocating enough space for destination strings
   ```c
   char dest[10];
   strcpy(dest, "This is too long!");  // DANGER!
   ```

2. **Forgetting Null Terminator**: Especially with `strncpy()`
   ```c
   char dest[10];
   strncpy(dest, "HelloWorld", 10);  // No null terminator!
   dest[10] = '\0';  // Always add this
   ```

3. **Using Wrong Comparison Operator**: Comparing strings with `==`
   ```c
   if (str1 == str2)  // WRONG! Compares pointers, not content
   if (strcmp(str1, str2) == 0)  // CORRECT
   ```

4. **Not Checking NULL Returns**: Functions like `strchr()`, `strstr()`, `strdup()` can return NULL
   ```c
   char *result = strstr(text, "pattern");
   if (result != NULL) {  // Always check!
       // Use result
   }
   ```

5. **Modifying String Literals**: Attempting to modify read-only memory
   ```c
   char *str = "hello";  // String literal - read only!
   str[0] = 'H';  // UNDEFINED BEHAVIOR
   ```

### Best Practices

1. **Use `strncpy()`, `strncat()`, `strncmp()`** instead of their unsafe counterparts when possible
2. **Always null-terminate** strings after manual operations
3. **Use `sizeof()` correctly** — know the difference between array and pointer
4. **Free memory** allocated by `strdup()`
5. **Validate input** before processing

---

## 6. Delhi University Syllabus Context

This content aligns with the **MCA Programming Fundamentals C** syllabus (Revised June 2024), specifically covering:

- String handling in C
- Standard library string functions
- Character manipulation
- Memory safety considerations
- Practical string processing applications

**Recommended Practical Exercises from Syllabus:**
1. Implement your own version of `strlen()`, `strcpy()`, `strcat()`
2. Write a program to reverse a string without using `strrev()`
3. Check if a string is a palindrome
4. Count vowels and consonants in a string
5. Remove all duplicate characters from a string

---

## 7. Exam Tips and Important Concepts

### For University Examinations:

1. **Memory Diagram Questions**: Be prepared to draw how strings are stored in memory
2. **Function Output Prediction**: Know what each function returns
3. **Error Identification**: Spot common errors in string manipulation code
4. **Implementing Without Library**: Some exams ask to implement string functions manually

### High-Weightage Topics:
- `strcmp()` return values
- `strtok()` behavior and limitations
- Difference between `strcpy()` and `strncpy()`
- Buffer overflow vulnerabilities

---

## 8. Key Takeaways

1. **Strings in C are character arrays** terminated by a null character (`\0`)

2. **Always ensure sufficient buffer space** when copying or concatenating strings

3. **`strcmp()` returns:**
   - `0` for equal strings
   - Negative when first < second
   - Positive when first > second (lexicographically)

4. **`strtok()` modifies the original string** and requires multiple calls to process one string

5. **Always null-terminate** strings manually when using `strncpy()` or when creating strings character-by-character

6. **Use `strncpy()`, `strncat()`, `strncmp()`** for safer string operations with known lengths

7. **Check for NULL returns** from functions like `strchr()`, `strstr()`, `strdup()`

8. **The `<string.h>` header** contains all standard string manipulation functions

9. **Understanding pointer arithmetic** is essential for effective string manipulation in C

10. **Practice implementing basic string functions** from scratch to deeply understand how they work

---

## 9. Advanced Sample MCQs

### Multiple Choice Questions

**Q1. What is the output of the following code?**

```c
char str1[] = "Hello";
char str2[] = "Hello";
printf("%d", strcmp(str1, str2));
```

A) -1  
B) 0  
C) 1  
D) Undefined

**Answer: B) 0**

---

**Q2. What does the following code print?**

```c
char str[] = "MCA";
printf("%zu", sizeof(str));
```

A) 2  
B) 3  
C) 4  
D) 6

**Answer: B) 3** (Actually C) 4 — includes null terminator. **Correction: C) 4**

---

**Q3. What is the correct way to safely copy a string in C?**

A) `strcpy(dest, src)`  
B) `strncpy(dest, src, n)`  
C) Both A and B  
D) Neither is safe

**Answer: B** — `strncpy` is safer, but requires proper null-termination.

---

**Q4. After executing the following code, what is the content of `str`?**

```c
char str[] = "Hello";
str[0] = '\0';
printf("%s", str);
```

A) Hello  
B) H  
C) (empty string)  
D) \0

**Answer: C) (empty string)**

---

**Q5. Which function is used to find a substring within a string?**

A) `strchr()`  
B) `strstr()`  
C) `strrchr()`  
D) `strtok()`

**Answer: B) `strstr()`**

---

**Q6. What is the return type of `strlen()`?**

A) `int`  
B) `unsigned int`  
C) `size_t`  
D) `long`

**Answer: C) `size_t`**

---

**Q7. What happens when `strtok()` cannot find any more tokens?**

A) Returns an empty string  
B) Returns NULL  
C) Returns the original string  
D) Causes segmentation fault

**Answer: B) Returns NULL**

---

**Q8. Consider the following code:**

```c
char s1[5] = "Test";
char s2[] = "Test";
```

What is the difference between `s1` and `s2`?

A) No difference  
B) s1 has extra space for null terminator  
C) s2 has extra space for null terminator  
D) Both cause compilation errors

**Answer: C) `s2` has extra space for null terminator (size 5), `s1` has size 5 with implicit null**

---

**End of Study Material**

*Prepared for MCA Delhi University (Revised June 2024) — Programming Fundamentals C*