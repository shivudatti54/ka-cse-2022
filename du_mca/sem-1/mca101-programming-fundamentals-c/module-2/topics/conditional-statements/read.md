# Conditional Statements
## Introduction

Conditional statements are a fundamental concept in programming that allow you to control the flow of your program based on certain conditions or decisions. They enable you to write code that can adapt to different situations and make decisions based on user input, data, or other factors. In this topic, we will explore the different types of conditional statements in programming, their syntax, and how to use them effectively.

Conditional statements are crucial in programming because they allow you to write code that can handle different scenarios and make decisions based on various conditions. Without conditional statements, your code would be linear and unable to adapt to changing circumstances. In real-world applications, conditional statements are used extensively in decision-making algorithms, data validation, and user interaction.

## Key Concepts

### 1. If Statement

The if statement is the most basic type of conditional statement. It checks a condition and executes a block of code if the condition is true. The syntax of an if statement is as follows:

```
if (condition) {
    // code to be executed
}
```

### 2. If-Else Statement

The if-else statement is an extension of the if statement. It checks a condition and executes one block of code if the condition is true and another block of code if the condition is false. The syntax of an if-else statement is as follows:

```
if (condition) {
    // code to be executed if condition is true
} else {
    // code to be executed if condition is false
}
```

### 3. If-Else If Statement

The if-else if statement is used to check multiple conditions and execute different blocks of code based on those conditions. The syntax of an if-else if statement is as follows:

```
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition1 is false and condition2 is true
} else {
    // code to be executed if both condition1 and condition2 are false
}
```

### 4. Switch Statement

The switch statement is used to execute different blocks of code based on the value of a variable or expression. The syntax of a switch statement is as follows:

```
switch (expression) {
    case value1:
        // code to be executed if expression equals value1
        break;
    case value2:
        // code to be executed if expression equals value2
        break;
    default:
        // code to be executed if expression does not equal any of the values
        break;
}
```

## Examples

### Example 1: If Statement

Write a program that checks if a number is positive or not.

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    
    if (num > 0) {
        printf("%d is a positive number.\n", num);
    }
    
    return 0;
}
```

### Example 2: If-Else Statement

Write a program that checks if a number is even or odd.

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    
    if (num % 2 == 0) {
        printf("%d is an even number.\n", num);
    } else {
        printf("%d is an odd number.\n", num);
    }
    
    return 0;
}
```

### Example 3: Switch Statement

Write a program that checks the day of the week based on a number.

```c
#include <stdio.h>

int main() {
    int day;
    printf("Enter a number (1-7): ");
    scanf("%d", &day);
    
    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        case 7:
            printf("Sunday\n");
            break;
        default:
            printf("Invalid day\n");
            break;
    }
    
    return 0;
}
```

## Exam Tips

1. Understand the syntax and usage of if, if-else, and switch statements.
2. Practice writing programs that use conditional statements to solve real-world problems.
3. Learn to use conditional statements to handle different scenarios and make decisions based on user input or data.
4. Understand the importance of using break statements in switch statements.
5. Be able to identify and correct errors in conditional statements.
6. Learn to use conditional statements to validate user input and handle errors.
7. Understand the difference between if-else and switch statements and when to use each.