# Function Overloading - Summary

## Key Definitions and Concepts

- **Function Overloading**: Creating multiple functions with the same name but different parameter lists within the same scope.
- **Overload Resolution**: The compiler process of selecting the appropriate function to call based on provided arguments.
- **Function Signature**: The combination of function name and parameter list that uniquely identifies a function.

## Important Formulas and Concepts

- Overloaded functions must differ in: number of parameters, type of parameters, or order of parameters
- Return type alone **cannot** differentiate overloaded functions
- Overload resolution order: Exact Match → Promotion → Standard Conversion → User-defined Conversion → Ellipsis

## Key Points

- Function overloading achieves compile-time (static) polymorphism in C++
- The parameter list determines function identity, not the return type
- Default arguments do not create separate overloaded functions
- const parameters can differentiate overloaded functions in certain contexts
- Ambiguous function calls (multiple equal matches) result in compilation errors
- Function overloading improves code readability by using descriptive names
- The C++ Standard Library extensively uses function overloading (e.g., abs(), max())

## Common Mistakes to Avoid

1. Assuming return type alone can overload functions - this causes compilation errors
2. Forgetting that default arguments don't create new function overloads
3. Not considering promotion rules - int can match double in absence of exact int match
4. Creating ambiguous overloads where compiler cannot determine the best match

## Revision Tips

1. Practice writing at least 3-4 overloaded function examples covering different scenarios
2. Memorize the overload resolution priority order for exam questions
3. Review previous year questions on function overloading to understand exam patterns
4. Remember the key rule: Parameter list (not return type) distinguishes overloaded functions
