# Arrays And Expressions – C++ Programming

## Introduction

In C++ programming, **arrays** serve as fundamental data structures for storing multiple elements of the same data type in contiguous memory locations, while **expressions** combine operators and operands to compute values. These concepts form the backbone of algorithmic problem-solving and are essential for the Delhi University NEP 2024 UGCF syllabus in Programming Using C++.

## Key Concepts

### Arrays
- **Definition**: A collection of elements of the same type stored in contiguous memory locations, accessed via an index
- **One-Dimensional Arrays**:
  - Declaration: `data_type array_name[size];`
  - Initialization: `int arr[5] = {1, 2, 3, 4, 5};` or `int arr[] = {1, 2, 3};`
  - Accessing elements: `arr[0]` to `arr[size-1]` (0-based indexing)
- **Two-Dimensional Arrays**:
  - Declaration: `data_type array_name[rows][cols];`
  - Initialization: `int matrix[2][3] = {{1,2,3}, {4,5,6}};`
  - Row-major and column-major representation
- **Multidimensional Arrays**: Arrays with more than two dimensions (e.g., `int arr[2][3][4]`)
- **Static vs Dynamic Arrays**: Static arrays have fixed size at compile time; dynamic arrays use pointers and memory allocation
- **Common Operations**: Traversal, searching (linear/binary), sorting (bubble, selection)
- **Limitations**: Fixed size, homogeneous data type, no built-in bounds checking

### Expressions and Operators
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%` (modulus)
- **Relational Operators**: `<`, `>`, `<=`, `>=`, `==`, `!=`
- **Logical Operators**: `&&` (AND), `||` (OR), `!` (NOT)
- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- **Increment/Decrement**: `++` (prefix/postfix), `--` (prefix/postfix)
- **Operator Precedence**: 
  - Highest: `()` → `++`, `--` → `*`, `/`, `%` → `+`, `-` → `<`, `>`, `<=`, `>=` → `==`, `!=` → `&&` → `||` → `=` 
  - Use parentheses to override precedence
- **Type Conversion**: Implicit (automatic) and explicit (casting) conversions in expressions
- **Compound Expressions**: Multiple operators in a single expression evaluation

### String Arrays (Character Arrays)
- Declaration: `char name[20];`
- String handling functions: `strlen()`, `strcpy()`, `strcmp()`, `strcat()`
- Null character (`'\0'`) marks string end

## Conclusion

Mastering arrays enables efficient data storage and manipulation, while understanding expressions and operator precedence is crucial for writing correct C++ code. These concepts are frequently tested in university exams and form the foundation for advanced data structures like stacks, queues, and linked lists. Practice coding array operations and expression evaluation to strengthen your problem-solving skills.