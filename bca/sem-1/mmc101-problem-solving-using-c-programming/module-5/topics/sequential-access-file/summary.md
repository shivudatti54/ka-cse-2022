# Sequential Access File - Summary

## Key Definitions and Concepts

- **Sequential Access File**: A file where data is read or written in sequential order from beginning to end, without random access capabilities
- **FILE Structure**: A data structure in C that stores information about an open file, accessed through a file pointer (FILE*)
- **EOF (End-of-File)**: A macro typically defined as -1, indicating the end of a file or an error condition
- **File Stream**: A sequential series of data bytes flowing between the program and a file

## Important Formulas and Theorems

- **fopen()**: FILE* fopen(const char *filename, const char *mode) — Opens a file in specified mode
- **fputc()**: int fputc(int c, FILE *fp) — Writes single character, returns character on success, EOF on failure
- **fgetc()**: int fgetc(FILE *fp) — Reads single character, returns character cast to int, or EOF
- **fputs()**: int fputs(const char *s, FILE *fp) — Writes string, returns non-negative on success, EOF on failure
- **fgets()**: char *fgets(char *s, int n, FILE *fp) — Reads up to n-1 characters, returns buffer pointer or NULL
- **fprintf()**: int fprintf(FILE *fp, const char *format, ...) — Formatted output to file
- **fscanf()**: int fscanf(FILE *fp, const char *format, ...) — Formatted input from file
- **fclose()**: int fclose(FILE *fp) — Closes file, returns 0 on success, EOF on error

## Key Points

- File modes "r", "w", "a" are for text files; "rb", "wb", "ab" are for binary files
- "w" mode truncates existing file to zero length; "a" mode appends to end of file
- Always store fgetc() return value in an int variable to correctly detect EOF
- Always check if fopen() returns NULL before using the file pointer
- fgets() includes newline character if read; it stops at newline, EOF, or n-1 characters
- fscanf() returns the number of items successfully read, which can be used for EOF detection
- The rewind() function resets file position to beginning for rereading
- Binary files require "b" mode to prevent text-mode translations that corrupt data

## Common Mistakes to Avoid

1. Using a char variable to store fgetc() return value, which fails to detect EOF correctly
2. Using "w" mode when intending to preserve existing file data, resulting in data loss
3. Forgetting to close files after operations, potentially causing data loss from unflushed buffers
4. Not checking for NULL file pointer after fopen(), leading to segmentation faults
5. Confusing text and binary modes, causing corruption when handling non-text data

## Revision Tips

1. Practice writing small programs that create, write, read, and append to files to build muscle memory
2. Memorize the file mode table and understand the behavior of each mode thoroughly
3. Remember the int vs char distinction for fgetc() return values—this is a classic exam question
4. Review error handling patterns: always check NULL after fopen(), check return values for EOF
5. Understand the difference between formatted functions (fprintf, fscanf) and character/string functions