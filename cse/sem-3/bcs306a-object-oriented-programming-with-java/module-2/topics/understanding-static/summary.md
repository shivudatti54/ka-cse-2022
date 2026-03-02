# Understanding Static

## Overview

In Java, the `static` keyword is used to denote a variable, method, or block that belongs to the class itself, rather than an instance of the class. Static variables are shared among all instances of a class, while instance variables are unique to each instance.

## Key Points

- A static variable is shared among all instances of a class.
- Static variables are loaded into memory only once, when the class is loaded.
- Changes to a static variable affect all instances of the class.
- Instance variables are unique to each instance of a class.
- Static methods can access only static variables.
- Static methods can be called without creating an instance of the class.

## Important Definitions

- **Static Variable**: A variable that is shared among all instances of a class.
- **Instance Variable**: A variable that is unique to each instance of a class.

## Key Formulas / Syntax

- `static` keyword is used to declare a static variable or method.
- Example: `static String company = "";`

## Exam Tips

- Be prepared to identify and explain the use of static variables in a given Java program.
- Understand how changes to a static variable affect all instances of a class.
- Focus on the differences between static and instance variables.
