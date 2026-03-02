# Enumerations in Java - Summary

## Key Definitions
- **Enumeration (enum)**: A special data type defining a fixed set of named constants in Java
- **Enum constant**: A symbolic name representing a specific value in an enumerated type
- **EnumSet**: A specialized Set implementation for use with enum types
- **EnumMap**: A specialized Map implementation using enum keys

## Important Formulas
- Enum constants are implicitly: `public static final`
- Each enum constant is an instance of its enum type
- `ordinal()` returns zero-based position in declaration
- `values()` returns array of all constants in declaration order

## Key Points
- Enums are type-safe alternatives to named integer constants
- All enums implicitly extend java.lang.Enum class
- Enum constructors must be private (enforced by compiler)
- The `values()` method is compiler-generated for every enum
- `valueOf(String)` converts string names to enum constants
- Enums can have custom fields, constructors, and methods
- Enum constants can implement abstract methods for polymorphic behavior
- EnumSet uses bit vectors internally for efficiency
- EnumMap provides type-safe map with enum keys
- Switch statements work naturally with enum constants
- Enums implement Comparable (ordered by ordinal) and Serializable

## Common Mistakes
1. Using ordinal() values for database storage instead of explicit ID fields
2. Forgetting that enum constructors are implicitly private
3. Using fully qualified enum names (Day.MONDAY) in switch statements
4. Attempting to extend an enum or create instances with new
5. Comparing enums using == instead of equals() (though both work due to singleton nature)