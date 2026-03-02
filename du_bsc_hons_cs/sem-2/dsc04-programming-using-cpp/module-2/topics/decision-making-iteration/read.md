# Decision Making and Iteration in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Table of Contents

1. [Introduction and Learning Objectives](#1-introduction-and-learning-objectives)
2. [Decision Making Statements](#2-decision-making-statements)
3. [Iteration Statements (Loops)](#3-iteration-statements-loops)
4. [Loop Control Statements: break and continue](#4-loop-control-statements-break-and-continue)
5. [Nested Loops](#5-nested-loops)
6. [Common Programming Patterns](#6-common-programming-patterns)
7. [Real-World Applications](#7-real-world-applications)
8. [Common Pitfalls and Best Practices](#8-common-pitfalls-and-best-practice)
9. [Multiple Choice Questions](#9-multiple-choice-questions)
10. [Flashcards: Application-Based Learning](#10-flashcards-application-based-learning)
11. [Key Takeaways](#11-key-takeaways)

---

## 1. Introduction and Learning Objectives

### Overview

Decision making and iteration form the backbone of procedural programming. In C++, these constructs allow programs to make choices based on conditions and repeat actions efficiently. This topic is foundational for the Delhi University BSc (Hons) Computer Science curriculum under the NEP 2024 UGCF framework, specifically aligned with the "Programming Using C++" paper.

### Real-World Relevance

Consider these practical scenarios:

- **Banking Systems**: Validating ATM withdrawals requires decision making (if balance > withdrawal amount, proceed; else show error)
- **Game Development**: Game loops run continuously until the player quits, processing input and rendering graphics each iteration
- **Data Processing**: Iterating through thousands of student records to calculate GPA or filter results
- **E-commerce Platforms**: Calculating shipping costs based on weight ranges using decision ladders

### Learning Objectives

By the end of this unit, you will be able to:

1. Implement all types of decision-making constructs in C++
2. Choose appropriate loop types for different scenarios
3. Design nested loop solutions for matrix and pattern problems
4. Analyze time complexity of iterative constructs
5. Avoid common pitfalls in loop and decision implementations

---

## 2. Decision Making Statements

### 2.1 The `if` Statement

The `if` statement is the simplest form of decision making. It executes a block of code only when a specified condition evaluates to `true`.

**Syntax:**

```cpp
if (condition) {
    // statements to execute if condition is true
}
```

**Important Points:**
- The condition must evaluate to a boolean value (non-zero values are treated as `true`)
- Always use curly braces `{}` even for single statements for code clarity and maintainability

**Example 1: Checking Voting Eligibility**

```cpp
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: ";
    cin >> age;
    
    if (age >= 18) {
        cout << "You are eligible to vote!" << endl;
    }
    
    cout << "Program continues..." << endl;
    return 0;
}
```

### 2.2 The `if-else` Statement

The `if-else` statement provides an alternative path when the condition is false.

**Syntax:**

```cpp
if (condition) {
    // statements if condition is true
} else {
    // statements if condition is false
}
```

**Example 2: Finding Maximum of Two Numbers**

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, max;
    
    cout << "Enter two numbers: ";
    cin >> a >> b;
    
    if (a > b) {
        max = a;
    } else {
        max = b;
    }
    
    cout << "Maximum: " << max << endl;
    return 0;
}
```

### 2.3 The `else-if` Ladder

For multiple conditions tested sequentially, use the `else-if` structure.

**Syntax:**

```cpp
if (condition1) {
    // block 1
} else if (condition2) {
    // block 2
} else if (condition3) {
    // block 3
} else {
    // default block
}
```

**Example 3: Grade Classification System**

```cpp
#include <iostream>
using namespace std;

int main() {
    int marks;
    char grade;
    
    cout << "Enter marks (0-100): ";
    cin >> marks;
    
    if (marks >= 90) {
        grade = 'O';  // Outstanding
    } else if (marks >= 80) {
        grade = 'A';
    } else if (marks >= 70) {
        grade = 'B';
    } else if (marks >= 60) {
        grade = 'C';
    } else if (marks >= 50) {
        grade = 'D';
    } else {
        grade = 'F';
    }
    
    cout << "Grade: " << grade << endl;
    return 0;
}
```

### 2.4 The `switch` Statement

The `switch` statement provides a cleaner way to handle multiple discrete values compared to else-if ladders, especially when comparing a single variable against constant values.

**Syntax:**

```cpp
switch (expression) {
    case constant1:
        // statements
        break;
    case constant2:
        // statements
        break;
    default:
        // default statements
}
```

**Key Rules:**
- The expression must evaluate to an integral type (`int`, `char`, `enum`) or a class type with conversion operators
- Each `case` label must be a constant expression
- The `break` statement prevents fall-through (unless intentionally used)
- The `default` case is optional

**Example 4: Simple Calculator**

```cpp
#include <iostream>
using namespace std;

int main() {
    char op;
    int a, b, result;
    
    cout << "Enter operation (+, -, *, /): ";
    cin >> op;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    
    switch (op) {
        case '+':
            result = a + b;
            break;
        case '-':
            result = a - b;
            break;
        case '*':
            result = a * b;
            break;
        case '/':
            if (b != 0) {
                result = a / b;
            } else {
                cout << "Error: Division by zero!" << endl;
                return 1;
            }
            break;
        default:
            cout << "Invalid operation!" << endl;
            return 1;
    }
    
    cout << "Result: " << result << endl;
    return 0;
}
```

### 2.5 The `goto` Statement (Historical Note)

While present in C++, the `goto` statement is generally discouraged in structured programming. It allows unconditional jumping within a function. However, for the sake of completeness in the Delhi University syllabus:

**Syntax:**

```cpp
label:
    statement;

goto label;  // jumps to the labeled statement
```

**Warning:** Excessive use of `goto` leads to "spaghetti code." Modern C++ prefers structured constructs like loops and functions.

---

## 3. Iteration Statements (Loops)

Iteration statements (loops) allow repeated execution of a block of code. C++ provides four loop constructs.

### 3.1 The `while` Loop

The `while` loop repeats a statement or block as long as its condition remains true. The condition is evaluated before each iteration.

**Syntax:**

```cpp
while (condition) {
    // loop body - executed repeatedly while condition is true
}
```

**Key Characteristic:** Zero or more iterations (if condition is false initially)

**Example 5: Calculating Factorial**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    unsigned long long factorial = 1;
    
    cout << "Enter a non-negative integer: ";
    cin >> n;
    
    if (n < 0) {
        cout << "Error: Factorial not defined for negative numbers!" << endl;
        return 1;
    }
    
    int i = 1;
    while (i <= n) {
        factorial *= i;
        i++;
    }
    
    cout << n << "! = " << factorial << endl;
    return 0;
}
```

### 3.2 The `do-while` Loop

The `do-while` loop is similar to `while`, but it executes the loop body **at least once** before checking the condition.

**Syntax:**

```cpp
do {
    // loop body - executed at least once
} while (condition);
```

**Key Characteristic:** One or more iterations (guaranteed at least one execution)

**Example 6: Menu-Driven Program**

```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    
    do {
        cout << "\n=== MAIN MENU ===" << endl;
        cout << "1. Check Balance" << endl;
        cout << "2. Deposit Money" << endl;
        cout << "3. Withdraw Money" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1:
                cout << "Your balance is: Rs. 10,000" << endl;
                break;
            case 2:
                cout << "Processing deposit..." << endl;
                break;
            case 3:
                cout << "Processing withdrawal..." << endl;
                break;
            case 4:
                cout << "Thank you for using our service!" << endl;
                break;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    } while (choice != 4);
    
    return 0;
}
```

### 3.3 The `for` Loop

The `for` loop provides a compact way to iterate when the number of iterations is known.

**Syntax:**

```cpp
for (initialization; condition; increment/decrement) {
    // loop body
}
```

**Components:**
1. **Initialization**: Executed once before the loop begins
2. **Condition**: Evaluated before each iteration; loop continues if true
3. **Increment/Decrement**: Executed after each iteration

**Key Characteristic:** Zero or more iterations

**Example 7: Fibonacci Series**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, t1 = 0, t2 = 1, nextTerm;
    
    cout << "Enter number of terms: ";
    cin >> n;
    
    cout << "Fibonacci Series: ";
    
    for (int i = 1; i <= n; ++i) {
        cout << t1;
        if (i < n) cout << ", ";
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    
    cout << endl;
    return 0;
}
```

### 3.4 Range-Based `for` Loop (C++11)

Modern C++ introduces the range-based for loop for easier iteration over containers.

**Syntax:**

```cpp
for (variable : container) {
    // statements
}
```

**Example:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers = {10, 20, 30, 40, 50};
    
    cout << "Elements: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    // Using auto for type inference
    cout << "Squares: ";
    for (auto num : numbers) {
        cout << num * num << " ";
    }
    cout << endl;
    
    return 0;
}
```

---

## 4. Loop Control Statements: `break` and `continue`

### 4.1 The `break` Statement

The `break` statement terminates the nearest enclosing loop or switch statement immediately.

**Example: Prime Number Check**

```cpp
#include <iostream>
using namespace std;

int main() {
    int num;
    bool isPrime = true;
    
    cout << "Enter a positive integer: ";
    cin >> num;
    
    if (num <= 1) {
        isPrime = false;
    } else {
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                isPrime = false;
                break;  // Exit loop as soon as we find a divisor
            }
        }
    }
    
    if (isPrime) {
        cout << num << " is a prime number." << endl;
    } else {
        cout << num << " is not a prime number." << endl;
    }
    
    return 0;
}
```

### 4.2 The `continue` Statement

The `continue` statement skips the rest of the current iteration and proceeds to the next iteration of the loop.

**Example: Printing Odd Numbers Only**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    
    cout << "Enter the limit: ";
    cin >> n;
    
    cout << "Odd numbers from 1 to " << n << ": ";
    
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            continue;  // Skip even numbers
        }
        cout << i << " ";
    }
    
    cout << endl;
    return 0;
}
```

### 4.3 Comparing `break` and `continue`

| Aspect | `break` | `continue` |
|--------|---------|------------|
| Behavior | Exits the loop entirely | Skips to next iteration |
| Applicable To | Loops and switch | Loops only |
| After Execution | Control flows to statement after loop | Control flows to loop condition |

---

## 5. Nested Loops

A nested loop consists of one loop inside another. The inner loop completes all its iterations for each single iteration of the outer loop.

### 5.1 Nested `for` Loops

**Example: Multiplication Table**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    
    cout << "Enter a number for multiplication table: ";
    cin >> n;
    
    cout << "\nMultiplication Table of " << n << ":\n";
    for (int i = 1; i <= 10; i++) {
        cout << n << " x " << i << " = " << n * i << endl;
    }
    
    return 0;
}
```

### 5.2 Nested While Loops

**Example: Sum of Digits Until Single Digit**

```cpp
#include <iostream>
using namespace std;

int main() {
    int num, sum;
    
    cout << "Enter a number: ";
    cin >> num;
    
    // Keep reducing to single digit
    while (num >= 10) {
        sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        num = sum;
        cout << "Reduced to: " << num << endl;
    }
    
    cout << "Final digit: " << num << endl;
    return 0;
}
```

### 5.3 Pattern Printing (Examination Favorite)

**Example: Right Triangle Pattern**

```
*
**
***
****
*****
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows;
    
    cout << "Enter number of rows: ";
    cin >> rows;
    
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    return 0;
}
```

**Example: Inverted Pyramid**

```
*****
****
***
**
*
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int rows;
    
    cout << "Enter number of rows: ";
    cin >> rows;
    
    for (int i = rows; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
    
    return 0;
}
```

### 5.4 Matrix Operations

**Example: Matrix Addition**

```cpp
#include <iostream>
using namespace std;

int main() {
    int r, c;
    
    cout << "Enter rows and columns: ";
    cin >> r >> c;
    
    int A[10][10], B[10][10], C[10][10];
    
    cout << "Enter elements of matrix A:\n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> A[i][j];
        }
    }
    
    cout << "Enter elements of matrix B:\n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> B[i][j];
        }
    }
    
    // Addition
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    
    cout << "Resultant Matrix:\n";
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

---

## 6. Common Programming Patterns

### 6.1 Infinite Loops

Sometimes intentionally used in server programs or game loops:

```cpp
// Using for loop
for (;;) {
    // runs forever
}

// Using while loop
while (true) {
    // runs forever
}
```

**Important:** Always provide an exit condition using `break` or `return`.

### 6.2 Loop with Multiple Conditions

```cpp
// Find first number divisible by both 3 and 7
int i = 1;
while (i <= 1000 && !(i % 3 == 0 && i % 7 == 0)) {
    i++;
}
cout << "First number: " << i << endl;
```

### 6.3 Comma Operator in Loops

```cpp
// Print table of 5, stopping when product exceeds 50
for (int i = 1; i <= 10; cout << (5 * i++) << endl) {
    if (5 * i > 50) break;
}
```

---

## 7. Real-World Applications

### 7.1 Traffic Light Simulation

```cpp
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;

int main() {
    while (true) {
        cout << "RED - Stop!" << endl;
        this_thread::sleep_for(chrono::seconds(3));
        
        cout << "GREEN - Go!" << endl;
        this_thread::sleep_for(chrono::seconds(3));
        
        cout << "YELLOW - Prepare to stop!" << endl;
        this_thread::sleep_for(chrono::seconds(1));
    }
    return 0;
}
```

### 7.2 Simple Authentication System

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string correctPassword = "admin123";
    string enteredPassword;
    int attempts = 0;
    const int MAX_ATTEMPTS = 3;
    
    while (attempts < MAX_ATTEMPTS) {
        cout << "Enter password: ";
        cin >> enteredPassword;
        
        if (enteredPassword == correctPassword) {
            cout << "Access Granted!" << endl;
            return 0;
        } else {
            attempts++;
            cout << "Incorrect password. " << (MAX_ATTEMPTS - attempts) << " attempts left." << endl;
        }
    }
    
    cout << "Account locked due to multiple failed attempts." << endl;
    return 1;
}
```

---

## 8. Common Pitfalls and Best Practices

### Pitfalls

1. **Off-by-One Errors**: Using `<=` instead of `<` or vice versa
   ```cpp
   // Common mistake: prints 0 to 9 instead of 1 to 10
   for (int i = 0; i <= 10; i++)  // Should be i < 10 or i <= 9
   ```

2. **Infinite Loops**: Forgetting to update loop variable
   ```cpp
   int i = 1;
   while (i <= 10) {
       cout << i;  // Missing i++ causes infinite loop
   }
   ```

3. **Floating-Point Comparison in Loops**
   ```cpp
   // Dangerous: floating-point comparison
   for (double d = 0.1; d != 1.0; d += 0.1)  // May never equal exactly
   ```

4. **Missing Braces**: Leads to the "goto fail" bug
   ```cpp
   if (condition)
       doThis();
       doThat();  // Always executes (not part of if)
   ```

### Best Practices

1. **Initialize loop variables before use**
2. **Prefer `<` over `<=` for clarity**
3. **Use meaningful variable names** (`i`, `j` for simple counters; descriptive names for complex loops)
4. **Limit nested loops to 2-3 levels** for readability
5. **Always use braces** even for single statements
6. **Consider using algorithms** (`std::find`, `std::count`) for complex iterations

---

## 9. Multiple Choice Questions

### Conceptual Questions

**Q1.** What is the output of the following code?

```cpp
int x = 5;
if (x = 10) {
    cout << "True";
} else {
    cout << "False";
}
```

A) True  
B) False  
C) Compilation Error  
D) Undefined Behavior  

**Answer: A** — Here, `x = 10` is an assignment, not comparison. It assigns 10 to x and evaluates to 10 (non-zero), which is true.

---

**Q2.** What does `break` do inside a nested loop?

A) Exits only the innermost loop  
B) Exits all loops  
C) Skips current iteration of all loops  
D) No effect on loops  

**Answer: A** — `break` terminates only the nearest enclosing loop.

---

**Q3.** Which loop guarantees at least one execution?

A) while  
B) for  
C) do-while  
D) All of the above  

**Answer: C** — do-while checks condition after the first iteration.

---

**Q4.** What is the time complexity of a single for loop from 1 to n?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)  

**Answer: B** — The loop executes n times.

---

**Q5.** In a switch statement, what happens if `break` is omitted after a case?

A) Compilation Error  
B) Runtime Error  
C) Fall-through to next case  
D) Exit the switch  

**Answer: C** — Without break, execution continues to the next case (fall-through).

---

**Q6.** What is the output?

```cpp
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == j) continue;
        cout << i << j << " ";
    }
}
```

A) 01 02 12 20 21  
B) 01 02 12 20 21 10  
C) 01 02 12 20 21 22  
D) 01 02 12  

**Answer: A** — When i == j, the inner continue skips printing, resulting in pairs where i ≠ j.

---

**Q7.** Which is NOT a valid loop in C++?

A) while  
B) do-while  
C) repeat-until  
D) for  

**Answer: C** — C++ does not have a `repeat-until` loop.

---

**Q8.** What is the output?

```cpp
int i = 0;
while (i++ < 5) {
    cout << i << " ";
}
```

A) 0 1 2 3 4  
B) 1 2 3 4 5  
C) 0 1 2 3 4 5  
D) 1 2 3 4  

**Answer: B** — Post-increment returns old value, then increments. So comparison happens with 0, but i becomes 1 before printing.

---

**Q9.** The continue statement:

A) Exits the loop  
B) Exits the program  
C) Skips to the next iteration  
D) Jumps to a label  

**Answer: C** — continue skips remaining statements in the current iteration.

---

**Q10.** What is the maximum number of times the following loop executes?

```cpp
int n = -5;
while (n > 0) {
    cout << n;
    n--;
}
```

A) 5  
B) 0  
C) Infinite  
D) -5  

**Answer: B** — Condition is false initially (n = -5 is not > 0), so zero iterations.

---

### Application-Based Questions

**Q11.** What is the output?

```cpp
int count = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;
    count++;
}
cout << count;
```

A) 5  
B) 10  
C) 6  
D) 4  

**Answer: A** — Counts odd numbers from 1 to 10: 1, 3, 5, 7, 9 → 5 numbers.

---

**Q12.** What is the output?

```cpp
int x = 0;
for (;;) {
    if (x > 3) break;
    x++;
}
cout << x;
```

A) 0  
B) 3  
C) 4  
D) Infinite  

**Answer: C** — Loop increments until x > 3, then breaks. Final value is 4.

---

**Q13.** Which loop is best suited for iterating over a container when the number of elements is unknown?

A) for loop  
B) while loop  
C) do-while loop  
D) switch  

**Answer: B** — while loop is ideal when the iteration count is not predetermined.

---

**Q14.** What will be printed?

```cpp
int i = 1;
while (i < 3) {
    int j = i;
    while (j < 3) {
        cout << j;
        j++;
    }
    i++;
}
```

A) 1 2  
B) 1 2 2  
C) 1 12 2  
D) 1 2 1 2  

**Answer: B** — First iteration: j=1 prints 1,2. Second iteration: j=2 prints 2.

---

**Q15.** In a nested loop (outer loop n times, inner loop m times), how many total iterations occur?

A) n + m  
B) n * m  
C) n^m  
D) max(n, m)  

**Answer: B** — Total iterations = n × m (Cartesian product).

---

### Performance and Common Mistakes

**Q16.** What is the most efficient way to check if a number is prime?

A) Check divisibility by all numbers from 2 to n-1  
B) Check divisibility by all odd numbers from 3 to √n  
C) Check divisibility by all even numbers  
D) Use a switch statement  

**Answer: B** — Checking only up to √n reduces time complexity from O(n) to O(√n).

---

**Q17.** What is wrong with the following code?

```cpp
int *ptr = new int[10];
for (int i = 0; i <= 10; i++) {
    ptr[i] = i;
}
```

A) Memory leak  
B) Array index out of bounds (buffer overflow)  
C) Syntax error  
D) Nothing wrong  

**Answer: B** — The loop goes from 0 to 10 (11 iterations), but array size is 10 (indices 0-9). Writing to ptr[10] causes buffer overflow.

---

**Q18.** What does this code print?

```cpp
int n = 12345, sum = 0;
while (n > 0) {
    sum += n % 10;
    n /= 10;
}
cout << sum;
```

A) 12345  
B) 15  
C) 54321  
D) 1  

**Answer: B** — Extracts digits: 5 + 4 + 3 + 2 + 1 = 15.

---

**Q19.** Which statement about switch is FALSE?

A) case labels must be constant expressions  
B) switch can only test integral types  
C) default must be the last case  
D) break is optional  

**Answer: C** — default can appear anywhere in the switch, not necessarily last.

---

**Q20.** What is the output?

```cpp
char grade = 'B';
switch (grade) {
    case 'A': cout << "Excellent"; break;
    case 'B': cout << "Good";
    case 'C': cout << "Average"; break;
    default: cout << "Invalid";
}
```

A) Good  
B) GoodAverage  
C) GoodInvalid  
D) Average  

**Answer: B** — Missing break after 'B' causes fall-through to 'C', printing "GoodAverage".

---

## 10. Flashcards: Application-Based Learning

### Flashcard 1
**Q:** Write a C++ program to check whether a number is a palindrome using a while loop.

**A:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int num, original, reversed = 0, digit;
    
    cout << "Enter a number: ";
    cin >> num;
    original = num;
    
    while (num > 0) {
        digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }
    
    if (original == reversed) {
        cout << "Palindrome" << endl;
    } else {
        cout << "Not a palindrome" << endl;
    }
    return 0;
}
```

---

### Flashcard 2
**Q:** Explain the difference between `while` and `do-while` with a practical example where they behave differently.

**A:**
- **while**: Condition checked before iteration. If false initially, loop body never executes.
- **do-while**: Condition checked after iteration. Loop body always executes at least once.

**Example:** Password validation
- Using `while`: If no password entered, loop doesn't run → no error message
- Using `do-while`: At least prompts once → ensures user gets feedback

---

### Flashcard 3
**Q:** Write a program to generate the following pattern using nested loops:
```
1
1 2
1 2 3
1 2 3 4
```

**A:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}
```

---

### Flashcard 4
**Q:** Why is `goto` generally avoided in modern programming? Provide an example of how to rewrite a goto-based code without it.

**A:**
`goto` creates "spaghetti code" - difficult to follow program flow. Modern structured programming prefers:
- Loops (for, while, do-while)
- Functions
- break/continue

**Example rewrite:**
```cpp
// With goto (avoid this)
loop:
    // code
    if (condition) goto loop;

// Without goto (preferred)
while (condition) {
    // code
}
```

---

### Flashcard 5
**Q:** Write a program to find the sum of the series: 1 + 1/2 + 1/3 + ... + 1/n using a for loop.

**A:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    double sum = 0.0;
    
    cout << "Enter n: ";
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / i;
    }
    
    cout << "Sum = " << sum << endl;
    return 0;
}
```

---

### Flashcard 6
**Q:** What will be the output of this code? Trace the execution manually.

```cpp
int i = 5, j = 0;
while (i--) {
    j++;
    if (i == 2) continue;
    cout << i << " ";
}
cout << "\nFinal j = " << j;
```

**A:**
**Execution trace:**
- i=5: print 4, j=1
- i=4: print 3, j=2  
- i=3: print 2, j=3
- i=2: continue (skip print), j=4
- i=1: print 0, j=5
- i=0: loop ends (i becomes -1 after decrement)

**Output:** `4 3 2 0`  
**Final j = 5**

---

### Flashcard 7
**Q:** Write a menu-driven program using do-while and switch to perform basic arithmetic operations.

**A:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int choice;
    double a, b;
    
    do {
        cout << "\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;
        
        if (choice >= 1 && choice <= 4) {
            cout << "Enter two numbers: ";
            cin >> a >> b;
        }
        
        switch (choice) {
            case 1: cout << "Result: " << a + b << endl; break;
            case 2: cout << "Result: " << a - b << endl; break;
            case 3: cout << "Result: " << a * b << endl; break;
            case 4: 
                if (b != 0) cout << "Result: " << a / b << endl;
                else cout << "Error: Division by zero\n";
                break;
            case 5: cout << "Exiting...\n"; break;
            default: cout << "Invalid choice\n";
        }
    } while (choice != 5);
    
    return 0;
}
```

---

### Flashcard 8
**Q:** Explain why checking `i * i <= n` might cause overflow and how to avoid it when checking for prime numbers.

**A:**
When `i * i` exceeds the range of `int`, overflow occurs (undefined behavior).

**Solution:** Use `i <= n / i` instead of `i * i <= n`

**Example:**
```cpp
// Potential overflow for large n
for (int i = 2; i * i <= n; i++)

// Safe alternative
for (int i = 2; i <= n / i; i++)
```

---

## 11. Key Takeaways

### Decision Making Statements
1. **`if`**: Executes block conditionally (0 or 1 execution)
2. **`if-else`**: Provides two mutually exclusive paths
3. **`else-if` ladder**: Handles multiple sequential conditions (evaluated top-to-bottom)
4. **`switch`**: Efficient for discrete value matching; uses break to prevent fall-through
5. **`goto`**: Avoid in modern code; leads to unstructured "spaghetti code"

### Iteration Statements
1. **`while`**: Pre-test loop (0+ iterations); use when iteration count unknown
2. **`do-while`**: Post-test loop (1+ iterations); guarantees at least one execution
3. **`for`**: Pre-test loop with initialization; ideal when iterations known
4. **Range-based for**: Modern C++11+ feature for container iteration

### Loop Control
- **`break`**: Exits the nearest loop/switch immediately
- **`continue`**: Skips to next iteration of the loop

### Nested Loops
- Outer loop controls rows; inner loop controls columns
- Total iterations = outer × inner
- Common applications: pattern printing, matrix operations, multi-dimensional data processing

### Best Practices
- Initialize loop variables
- Ensure termination conditions are met
- Prefer `<` over `<=` for clarity
- Use meaningful variable names
- Always use braces for blocks
- Avoid deep nesting (>3 levels)

### Delhi University Syllabus Alignment
This content covers:
- Unit I: Fundamentals of C++ — Decision making constructs
- Unit II: Control structures — All loop types
- Unit III: Practical applications — Pattern problems, menu-driven programs
- Unit IV: Common errors — Off-by-one, infinite loops, buffer overflow

---

*Generated for BSc (Hons) Computer Science — Delhi University, NEP 2024 UGCF Curriculum*