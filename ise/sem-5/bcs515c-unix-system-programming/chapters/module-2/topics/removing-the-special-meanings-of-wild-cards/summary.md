# Removing the Special Meanings of Wild Cards

### UNIX SYSTEM PROGRAMMING

#### File Attributes and Permissions: The `ls` command with options

### Removing the Special Meanings of Wild Cards

- **What are wild cards?**
  - Special characters used in patterns to match multiple files or directories.
  - `*` matches any characters, `?` matches a single character.
- **Special meanings of wild cards in file names:**
  - `*` matches any characters, including none (empty string).
  - `?` matches a single character.
- **Removing the special meanings of wild cards:**
  - Use the `-n` option with `ls` to prevent the special meanings of wild cards.
  - Example: `ls -n *` will list files without removing special meanings.
- **Formula:**
  - `ls -n *`
- **Theorem:**
  - The `-n` option suppresses the special meanings of wild cards in file names.

## Revision Tips

- Practice using the `-n` option with `ls` to remove special meanings of wild cards.
- Understand the differences between the special meanings of wild cards in file names.
- Review the formula and theorem related to removing special meanings of wild cards.
