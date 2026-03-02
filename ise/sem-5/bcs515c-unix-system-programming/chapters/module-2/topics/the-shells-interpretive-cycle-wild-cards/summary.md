# **The Shells Interpretive Cycle: Wild Cards Revision Notes**

## **Key Points**

- The shells interpretive cycle involves the following steps:
  - Read the input
  - Break the input into tokens
  - Analyze the tokens
  - Execute the tokens
- Wild cards are used to match patterns in the input
- **Globbing Pattern**: A pattern that matches files or directories
- **Pattern Expansion**: Replacement of wild cards with actual file names

## **Globbing Pattern**

- **Built-in Patterns**:
  - `*` - matches any characters
  - `?` - matches any single character
  - `[seq]` - matches any character in seq
  - `[!seq]` - matches any character not in seq
  - `{seq}` - matches any character in seq
  - `{!seq}` - matches any character not in seq
- **Special Characters**:
  - `.` - matches any character except `/`
  - `[()` `]` - matches any character except the special character inside
  - `{}` - matches any character except the special character inside

## **Pattern Expansion**

- `*` matches any characters (e.g., `*` matches "hello", "world", etc.)
- `?` matches any single character (e.g., `?` matches "a", "b", etc.)
- `[seq]` matches any character in seq (e.g., `[a-z]` matches any lowercase letter)
- `[!seq]` matches any character not in seq (e.g., `[!a-z]` matches any character not a lowercase letter)
- `{seq}` matches any character in seq (e.g., `{a-z}` matches any lowercase letter)
- `{!seq}` matches any character not in seq (e.g., `{!a-z}` matches any character not a lowercase letter)

## **Example Formulas**

- `ls -l *.txt` matches all files with ".txt" extension
- `ls -l ??.txt` matches all files with any single character followed by ".txt" extension

## **Important Definitions**

- **Shell**: A program that reads and executes commands
- **Glob**: A pattern that matches files or directories
- **Pattern**: A sequence of characters that matches a file or directory
