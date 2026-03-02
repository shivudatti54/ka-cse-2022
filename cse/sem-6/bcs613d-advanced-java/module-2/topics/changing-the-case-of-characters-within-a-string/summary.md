# String Case Conversion: Technical Summary

## Core Concepts

The Java `String` class provides `toUpperCase()` and `toLowerCase()` methods for character case transformation. These methods return new `String` objects, preserving the original string due to immutability—a fundamental design characteristic of Java strings.

## Technical Specifications

- **Return Type**: `String` (new object created)
- **Original Object**: Remains unchanged (immutability)
- **Parameterless Variants**: Use default system locale
- **Locale-Aware Variants**: Accept `Locale` parameter for language-specific rules
- **Character Scope**: Unicode code points, not just ASCII

## Critical Implementation Details

1. **Immutability Implication**: Always assign the return value; the original string is never modified
2. **Locale Sensitivity**: Default methods use the system locale, which may produce unexpected results
3. **Turkish I Problem**: Turkish locale treats 'I'/'i' differently; use `Locale.ENGLISH` for consistent behavior
4. **Case-Insensitive Comparison**: Apply `toLowerCase()` or `toUpperCase()` to both strings before `.equals()`
5. **Combining Operations**: Chain with `trim()`, `replace()`, and other string methods for input normalization

## Common Pitfalls

- Forgetting to assign the returned value to a variable
- Assuming case conversion affects the original string
- Ignoring locale-specific behavior in internationalized applications
- Using case conversion for security-sensitive comparisons without proper validation

## Examination Focus Areas

Understand that `toUpperCase()` creates a new `String` object, demonstrate case-insensitive comparison using `str1.toLowerCase().equals(str2.toLowerCase())`, and recognize when locale-specific conversion is necessary.
===SUMMARY_MD===