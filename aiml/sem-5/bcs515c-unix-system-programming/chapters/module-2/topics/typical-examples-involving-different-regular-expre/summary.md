# **Typical Examples Involving Different Regular Expressions**

## **Introduction**

Regular expressions (regex) are a powerful tool for pattern matching in strings. Here are some key points to help you revise:

### Basic Concepts

- **Regex Patterns**: A sequence of characters that define a search pattern.
- **Match**: A location in a string where the regex pattern is found.
- **Group**: A part of a regex pattern that can be referenced later.

### Common Regex Patterns

- **Literal Characters**: `.` (any character), `^` (start of string), `$` (end of string)
- **Character Classes**: `[abc]` (any of the characters in the brackets), `\d` (any digit), `\w` (any word character)
- **Quantifiers**: `*` (zero or more occurrences), `+` (one or more occurrences), `{n}` (exactly n occurrences)
- **Metacharacters**: `|` (or), `(`, `)` (grouping), `?` (optional)

### Examples

- **Matching a Phone Number**: `\d{3}-\d{3}-\d{4}`
- **Matching an Email Address**: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- **Matching a Username**: `[a-zA-Z0-9]+`

### Regex Operators

- **Prefix**: `^` (start of string), `$` (end of string)
- **Suffix**: `\b` (word boundary)
- **Modifier**: `(?=...)` (positive lookahead), `(?<=...)` (positive lookbehind)

### Important Formulas, Definitions, and Theorems

- **Regular Expression Syntax**: `^regex` (search for the regex pattern)
- **Regex Engine**: A software component that interprets the regex pattern and matches it against a string.
- **The Regular Expression Theorem**: A fundamental theorem that describes the properties of regular expressions.

### Practice Questions

- Match the following strings using the regex pattern `\d{3}-\d{3}-\d{4}`: `123-456-7890`, `1234567890`, `123-456-7891`
- Write a regex pattern to match a password with at least 8 characters, one uppercase letter, one lowercase letter, and one digit.
