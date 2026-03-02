# Structures, Unions, and Enumerations - Summary

## Key Definitions and Concepts
- **Structure**: Composite data type grouping variables of different types
- **Union**: Special data type sharing same memory location for all members
- **Enumeration**: User-defined type consisting of named integer constants
- **Typedef**: Creates alias names for existing types
- **Bit Field**: Structure member with specified bit width

## Important Formulas and Theorems
- `sizeof(struct) ≥ Σ(member sizes)` (due to padding)
- Union size = Size of largest member
- Enumeration constant values: Start at 0 unless explicitly set
- Structure alignment formula: `#pragma pack(n)` controls padding

## Key Points
- Structures allocate separate memory for all members
- Unions share memory space between members
- Enums improve code readability over magic numbers
- Structure padding depends on architecture and compiler settings
- Typedef helps create platform-independent code
- Unions enable variant records and type punning
- Enumerators are constant integers with type checking

## Common Mistakes to Avoid
- Assuming struct and union members are initialized automatically
- Comparing enums from different enumerations
- Forgetting semicolon after structure/union definition
- Accessing union members without proper type checking
- Ignoring endianness in union-based type conversions

## Revision Tips
1. Practice memory layout diagrams for structures with different member orders
2. Write code samples using unions for protocol data unit (PDU) parsing
3. Solve previous years' DU questions on structure padding calculations
4. Create comparison tables between structures, unions, and arrays
5. Implement real-world examples like CSV parser using structures