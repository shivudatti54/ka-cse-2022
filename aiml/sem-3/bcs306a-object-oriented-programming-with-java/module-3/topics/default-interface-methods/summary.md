# Default Interface Methods

## Overview

Default interface methods in Java allow interfaces to have methods with an implementation, enabling more flexibility in interface design. This feature was introduced in Java 8. Interfaces can now contain both abstract and non-abstract methods.

## Key Points

- Interfaces can have default methods with an implementation.
- Default methods are non-abstract and can be used directly by any class implementing the interface.
- Interfaces can still have abstract methods without an implementation.
- Classes implementing an interface can override default methods.
- Default methods are useful for adding new functionality to existing interfaces without breaking backward compatibility.

## Important Definitions

- **Default Method**: A non-abstract method in an interface with an implementation.
- **Abstract Method**: A method declared in an interface without an implementation.

## Key Syntax

- `default void methodName() { // implementation }`

## Exam Tips

- Focus on understanding the purpose and usage of default methods in interfaces.
- Be prepared to identify and explain the differences between abstract and default methods in interfaces.
