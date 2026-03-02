# Applications of Regular Expressions - Summary

## Key Definitions and Concepts

- **Regular Expression (Regex)**: A sequence of characters defining a search pattern for matching strings based on specific rules.

- **Metacharacters**: Special characters with reserved meanings in regex: `. ^ $ * + ? \ [ ] { } ( ) |`

- **Character Class**: A set of characters enclosed in square brackets `[]` that matches any single character from that set.

- **Quantifiers**: Symbols specifying how many times an element should be matched: `*` (0+), `+` (1+), `?` (0 or 1), `{n,m}` (range).

- **Anchors**: Special characters matching positions: `^` (start), `$` (end), `\b` (word boundary).

- **Groups**: Expressions enclosed in parentheses that capture matched text for later use.

## Important Formulas and Patterns

- **Digit**: `\d` or `[0-9]`
- **Word character**: `\w` or `[a-zA-Z0-9_]`
- **Whitespace**: `\s`
- **Email**: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- **Phone**: `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`
- **Date (YYYY-MM-DD)**: `^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$`
- **URL**: `https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+`

## Key Points

1. Regular expressions provide a powerful mechanism for pattern matching in text processing.

2. The dot (`.`) metacharacter matches any single character except newline by default.

3. Character classes using ranges like `[a-z]` efficiently match categories of characters.

4. Anchors `^` and `$` ensure matches occur at string boundaries, preventing partial matches.

5. Greedy quantifiers match as much as possible; lazy quantifiers (with `?`) match the minimum.

6. Regular expressions are used in lexical analyzers for token identification in compilers.

7. Capturing groups allow extraction and later reference of matched substrings.

8. The backslash (`\`) is used to escape metacharacters when literal matching is needed.

9. Regular expressions follow precedence rules: parentheses > quantifiers > alternation.

10. Different programming languages have slightly varying regex implementations and escape requirements.

## Common Mistakes to Avoid

1. **Forgetting to escape special characters**: Using `.` instead of `\.` when matching a literal dot.

2. **Confusing `*` with `+`**: Using `*` when at least one occurrence is required (use `+`).

3. **Incorrect character class ranges**: Writing `[A-z]` instead of `[A-Z]` or `[a-z]` (includes non-letter characters).

4. **Not using anchors for complete matching**: Missing `^` and `$` allows partial string matches.

5. **Forgetting greedy behavior**: Not accounting for how greedy quantifiers can over-match in extraction scenarios.

## Revision Tips

1. Practice writing regex patterns for common validation scenarios (email, phone, date, URL).

2. Use online regex testers to visualize how patterns match different strings.

3. Memorize the three main shorthand character classes: `\d`, `\w`, `\s`.

4. Remember the regex precedence order when building complex patterns.

5. Review the connection between regular expressions and finite automata (NFA/DFA) for theory exam preparation.
