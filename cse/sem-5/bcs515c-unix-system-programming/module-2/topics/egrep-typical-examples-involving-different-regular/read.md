# Egrep and Regular Expressions - Typical Examples

## Introduction

Egrep (extended grep) is a powerful command-line utility in Unix/Linux systems used for searching text using extended regular expressions. It is an essential tool for text processing, pattern matching, and data extraction in system administration, software development, and data analysis. Unlike the basic grep command, egrep supports extended regular expression metacharacters, making it more versatile for complex pattern matching.

In the context of 's Computer Science and Engineering curriculum, understanding egrep and regular expressions is crucial for courses like Unix Programming, Shell Scripting, and Data Analytics. These tools are widely used in real-world scenarios such as log file analysis, text parsing, validation of user inputs, and searching through large codebases. This module covers the fundamental concepts of regular expressions and demonstrates practical examples using egrep to solve common text processing problems.

## Key Concepts

### What is Egrep?

Egrep stands for "Extended Grep" and is invoked using the command `egrep`. It interprets patterns as extended regular expressions, which include all basic regular expression metacharacters plus additional ones like `+`, `?`, `|`, and parentheses for grouping. In modern systems, `grep -E` is often used as a replacement for egrep, as it provides the same functionality.

### Basic Metacharacters in Egrep

1. **Dot (.)** - Matches any single character except newline
2. **Asterisk (\*)** - Matches zero or more occurrences of the preceding character
3. **Plus (+)** - Matches one or more occurrences of the preceding character
4. **Question Mark (?)** - Matches zero or one occurrence of the preceding character
5. **Caret (^)** - Matches the beginning of a line
6. **Dollar Sign ($)** - Matches the end of a line
7. **Square Brackets []** - Matches any character within the brackets
8. **Pipe (|)** - Alternation - matches either the expression before or after the pipe
9. **Parentheses ()** - Groups expressions together
10. **Backslash (\)** - Escapes special characters

### Character Classes

- `[abc]` - Matches any character: a, b, or c
- `[^abc]` - Matches any character except a, b, or c
- `[a-z]` - Matches any lowercase letter
- `[A-Z]` - Matches any uppercase letter
- `[0-9]` - Matches any digit
- `[[:alpha:]]` - Matches any alphabetic character
- `[[:digit:]]` - Matches any digit
- `[[:space:]]` - Matches any whitespace character

### Quantifiers

- `{n}` - Matches exactly n occurrences
- `{n,}` - Matches n or more occurrences
- `{n,m}` - Matches between n and m occurrences

## Examples

### Example 1: Finding Lines Starting with a Specific Pattern

**Problem:** Find all lines in a file that start with "Error" or "WARNING".

**Solution:**

```bash
egrep '^(Error|WARNING)' logfile.txt
```

**Explanation:**

- `^` anchors the match to the beginning of the line
- `(Error|WARNING)` uses alternation to match either "Error" or "WARNING"
- This is useful for analyzing log files to identify error messages

### Example 2: Matching Phone Numbers in Specific Format

**Problem:** Find all valid phone numbers in the format XXX-XXX-XXXX (where X is a digit).

**Solution:**

```bash
egrep '[0-9]{3}-[0-9]{3}-[0-9]{4}' contact.txt
```

**Explanation:**

- `[0-9]{3}` matches exactly 3 digits
- The hyphens match literal hyphen characters
- This pattern can be used to extract phone numbers from text files

### Example 3: Finding Email Addresses

**Problem:** Extract all email addresses from a text file.

**Solution:**

```bash
egrep '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' data.txt
```

**Explanation:**

- `[A-Za-z0-9._%+-]+` matches the username part (letters, digits, and special characters)
- `@` matches the literal @ symbol
- `[A-Za-z0-9.-]+` matches the domain name
- `\.[A-Za-z]{2,}` matches the top-level domain (like .com, .org)

### Example 4: Finding Words with Specific Patterns

**Problem:** Find all words that contain exactly two consecutive vowels.

**Solution:**

```bash
egrep '[aeiou]{2}' words.txt
```

**Explanation:**

- `[aeiou]{2}` matches exactly two consecutive vowels
- This pattern is useful for linguistic analysis

### Example 5: IP Address Validation

**Problem:** Find and validate IPv4 addresses from a network log file.

**Solution:**

```bash
egrep '([0-9]{1,3}\.){3}[0-9]{1,3}' network.log
```

**Explanation:**

- `([0-9]{1,3}\.){3}` matches three octets followed by a period
- `[0-9]{1,3}` matches the fourth octet (0-999)
- Note: This doesn't validate that each octet is ≤255

### Example 6: Finding Lines with Repeated Words

**Problem:** Find lines containing repeated consecutive words (like "the the").

**Solution:**

```bash
egrep '\b(\w+)\s+\1\b' textfile.txt
```

**Explanation:**

- `\b` denotes word boundaries
- `(\w+)` captures a word
- `\s+` matches whitespace
- `\1` is a backreference to the first captured group
- This finds duplicate consecutive words

### Example 7: Extracting Dates in Various Formats

**Problem:** Find dates in DD-MM-YYYY or YYYY-MM-DD format.

**Solution:**

```
egrep '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])-[0-9]{4}|[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])' dates.txt
```

**Explanation:**

- The first part matches DD-MM-YYYY format with proper date validation
- The second part matches YYYY-MM-DD format
- `|` provides alternation between the two formats

## Exam Tips

1. **Remember the difference between basic and extended grep**: Egrep supports `+`, `?`, `|`, and `()` without escaping, while basic grep requires them to be escaped.

2. **Practice with real-world patterns**: Common exam questions involve validating emails, phone numbers, IP addresses, and dates.

3. **Understand anchoring**: `^` and `$` are crucial for line-level matching. Don't forget them when searching for complete patterns.

4. **Use character classes wisely**: Instead of `[abc]`, use `[[:alpha:]]` for broader matching in exams.

5. **Remember backreferences**: The `\1`, `\2` notation references previously matched groups and is a common exam topic.

6. **Escape special characters**: When searching for literal characters like `.`, `*`, or `+`, remember to escape them with `\.`, `\*`, `\+`.

7. **Practice case-insensitive search**: Use the `-i` flag with egrep for case-insensitive matching, which is often required in real applications.
