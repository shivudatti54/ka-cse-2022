# Pipe, Basic and Extended Regular Expressions, and Grep

## Introduction

The Unix/Linux command line provides powerful text processing capabilities through the combination of pipes, regular expressions, and the grep family of tools. These concepts form the backbone of text manipulation and pattern matching in Unix-like operating systems, which are essential skills for any Computer Science engineer.

A **pipe** (represented by the vertical bar `|`) is a mechanism that allows the output of one command to be used as input for another command. This enables the chaining of multiple commands to perform complex operations without creating intermediate files. The pipe operator is fundamental to the Unix philosophy of designing small, focused programs that can be combined to accomplish sophisticated tasks.

**Regular expressions** (regex) are powerful pattern matching tools used to search, match, and manipulate text. They provide a concise and flexible means of specifying search patterns. Unix supports two variants: **Basic Regular Expressions (BRE)** and **Extended Regular Expressions (ERE)**. BRE is the default syntax used by the traditional grep command, while ERE provides additional metacharacters and is used by egrep and modern grep with the -E flag.

**Grep** (Global Regular Expression Print) is a command-line utility for searching plain-text data sets for lines that match a specified pattern. The grep family includes grep (basic), egrep (extended), fgrep (fixed string), and their variants. These tools are indispensable for system administrators, developers, and anyone working with text files.

## Key Concepts

### Pipe (|)

The pipe operator connects two or more commands in a sequence, where the standard output (stdout) of one command becomes the standard input (stdin) of the next command. This process is known as **pipelining**. The syntax is:

```bash
command1 | command2 | command3
```

Key characteristics of pipes:

- Data flows left to right through the pipeline
- Each command executes in parallel (not sequentially)
- If any command fails, the pipeline typically stops
- Pipes do not modify the original files
- The pipeline works with any commands that read from stdin and write to stdout

Common pipe examples include:

- `ls -l | less` - View directory listing one page at a time
- `cat file.txt | sort | uniq` - Sort and remove duplicates
- `ps aux | grep firefox` - Find processes matching "firefox"

### Basic Regular Expressions (BRE)

BRE is the default regular expression syntax used by grep. In BRE, certain metacharacters have their literal meaning unless escaped with a backslash.

**Basic metacharacters in BRE:**

| Metacharacter | Meaning                                         |
| ------------- | ----------------------------------------------- |
| `^`           | Anchors pattern to the beginning of a line      |
| `$`           | Anchors pattern to the end of a line            |
| `.`           | Matches any single character                    |
| `*`           | Matches zero or more of the preceding character |
| `[abc]`       | Matches any character in the set a, b, or c     |
| `[^abc]`      | Matches any character NOT in the set            |
| `\{n,m\}`     | Matches between n and m occurrences             |
| `\( \) \)`    | Groups expressions (capture groups)             |
| `\< \>`       | Word boundaries                                 |

Important notes about BRE:

- The `+`, `?`, and `|` metacharacters are treated as literals
- To use them as metacharacters, they must be escaped: `\+`, `\?`, `\|`
- Curly braces must be escaped: `\{n\}`

### Extended Regular Expressions (ERE)

ERE provides additional metacharacters that make patterns more readable and powerful. It is used by `egrep` or `grep -E`.

**Additional metacharacters in ERE:**

| Metacharacter | Meaning                                        |
| ------------- | ---------------------------------------------- |
| `+`           | Matches one or more of the preceding character |
| `?`           | Matches zero or one of the preceding character |
| `\|`          | Alternation (OR) - matches either expression   |
| `{n,m}`       | Matches between n and m occurrences            |
| `( )`         | Groups expressions without escaping            |
| `\b`          | Word boundary                                  |

### The Grep Family

**grep (Basic Regular Expression)**

- Searches for patterns using BRE
- Syntax: `grep [options] pattern [file...]`
- Common options:
- `-i` - Ignore case
- `-v` - Invert match (show non-matching lines)
- `-n` - Show line numbers
- `-c` - Count matching lines
- `-l` - Show only filenames with matches
- `-r` - Recursive search
- `-w` - Match whole words only

**egrep (Extended grep)**

- Uses Extended Regular Expressions (ERE)
- Equivalent to `grep -E`
- Supports `+`, `?`, `|`, and `()` without escaping
- Syntax: `egrep [options] pattern [file...]`

**fgrep (Fixed string grep)**

- Searches for literal strings (no regex interpretation)
- Equivalent to `grep -F`
- Faster than grep for fixed patterns
- Useful when searching for strings containing regex metacharacters
- Syntax: `fgrep [options] string [file...]`

**grep -E and grep -F**

- Modern grep supports all modes through options
- `grep -E` enables ERE
- `grep -F` enables fixed string matching
- `grep -E` is preferred over standalone egrep (POSIX standard)

## Examples

### Example 1: Using Pipes with grep

**Problem:** Find all Python files modified in the last 7 days and list only those containing the word "function".

**Solution:**

```bash
find . -mtime -7 -name "*.py" | xargs grep -l "function"
```

**Step-by-step explanation:**

1. `find . -mtime -7 -name "*.py"` - Finds all .py files modified within 7 days
2. `xargs grep -l "function"` - Passes filenames to grep, which searches for "function" and prints only filenames

**Alternative using pipe:**

```bash
ls -lt *.py | head -10 | awk '{print $9}'
```

This lists the 10 most recently modified Python files.

### Example 2: Basic Regular Expressions with grep

**Problem:** Find all lines in a file that start with a capital letter and end with a period.

**Solution:**

```bash
grep '^[A-Z].*\.$' filename.txt
```

**Pattern breakdown:**

- `^` - Start of line
- `[A-Z]` - Match any uppercase letter
- `.*` - Match any characters (zero or more)
- `\.` - Match literal period (escaped)
- `$` - End of line

**Problem:** Find lines containing exactly 3 digits.

**Solution:**

```bash
grep -E '^[0-9]{3}$' filename.txt
```

Or with basic grep:

```bash
grep '^[0-9]\{3\}$' filename.txt
```

### Example 3: Extended Regular Expressions with egrep

**Problem:** Find all email addresses in a file (simple pattern).

**Solution:**

```bash
egrep -i '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' filename.txt
```

**Pattern breakdown:**

- `[a-zA-Z0-9._%+-]+` - Username: letters, numbers, special chars
- `@` - Literal @ symbol
- `[a-zA-Z0-9.-]+` - Domain name
- `\.` - Literal dot
- `[a-zA-Z]{2,}` - Top-level domain (2 or more letters)

**Problem:** Find lines containing either "error" or "warning" or "critical".

**Solution:**

```bash
egrep 'error|warning|critical' logfile.txt
```

This is simpler than the BRE equivalent:

```bash
grep 'error\|warning\|critical' logfile.txt
```

### Example 4: Practical Pipeline with Multiple Commands

**Problem:** From a system log file, extract all failed login attempts, count occurrences per IP, and sort by count (descending).

**Solution:**

```bash
grep "Failed password" /var/log/auth.log | \
 awk '{print $11}' | \
 sort | \
 uniq -c | \
 sort -rn
```

**Step-by-step breakdown:**

1. `grep "Failed password"` - Extracts failed login lines
2. `awk '{print $11}'` - Extracts the 11th field (IP address)
3. `sort` - Sorts IPs alphabetically
4. `uniq -c` - Counts unique occurrences
5. `sort -rn` - Sorts numerically in reverse order

### Example 5: Using fgrep for Literal Strings

**Problem:** Search for the exact string "[0-9]+" in all .txt files (no regex interpretation).

**Solution:**

```bash
fgrep "[0-9]+" *.txt
```

Using regular grep would find any lines containing digits and plus signs, not the literal string.

## Exam Tips

1. **Remember the difference between BRE and ERE**: In exams, note that basic grep uses BRE where `+`, `?`, `|`, and `()` are literals unless escaped. Extended grep (egrep) treats them as metacharacters.

2. **Escape sequences matter**: In BRE, to match special characters like `+`, `?`, `{`, `}`, use `\+`, `\?`, `\{`, `\}` respectively. In ERE, use them directly.

3. **Pipe does not create temporary files**: Emphasize in answers that pipes connect commands directly without intermediate storage, making them efficient.

4. **grep vs egrep vs fgrep**: Know when to use each:

- grep: Simple patterns with BRE
- egrep: Complex patterns with ERE (alternation, grouping)
- fgrep: When pattern contains many metacharacters (faster)

5. **Common grep options for exams**: Remember `-i` (ignore case), `-v` (invert), `-n` (line numbers), `-c` (count), `-l` (filenames only), `-r` (recursive).

6. **Word boundaries**: Use `\<word\>` in BRE or `\bword\b` in ERE to match whole words only, not substrings.

7. **Anchoring patterns**: Always remember `^` matches beginning of line and `$` matches end of line. These are frequently tested in exams.

8. **Combining with other commands**: Pipes can combine any Unix commands. Common combinations include `sort | uniq`, `head | tail`, `awk | sort`.

9. **Practice pattern writing**: Be comfortable writing patterns for common requirements like phone numbers, email addresses, IP addresses, and dates.

10. **xargs for filename lists**: Remember that `find` combined with grep uses xargs to pass filenames, preventing "argument list too long" errors.
