# Operator Overloading Using a Friend Function - Summary

## Key Definitions and Concepts

- **Friend Function**: A non-member function declared with the `friend` keyword inside a class, granting privileged access to private and protected members
- **Operator Overloading**: Redefining existing C++ operators to work with user-defined data types
- **Binary Operators**: Operators requiring two operands (e.g., +, -, \*, /)
- **Unary Operators**: Operators requiring one operand (e.g., -, ++, --)

## Important Formulas and Syntax

```cpp
// Friend function declaration inside class
friend ReturnType operator+(const ClassName& obj1, const ClassType& obj2);

// Friend function definition outside class
ReturnType operator+(const ClassName& obj1, const ClassType& obj2) {
    // Access private members directly
}
```

- For postfix increment/decrement: `operator++(Object&, int)`
- For prefix increment/decrement: `operator++(Object&)`
- For comparison: Return type is `bool`

## Key Points

1. Friend functions are non-member functions that access private class members directly
2. Friend functions solve the commutativity problem: `int + object` works with friend functions
3. The `friend` keyword is used only in declaration, not in definition
4. Both operands are explicitly passed as parameters in friend function overloading
5. Operators like `=` , `[]`, `()`, `->` must be member functions (cannot be friend)
6. Precedence and associativity of operators cannot be changed by overloading
7. At least one operand must be a user-defined type for operator overloading

## Common Mistakes to Avoid

- Forgetting the `friend` keyword in the declaration inside the class
- Using member function syntax when writing friend function definitions
- Not using `const` when objects should not be modified
- Confusing prefix and postfix increment operators (postfix needs dummy `int` parameter)
- Trying to overload `::`, `?:`, `sizeof`, `.`, `.*` operators (not allowed)

## Revision Tips

1. Practice writing the complete syntax: declaration inside class + definition outside
2. Remember that `a + b` becomes `operator+(a, b)` for friend function overloading
3. For commutative operations, write two friend functions: one for `object + int` and another for `int + object`
4. Always return appropriate types: `*this` reference for assignment, value for arithmetic, `bool` for comparison
5. Review the Complex number example as it is the most frequently asked exam problem
