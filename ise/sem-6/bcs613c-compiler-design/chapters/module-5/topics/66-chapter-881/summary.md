### 6.6 Chapter 8: 8.1 - Control Flow Variants

#### Revision Notes

**Key Concepts:**

- **Control Flow Statements:** Statements that control the flow of a program's execution.
- **Conditional Statements:** Used to execute different blocks of code based on conditions.
- **Loops:** Used to execute blocks of code repeatedly.
- **Jump Statements:** Used to transfer control to different parts of the program.

### Control Flow Variants

- **If-Else Statements:**
  - Definition: Used to execute different blocks of code based on conditions.
  - Syntax: `if (condition) { statement } else { statement }`
  - Example: `if (x > 5) { y = x * 2; } else { y = x / 2; }`

- **Switch Statements:**
  - Definition: Used to execute different blocks of code based on the value of a variable.
  - Syntax: `switch (expression) { case value1: statement; break; case value2: statement; break; ... }`
  - Example: `switch (day) { case "Monday": System.out.println("Today is Monday"); break; case "Tuesday": System.out.println("Today is Tuesday"); break; ... }`

- **For Loops:**
  - Definition: Used to execute a block of code repeatedly for a specified number of iterations.
  - Syntax: `for (initialization; condition; increment/decrement) { statement }`
  - Example: `for (int i = 0; i < 5; i++) { System.out.println(i); }`

- **While Loops:**
  - Definition: Used to execute a block of code repeatedly while a specified condition is true.
  - Syntax: `while (condition) { statement }`
  - Example: `int i = 0; while (i < 5) { System.out.println(i); i++; }`

- **Do-While Loops:**
  - Definition: Used to execute a block of code repeatedly while a specified condition is true.
  - Syntax: `do { statement } while (condition)`
  - Example: `int i = 0; do { System.out.println(i); i++; } while (i < 5);`

### Important Formulas and Theorems

- **Postcondition:** A statement about the state of the program after executing a sequence of statements.
- **Precondition:** A statement about the state of the program before executing a sequence of statements.
- **Refinement:** A method of specifying a program's behavior by breaking it down into smaller, more manageable pieces.

### Key Definitions

- **Termination:** The process of halting the execution of a program.
- **Concurrency:** The ability of multiple tasks to execute simultaneously.
- **Synchronization:** The process of coordinating the execution of multiple tasks to avoid conflicts.

### Important Definitions

- **Control Flow Graph (CFG):** A graph that represents the control flow of a program.
- **Reachability:** The ability of a program to execute certain statements.
- **Termination Property:** A property that ensures a program will eventually terminate.
