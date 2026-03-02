# Formatted Input/Output in C++ - Summary

## Key Definitions and Concepts

- **Stream**: An abstraction representing a sequence of bytes flowing from a source (input) or to a destination (output)
- **Manipulator**: Special functions that can be inserted into or extracted from streams to modify formatting behavior
- **Format Flags**: Bitmask values in ios_base that control various formatting options
- **Sticky Manipulators**: Formatting settings that persist until explicitly changed (precision, alignment)
- **Non-Sticky Manipulators**: Settings that apply only to the next I/O operation (setw)

## Important Formulas and Theorems

| Manipulator                 | Purpose                 | Sticky? |
| --------------------------- | ----------------------- | ------- |
| `hex`, `oct`, `dec`         | Integer base            | Yes     |
| `scientific`, `fixed`       | Floating-point notation | Yes     |
| `setprecision(n)`           | Digits of precision     | Yes     |
| `setw(n)`                   | Field width             | No      |
| `setfill(ch)`               | Fill character          | Yes     |
| `left`, `right`, `internal` | Alignment               | Yes     |
| `boolalpha`, `noboolalpha`  | Boolean format          | Yes     |
| `showbase`, `noshowbase`    | Base prefix             | Yes     |

## Key Points

- The iostream library provides cin (input), cout (output), cerr and clog (error) streams
- Format flags are managed through setf(), unsetf(), and flags() member functions
- Parameterized manipulators require the `<iomanip>` header
- setw() only affects the immediately following output operation
- In default mode, precision controls significant digits; in fixed mode, it controls decimal places
- User-defined manipulators must return the stream reference for chaining
- Always check stream state (fail(), eof()) before processing input
- File streams (ifstream, ofstream) support the same formatting as console streams

## Common Mistakes to Remember

1. **Forgetting to reset setw()**: Unlike alignment, width doesn't persist—don't assume it applies to all subsequent outputs
2. **Confusing precision modes**: Remember that precision meaning changes between default and fixed notation
3. **Not resetting base**: Forgetting to switch back to dec after using hex or oct
4. **Missing headers**: Using parameterized manipulators without including <iomanip>
5. **Not checking input validity**: Always verify stream state after extraction operations

## Revision Tips

1. Practice writing programs that format tables with proper alignment and headers
2. Memorize which manipulators are sticky vs non-sticky
3. Remember that endl outputs newline AND flushes—use '\n' when flushing isn't needed
4. Review the stream class hierarchy: ios_base → ios → istream/ostream → iostream
5. Create a reference table of common manipulators for quick review before exams
