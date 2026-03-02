# Method Overriding in Java

## Overview

Method overriding is a feature in Java where a subclass provides its own implementation of a method already defined in its superclass. The method in the subclass must have the same name, return type, and parameter list. This enables runtime polymorphism.

## Key Points

- Same method signature (name + parameters) as superclass method.
- Return type must be same or covariant (subtype).
- Access modifier cannot be more restrictive.
- Cannot override final, static, or private methods.
- @Override annotation is optional but recommended.
- Enables runtime polymorphism.

## Important Definitions

- **Method Overriding**: Providing a specific implementation for a method already defined in its superclass.
- **Covariant Return Type**: A return type that is a subtype of the return type of the overridden method.

## Key Syntax

- `@Override` annotation to verify method overriding.

## Exam Tips

- Focus on method signature, return type, and access modifiers.
- Understand runtime polymorphism and its relation to method overriding.
- Be prepared to identify correct and incorrect method overriding examples.
