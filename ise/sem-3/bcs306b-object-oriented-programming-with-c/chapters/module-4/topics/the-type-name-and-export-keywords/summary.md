# **The Type Name and Export Keywords**

## **Overview**

This section covers the type name and export keywords in C++, which are used to declare and manage object-oriented programming concepts.

## **Key Points**

- **Type Name**: A type name is a keyword that is used to specify the type of a variable, function, or object.
  - Examples: `int`, `double`, `std::string`
- **Export**: The `export` keyword is used to specify that a function or variable can be accessed from outside the current translation unit.
  - Example: `void foo() export;`
- **Export Specifier**: The `export` specifier is used to specify the visibility of a function or variable.
  - Examples:
    - `static` : not visible outside current translation unit
    - `extern` : visible outside current translation unit
    - `static extern` : not visible outside current translation unit
- **Exported Functions**: A function is exported if it has the `export` keyword and is not `inline`.
  - Example: `void foo() { ... } export;`
- **Exported Variables**: A variable is exported if it has the `export` keyword and is not a local variable.
  - Example: `int x; export;`

## **Important Formulas and Definitions**

- **Visibility**: The level of access a function or variable has to other parts of the program.
- **Linkage**: The way in which a function or variable is referenced by other parts of the program.
- **Export Specifier**: A keyword that specifies the visibility of a function or variable.

## **Theorems**

- **Exported Functions**: A function is exported if it has the `export` keyword and is not `inline`.
- **Exported Variables**: A variable is exported if it has the `export` keyword and is not a local variable.

## **Quick Revision**

- Type name: `int`, `double`, `std::string`
- Export: `void foo() export;`
- Export specifier: `static`, `extern`, `static extern`
- Exported functions: `void foo() { ... } export;`
- Exported variables: `int x; export;`
