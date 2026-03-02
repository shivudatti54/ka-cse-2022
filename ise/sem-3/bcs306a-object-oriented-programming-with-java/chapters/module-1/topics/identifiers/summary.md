# Identifiers in Java - Summary

## Key Definitions and Concepts

An identifier in Java is a user-defined name given to program elements such as classes, methods, variables, interfaces, and packages. It serves as a unique reference point within the code that allows the compiler and programmer to identify and work with specific program elements.

## Important Rules for Identifiers

Java identifiers MUST follow these mandatory rules: they must begin with a letter, dollar sign ($), or underscore (_); they cannot be Java reserved keywords; they cannot contain spaces or special characters except $ and _; and they are case-sensitive, meaning `count`, `Count`, and `COUNT` are three distinct identifiers.

## Java Naming Conventions

Java recommends three primary naming conventions: PascalCase for classes and interfaces (e.g., `StudentDetails`); camelCase for variables and methods (e.g., `calculateTotal`); and SCREAMING_SNAKE_CASE for constants (e.g., `MAXIMUM_SIZE`).

## Reserved Keywords

Java has 51 reserved keywords that cannot be used as identifiers, including primitive types (int, double, boolean), access modifiers (public, private, protected), control flow keywords (if, while, for), and OOP keywords (class, extends, new).

## Key Points

- Identifiers are names given to program elements in Java
- The first character must be a letter, $, or _
- Keywords and reserved words cannot be used as identifiers
- Java identifiers are case-sensitive
- Unicode characters are supported in identifiers
- Following naming conventions improves code readability
- The compiler enforces rules but not conventions

## Common Mistakes to Avoid

Common errors include using Java keywords as identifiers (e.g., using `class` as a variable name), starting an identifier with a digit (e.g., `2value`), including spaces or hyphens in identifiers (e.g., `my-variable`), and ignoring naming conventions which, while not causing compile errors, makes code harder to maintain.

## Revision Tips

When preparing for exams, practice identifying valid and invalid identifiers by applying each rule systematically. Memorize the list of Java keywords as questions frequently test this knowledge. Write sample code to reinforce naming convention concepts and review previous year question papers to understand the exam pattern.