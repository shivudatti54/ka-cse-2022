# Removing the Special Meanings of Wild Cards

======================================================

## **Introduction**

In UNIX, wild cards are used to specify files or directories in the `ls` command. However, sometimes you may want to remove the special meanings of wild cards, for example, to use them as literal characters. In this topic, we will discuss how to remove the special meanings of wild cards and provide examples.

## **What are Wild Cards?**

Wild cards are special characters used in the `ls` command to specify files or directories. The most common wild cards are:

- `*` (asterisk) - matches any sequence of characters
- `?` (question mark) - matches any single character
- `[seq]` - matches any character in the specified sequence
- `[!seq]` - matches any character not in the specified sequence

## **Removing the Special Meanings of Wild Cards**

To remove the special meanings of wild cards, you can use the `-n` or `--number` option of the `ls` command. This option tells `ls` not to interpret wild cards and to treat them as literal characters.

### Using `-n` Option

The `-n` option is used to disable the interpretation of special characters. When you use the `-n` option, all characters in the `ls` command are treated as literal characters.

```bash
$ ls -n *  # displays all files and directories
```

In the above example, `*` is treated as a literal character and does not match any sequence of characters.

### Using `--number` Option

The `--number` option is used to display numbers instead of names for each entry. When you use the `--number` option, all characters in the `ls` command are treated as literal characters.

```bash
$ ls --number *  # displays numbers instead of names for each entry
```

In the above example, `*` is treated as a literal character and does not match any sequence of characters.

## **Examples**

### Example 1: Using `-n` Option with Wild Cards

Suppose you want to list all files and directories in the current directory without interpreting wild cards. You can use the `-n` option with the `ls` command.

```bash
$ ls -n */path/to/directory
```

In the above example, `*/path/to/directory` is treated as a literal directory path and does not match any sequence of characters.

### Example 2: Using `--number` Option with Wild Cards

Suppose you want to list numbers instead of names for each entry in the current directory without interpreting wild cards. You can use the `--number` option with the `ls` command.

```bash
$ ls --number */path/to/directory
```

In the above example, `*/path/to/directory` is treated as a literal directory path and does not match any sequence of characters.

## **Key Concepts**

- The `-n` option is used to disable the interpretation of special characters.
- The `--number` option is used to display numbers instead of names for each entry.
- Wild cards can be used to specify files or directories in the `ls` command.
- The `*` character matches any sequence of characters.
- The `?` character matches any single character.
- The `[seq]` character matches any character in the specified sequence.
- The `[!seq]` character matches any character not in the specified sequence.

By using the `-n` option or the `--number` option, you can remove the special meanings of wild cards and treat them as literal characters in the `ls` command.
