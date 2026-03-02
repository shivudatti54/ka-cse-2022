# Reading Dictionaries in Unix System Programming - Summary

## Key Definitions

- **Dictionary File**: A plain text file containing a list of words, typically one word per line, stored in standardized locations on Unix systems.

- **System Calls**: Low-level functions (open, read, write, close) that provide direct interface to the Unix kernel for file operations.

- **Standard I/O Library**: Higher-level C library functions (fopen, fgets, fprintf) that provide buffered I/O with simplified interface.

- **File Descriptor**: An integer returned by open() that identifies an open file in the process's file table.

- **FILE Pointer**: A pointer to an opaque structure returned by fopen() that represents a buffered stream.

## Important Formulas

- **Hash Function**: `hash = ((hash << 5) + hash) + c` - Simple polynomial hash for string keys (djb2 variant)

- **Linear Search Complexity**: O(n) - Must potentially examine every entry

- **Binary Search Complexity**: O(log n) - Logarithmic reduction of search space

- **Hash Table Lookup**: O(1) average case - Constant time with proper hash function and table size

## Key Points

- Dictionary files on Unix systems are typically located at `/usr/share/dict/words` and contain plain ASCII text with one word per line.

- Two primary approaches exist for reading dictionary files: system calls (open/read/close) offering direct kernel access without buffering, and standard I/O library (fopen/fgets/fread) providing buffered streams with easier interface.

- The fgets() function is particularly suitable for dictionary reading because dictionaries are line-oriented, returning each word along with its newline character.

- Binary search requires sorted dictionaries and random file access via fseek(), achieving O(log n) complexity compared to O(n) for linear search.

- Hash tables provide O(1) average-case lookup performance after O(n) preprocessing time to build the index, trading memory for speed.

- Memory-mapped I/O using mmap() allows efficient access to large dictionary files without loading entire files into RAM.

- Always handle file errors through proper return value checking and use perror() for descriptive error messages.

- Buffer size selection is critical: too small risks truncation, too large wastes memory; 256 bytes is sufficient for most English dictionary words.

## Common Mistakes

1. **Forgetting to remove newline characters**: After fgets() reads a line, the buffer contains the newline character. Failing to remove it causes string comparisons to fail unexpectedly.

2. **Not checking for NULL return**: fgets() returns NULL on error or end-of-file; failing to check this can cause programs to process invalid data or loop infinitely.

3. **Using wrong buffer size with fgets**: Passing sizeof(buffer) when buffer is a pointer (not an array) results in wrong size calculation; always pass the actual buffer capacity.

4. **Confusing file descriptors with FILE pointers**: System calls use file descriptors (integers), while standard I/O uses FILE pointers. Do not mix close() with fopen() results or fclose() with open() results.

5. **Ignoring memory leaks**: When using strdup() or malloc() for dictionary entries (e.g., in hash table construction), failing to free memory causes resource leaks.