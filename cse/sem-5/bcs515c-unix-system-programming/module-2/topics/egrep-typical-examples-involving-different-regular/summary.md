# Egrep and Regular Expressions - Summary

## Key Definitions and Concepts

- **Egrep**: Extended grep command that supports extended regular expressions with metacharacters like `+`, `?`, `|`, and `()`
- **Regular Expression**: A pattern that describes text to be matched
- **Metacharacters**: Special characters with specific meanings in regex (`.`, `*`, `+`, `?`, `^`, `$`, `[]`, `|`, `()`)
- **Character Class**: A set of characters enclosed in `[]` to match any single character from the set
- **Quantifiers**: Specify how many times a pattern should match (`{n}`, `{n,}`, `{n,m}`)
- **Anchors**: `^` for beginning of line, `$` for end of line
- **Backreference**: `\1`, `\2` referring to previously captured groups

## Important Formulas and Theorems

| Pattern | Meaning                  |
| ------- | ------------------------ |
| `.`     | Any single character     |
| `*`     | Zero or more occurrences |
| `+`     | One or more occurrences  |
| `?`     | Zero or one occurrence   |
| `^`     | Start of line            |
| `$`     | End of line              |
| `[]`    | Character class          |
| `[^]`   | Negated character class  |
| `\|`    | Alternation (OR)         |
| `()`    | Grouping                 |
| `\b`    | Word boundary            |
| `{n}`   | Exactly n times          |

## Key Points

- Egrep is invoked with `egrep` or `grep -E` in modern systems
- Extended regex supports `+`, `?`, `|`, `()` without escaping (unlike basic grep)
- Character classes like `[[:alpha:]]`, `[[:digit:]]` are portable across locales
- Use `\` to escape special characters when matching literally
- Backreferences (`\1`, `\2`) refer to captured groups in the same pattern
- Word boundaries (`\b`) prevent partial word matches
- The `-i` flag makes search case-insensitive

## Common Mistakes to Avoid

1. Forgetting to escape special characters when searching for literal symbols
2. Confusing basic grep and extended grep metacharacter requirements
3. Not using anchors (`^`, `$`) when full-line matching is required
4. Incorrect quantifier usage leading to overly greedy matches
5. Not using word boundaries when matching complete words

## Revision Tips

1. Practice writing patterns for common validations (email, phone, IP)
2. Use online regex testers to visualize pattern matching
3. Remember: `.` does not match newline by default
4. Group related patterns with parentheses for clarity
5. Test patterns with `egrep` on sample files before using in scripts
