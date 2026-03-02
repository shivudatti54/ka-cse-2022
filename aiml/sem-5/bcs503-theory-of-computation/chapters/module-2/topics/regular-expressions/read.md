# Regular Expressions with grep

## Introduction to Regular Expressions

Regular expressions (regex) are powerful pattern-matching sequences used to search, filter, and manipulate text. In Unix/Linux systems, they form an essential tool for text processing and are extensively used with commands like `grep`, `sed`, and `awk`.

A regular expression is a sequence of characters that defines a search pattern. Think of it as an advanced version of wildcard matching but with much more precision and flexibility.

**Basic Concept:**

```
Pattern: '^hello.*world$'
Text:   'hello beautiful world'
Match:  ✓ (entire string matches)
```

## The grep Command

`grep` (Global Regular Expression Print) is one of the most fundamental Unix commands for searching text. It searches for patterns in files or input streams and prints lines containing matches.

**Basic Syntax:**

```bash
grep [options] pattern [file...]
```

**Common Options:**

- `-i`: Ignore case distinctions
- `-v`: Invert match (show non-matching lines)
- `-n`: Show line numbers
- `-c`: Count matching lines
- `-l`: List files with matches
- `-r`: Recursive search

## Basic Regular Expressions (BRE)

Basic regular expressions are the fundamental pattern matching constructs supported by standard `grep`.

### Literal Characters

Most characters match themselves literally:

- `grep 'hello' file.txt` → Finds lines containing "hello"

### Special Characters (Metacharacters)

These characters have special meaning in regex:

```
. ^ $ [ ] * \ + ? { } | ( )
```

### Common BRE Patterns

**1. The Dot (.)**
Matches any single character except newline:

- `grep 'a.c' file` → Matches "abc", "a c", "a-c"

**2. Character Classes ([ ])**
Match any one character from a set:

- `grep '[aeiou]' file` → Lines containing vowels
- `grep '[A-Z]' file` → Lines with uppercase letters
- `grep '[0-9]' file` → Lines with digits

**Negated Character Class ([^ ]):**

- `grep '[^0-9]' file` → Lines containing non-digit characters

**3. Anchors**

- `^` → Start of line: `grep '^Hello' file`
- `$` → End of line: `grep 'end$' file`
- `^$` → Empty lines

**4. Asterisk (\*)**
Matches zero or more occurrences of the preceding character:

- `grep 'ab*c' file` → Matches "ac", "abc", "abbc", etc.

## Extended Regular Expressions (ERE) with egrep

Extended regular expressions provide additional metacharacters and capabilities, accessible via `grep -E` or `egrep`.

### Additional ERE Metacharacters

**1. Plus (+)**
Matches one or more occurrences:

- `egrep 'ab+c' file` → Matches "abc", "abbc" but not "ac"

**2. Question Mark (?)**
Matches zero or one occurrence:

- `egrep 'ab?c' file` → Matches "ac" or "abc"

**3. Alternation (|)**
Matches either pattern:

- `egrep 'cat|dog' file` → Lines containing "cat" or "dog"

**4. Grouping ( )**
Groups patterns together:

- `egrep '(ab)+' file` → Matches "ab", "abab", etc.

**5. Range Repetition ({ })**
Specifies exact repetition counts:

- `egrep 'a{3}' file` → Matches "aaa"
- `egrep 'a{2,4}' file` → Matches "aa", "aaa", "aaaa"
- `egrep 'a{2,}' file` → Matches two or more "a"s

## Practical Examples and Use Cases

### 1. Searching for Specific Patterns

```bash
# Find email addresses
egrep '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' file.txt

# Find phone numbers (US format)
egrep '\([0-9]{3}\) [0-9]{3}-[0-9]{4}' file.txt
```

### 2. Filtering Command Output

```bash
# Show running processes except grep itself
ps aux | grep '[a]pache'  # Clever trick to exclude grep from results

# Find files containing specific pattern
grep -r 'function_name' /path/to/code/
```

### 3. System Administration Tasks

```bash
# Check for error messages in log files
grep -i 'error' /var/log/syslog

# Find users with shell access
grep '/bin/bash$' /etc/passwd
```

## Comparison: BRE vs ERE

| Feature          | Basic RE (grep)   | Extended RE (egrep) |
| ---------------- | ----------------- | ------------------- | --- | --- |
| `+` quantifier   | `\+` (escaped)    | `+`                 |
| `?` quantifier   | `\?` (escaped)    | `?`                 |
| `                | ` alternation     | `\|` (escaped)      | `   | `   |
| `{ }` quantifier | `\{ \}` (escaped) | `{ }`               |
| `( )` grouping   | `\( \)` (escaped) | `( )`               |

## ASCII Diagram: grep Processing Flow

```
Input Source
    │
    ▼
[ File or STDIN ]
    │
    ▼
[ Read Line by Line ]
    │
    │
    ▼                      No
[ Apply Regex Pattern ] ────→ [ Discard Line ]
    │
    Yes
    │
    ▼
[ Perform Action ] → Print/Count/List
    │
    ▼
[ Output Result ]
```

## Common Regex Patterns Reference Table

| Pattern  | Meaning                  | Example Matches              |
| -------- | ------------------------ | ---------------------------- | ---- | --------------------- |
| `^`      | Start of line            | `^hello` → "hello world"     |
| `$`      | End of line              | `world$` → "hello world"     |
| `.`      | Any single character     | `a.c` → "abc", "a c"         |
| `*`      | Zero or more of previous | `ab*c` → "ac", "abc", "abbc" |
| `[abc]`  | Any of a, b, or c        | `[aeiou]` → vowels           |
| `[^abc]` | Not a, b, or c           | `[^0-9]` → non-digits        |
| `[a-z]`  | Any lowercase letter     | `[a-z]` → "a" to "z"         |
| `\`      | Escape character         | `\.` → literal dot           |
| `+`      | One or more (ERE)        | `a+` → "a", "aa", "aaa"      |
| `?`      | Zero or one (ERE)        | `a?b` → "b", "ab"            |
| `        | `                        | Alternation (ERE)            | `cat | dog` → "cat" or "dog" |

## Exam Tips

1. **Remember the difference** between BRE and ERE metacharacters. BRE requires escaping for `+`, `?`, `{`, `}`, `|`, `(`, and `)`.

2. **Anchors are crucial**: `^` for start of line, `$` for end of line. They don't match characters but positions.

3. **Character classes** `[ ]` match only one character from the set. Use `[0-9]` instead of `[0-9]+` if you want to match just one digit.

4. **The dot (.)** matches any single character except newline. To match a literal dot, escape it: `\.`

5. **For complex patterns**, use extended regular expressions (`grep -E` or `egrep`) as they're more readable and powerful.

6. **Practice common patterns** like email matching, phone numbers, and IP addresses as these are frequently tested.

7. **Use `grep -v`** to invert matches when you need to exclude certain patterns.

8. **Combine grep with other commands** using pipes for powerful text processing pipelines.
