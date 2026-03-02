# Basis Path Testing
## Introduction

Basis path testing is a white-box testing technique used to test the control flow of a program. It is based on the concept of cyclomatic complexity, which measures the complexity of a program's control flow. The goal of basis path testing is to ensure that every possible path through the program is executed at least once, thereby covering all possible scenarios.

Basis path testing is an important technique in software engineering because it helps to identify errors in the program's control flow, such as infinite loops, unreachable code, and incorrect conditional statements. By testing every possible path through the program, basis path testing can help to ensure that the program behaves correctly under all possible inputs and conditions.

## Key Concepts

* **Cyclomatic Complexity**: Cyclomatic complexity is a measure of the complexity of a program's control flow. It is calculated by counting the number of linearly independent paths through the program's control flow graph.
* **Control Flow Graph**: A control flow graph is a graphical representation of a program's control flow. It consists of nodes representing the program's statements and edges representing the flow of control between statements.
* **Basis Paths**: Basis paths are the minimum number of paths required to cover all possible paths through the program's control flow graph.
* **Path Testing**: Path testing is the process of testing each basis path to ensure that it executes correctly.

## Examples

### Example 1: Calculating Cyclomatic Complexity

Consider the following program:
```
if (x > 0) {
  y = x * 2;
} else {
  y = x / 2;
}
```
The control flow graph for this program has 3 nodes and 2 edges. The cyclomatic complexity is therefore 2.

### Example 2: Identifying Basis Paths

Consider the following program:
```
if (x > 0) {
  if (y > 0) {
    z = x + y;
  } else {
    z = x - y;
  }
} else {
  z = x * y;
}
```
The control flow graph for this program has 5 nodes and 4 edges. The basis paths are:
* x > 0, y > 0
* x > 0, y <= 0
* x <= 0

### Example 3: Testing Basis Paths

Consider the following program:
```
int sum(int[] arr) {
  int sum = 0;
  for (int i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
```
The basis paths for this program are:
* arr.length > 0
* arr.length == 0

To test the basis paths, we can write test cases that cover each path. For example:
* Test case 1: arr = [1, 2, 3]
* Test case 2: arr = []

## Exam Tips

1. Understand the concept of cyclomatic complexity and how it is used to calculate the number of basis paths.
2. Be able to draw control flow graphs for simple programs.
3. Identify basis paths from control flow graphs.
4. Write test cases to cover each basis path.
5. Understand the importance of basis path testing in ensuring the correctness of a program.
6. Be able to calculate cyclomatic complexity for simple programs.
7. Understand the limitations of basis path testing.