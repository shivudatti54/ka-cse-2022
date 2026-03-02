# Access Control in Java

## Overview

Access control in Java restricts the visibility of classes, methods, and variables, implementing **encapsulation** through four access levels: public, protected, default, and private. Proper use of access control ensures data hiding and code security. Access levels are defined using access modifiers.

## Key Points

- Four access levels: public, protected, default, and private.
- **public**: accessible from any class in any package.
- **private**: accessible only within its own class.
- **protected**: accessible within same package and by subclasses in other packages.
- No modifier means **default** (package-private) access.
- **Encapsulation**: private fields + public getters/setters.

## Important Definitions

- **Encapsulation**: hiding internal implementation details and exposing only necessary information.
- **Access Modifier**: a keyword that defines the access level of a class, method, or variable.

## Key Syntax

- `public class ClassName { ... }`
- `private dataType variableName;`
- `protected dataType variableName;`

## Comparisons

| Modifier  | Same Class | Same Package | Subclass (diff pkg) | Other Packages |
| --------- | ---------- | ------------ | ------------------- | -------------- |
| public    | Yes        | Yes          | Yes                 | Yes            |
| protected | Yes        | Yes          | Yes                 | No             |
| default   | Yes        | Yes          | No                  | No             |
| private   | Yes        | No           | No                  | No             |

## Exam Tips

- Focus on understanding the four access levels and their usage.
- Remember that no modifier means default (package-private) access.
- Encapsulation is a key concept in object-oriented programming; know how to implement it using access control.
