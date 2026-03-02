# Comments in Java - Summary

## Key Definitions and Concepts

- **Comments** are non-executable statements in Java that are ignored by the compiler. They provide internal documentation within source code to help programmers understand and maintain the code.

## Important Types of Comments

1. **Single-Line Comments (//):** Begin with // and continue to the end of the line. Used for brief notes about specific lines of code.

2. **Multi-Line Comments (/\* \*/):** Start with /_ and end with _/. Can span multiple lines for longer explanations.

3. **Documentation Comments (/** \*/):\*\* Special multi-line comments used with Javadoc tool to generate external HTML documentation. Include special tags like @param, @return, @author, and @version.

## Important Formulas and Syntax

```java
// Single-line comment syntax
// comment text here

/* Multi-line comment syntax */
/* comment
 text
 here */

/** Documentation comment syntax */
/** @author Name
 * @version 1.0
 * @param variableName description
 * @return description */
```

## Key Points

- Java supports three types of comments: single-line, multi-line, and documentation comments.
- Comments are completely ignored by the Java compiler and do not affect program execution.
- Documentation comments begin with /\*\* and are used by the Javadoc tool.
- Common Javadoc tags include @author, @version, @param, @return, @since, and @throws.
- Java does NOT support nested multi-line comments.
- Comments should explain "why" the code does something, not "what" it does.
- Comments should be kept updated when code is modified.
- Proper commenting demonstrates professional programming practices.
- The Javadoc tool generates HTML documentation from documentation comments.
- Comments facilitate code maintenance and team collaboration.

## Common Mistakes to Avoid

1. **Confusing comment syntax:** Using // for multi-line comments or mixing up /\* with /\*\*.

2. **Writing unnecessary comments:** Commenting obvious code that doesn't need explanation.

3. **Leaving outdated comments:** Keeping old comments that no longer match the code.

4. **Attempting nested comments:** Java does not support nesting multi-line comments.

## Revision Tips

1. Practice writing all three types of comments in sample Java programs.

2. Remember that // is for single-line, /\* _/ for multi-line, and /\*\* _/ for documentation comments.

3. Create a sample class with complete Javadoc comments to understand documentation generation.

4. Focus on Javadoc tags as they frequently appear in practical exams.

5. Understand that comments improve code readability but have no effect on execution.
