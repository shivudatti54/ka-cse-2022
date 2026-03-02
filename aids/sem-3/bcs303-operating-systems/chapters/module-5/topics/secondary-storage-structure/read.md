# Control Structures in C++

Control structures are fundamental building blocks of any programming language. They allow you to dictate the flow of execution of your program, enabling you to make decisions, repeat tasks, and jump to different parts of your code based on specific conditions. Mastering control structures is essential for writing logical and efficient C++ programs.

## 1. Introduction to Program Flow

By default, a C++ program executes statements sequentially, from top to bottom. This is known as **sequential flow**.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5;  // Statement 1
    int b = 10; // Statement 2
    int sum = a + b; // Statement 3
    cout << "Sum: " << sum << endl; // Statement 4
    return 0; // Statement 5
}
```

_Output:_

```
Sum: 15
```

Control structures break this sequential flow, allowing for more complex and dynamic behavior. They are categorized into three main types:

1.  **Selection Statements**: Make decisions (`if`, `if-else`, `switch`)
2.  **Iteration Statements**: Create loops (`for`, `while`, `do-while`)
3.  **Jump Statements**: Alter the flow directly (`break`, `continue`, `goto`, `return`)

## 2. Selection Statements

Selection statements allow your program to choose between different paths of execution based on whether a condition is `true` or `false`.

### 2.1 The `if` Statement

The `if` statement executes a block of code only if its condition evaluates to true.

**Syntax:**

```cpp
if (condition) {
    // Code to execute if condition is true
}
```

**Example:**

```cpp
int number = -5;
if (number < 0) {
    cout << number << " is a negative number." << endl;
}
```

_Output:_

```
-5 is a negative number.
```

### 2.2 The `if-else` Statement

The `if-else` statement provides an alternative block of code to execute if the condition is false.

**Syntax:**

```cpp
if (condition) {
    // Code to execute if condition is true
} else {
    // Code to execute if condition is false
}
```

**Example:**

```cpp
int age = 17;
if (age >= 18) {
    cout << "You are eligible to vote." << endl;
} else {
    cout << "You are not eligible to vote." << endl;
}
```

_Output:_

```
You are not eligible to vote.
```

### 2.3 The `if-else-if` Ladder

This structure is used to check multiple conditions in sequence.

**Syntax:**

```cpp
if (condition1) {
    // Code if condition1 is true
} else if (condition2) {
    // Code if condition2 is true
} else if (condition3) {
    // Code if condition3 is true
} else {
    // Code if all conditions are false
}
```

**Example:**

```cpp
int score = 85;
char grade;

if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else if (score >= 70) {
    grade = 'C';
} else if (score >= 60) {
    grade = 'D';
} else {
    grade = 'F';
}
cout << "Your grade is: " << grade << endl;
```

_Output:_

```
Your grade is: B
```

### 2.4 The `switch` Statement

The `switch` statement provides a clean way to dispatch execution to different parts of code based on the value of an expression. It is often more efficient than a long `if-else-if` ladder when comparing the same variable against multiple constant values.

**Syntax:**

```cpp
switch (expression) {
    case constant1:
        // Code for constant1
        break;
    case constant2:
        // Code for constant2
        break;
    ...
    default:
        // Code if no case matches
}
```

**Example:**

```cpp
int dayNumber = 3;
string day;

switch (dayNumber) {
    case 1: day = "Monday"; break;
    case 2: day = "Tuesday"; break;
    case 3: day = "Wednesday"; break;
    case 4: day = "Thursday"; break;
    case 5: day = "Friday"; break;
    case 6: day = "Saturday"; break;
    case 7: day = "Sunday"; break;
    default: day = "Invalid day";
}
cout << "Day " << dayNumber << " is " << day << endl;
```

_Output:_

```
Day 3 is Wednesday
```

**The `break` statement is crucial** inside a `switch`. Without it, execution will "fall through" to the next `case` until a `break` is encountered. Fall-through can be used intentionally for multiple cases to execute the same code.

```cpp
char vowel = 'e';
bool isVowel;

switch (vowel) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
    case 'A':
    case 'E':
    case 'I':
    case 'O':
    case 'U':
        isVowel = true;
        break;
    default:
        isVowel = false;
}
cout << "'" << vowel << "' is a vowel: " << boolalpha << isVowel << endl;
```

_Output:_

```
'e' is a vowel: true
```

## 3. Iteration Statements (Loops)

Loops are used to execute a block of code repeatedly until a specified condition is met.

### 3.1 The `for` Loop

The `for` loop is ideal when you know exactly how many times you want to iterate. It combines initialization, condition checking, and iteration into a single, readable line.

**Syntax:**

```cpp
for (initialization; condition; iteration) {
    // Code to execute in each iteration
}
```

**Flowchart:**

```
      +-----------------+
      | Initialization  |
      +--------+--------+
               |
               v
      +--------+--------+
      |   Condition     +----False----> Exit Loop
      +--------+--------+
               | True
               v
      +--------+--------+
      | Loop Body       |
      | (Code to repeat)|
      +--------+--------+
               |
               v
      +--------+--------+
      |  Iteration     |
      | (e.g., i++)    |
      +--------+--------+
               |
               +<-------+
```

**Example:**

```cpp
// Print numbers from 1 to 5
for (int i = 1; i <= 5; i++) {
    cout << i << " ";
}
```

_Output:_

```
1 2 3 4 5
```

### 3.2 The `while` Loop

The `while` loop repeats a block of code as long as a given condition is true. It is used when the number of iterations is not known beforehand.

**Syntax:**

```cpp
while (condition) {
    // Code to execute
}
```

**Example:**

```cpp
// Countdown from 5
int count = 5;
while (count > 0) {
    cout << count << " ";
    count--;
}
cout << "Liftoff!" << endl;
```

_Output:_

```
5 4 3 2 1 Liftoff!
```

### 3.3 The `do-while` Loop

The `do-while` loop is similar to the `while` loop, but with a key difference: it guarantees that the loop body will be executed **at least once** because the condition is checked at the end of the iteration.

**Syntax:**

```cpp
do {
    // Code to execute
} while (condition);
```

**Example:**

```cpp
// Get user input until it's valid
int number;
do {
    cout << "Enter a positive number: ";
    cin >> number;
} while (number <= 0);

cout << "You entered: " << number << endl;
```

_Possible Output:_

```
Enter a positive number: -5
Enter a positive number: 0
Enter a positive number: 10
You entered: 10
```

### Comparison of Loop Types

| Feature             | `for` Loop                             | `while` Loop                           | `do-while` Loop                                |
| :------------------ | :------------------------------------- | :------------------------------------- | :--------------------------------------------- |
| **Initialization**  | Done within the loop syntax            | Done before the loop                   | Done before the loop                           |
| **Condition Check** | At the **beginning** of each iteration | At the **beginning** of each iteration | At the **end** of each iteration               |
| **Use Case**        | Known number of iterations             | Unknown number of iterations           | Unknown iterations, but must run at least once |
| **Syntax**          | `for(init; cond; iter) { }`            | `while(cond) { }`                      | `do { } while(cond);`                          |

## 4. Jump Statements

Jump statements transfer control unconditionally to another part of the program.

### 4.1 The `break` Statement

The `break` statement terminates the nearest enclosing loop (`for`, `while`, `do-while`) or `switch` statement. Control is passed to the statement immediately following the terminated loop or switch.

**Example in a loop:**

```cpp
// Search for a number and break when found
int numbers[] = {10, 20, 30, 40, 50};
int target = 30;

for (int num : numbers) {
    if (num == target) {
        cout << "Target found!" << endl;
        break; // Exit the loop immediately
    }
    cout << "Checking " << num << "... Not the target." << endl;
}
```

_Output:_

```
Checking 10... Not the target.
Checking 20... Not the target.
Target found!
```

### 4.2 The `continue` Statement

The `continue` statement skips the rest of the current iteration of a loop and immediately jumps to the next iteration (i.e., it goes back to checking the loop condition).

**Example:**

```cpp
// Print only odd numbers between 1 and 10
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) { // If the number is even...
        continue; // ...skip the printing code.
    }
    cout << i << " ";
}
```

_Output:_

```
1 3 5 7 9
```

### 4.3 The `goto` Statement

The `goto` statement performs an unconditional jump to a labeled statement in the same function. Its use is **highly discouraged** in modern C++ as it can make code very difficult to read, understand, and maintain (often called "spaghetti code"). It is mentioned here for completeness.

**Syntax:**

```cpp
goto label;
...
...
label:
// Code
```

## 5. Nested Control Structures

Control structures can be placed inside other control structures. This is known as **nesting**.

**Example: Nested `for` loops to print a pattern**

```cpp
// Print a right-angled triangle of stars
int rows = 5;

for (int i = 1; i <= rows; ++i) { // Outer loop for rows
    for (int j = 1; j <= i; ++j) { // Inner loop for columns in each row
        cout << "* ";
    }
    cout << endl; // Move to the next line after each row
}
```

_Output:_

```
*
* *
* * *
* * * *
* * * * *
```

## 6. Best Practices and Common Pitfalls

1.  **Always use braces `{}`**: Even if a block contains only one statement, using braces prevents errors when adding more statements later.

    ```cpp
    // Good practice
    if (condition) {
        doSomething();
    }

    // Risky practice
    if (condition)
        doSomething(); // Adding another line here will break the logic.
    ```

2.  **Avoid infinite loops**: Ensure your loop's condition will eventually become false. A loop like `while(true)` requires a `break` statement inside to exit.

    ```cpp
    // Infinite loop (BAD)
    while (1) {
        cout << "This will print forever!" << endl;
    }

    // Controlled infinite loop with break (GOOD)
    while (true) {
        int input;
        cin >> input;
        if (input == 0) break;
        // process input
    }
    ```

3.  **Prefer `for` loops for counting**: When you know the number of iterations, a `for` loop is almost always the clearest choice.

4.  **Choose `switch` for multi-way branches**: When comparing one variable against many constant values, a `switch` statement is more efficient and readable than a long `if-else-if` chain.

5.  **Minimize `goto` usage**: Favor structured loops (`break`, `continue`) and functions over `goto` for managing control flow.

## Exam Tips

- **Understand the difference**: Be clear on when to use `if-else` (conditions involving ranges or complex expressions) vs. `switch` (matching a single value against discrete constants).
- **Trace the code**: For exam questions, manually trace through loop iterations and condition checks. Use a table to track variable values.
- **Watch for off-by-one errors**: A common mistake in loops is iterating one time too many or too few (e.g., `i < 5` vs. `i <= 5`).
- **Remember `break` in `switch`**: Forgetting a `break` statement is a frequent source of bugs in `switch` cases, causing unintended fall-through.
- **`do-while` guarantees one execution**: A question might try to trick you by showing a `do-while` loop with a condition that is false from the start. Remember, the body will still execute once.
