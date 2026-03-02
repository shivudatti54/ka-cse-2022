# Typical Examples Involving Different Regular Expressions

### Introduction

Regular expressions (regex) are a powerful tool for pattern matching in strings. In this section, we will explore typical examples involving different regular expressions, including character classes, quantifiers, repetition, and more.

### Character Classes

A character class is a set of characters enclosed in square brackets (`[]`). It matches any single character within the class.

- `.` (dot) matches any single character except a newline
- `^` matches the start of the string
- `$` matches the end of the string
- `[abc]` matches any single character in the set `a`, `b`, or `c`
- `[a-zA-Z]` matches any single character in the set of all letters (both uppercase and lowercase)
- `[^abc]` matches any single character except `a`, `b`, or `c`

Example:

```bash
$ echo "Hello, World!" | grep "[a-zA-Z]"
Hello, World!
```

In this example, the regular expression `[a-zA-Z]` matches any single character in the set of all letters, and the `grep` command prints the line that matches this pattern.

### Quantifiers

A quantifier is a symbol that specifies the number of times a preceding element should be matched.

- `*` matches zero or more occurrences of the preceding element
- `+` matches one or more occurrences of the preceding element
- `?` matches zero or one occurrence of the preceding element
- `{n}` matches exactly `n` occurrences of the preceding element
- `{n, m}` matches at least `n` and at most `m` occurrences of the preceding element

Example:

```bash
$ echo "Hello, World!" | grep "o*"
Hello, World!
```

In this example, the regular expression `o*` matches zero or more occurrences of the character `o`, and the `grep` command prints the line that matches this pattern.

### Repetition

Repetition is used to specify how often a preceding element should be matched.

- `^` matches the start of the string
- `$` matches the end of the string
- `{n}` matches exactly `n` occurrences of the preceding element
- `{n, m}` matches at least `n` and at most `m` occurrences of the preceding element

Example:

```bash
$ echo "Hello, World!" | grep "^H"
Hello, World!
```

In this example, the regular expression `^H` matches the start of the string and the character `H`, and the `grep` command prints the line that matches this pattern.

### Anchors

An anchor is a symbol that specifies the position of the match in the string.

- `^` matches the start of the string
- `$` matches the end of the string

Example:

```bash
$ echo "Hello, World!" | grep "o$"
World!
```

In this example, the regular expression `o$` matches the character `o` at the end of the string, and the `grep` command prints the line that matches this pattern.

### Word Boundaries

A word boundary is a symbol that specifies the position of the match in relation to word characters.

- `\b` matches a word boundary
- `\B` matches a non-word boundary

Example:

```bash
$ echo "Hello, World!" | grep "\bWorld\b"
World!
```

In this example, the regular expression `\bWorld\b` matches the word "World" as a whole word, and the `grep` command prints the line that matches this pattern.

### Other Examples

- Matching email addresses: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- Matching phone numbers: `^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$`
- Matching credit card numbers: `^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11})$`

These are just a few examples of the many types of regular expressions that can be used to match different patterns in strings. By mastering regular expressions, you can write powerful and efficient programs to manipulate and search strings.
