# WC and OD Commands - Summary

## Key Definitions and Concepts

- **WC (Word Count):** A Linux utility that counts lines, words, characters, and bytes in files or standard input.

- **OD (Octal Dump):** A command that dumps file contents in various formats (octal, decimal, hexadecimal, character) for binary file analysis.

- **Magic Numbers:** Signature bytes at the beginning of files used to identify file types, viewable with `od`.

## Important Formulas and Commands

**WC Command Syntax:**

```bash
wc [OPTION]... [FILE]...
```

**Key WC Options:**

- `-l`: Count lines
- `-w`: Count words
- `-c`: Count bytes
- `-m`: Count characters
- `-L`: Length of longest line

**OD Command Syntax:**

```bash
od [OPTION]... [FILE]...
```

**Key OD Options:**

- `-A [d|o|x|n]`: Address base (decimal/octal/hex/none)
- `-t [c|d|o|x|f]`: Output type (character/decimal/octal/hex/float)
- `-j N`: Skip N bytes from beginning
- `-N N`: Limit output to N bytes

## Key Points

1. `wc` without options displays: lines, words, characters, bytes, and filename.

2. When multiple files are given to `wc`, it shows individual stats plus a total line.

3. `od` defaults to octal format with 16 bytes per output line.

4. Type specifiers in `od` can include size: `-t d1`, `-t d2`, `-t d4` for 1/2/4-byte integers.

5. Both commands support reading from standard input using pipes.

6. `od -t c` displays printable characters with escape sequences for non-printable bytes.

7. The `-v` option in `od` prevents `*` from marking repeated lines.

8. WC is often used in pipelines with `grep`, `sort`, and other commands for data processing.

9. OD can identify file types by examining magic numbers in file headers.

10. Address base options (`-A`) control how file offsets are displayed in `od` output.

## Common Mistakes to Avoid

1. **Confusing character count with byte count:** `-m` counts characters (may differ from bytes in Unicode), `-c` counts raw bytes.

2. **Forgetting OD default format:** OD defaults to octal; use `-t x` for hexadecimal.

3. **Not using quotes with special characters:** When using od with certain characters, proper quoting is essential.

4. **Ignoring the difference between octal and decimal addresses in OD output.**

## Revision Tips

1. Practice using all `wc` options with sample text files to remember each flag's purpose.

2. Create binary test files and examine them with different `od` format specifiers.

3. Use `od` to examine common file headers (JPEG, PNG, PDF) to understand magic numbers.

4. Build compound commands: `cat file.txt | wc -l` versus `wc -l < file.txt` both work.

5. Remember the output order of `wc`: lines → words → characters → bytes.
