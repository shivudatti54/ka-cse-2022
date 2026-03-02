# Introduction to Files in C Programming - Summary

## Key Definitions and Concepts

- FILE: A data structure defined in stdio.h that contains information about an open file including buffer pointer, file position, and access mode.
- File Pointer: A pointer to a FILE structure (FILE *), used as a handle for all file operations.
- Text File: A file where data is stored as readable ASCII characters, with lines ending in newline characters.
- Binary File: A file where data is stored in the same binary format as computer memory, without character conversion.
- EOF: End-of-file marker, typically defined as -1, returned by functions like fgetc() when end of file is reached.

## Important Formulas and Functions

| Function | Purpose |
|----------|---------|
| fopen(filename, mode) | Opens a file and returns FILE pointer |
| fclose(fp) | Closes an open file |
| fprintf(fp, format, ...) | Writes formatted data to file |
| fscanf(fp, format, ...) | Reads formatted data from file |
| fputs(str, fp) | Writes a string to file |
| fgets(str, n, fp) | Reads a string from file |
| fputc(ch, fp) | Writes a character to file |
| fgetc(fp) | Reads a character from file |
| fwrite(ptr, size, n, fp) | Writes binary data to file |
| fread(ptr, size, n, fp) | Reads binary data from file |
| feof(fp) | Returns non-zero if at end of file |
| ferror(fp) | Returns non-zero if error occurred |

## Key Points

1. Files enable permanent data storage beyond program execution.
2. Always verify fopen() returns non-NULL before file operations.
3. Mode "r" requires existing file; "w" creates/truncates; "a" appends or creates.
4. Add "b" for binary mode: "rb", "wb", "ab".
5. fscanf() stops reading at whitespace; fgets() reads entire line including spaces.
6. Binary files (fread/fwrite) are more efficient for structured data like structs.
7. EOF is returned after attempting to read past end-of-file, not when at the end.
8. Always close files with fclose() to flush buffers and free resources.
9. Standard files: stdin (keyboard), stdout (screen), stderr (error output).

## Common Mistakes to Avoid

1. Not checking for NULL after fopen() - leads to segmentation faults.
2. Using wrong mode (reading from "w" mode file returns NULL).
3. Confusing text and binary modes for different types of data.
4. Not using & address operator with fscanf() for variables.
5. Assuming feof() returns true when at end - it returns true AFTER a read past end.
6. Forgetting to close files, causing data loss from unflushed buffers.
7. Using "/" vs "\" in file paths - C accepts both but "\" needs escape sequence.

## Revision Tips

1. PRACTICE WRITING small programs to create, read, and modify files.
2. MEMORIZE the mode strings and their effects on file creation/truncation.
3. UNDERSTAND the difference between fscanf() and fgets() for string input.
4. REVISIT the binary file example with structures - this is commonly asked in exams.
5. REMEMBER error handling: always close files even when errors occur.
6. Review command-line arguments as they often accompany file handling questions.