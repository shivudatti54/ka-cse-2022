# Software Design Principles

## SOLID Principles

### S - Single Responsibility Principle

A class should have only one reason to change.

- One class = one job
- Improves maintainability

### O - Open/Closed Principle

Open for extension, closed for modification.

- Add new functionality without changing existing code
- Use inheritance, interfaces

### L - Liskov Substitution Principle

Subtypes must be substitutable for base types.

- Child class should not break parent behavior
- Square/Rectangle problem

### I - Interface Segregation Principle

Clients should not depend on interfaces they don't use.

- Prefer many specific interfaces over one general
- Avoid "fat" interfaces

### D - Dependency Inversion Principle

Depend on abstractions, not concretions.

- High-level modules shouldn't depend on low-level
- Both should depend on interfaces

## Other Principles

### DRY - Don't Repeat Yourself

Every piece of knowledge should have a single representation.

### KISS - Keep It Simple, Stupid

Simplest solution is usually the best.

### YAGNI - You Ain't Gonna Need It

Don't add functionality until needed.

## Coupling & Cohesion

- **Low Coupling**: Minimize dependencies between modules
- **High Cohesion**: Related functionality stays together
