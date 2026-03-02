# Modular Programming - Summary

## Key Definitions and Concepts

MODULAR PROGRAMMING is a software design technique that separates a program into independent, interchangeable modules, each containing everything needed to execute one aspect of functionality. Each module in C is typically implemented as a collection of related functions in a separate source file with a corresponding header file.

## Important Formulas and Techniques

There are no specific formulas in modular programming, but key techniques include:
- Header guards (#ifndef, #define, #endif) to prevent multiple inclusions
- Function prototypes declared in headers for interface definition
- Static functions for internal implementation hiding
- Parameter passing to achieve loose coupling between modules

## Key Points

- MODULAR PROGRAMMING breaks large problems into smaller, manageable sub-problems

- SINGLE RESPONSIBILITY PRINCIPLE states each module should have one reason to change

- ENCAPSULATION hides implementation details behind well-defined interfaces

- LOOSE COUPLING minimizes dependencies between modules through parameter passing

- HIGH COHESION ensures elements within a module belong together logically

- HEADER FILES (.h) contain declarations that other modules need to use
- SOURCE FILES (.c) contain actual implementations of declared functions
- The STATIC KEYWORD makes functions visible only within their source file

## Common Mistakes to Avoid

- PUTTING ALL CODE IN MAIN() without creating separate functions for different tasks
- USING GLOBAL VARIABLES extensively instead of passing data through parameters
- NOT USING HEADER GUARDS, which can cause compilation errors with multiple inclusions
- CONFUSING DECLARATIONS with definitions—both serve different purposes in modular code

## Revision Tips

- Practice converting a monolithic program into a modular structure with separate files
- Memorize the four principles and be able to explain each with an example
- Remember that header files declare functions, source files implement them
- Review previous topics on function prototypes and calls as they form the foundation of modular design
- Understand scope rules thoroughly—know the difference between automatic, static, and global variables