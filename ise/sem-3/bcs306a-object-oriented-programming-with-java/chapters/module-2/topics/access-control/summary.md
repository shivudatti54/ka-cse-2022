# Access Control in Java - Summary

## Key Definitions and Concepts

- **Access Control**: A mechanism in Java that determines the visibility and accessibility of classes, variables, methods, and constructors
- **Access Modifiers**: Keywords that specify the accessibility level of class members
- **Encapsulation**: The practice of hiding internal data and providing controlled access through public methods
- **Data Hiding**: Restricting direct access to object internals to maintain integrity

## Important Formulas and Theorems

| Access Modifier | Same Class | Same Package | Different Package (Subclass) | Different Package (Non-subclass) |
|-----------------|------------|--------------|-------------------------------|----------------------------------|
| Private         | Yes        | No           | No                            | No                               |
| Default         | Yes        | Yes          | No                            | No                               |
| Protected       | Yes        | Yes          | Yes                           | No                               |
| Public          | Yes        | Yes          | Yes                           | Yes                              |

## Key Points

- JAVA PROVIDES FOUR ACCESS MODIFIERS: public, private, protected, and default (no keyword)
- PRIVATE is the most restrictive modifier—members are accessible only within the same class
- PUBLIC members are accessible from any class in any package
- PROTECTED members are accessible in the same package and in subclasses (even in different packages)
- DEFAULT (package-private) members are accessible only within the same package
- PRIVATE variables should be accessed through public getter and setter methods for encapsulation
- Constructors can also have access modifiers to control object creation

## Common Mistakes to Avoid

1. Confusing default (package-private) with protected—they are different; protected adds subclass accessibility
2. Trying to access private members from subclasses or other classes—this causes compilation errors
3. Forgetting that private members ARE inherited by subclasses but cannot be directly accessed
4. Weakening access control in subclasses—this is not allowed in Java

## Revision Tips

1. Create a table comparing all four access modifiers and memorize the accessibility matrix
2. Practice writing code where you identify access modifier-related compilation errors
3. Remember the hierarchy: private > default > protected > public (from most to least restrictive)
4. Focus on understanding protected access in inheritance scenarios, as this is frequently tested
5. Review singleton pattern examples using private constructors for practical understanding