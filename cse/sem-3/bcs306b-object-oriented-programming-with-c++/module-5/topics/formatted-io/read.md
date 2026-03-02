# Formatted Input/Output in C++

## Introduction

Formatted Input/Output (I/O) is a fundamental aspect of C++ programming that allows developers to control how data is displayed and read. The iostream library provides two primary streams: `cin` for input and `cout` for output, along with `cerr` and `clog` for error handling. Beyond basic stream operations, C++ offers powerful formatting capabilities through manipulators, format flags, and member functions that enable precise control over how numbers, strings, and other data types appear on the console or in files.

In object-oriented programming with C++, understanding formatted I/O is essential for creating user-friendly applications, generating reports, debugging programs, and handling file operations effectively. The 2022 the scheme emphasizes these concepts as they form the backbone of interactive C++ applications. This topic covers both the traditional C-style printf/scanf approaches and the modern C++ stream-based formatting, with emphasis on the latter as it integrates seamlessly with OOP principles through operator overloading and stream classes.

## Key Concepts

### 1. Stream Classes Hierarchy

C++ I/O is implemented through a hierarchy of classes. The base class `ios_base` provides common functionality, while `ios` adds formatting state and error handling. The `istream` class handles input operations, and `ostream` handles output. The `iostream` class combines both. Key derived classes include `ifstream` (file input), `ofstream` (file output), and `fstream` (file I/O).

### 2. Format Flags and Format State

The `ios_base` class maintains a format state through flags stored in a `fmtflags` bitmask. These flags control various formatting options:

- **boolalpha/noboolalpha**: Controls boolean output as "true"/"false" or "1"/"0"
- **hex/oct/dec**: Sets numeric base for integer output (hexadecimal, octal, decimal)
- **showbase/noshowbase**: Shows/hides base prefix (0x for hex, 0 for octal)
- **showpoint/noshowpoint**: Shows/hides decimal point for floating-point
- **showpos/noshowpos**: Shows/hides positive sign for positive numbers
- **uppercase/nouppercase**: Controls uppercase/lowercase for hex letters and scientific notation
- **scientific/fixed**: Controls floating-point notation style
- **left/right/internal**: Controls alignment with padding characters

Format flags are set using the `setf()` and `unsetf()` member functions, or the `flags()` function that returns the previous flags.

### 3. Stream Manipulators

Manipulators are special functions that can be inserted into or extracted from streams to modify their behavior. They provide a cleaner syntax than direct function calls.

**No-argument Manipulators (in `<ios>`)**:

- `endl`: Outputs newline and flushes the stream
- `ends`: Outputs null character
- `flush`: Flushes the stream
- `ws`: Extracts whitespace characters

**Integer Base Manipulators**:

- `dec`, `oct`, `hex`: Set integer base

**Floating-Point Manipulators**:

- `scientific`, `fixed`, `defaultfloat`: Control floating-point notation

**Alignment and Padding Manipulators**:

- `left`, `right`, `internal`: Set alignment
- `setfill(ch)`: Set fill character
- `setw(n)`: Set field width (applies to next output/input only)

**Boolean Manipulators**:

- `boolalpha`, `noboolalpha`: Boolean text format

**Numeric Base Display**:

- `showbase`, `noshowbase`: Show/hide base prefix
- `showpoint`, `noshowpoint`: Show/hide decimal point
- `showpos`, `noshowpos`: Show/hide positive sign

### 4. Parameterized Manipulators

The `<iomanip>` header provides manipulators that take arguments:

- `setbase(base)`: Set integer base (8, 10, or 16)
- `setw(width)`: Set field width
- `setfill(ch)`: Set fill character
- `setprecision(precision)`: Set precision for floating-point
- `setiosflags(mask)`: Set multiple flags
- `resetiosflags(mask)`: Clear multiple flags

### 5. Member Functions for Formatting

Beyond manipulators, stream objects provide member functions:

- `width()`: Get/set field width
- `precision()`: Get/set precision
- `fill()`: Get/set fill character
- `rdstate()`, `setstate()`, `clear()`: Error state management
- `good()`, `eof()`, `fail()`, `bad()`: Check stream state
- `tie()`: Manage stream synchronization

### 6. User-Defined Manipulators

Programmers can create custom manipulators by implementing either:

**Simple output manipulators**:

```cpp
ostream& manipulator(ostream& os) {
 // Perform operations
 return os;
}
```

**Parameterized manipulators**:

```cpp
// Class for parameterized manipulator
class SetWidth {
 int width;
public:
 SetWidth(int w) : width(w) {}
 friend ostream& operator<<(ostream& os, const SetWidth& sw) {
 os.width(sw.width);
 return os;
 }
};
```

## Examples

### Example 1: Basic Number Formatting

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
 int num = 255;
 double value = 123.456789;

 cout << "Default: " << num << endl;
 cout << "Hex: " << hex << num << endl;
 cout << "Octal: " << oct << num << endl;
 cout << "Decimal (back): " << dec << num << endl;

 cout << "\nWith showbase:" << endl;
 cout << showbase;
 cout << hex << num << endl;
 cout << oct << num << endl;
 cout << dec << num << endl;
 cout << noshowbase;

 cout << "\nFloating point:" << endl;
 cout << "Default: " << value << endl;
 cout << fixed << setprecision(2) << value << endl;
 cout << scientific << value << endl;

 return 0;
}
```

**Output**:

```
Default: 255
Hex: ff
Octal: 377
Decimal (back): 255

With showbase:
0xff
0377
255

Floating point:
123.457
123.46
1.234568e+02
```

### Example 2: Field Width and Alignment

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
 // Set field width and alignment
 cout << "--- Field Width Demonstration ---" << endl;

 cout << setw(10) << 42 << endl; // Right-aligned (default)
 cout << left << setw(10) << 42 << endl; // Left-aligned
 cout << right; // Reset to right

 cout << "\n--- Table Format ---" << endl;
 cout << setw(10) << "Name" << setw(10) << "Age" << setw(10) << "Score" << endl;
 cout << setw(10) << "Alice" << setw(10) << 25 << setw(10) << 95.5 << endl;
 cout << setw(10) << "Bob" << setw(10) << 30 << setw(10) << 87.3 << endl;

 cout << "\n--- Fill Character ---" << endl;
 cout << setfill('*') << setw(15) << 42 << endl;
 cout << left << setw(15) << "Hello" << endl;
 cout << setfill(' '); // Reset fill

 return 0;
}
```

**Output**:

```
--- Field Width Demonstration ---
 42
42
--- Table Format ---
 Name Age Score
 Alice 25 95.5
 Bob 30 87.3
--- Fill Character ---
*************42
Hello*********
```

### Example 3: Precision and Combined Formatting

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
 double pi = 3.14159265358979;
 double numbers[] = {1.5, 2.75, 3.0};

 cout << "--- Precision Control ---" << endl;
 cout << "Default precision: " << pi << endl;
 cout << "Precision 2: " << setprecision(2) << pi << endl;
 cout << "Precision 5: " << setprecision(5) << pi << endl;

 cout << "\n--- Fixed Point ---" << endl;
 cout << fixed;
 cout << setprecision(2) << pi << endl;
 cout << setprecision(4) << pi << endl;

 cout << "\n--- Combined Formatting ---" << endl;
 cout.unsetf(ios::fixed); // Reset
 cout << hex << showbase;
 cout << "Integer: " << setw(10) << setfill('0') << 255 << endl;

 cout << "\n--- Boolean Formatting ---" << endl;
 bool flag = true;
 cout << "Default: " << flag << endl;
 cout << boolalpha << flag << " / " << !flag << endl;
 cout << noboolalpha;

 return 0;
}
```

**Output**:

```
--- Precision Control ---
Default precision: 3.1416
Precision 2: 3.1
Precision 5: 3.1416
--- Fixed Point ---
3.14
3.1416
--- Combined Formatting ---
Integer: 0000000xff
--- Boolean Formatting ---
Default: 1
true / false
```

## Exam Tips

1. **Manipulators vs Member Functions**: Remember that `setw()` only affects the next I/O operation, while `setprecision()`, `setfill()`, and alignment settings persist until changed.

2. **Base Manipulators Persistence**: Unlike `setw()`, the `hex`, `oct`, and `dec` manipulators are sticky—they remain in effect until changed again. Always remember to reset to `dec` when needed.

3. **Precision Meaning**: In default (non-fixed) mode, precision sets the total number of significant digits. In fixed mode, it sets the number of digits after the decimal point.

4. **Fill Character Persistence**: The fill character persists across operations, unlike width. Always reset fill to space when done.

5. **ios::fmtflags Type**: The format flags are stored in `ios::fmtflags` type. Use `setf()` with specific flags and `unsetf()` to clear them.

6. **include Headers**: Remember that basic manipulators like `endl`, `hex` are in `<iostream>` or `<ios>`, while parameterized manipulators like `setprecision()` are in `<iomanip>`.

7. **User-Defined Manipulators**: For custom manipulators, always return the stream reference (`ostream&` or `istream&`) to allow chaining.

8. **Stream State Checking**: Always check stream state using `fail()` or `!stream` before processing input to handle invalid data gracefully.

9. **File I/O with Formatting**: The same formatting manipulators work with file streams (`ofstream`, `ifstream`) as with console streams (`cout`, `cin`).

10. **Synchronization**: Use `ios::sync_with_stdio(false)` to unsync C and C++ I/O for better performance, but do this before any I/O operations.
