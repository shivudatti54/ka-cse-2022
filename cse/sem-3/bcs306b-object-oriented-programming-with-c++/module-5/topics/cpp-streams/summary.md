# C++ Streams and File I/O - Summary

## Key Definitions and Concepts

- **Stream**: An abstraction representing a sequence of bytes that can be read from or written to, providing a uniform interface for I/O operations regardless of the underlying data source.

- **Stream Buffer**: The underlying mechanism managed by `streambuf` classes that actually stores and transfers characters between the program and the data source.

- **File Stream**: A stream associated with a file on disk, managed by `ifstream` (input), `ofstream` (output), and `fstream` (bidirectional).

- **String Stream**: In-memory streams using `stringstream`, `istringstream`, and `ostringstream` for string manipulation and type conversion.

- **Stream Manipulator**: Special functions (like `endl`, `setw`, `setprecision`) that modify stream formatting when inserted or extracted.

## Important Formulas and Theorems

- File opening: `stream.open(filename, mode)` - mode is a combination of `ios::in`, `ios::out`, `ios::app`, `ios::trunc`, `ios::binary`, `ios::ate`

- Stream state checking: `stream.good()`, `stream.eof()`, `stream.fail()`, `stream.bad()` - all return boolean values

- String conversion: `ostringstream oss; oss << value; string s = oss.str();`

- Field width: `setw(n)` sets minimum width for next insertion only; `setfill(c)` sets fill character

## Key Points

- C++ streams follow an object-oriented class hierarchy with `ios_base` as the root

- Standard streams: `cin` (stdin), `cout` (stdout), `cerr` (stderr unbuffered), `clog` (stderr buffered)

- File modes determine how files are opened and must be chosen based on read/write/append requirements

- Always verify file open success using `is_open()` or stream object testing

- String streams enable safe type conversion without C-style atoi/itoa functions

- `endl` flushes the buffer; use `"\n"` for better performance in loops

- Stream manipulators like `hex`, `oct`, `dec` persist until changed, while `setw` applies only once

- Unformatted I/O (get, getline, read, write) provides direct character access without parsing

## Common Mistakes to Avoid

1. **Not checking file open status**: Always verify the file opened successfully before attempting I/O operations.

2. **Using endl unnecessarily**: Using `endl` in loops causes performance issues due to repeated buffer flushing.

3. **Forgetting to change number base**: Once `std::hex` or similar is set, it remains until explicitly changed back to `std::dec`.

4. **Incorrect file modes**: Opening with wrong mode (e.g., trying to read from ofstream without ios::in) causes failures.

5. **Not including required headers**: Remember `<fstream>` for file streams, `<sstream>` for string streams, and `<iomanip>` for manipulators.

## Revision Tips

1. Practice writing code to open, read, write, and close files in different modes

2. Memorize the stream class hierarchy and which header each class belongs to

3. Write example programs converting between strings and numbers using string streams

4. Review all stream manipulators and their effects on output formatting

5. Understand the difference between recoverable (fail) and fatal (bad) stream errors
