# Packages and Member Access in Java

## Overview

Java packages organize classes into logical groups, while member access modifiers control visibility of variables, methods, and constructors. These features are fundamental for encapsulation and proper class design in Java programs.

## Key Points

- **Package** is a namespace that groups related classes and interfaces
- Package declaration must be the first statement in a Java file: `package packagename;`
- **Default (package-private)**: Accessible only within the same package
- **Private**: Accessible only within the same class
- **Protected**: Accessible within same package and subclasses in different packages
- **Public**: Accessible from any class in any package
- Classes can be imported using `import packagename.ClassName;` or `import packagename.*;`
- Static import: `import static packagename.ClassName.MEMBER;`

## Important Definitions

- **Package**: A group of related classes and interfaces stored in a directory structure
- **Encapsulation**: Bundling data and methods while restricting direct access to some components
- **Access Modifier**: Keyword that defines the visibility scope of a class, method, or variable

## Key Formulas / Syntax

```java
package com..mypackage; // Must be first line

import java.util.Scanner; // Single class import
import java.util.*; // Wildcard import

public class MyClass {
 public int a;
 private int b;
 protected int c;
 int d; // default/package-private
}
```

## Comparisons

| Modifier  | Same Class | Same Package | Subclass (diff pkg) | Different Package |
| --------- | ---------- | ------------ | ------------------- | ----------------- |
| public    | ✓          | ✓            | ✓                   | ✓                 |
| protected | ✓          | ✓            | ✓                   | ✗                 |
| default   | ✓          | ✓            | ✗                   | ✗                 |
| private   | ✓          | ✗            | ✗                   | ✗                 |

## Exam Tips

- Remember the visibility hierarchy: private < default < protected < public
- **Common Question**: Predict output or identify compilation errors based on access modifier usage
- Note that top-level classes can only have public or default access
- Protected members are accessible in subclasses even if in different package
- Focus on understanding when to use each modifier for encapsulation
