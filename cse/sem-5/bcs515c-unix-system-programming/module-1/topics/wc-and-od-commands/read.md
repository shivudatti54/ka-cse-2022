# WC and OD Commands in Linux

## Introduction

The `wc` (word count) and `od` (octal dump) commands are essential text processing utilities in Linux/Unix systems. These commands are fundamental tools that every Computer Science engineer must master for file analysis, data processing, and system administration tasks. While `wc` provides quick statistics about files, `od` is crucial for examining binary files and understanding low-level data representation.

The `wc` command is used to count lines, words, characters, and bytes in files, making it invaluable for text analysis, document processing, and scripting. On the other hand, `od` provides a different perspective by displaying file contents in various formats including octal, decimal, hexadecimal, and character representations. This becomes particularly useful when working with binary files, debugging, or understanding file structures at the byte level.

In the context of 's CSE curriculum, these commands form the foundation of shell scripting and Unix utilities, appearing frequently in practical examinations and laboratory sessions. Understanding these commands not only helps in academic success but also prepares students for real-world scenarios where file manipulation and analysis are daily tasks for software professionals.

## Key Concepts

### WC Command (Word Count)

The `wc` command is one of the most frequently used utilities in Linux for obtaining file statistics. It can count:

- Lines (using `-l` option)
- Words (using `-w` option)
- Characters (using `-m` option)
- Bytes (using `-c` option)

**Basic Syntax:**

```
wc [OPTION]... [FILE]...
```

**Important Options:**

- `-l` or `--lines`: Print the line counts
- `-w` or `--words`: Print the word counts
- `-c` or `--bytes`: Print the byte counts
- `-m` or `--chars`: Print the character counts
- `-L` or `--max-line-length`: Print the length of the longest line
- When no option is specified, `wc` prints all four counts (lines, words, characters, bytes)

**Working with Multiple Files:**
When multiple files are specified, `wc` displays statistics for each file followed by a total line. The output format is: line count, word count, character count, byte count, and then the filename.

**Using with Standard Input:**
The `wc` command can read from standard input using pipes (`|`) or by using a hyphen (`-`) as the filename. This makes it extremely useful in command pipelines for processing data dynamically.

### OD Command (Octal Dump)

The `od` command is used to dump file contents in a specified format. Unlike text editors that attempt to interpret files as text, `od` displays the raw binary data in various formats, making it essential for analyzing non-text files.

**Basic Syntax:**

```
od [OPTION]... [FILE]...
od -A [address_base] -t [type] [FILE]
```

**Address Base Options (-A):**

- `-A d` or `--address-radix=decimal`: Address in decimal
- `-A o` or `--address-radix=octal`: Address in octal (default)
- `-A x` or `--address-radix=hex`: Address in hexadecimal
- `-A n` or `--address-radix=none`: No address displayed

**Type Specifiers (-t):**

- `-t c` or `--format=character`: Character representation (printable ASCII + escape sequences)
- `-t d1` or `--format=decimal`: Signed decimal (1-byte units)
- `-t u1` or `--format=unsigned`: Unsigned decimal
- `-t o1` or `--format=octal`: Octal (default, 1-byte units)
- `-t x1` or `--format=hex`: Hexadecimal (1-byte units)
- `-t f4` or `--format=float`: Floating point (4-byte float)
- `-t d2`, `-t d4`, etc.: Can specify different byte sizes (1, 2, 4, 8)

**Other Important Options:**

- `-j N` or `--skip-bytes=N`: Skip N bytes from the beginning
- `-N N` or `--read-bytes=N`: Limit output to N bytes
- `-v` or `--no-stringing`: Don't use `*` to indicate repeated lines
- `-w N`: Specify the number of bytes per output line (default is 16)

## Examples

### Example 1: Using WC Command

**Problem:** Count lines, words, and characters in a file named "notes.txt"

**Solution:**

```bash
# Count lines only
wc -l notes.txt

# Count words only
wc -w notes.txt

# Count characters only
wc -m notes.txt

# Count all (lines, words, characters, bytes)
wc notes.txt

# Count lines in multiple files
wc -l file1.txt file2.txt file3.txt
```

**Sample Output:**

```
$ wc -l notes.txt
42 notes.txt

$ wc -w notes.txt
287 notes.txt

$ wc notes.txt
 42 287 1654 1654 notes.txt
```

The output shows: 42 lines, 287 words, 1654 characters, and 1654 bytes.

### Example 2: WC with Pipelines

**Problem:** Count the number of processes running for a specific user

**Solution:**

```bash
# Count lines in process list (excluding header)
ps -aux | grep username | wc -l

# Count number of files in a directory
ls -1 | wc -l

# Count total number of users in system
cat /etc/passwd | wc -l
```

### Example 3: Using OD Command with Different Formats

**Problem:** Examine the contents of a file "data.bin" in multiple formats

**Solution:**

```bash
# Default octal dump (16 bytes per line)
od data.bin

# Character dump with addresses in hexadecimal
od -A x -t c data.bin

# Hexadecimal dump, skipping first 16 bytes
od -A d -t x1 -j 16 data.bin

# Decimal dump, limiting output to 32 bytes
od -A d -t d1 -N 32 data.bin
```

**Sample Output:**

```
$ od -A x -t c example.txt
0000000 H e l l o \n W o r l d \n
000000c

$ od -A x -t x1 example.txt
0000000 48 65 6c 6c 6f 0a 57 6f 72 6c 64 0a
000000c
```

### Example 4: Practical OD Usage

**Problem:** Examine the header of an image file to identify its format

**Solution:**

```bash
# Check first 16 bytes in hex to identify file type
od -A n -t x1 -N 16 image.jpg

# View text file with both octal and character representation
od -c textfile.txt
```

**Sample Output:**

```
$ od -A n -t x1 -N 16 image.jpg
ff d8 ff e0 00 10 4a 46 49 46 00 01 01 00 00 01
```

This output shows the JPEG magic numbers (FF D8 FF E0), confirming it's a JPEG file.

### Example 5: Combining WC and OD in Scripts

**Problem:** Create a script to analyze a log file and check for binary data

**Solution:**

```bash
#!/bin/bash
# Script to analyze log file

echo "Log File Analysis"
echo "=================="
echo "Total lines: $(wc -l < logfile.log)"
echo "Total words: $(wc -w < logfile.log)"
echo "Total size: $(wc -c < logfile.log) bytes"

# Check if file contains non-printable characters
non_printable=$(od -An -tc logfile.log | grep -cv '[[:print:]]')

if [ "$non_printable" -gt 0 ]; then
 echo "Warning: File may contain binary data"
else
 echo "File contains only text data"
fi
```

## Exam Tips

1. **WC Command Options:** Remember that `-l` counts lines, `-w` counts words, `-c` counts bytes, and `-m` counts characters. Without any option, wc displays all four.

2. **Output Order:** For `wc`, the output order is always: lines, words, characters, bytes, filename. This is crucial for interpreting results.

3. **OD Default Format:** By default, `od` displays output in octal format with addresses in octal. Use `-A` to change address base and `-t` to change data format.

4. **Type Specifiers:** Remember the type specifiers: `c` for character, `d` for decimal, `o` for octal, `x` for hexadecimal, and `f` for floating point.

5. **Combining Commands:** Both `wc` and `od` work excellently with pipes (`|`). This is frequently tested in practical exams.

6. **File Identification:** The `od` command can be used to identify file types by examining magic numbers in the first few bytes.

7. **Byte Size Specification:** In `od`, you can specify byte sizes like `-t d1` (1-byte decimal), `-t d2` (2-byte decimal), `-t d4` (4-byte decimal), etc.

8. **Standard Input:** Both commands can read from standard input using pipes, which is essential for building complex command pipelines.

9. **WC with Multiple Files:** When multiple files are given to `wc`, it shows individual statistics plus a total line at the end.

10. **OD Skip and Limit:** Remember `-j` for skipping bytes and `-N` for limiting output, which are useful for examining specific portions of files.
