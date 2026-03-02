# Packages in Java

## Overview

Packages are a grouping mechanism in Java that organize related classes, interfaces, and sub-packages. They provide namespace management, access control, and help avoid naming conflicts between classes.

## Key Points

- **package** keyword declares the package to which a source file belongs
- Package name must match the directory/folder structure (e.g., `com..mypackage` → folder `com//mypackage`)
- All source files in a package must have the same package declaration
- **import** keyword is used to access classes from other packages
- Java provides built-in packages: `java.lang`, `java.util`, `java.io`, `java.awt`, `java.net`
- A class without a package declaration belongs to the **default package**
- Package names follow reverse domain naming: `com.company.project`

## Important Definitions

- **Package**: A logical grouping of related classes and interfaces
- **Fully Qualified Name**: Complete path including package (e.g., `com..mypackage.MyClass`)
- **Default Package**: Unnamed package when no package declaration is present

## Key Formulas / Syntax

```java
// Package declaration (must be first line)
package com..mypackage;

// Import statement
import com..mypackage.MyClass;
import java.util.*;  // wildcard import
```

## Exam Tips

- Remember: package declaration must be the first executable statement in the file
- Classpath must include the root directory containing the package folders
- exams frequently ask: "What is the purpose of packages?" and "Write a Java program to create a user-defined package"
- Don't confuse `import` with C++ `#include` — import only makes classes accessible, doesn't copy code
