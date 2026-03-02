# Procedural vs OOP Overview

## Introduction

Programming paradigms are fundamental styles or approaches of writing code. The two most popular programming paradigms are Procedural Programming and Object-Oriented Programming (OOP). Understanding the differences between these two paradigms is crucial for any aspiring programmer. In this topic, we will delve into the world of Procedural and OOP, exploring their characteristics, advantages, and disadvantages.

Procedural Programming is a paradigm that focuses on procedures or functions that perform specific tasks. It is based on the concept of a procedure call, where a program is broken down into a set of procedures or functions that are called upon to perform a specific task. On the other hand, Object-Oriented Programming is a paradigm that revolves around the concept of objects and classes. It is based on the idea of creating objects that have properties and methods, which can be used to perform specific tasks.

## Key Concepts

### Procedural Programming

*   Focuses on procedures or functions that perform specific tasks
*   Based on the concept of a procedure call
*   Programs are broken down into a set of procedures or functions
*   Data is shared among procedures through parameters or global variables
*   Procedural Programming is often used for small, simple programs

### Object-Oriented Programming

*   Revolves around the concept of objects and classes
*   Based on the idea of creating objects that have properties and methods
*   Objects can be used to perform specific tasks
*   Data is encapsulated within objects, making it harder to access and modify accidentally
*   OOP is often used for large, complex programs

### Comparison of Procedural and OOP

|  **Characteristics**  | **Procedural Programming** | **Object-Oriented Programming** |
|  --------------------  | ------------------------- | ------------------------------ |
|  **Focus**             | Procedures or functions   | Objects and classes            |
|  **Data Sharing**      | Parameters or global variables | Encapsulated within objects  |
|  **Program Structure** | Broken down into procedures | Based on objects and classes  |
|  **Reusability**       | Low                        | High                          |
|  **Complexity**        | Suitable for small programs | Suitable for large programs   |

## Examples

### Example 1: Procedural Programming

Suppose we want to write a program that calculates the area and perimeter of a rectangle. In Procedural Programming, we would write two separate functions, one for calculating the area and another for calculating the perimeter.

```cpp
#include <iostream>

// Function to calculate the area of a rectangle
int calculateArea(int length, int width) {
    return length * width;
}

// Function to calculate the perimeter of a rectangle
int calculatePerimeter(int length, int width) {
    return 2 * (length + width);
}

int main() {
    int length = 10;
    int width = 5;

    int area = calculateArea(length, width);
    int perimeter = calculatePerimeter(length, width);

    std::cout << "Area: " << area << std::endl;
    std::cout << "Perimeter: " << perimeter << std::endl;

    return 0;
}
```

### Example 2: Object-Oriented Programming

Now, let's write the same program using Object-Oriented Programming. We will create a `Rectangle` class with `length` and `width` properties, and `calculateArea` and `calculatePerimeter` methods.

```cpp
#include <iostream>

class Rectangle {
private:
    int length;
    int width;

public:
    // Constructor to initialize the length and width
    Rectangle(int length, int width) {
        this->length = length;
        this->width = width;
    }

    // Method to calculate the area of the rectangle
    int calculateArea() {
        return length * width;
    }

    // Method to calculate the perimeter of the rectangle
    int calculatePerimeter() {
        return 2 * (length + width);
    }
};

int main() {
    Rectangle rectangle(10, 5);

    int area = rectangle.calculateArea();
    int perimeter = rectangle.calculatePerimeter();

    std::cout << "Area: " << area << std::endl;
    std::cout << "Perimeter: " << perimeter << std::endl;

    return 0;
}
```

## Exam Tips

1.  Understand the characteristics of Procedural Programming and Object-Oriented Programming.
2.  Be able to identify the advantages and disadvantages of each paradigm.
3.  Know how to write programs using both Procedural and OOP styles.
4.  Understand the concept of encapsulation in OOP.
5.  Be able to explain the differences between Procedural and OOP with examples.
6.  Understand how to use classes and objects in OOP.
7.  Practice writing programs that demonstrate the use of Procedural and OOP concepts.