# Main Function and Header Files in C++
## Introduction

C++ is a high-level, object-oriented programming language that is widely used for building operating systems, games, and other high-performance applications. The main function is the entry point of any C++ program, and header files are used to declare functions, variables, and classes that can be used in multiple source files. In this topic, we will discuss the main function and header files in C++.

The main function is the starting point of any C++ program. It is the function that is called when the program starts execution. The main function is responsible for calling other functions, initializing variables, and controlling the flow of the program.

Header files, on the other hand, are used to declare functions, variables, and classes that can be used in multiple source files. They provide a way to share code between multiple source files, making it easier to write and maintain large programs.

## Key Concepts

### Main Function

* The main function is the entry point of any C++ program.
* It is the function that is called when the program starts execution.
* The main function is responsible for calling other functions, initializing variables, and controlling the flow of the program.
* The main function should be declared with the return type int, indicating that it returns an integer value.
* The main function can take two arguments, argc and argv, which represent the number of command-line arguments and an array of strings containing the command-line arguments, respectively.

### Header Files

* Header files are used to declare functions, variables, and classes that can be used in multiple source files.
* They provide a way to share code between multiple source files, making it easier to write and maintain large programs.
* Header files typically have a .h or .hpp extension.
* Header files should be included in source files using the #include directive.
* Header files can contain function declarations, variable declarations, class declarations, and macro definitions.

## Examples

### Example 1: Main Function

```cpp
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

This example shows a simple main function that prints "Hello, World!" to the console.

### Example 2: Header File

```cpp
// mymath.h
#ifndef MYMATH_H
#define MYMATH_H

int add(int a, int b);
int subtract(int a, int b);

#endif
```

```cpp
// mymath.cpp
#include "mymath.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}
```

```cpp
// main.cpp
#include "mymath.h"

int main() {
    int result = add(2, 3);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
```

This example shows a header file mymath.h that declares two functions, add and subtract. The functions are defined in a separate source file mymath.cpp. The main function in main.cpp includes the header file and calls the add function.

## Exam Tips

1. The main function is the entry point of any C++ program.
2. The main function should be declared with the return type int.
3. Header files are used to declare functions, variables, and classes that can be used in multiple source files.
4. Header files should be included in source files using the #include directive.
5. Use header files to share code between multiple source files.
6. Use the #ifndef directive to prevent multiple inclusions of a header file.
7. Use the #define directive to define macros in a header file.