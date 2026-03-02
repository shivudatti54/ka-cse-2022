# Printf Command - Summary

## Key Definitions

- **Format Specifier**: A `%` character followed by a conversion character that defines how an argument should be displayed
- **Escape Sequence**: A backslash character followed by a character that represents a special function (like newline or tab)
- **Field Width**: The minimum number of characters to occupy in the output
- **Precision**: The number of digits after the decimal point for floating-point numbers

## Important Formulas

- Basic syntax: `printf "format string" [arguments]`
- String output: `%s`
- Integer output: `%d` or `%i`
- Floating-point: `%f` or `%.nf` (n = decimal places)
- Hexadecimal: `%x` (lowercase) or `%X` (uppercase)
- Octal: `%o`
- Character: `%c`
- Literal percent: `%%`
- Newline: `\n`
- Tab: `\t`

## Key Points

1. `printf` does NOT automatically add a newline (unlike `echo`)
2. Format specifiers must match the number and type of arguments provided
3. The format string MUST be quoted to prevent shell interpretation
4. Field width can be specified as `%Nw` where N is the width
5. Use `%-Nw` for left-aligned output within the field
6. Precision for floating-point uses `%.Nf` notation
7. Escape sequences like `\n` must be within quoted format strings
8. Missing arguments cause undefined behavior or partial output

## Common Mistakes

1. **Forgetting `\n`**: Users often forget that printf doesn't add a newline, causing subsequent prompts to appear on the same line

2. **Unquoted format string**: Writing `printf Hello %s` instead of `printf "Hello %s"` causes word splitting issues

3. **Argument count mismatch**: Having more format specifiers than arguments, or vice versa, produces unexpected output

4. **Confusing with C printf()**: While similar, Unix printf command has differences in some options and behaviors

5. **Using wrong specifier for type**: Using `%d` for floating-point numbers or vice versa can cause data loss or incorrect output