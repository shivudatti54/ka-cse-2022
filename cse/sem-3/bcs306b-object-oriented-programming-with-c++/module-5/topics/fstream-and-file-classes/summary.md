# File Handling in C++ - Summary

## Key Definitions and Concepts

- **File Stream:** A sequence of bytes stored on secondary storage devices, enabling persistent data storage between program executions.

- **ifstream:** Input file stream class used for reading data from files, inherited from istream.

- **ofstream:** Output file stream class used for writing data to files, inherited from ostream.

- **fstream:** File stream class supporting both input and output operations, inherited from iostream.

- **File Mode Flags:** Parameters specifying how a file should be opened (ios::in, ios::out, ios::app, ios::ate, ios::trunc, ios::binary).

- **Streampos:** Data type returned by tellg() and tellp() representing the current position in the stream.

## Important Formulas and Theorems

- **File Position Calculation:** To access record n in a binary file: `offset = (n-1) * sizeof(record_type)`

- **Random Access:** file.seekg(offset, ios::beg) moves to offset bytes from beginning; file.seekp(offset, ios::cur) moves relative to current position.

- **EOF Detection:** while(file >> variable) is more reliable than while(!file.eof())

## Key Points

1. The `<fstream>` header provides three classes: ifstream, ofstream, and fstream for file operations.

2. Always check file opening success using is_open() before performing operations.

3. ofstream defaults to ios::out | ios::trunc, which overwrites existing files.

4. Use ios::app mode to append data without truncating existing content.

5. Binary mode (ios::binary) is essential for storing non-text data like structures.

6. read() and write() functions require reinterpret_cast<char\*> for non-char data types.

7. seekg() manipulates read pointer; seekp() manipulates write pointer.

8. Explicit close() ensures buffer flushing and resource release.

9. Destructors automatically close files but explicit closing is recommended.

10. File streams inherit from standard stream classes, supporting all stream operations.

## Common Mistakes to Avoid

1. **Forgetting to check file opening:** Always verify files opened successfully before I/O operations.

2. **Using wrong mode combinations:** Using ios::out without ios::app on non-existent files creates new files, but on existing files it truncates content.

3. **Not using binary mode for structures:** Text mode corrupts binary data in structures due to newline translation.

4. **Confusing seekg() and seekp():** Using the wrong function leads to unexpected pointer positions.

5. **Not using reinterpret_cast:** Forgetting cast when using read() with non-char types causes compilation errors.

## Revision Tips

1. Practice coding file opening using both constructor and open() methods to understand both approaches.

2. Write small programs to test each file mode flag individually to understand their effects.

3. Use debug prints to verify file pointer positions after seekg()/seekp() operations.

4. Review binary file operations with simple structures containing different data types.

5. Memorize the inheritance hierarchy: ifstream→istream, ofstream→ostream, fstream→iostream.
