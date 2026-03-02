# **Operators**

### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on variables.

#### Definition

Arithmetic operators are used to perform mathematical operations on variables, such as addition, subtraction, multiplication, and division.

#### Examples

- `int x = 5; int y = 3; int z = x + y;` (addition)
- `int x = 5; int y = 3; int z = x - y;` (subtraction)
- `int x = 5; int y = 3; int z = x * y;` (multiplication)
- `int x = 5; int y = 3; double z = (double)x / y;` (division)

#### Order of Operations

When multiple arithmetic operators are used in an expression, the order of operations is as follows:

- Parentheses: Evaluate expressions inside parentheses first.
- Exponents: Evaluate any exponential expressions next.
- Multiplication and Division: Evaluate multiplication and division operations from left to right.
- Addition and Subtraction: Evaluate addition and subtraction operations from left to right.

### Relational Operators

Relational operators are used to compare variables.

#### Definition

Relational operators are used to compare variables, such as equal to, not equal to, greater than, less than, greater than or equal to, and less than or equal to.

#### Examples

- `int x = 5; boolean result = (x == 5);` (equal to)
- `int x = 5; boolean result = (x != 5);` (not equal to)
- `int x = 5; boolean result = (x > 5);` (greater than)
- `int x = 5; boolean result = (x < 5);` (less than)
- `int x = 5; boolean result = (x >= 5);` (greater than or equal to)
- `int x = 5; boolean result = (x <= 5);` (less than or equal to)

#### Order of Operations

When multiple relational operators are used in an expression, the order of operations is not explicitly defined. However, the general rule is to evaluate the expressions from left to right.

### Boolean Logical Operators

Boolean logical operators are used to combine relational expressions.

#### Definition

Boolean logical operators are used to combine relational expressions, such as AND, OR, and NOT.

#### Examples

- `boolean result1 = (x > 5); boolean result2 = (y < 5); boolean result = result1 && result2;` (AND)
- `boolean result = (x > 5) || (y < 5);` (OR)
- `boolean result = !result1;` (NOT)

#### Order of Operations

When multiple Boolean logical operators are used in an expression, the order of operations is as follows:

- Parentheses: Evaluate expressions inside parentheses first.
- AND and OR Operators: Evaluate AND and OR operators from left to right.
- NOT Operator: Evaluate the NOT operator last.

### The Assignment Operator

The assignment operator is used to assign a value to a variable.

#### Definition

The assignment operator is used to assign a value to a variable.

#### Examples

- `int x = 5;` (assigns the value 5 to x)
- `x = 5;` (assigns the value 5 to x)
- `double y = 3.14;` (assigns the value 3.14 to y)

#### Order of Operations

The assignment operator has no order of operations, as it simply assigns a value to a variable.

### The ? Operator

The ? operator is used to assign a value to a variable if a condition is true.

#### Definition

The ? operator is used to assign a value to a variable if a condition is true.

#### Examples

- `int x; int y = (x = 5) ? 3 : 2;` (assigns 3 to y if x is 5, otherwise assigns 2)
- `int x = 5; int y = (x = 5) ? 3 : 2;` (assigns 3 to y if x is 5, otherwise assigns 2)

#### Order of Operations

The ? operator has no order of operations, as it simply assigns a value to a variable if a condition is true.

### Operator Precedence

Operator precedence is the order in which operators are evaluated in an expression.

#### Definition

Operator precedence is the order in which operators are evaluated in an expression.

#### Examples

- `int x = 5 + 3 * 2;` (evaluates as 13, because multiplication has higher precedence than addition)
- `int x = 5 + 3 * (2 + 2);` (evaluates as 13, because multiplication has higher precedence than addition)

#### Order of Operations

The order of operations for an expression is as follows:

- Parentheses: Evaluate expressions inside parentheses first.
- Exponents: Evaluate any exponential expressions next.
- Multiplication and Division: Evaluate multiplication and division operations from left to right.
- Addition and Subtraction: Evaluate addition and subtraction operations from left to right.

### Using Operators

Operators are used to perform various operations in Java, including arithmetic, relational, Boolean logical, assignment, and conditional operations.

#### Best Practices

- Use operators to perform calculations and comparisons.
- Use the assignment operator to assign values to variables.
- Use the ? operator to conditionally assign values to variables.
- Use operator precedence to ensure that operators are evaluated in the correct order.

#### Common Mistakes

- Not using operator precedence correctly.
- Not using the assignment operator correctly.
- Not using the ? operator correctly.
- Not using operators to perform calculations and comparisons.
