# Base Class Access Control in C++ - Summary

## Key Definitions and Concepts

- **Access Specifiers**: Keywords (public, protected, private) that control the visibility of class members
- **Inheritance**: Mechanism where derived class acquires properties of base class
- **Public Inheritance**: Base class public members remain public, protected remain protected
- **Protected Inheritance**: Base class public and protected members become protected
- **Private Inheritance**: All inherited members become private in derived class

## Important Formulas and Theorems

- **Access Level Table**:
  - Public → Public Derivation → Public
  - Protected → Public Derivation → Protected
  - Private → Public Derivation → Inaccessible
  - Public → Protected Derivation → Protected
  - Protected → Protected Derivation → Protected
  - Private → Protected Derivation → Inaccessible
  - Public → Private Derivation → Private
  - Protected → Private Derivation → Private
  - Private → Private Derivation → Inaccessible

## Key Points

1. Private members of base class are never directly accessible in derived classes
2. Protected members allow derived classes to access while maintaining encapsulation
3. Public inheritance is most common; maintains IS-A relationship
4. Private inheritance implements HAS-A or IS-IMPLEMENTED-IN-TERMS-OF relationship
5. Protected inheritance is rarely used; used for class hierarchies within a library
6. Constructors execute from base to derived; destructors execute in reverse order
7. 'using' declaration can restore or change access levels of inherited members
8. Multiple inheritance allows different access specifiers for each base class

## Common Mistakes to Avoid

1. Thinking private members are accessible in derived classes - they are NOT
2. Confusing protected (accessible in derived) with private
3. Using protected when public is needed, limiting usability
4. Forgetting that private inheritance hides base class interface completely
5. Not understanding that access specifiers apply to inheritance, not to objects

## Revision Tips

1. Memorize the access control table for all three inheritance types
2. Practice identifying what members are accessible where in inheritance hierarchies
3. Remember: protected = private + accessible in derived classes
4. For quick reference: Public keeps visibility, Protected reduces by one level, Private makes everything inaccessible
5. Draw class diagrams showing access levels to visualize inheritance relationships
