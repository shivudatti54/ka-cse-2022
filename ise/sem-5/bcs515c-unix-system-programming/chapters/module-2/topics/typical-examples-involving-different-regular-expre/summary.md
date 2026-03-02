## Typical Examples Involving Different Regular Expressions

### UNIX SYSTEM PROGRAMMING - FILE ATTRIBUTES AND PERMISSIONS

#### Key Concepts

- **Regular Expressions (Regex)**: Patterns used to match character combinations in strings.
- **Pattern Matching**: Finding occurrences of a pattern within a string.
- **Modifiers**: Prepend to a regex pattern to change its behavior.

#### Examples

- **Matching**: Find all words containing the letter "e" in a string.
  - Pattern: `\w*e`
  - Regex engine: Finds all words that contain at least one "e".
- **Repeating Patterns**: Match a pattern zero or more times.
  - Pattern: `a*b`
  - Regex engine: Matches any string that starts with zero or more "a"s followed by zero or more "b"s.
- **Word Boundaries**: Match a pattern only when it's a whole word.
  - Pattern: `\bthe\b`
  - Regex engine: Matches the word "the" as a whole word, not part of another word.
- **Negation**: Match a pattern that doesn't match any characters.
  - Pattern: `[^\w]`
  - Regex engine: Matches any character that's not a word character.
- **Character Classes**: Match a pattern that includes a set of characters.
  - Pattern: `[abc]`
  - Regex engine: Matches any of the characters "a", "b", or "c".

#### Important Formulas, Definitions, Theorems

- **Regex Engine Evaluation**: The order of operations depends on the regex engine, but typically involves:
  1. Literal characters match literally.
  2. Special characters match their defined patterns.
  3. Groups match recursively.
  4. Quantifiers (e.g., `*`, `+`, `?`) match the preceding pattern zero or more times.

Note: This summary covers a limited set of regex concepts and examples. For a comprehensive understanding, refer to official regex documentation and online resources.
