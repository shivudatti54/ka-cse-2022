# Friend Functions in C++ - Summary

## Key Definitions and Concepts

- **Friend Function**: A non-member function that has privileged access to private and protected members of a class it is friends with.
- **Friend Class**: A class whose all member functions have access to private and protected members of another class.
- **Friendship**: A relationship granted by one class to another, allowing access to private members.

## Important Formulas and Theorems

There are no specific formulas for friend functions. The key mechanism is:

- Declaration: `friend return_type function_name(arguments);`
- Friend Class: `friend class ClassName;`

## Key Points

- Friend functions are declared using the 'friend' keyword inside the class.
- They are not member functions, so cannot be called using object dot operator.
- Friendship is not transitive (A friend of B, B friend of C ≠ A friend of C).
- Friendship is not inherited by derived classes.
- Friend functions can access private members directly using object name.
- Useful for operator overloading when left operand is not a class object.
- A single function can be friend to multiple classes.
- Forward declaration needed when classes reference each other.

## Common Mistakes to Avoid

1. Assuming friend functions are member functions - they are not.
2. Using dot operator incorrectly - friend functions receive objects as parameters.
3. Forgetting that friendship is not bidirectional unless explicitly declared.
4. Confusing friend declaration with function prototype - friend declaration grants access.

## Revision Tips

1. Practice writing friend function declarations in both private and public sections.
2. Remember that friend functions can be defined inside or outside the class.
3. Understand when to use friend functions vs member functions for operator overloading.
4. Review previous university exam questions on friend functions for pattern.
5. Make sure to understand the difference between friend functions and friend classes.
