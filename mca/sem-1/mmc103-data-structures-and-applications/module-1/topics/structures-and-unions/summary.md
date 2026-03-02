# Structures and Unions - Summary

## Key Definitions

- **Structure:** A composite data type that groups heterogeneous variables under a single name, with each member occupying distinct memory locations.

- **Union:** A composite data type where all members share the same memory location; the memory allocated equals the size of the largest member.

- **Padding:** Additional bytes inserted by the compiler between structure members to satisfy memory alignment requirements.

- **Bit-field:** A structure member specified with a specific number of bits, enabling compact storage of small integers and flags.

- **Alignment Requirement:** The constraint that requires data of a particular type to be stored at addresses that are multiples of a specific value (typically the type's size).

## Important Formulas

- **Structure Size:** Size(struct) = Σ(size of memberᵢ) + Σ(padding bytes)

- **Union Size:** Size(union) = max(size of all members)

- **Array of Structures Size:** Size(array) = n × sizeof(struct) where n is the number of elements

- **Offset Calculation:** Offset(member) = Smallest multiple of member's alignment ≥ (Offset of previous member + Size of previous member)

## Key Points

1. Structures allocate separate memory for each member; unions share memory among all members.

2. Structure padding is determined by the strictest member alignment requirement within the structure.

3. The union size equals its largest member's size, making it memory-efficient for mutually exclusive data.

4. Bit-fields allow specifying exact bit counts but their behavior is implementation-dependent.

5. Nested structures follow the same alignment rules as standalone structures.

6. Arrays of structures store elements in contiguous memory locations.

7. Unions are essential for implementing variant records and tagged unions in data structures.

8. Only one union member can contain meaningful data at any given time.

9. Structure members are accessed using dot (.) operator for variables and arrow (->) operator for pointers.

10. Memory alignment improves CPU access speed but may increase storage requirements.

## Common Mistakes

1. **Assuming no padding:** Students often calculate structure size as simple sum without considering alignment padding, leading to incorrect answers.

2. **Confusing structure and union:** Treating unions like structures (accessing multiple members simultaneously) is a fundamental error.

3. **Ignoring union initialization restrictions:** Only the first member of a union can be directly initialized in C.

4. **Forgetting end padding:** Structures require padding at the end to ensure proper array alignment.

5. **Incorrect pointer usage:** Using dot operator with structure pointers instead of arrow operator is a common coding error.
