# **The Shells Interpretive Cycle: Wild Cards**

### Key Points

- **Glob Pattern**: A pattern that matches files and directories.
- **Globbing**: The process of using glob patterns to match files and directories.
- **Pattern Expansion**: The process of substituting glob patterns into the command.

### Important Formulas and Definitions

- **Pattern Matching**: A process of matching a string against a pattern using regular expressions.
- **Wild Card Characters**: \*., ?, [, ] used to match files and directories.

### Theorems and Concepts

- **Distributive Law**: `(a . b) * c = (a * c) . (b * c)`
- **Associative Law**: `a * (b * c) = (a * b) * c`

### Important Commands

- `*` - matches any characters (including none)
- `?` - matches a single character
- `[seq]` - matches any character in the sequence
- `[seq!]` - matches any character not in the sequence

### Example Use Cases

- `ls -l *.txt` - lists all files with .txt extension
- `rm *.py` - removes all files with .py extension

### Quick Revision Tips

- Memorize common glob patterns and their meanings.
- Practice using glob patterns in different commands.
- Understand the distributive and associative laws of globbing.
