# **Removing the Special Meanings of Wild Cards**

## **What are Wild Cards?**

In the context of the `ls` command, wild cards are special characters that allow you to match patterns in file names. The two most common wild cards used in `ls` are:

- `*` (asterisk): matches any sequence of characters
- `?` (question mark): matches any single character

## **Removing Special Meanings of Wild Cards**

When using the `ls` command with wild cards, the special meanings of these characters can sometimes lead to unexpected results. To remove these special meanings, you can use the following techniques:

### 1. Quoting

Quoting the `*` and `?` characters in your command prevents `ls` from interpreting their special meanings. You can do this by surrounding the wild card with double quotes (`"`) or single quotes (`'`) like this:

- `ls "file\*"`
- `ls 'file\?'`

This tells `ls` to treat the characters literally, rather than as wild cards.

### 2. Using the `ls -l` Option

By default, the `ls` command uses a simple listing format. To remove the special meanings of wild cards, you can use the `-l` option, which displays a long listing format. In this format, the `*` and `?` characters are displayed literally, without their special meanings.

- `ls -l "file\*"`
- `ls -l 'file\?'`

### 3. Using the `glob` Option

If you want to remove the special meanings of wild cards from all `ls` commands, you can set the `glob` option. This option tells `ls` to treat wild cards as literal characters, rather than as patterns.

- `export GLOB=\*
- `export GLOB='?'`

Once you've set the `glob` option, you can use `ls` without quoting or using the `-l` option, and the special meanings of wild cards will be removed.

## **Example Use Cases**

Here are some examples of using wild cards in `ls` commands, with and without removing their special meanings:

### Removing Special Meanings with Quoting

- `ls "file\*"`: lists all files with the name "file" and any characters after it
- `ls "dir\*"`: lists all files and directories with the name "dir" and any characters after it

### Removing Special Meanings with the `-l` Option

- `ls -l "file\*"`: lists all files with the name "file" and any characters after it, in a long listing format
- `ls -l "dir\*"`: lists all files and directories with the name "dir" and any characters after it, in a long listing format

### Removing Special Meanings with the `glob` Option

- `export GLOB=\*
- `ls "file\*"`: lists all files with the name "file" and any characters after it
- `ls "dir\*"`: lists all files and directories with the name "dir" and any characters after it

By understanding how to remove the special meanings of wild cards in `ls` commands, you can use these characters to match patterns in file names and perform tasks more efficiently.
