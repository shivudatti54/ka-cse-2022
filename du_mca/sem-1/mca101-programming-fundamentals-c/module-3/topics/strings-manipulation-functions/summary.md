# Strings Manipulation Functions
## Programming Fundamentals C - MCA (Delhi University, Revised June 2024)

### Introduction
Strings in C are character arrays terminated by a null character (`\0`). The **string.h** header file provides numerous functions for string manipulation, which are essential for text processing in C programs. This topic carries significant weight in the Delhi University MCA examination.

### Key String Manipulation Functions

**String Length & Copy**
- `strlen(s)` - Returns the length of string s (excluding null character)
- `strcpy(dest, src)` - Copies entire string src to dest
- `strncpy(dest, src, n)` - Copies first n characters; pads if src < n

**String Concatenation**
- `strcat(dest, src)` - Appends src to end of dest
- `strncat(dest, src, n)` - Appends first n characters of src

**String Comparison**
- `strcmp(s1, s2)` - Compares strings (returns 0 if equal, <0 if s1<s2, >0 if s1>s2)
- `strncmp(s1, s2, n)` - Compares first n characters only

**String Searching**
- `strchr(s, ch)` - Returns pointer to first occurrence of character ch in s
- `strstr(s, sub)` - Returns pointer to first occurrence of substring sub in s
- `strrchr(s, ch)` - Returns pointer to last occurrence of character ch

**String Conversion**
- `strlwr(s)` - Converts string to lowercase
- `strupr(s)` - Converts string to uppercase
- `strrev(s)` - Reverses the string

**Other Important Functions**
- `strdup(s)` - Duplicates a string (allocates memory)
- `strtok(s, delim)` - Tokenizes string using delimiters

### String Input/Output Functions
- `gets(s)` - Reads string from stdin (unsafe, deprecated)
- `fgets(s, n, file)` - Safe string input (reads n-1 characters)
- `puts(s)` - Outputs string with newline
- `sprintf()` / `sscanf()` - Formatted string operations

### Exam Tips (Delhi University Syllabus)
- Remember: All string functions require `<string.h>` header
- Always ensure destination buffer is large enough to prevent buffer overflow
- `strcmp()` returns 0 for equal strings (not 1)
- Null character `\0` is automatically added by string functions
- Character arrays must be initialized properly to avoid garbage values

### Conclusion
String manipulation functions are fundamental for text processing in C. Master these functions to efficiently handle string operations in practical C programs. Focus on understanding return types, parameter requirements, and common pitfalls like buffer overflows for exam success.