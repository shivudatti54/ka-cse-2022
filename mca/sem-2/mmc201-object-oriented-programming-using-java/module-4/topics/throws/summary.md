# throws Clause in Java

## Overview

The **throws** clause in Java declares the exceptions that a method might throw, allowing the caller to handle them. It is mandatory for **checked exceptions** but optional for unchecked exceptions.

## Key Points

- Used in method declaration to indicate potential exceptions
- Declares exceptions without actually throwing them
- Mandatory for checked exceptions (IOException, SQLException, etc.)
- Optional for unchecked exceptions (RuntimeException, NullPointerException, etc.)
- Multiple exceptions can be declared separated by commas
- Caller must either catch or further propagate the exception

## Important Definitions

- **Checked Exception**: Exceptions that must be declared or caught (inherit from Exception but not RuntimeException)
- **Unchecked Exception**: Exceptions that don't require declaration (RuntimeException and its subclasses)
- **throw**: Keyword used to actually throw an exception instance

## Key Formulas / Syntax

```java
return_type method_name(parameters) throws ExceptionType1, ExceptionType2 {
 // method body
}
```

## Comparisons

| Aspect  | throw                          | throws                            |
| ------- | ------------------------------ | --------------------------------- |
| Purpose | Actually throws an exception   | Declares exceptions to be thrown  |
| Usage   | Inside method body             | In method declaration             |
| Object  | Followed by exception instance | Followed by exception class names |
| Count   | Single exception               | Multiple exceptions possible      |

## Exam Tips

- Remember: **throw** = verb (action), **throws** = noun (declaration)
- Always declare checked exceptions; unchecked are optional
- If overriding a method, throws clause must be compatible with superclass
- Common question: "Explain the difference between throw and throws with examples"
