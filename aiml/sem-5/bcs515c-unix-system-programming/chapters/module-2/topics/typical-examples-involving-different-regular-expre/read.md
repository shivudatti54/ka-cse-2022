# **Typical Examples Involving Different Regular Expressions**

## **Introduction**

Regular expressions, also known as regex, are a powerful tool for matching patterns in strings. In UNIX system programming, regular expressions are often used in combination with the `ls` command to filter and sort files based on their names, permissions, and other attributes. In this study material, we will cover typical examples involving different regular expressions.

## **What are Regular Expressions?**

Regular expressions are a way to describe a search pattern using a sequence of characters. They can be used to match text patterns, validate input, and extract data from strings.

## **Types of Regular Expressions**

### 1. Character Classes

Character classes are used to match a set of characters. For example:

- `[abc]` matches any of the characters 'a', 'b', or 'c'
- `[a-zA-Z]` matches any letter (both uppercase and lowercase)
- `[0-9]` matches any digit

## **Examples**

- Match any word that starts with 'a': `/a\w*$/`
- Match any word that contains the letter 'e': `/e\w*$/`
- Match any word that ends with 'ing': `/ing$/`

### 2. Quantifiers

Quantifiers are used to specify how many times a pattern should be matched. For example:

- `*` matches zero or more occurrences
- `+` matches one or more occurrences
- `?` matches zero or one occurrence
- `{n,m}` matches between n and m occurrences

## **Examples**

- Match any string that contains the letter 'e' at least twice: `/e{2,}/`
- Match any string that contains the letter 'a' one or more times: `/a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*/`
- Match any string that ends with 'ing' and has a length of at least 3 characters: `/ing\{3,\}$/`

### 3. Anchors

Anchors are used to match the start or end of a string. For example:

- `^` matches the start of the string
- `$` matches the end of the string
- `^w` matches any word (equivalent to `^[a-zA-Z0-9_]+`)
- `w$` matches any word (equivalent to `[a-zA-Z0-9_]+$`)

## **Examples**

- Match any string that starts with 'a': `/^a\w*$/`
- Match any string that ends with 'ing': `/[a-zA-Z0-9_]+ing$/`
- Match any string that contains only letters: `/^[a-zA-Z]+$/`

### 4. Groups

Groups are used to capture parts of a pattern for later reference. For example:

- `(` and `)` are used to define groups

## **Examples**

- Match any string that contains the letter 'e' and any word: `/e(\w+)/`
- Match any string that starts with 'a' and ends with 'ing': `/^a(\w+)ing$/`

### 5. Alternation

Alternation is used to match either of two patterns. For example:

- `\|` is used to specify alternation

## **Examples**

- Match any string that contains the letter 'e' or 'a': `/e\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w*|a\w\*|
