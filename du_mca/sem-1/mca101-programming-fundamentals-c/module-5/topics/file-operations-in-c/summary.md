# File Operations in C - Summary

## Key Definitions and Concepts
- **FILE**: Structure containing file control information
- **Stream**: Abstraction representing data flow
- **Buffer**: Temporary storage between program and file
- **EOF**: End-of-File marker (integer -1)

## Important Formulas and Theorems
- `FILE *fopen(const char *filename, const char *mode)`
- `int fclose(FILE *stream)`
- `size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)`
- `int fseek(FILE *stream, long offset, int whence)`
- `long ftell(FILE *stream)`

## Key Points
- Always check fopen() return value
- Binary mode preserves exact byte values
- fwrite()/fread() use item counts, not bytes
- fflush() ensures buffer writes to disk
- Use perror() for error diagnostics
- Random access requires calculating offsets
- Close files in reverse order of opening

## Common Mistakes to Avoid
- Using "w" mode when needing to preserve data
- Forgetting to close files (resource leak)
- Mixing fread() with fprintf()
- Not handling newline differences in text files
- Assuming file position after sequential operations

## Revision Tips
1. Practice with both text and binary files
2. Memorize mode strings using:
   - First letter: r(read), w(write), a(append)
   - + sign enables read/write
3. Write file operation sequences in pseudocode first
4. Use hex editors to inspect binary file contents