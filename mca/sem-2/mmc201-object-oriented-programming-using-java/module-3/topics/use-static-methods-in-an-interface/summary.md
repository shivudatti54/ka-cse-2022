# Use Static Methods in an Interface

## Overview

Java 8 introduced the ability to define static methods in interfaces, allowing for more flexibility and utility in interface design. Static methods in interfaces are used to provide a way to encapsulate utility methods that are related to the interface. These methods can be called without creating an instance of the interface.

## Key Points

- Interfaces can have static methods, which must have a body.
- Static methods in interfaces are implicitly public.
- Static methods are used to provide utility functions related to the interface.
- Static methods can be called using the interface name, without creating an instance.
- Static methods are useful for providing helper methods that don't depend on instance state.

## Important Definitions

- **Static Method**: A method that belongs to a class or interface, rather than an instance.
- **Interface**: A abstract class that defines a contract for classes to implement.

## Key Formulas / Syntax

- `static void methodName() { /* implementation */ }`

## Exam Tips

- Be prepared to explain the purpose and use of static methods in interfaces.
- Understand how to define and call static methods in interfaces.
- Focus on the benefits of using static methods in interfaces, such as providing utility functions without requiring instance creation.
