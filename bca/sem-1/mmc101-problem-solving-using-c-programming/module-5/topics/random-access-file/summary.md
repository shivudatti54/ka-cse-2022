# Random Access File - Summary

## Key Definitions and Concepts

- **Random Access File**: A file organization method that allows direct access to any record without having to read all preceding records, using the file position indicator.
- **File Position Indicator**: An internal maintained by C that tracks the current location in a file from which the next read or write operation will occur.
- **Fixed-Length Records**: Records of uniform size enabling calculation of any record's position using the formula: position = record_number × record_size.
- **Binary Mode**: File opening mode with "b" flag that prevents newline translation and ensures predictable byte offsets for random access.

## Important Formulas and Theorems

- **fseek(stream, offset, whence)**: Repositions file pointer
  - whence = SEEK_SET (0): offset from beginning
  - whence = SEEK_CUR (1): offset from current position
  - whence = SEEK_END (2): offset from end of file
  
- **Record Position Calculation**: byte_position = record_index × sizeof(record_structure)

- **File Size Calculation**: file_size = ftell(file_pointer) after fseek(fp, 0, SEEK_END)

## Key Points

- Random access files enable O(1) access to any record compared to O(n) for sequential access.

- Always use binary mode ("rb", "wb", "r+b") for random access operations to avoid newline translation issues.

- fseek() returns 0 on success and non-zero on failure; always check return values in exam solutions.

- ftell() returns long int to handle large files; avoid using int for file positions.

- The "r+b" mode allows both reading and writing, essential for updating existing records.

- rewind() not only resets position to beginning but also clears EOF and error indicators.

- Offset can be negative when using SEEK_CUR (moving backwards) but typically non-negative with SEEK_END.

- After fread() or fwrite(), the position indicator advances automatically by the number of bytes transferred.

## Common Mistakes to Avoid

- Using text mode instead of binary mode, causing unexpected offset calculations due to newline translations.

- Forgetting that record indices are zero-based; the first record is at position 0, not 1.

- Not checking if fopen() returns NULL before performing file operations, leading to segmentation faults.

- Using int instead of long for file position calculations, causing overflow in large files.

- Attempting negative offsets with SEEK_SET, which is invalid and causes undefined behavior.

## Revision Tips

- Practice writing small programs that create, read, update, and delete records at random positions.

- Memorize the three whence values and their meanings for fseek() calls.

- Understand the relationship between sizeof() structures and record positioning calculations.

- Review past DU exam questions on file handling to understand the question patterns and marking scheme.

- Create a flowchart of the sequence: open file → seek to position → read/write → close file.