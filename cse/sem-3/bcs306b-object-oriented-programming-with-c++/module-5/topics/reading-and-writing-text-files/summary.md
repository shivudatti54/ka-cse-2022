# Reading and Writing Text Files in C++ - Summary

## Key Definitions and Concepts

- **Stream:** An abstraction representing a sequence of bytes flowing from a source to a destination
- **ifstream:** Input file stream class used for reading from files (inherits from istream)
- **ofstream:** Output file stream class used for writing to files (inherits from ostream)
- **fstream:** File stream class providing both input and output capabilities (inherits from iostream)
- **File Opening Modes:** Flags specifying how a file should be opened (ios::in, ios::out, ios::app, ios::ate, ios::trunc, ios::binary)

## Important Formulas and Techniques

- Opening a file: `streamObject.open("filename", mode)`
- Checking if file opened: `streamObject.is_open()` returns boolean
- Reading with >>: `inFile >> variable` (whitespace-separated)
- Reading lines: `getline(inFile, stringVariable)`
- Reading characters: `inFile.get(charVariable)`
- Writing with <<: `outFile << data`
- Writing characters: `outFile.put(charVariable)`
- Closing file: `streamObject.close()`

## Key Points

1. Always include `<fstream>` header for file operations in C++
2. ifstream defaults to ios::in mode, ofstream defaults to ios::out|ios::trunc
3. ios::app opens file for appending - new data goes to end, existing data preserved
4. Use ios::binary for binary file operations; text mode is default
5. The extraction operator (>>) skips whitespace and stops at delimiters
6. getline() reads entire line including spaces, but discards newline character
7. Always verify file opening success with is_open() before operations
8. Files are automatically closed when stream objects go out of scope
9. while(stream >> var) is the standard pattern for reading entire file contents
10. fstream requires explicit mode specification (ios::in, ios::out, or both)

## Common Mistakes to Avoid

1. **Forgetting to include <fstream>:** Leads to compilation errors as stream classes are not defined
2. **Not checking if file opened:** Program continues blindly and fails silently without writing/reading data
3. **Using wrong mode:** Writing to a file opened with only ios::in causes failure
4. **Confusing >> with getline():** >> leaves newline in buffer causing unexpected behavior in subsequent reads
5. **Not closing files:** May result in data not being written to disk (buffer not flushed)

## Revision Tips

1. Practice opening files in different modes and observe the behavior with existing files
2. Write programs that copy files line-by-line and word-by-word to understand different read methods
3. Create a simple database application that stores and retrieves records using file I/O
4. Trace through code examples to understand the flow of data between variables and files
5. Remember: ifstream = input (reading), ofstream = output (writing), fstream = both
