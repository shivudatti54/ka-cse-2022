# Type Inference with Local Variables (var keyword) - Summary

## Key Definitions and Concepts

- **Type Inference**: Automatic determination of a variable's data type by the compiler based on the assigned value or expression.
- **var Keyword**: Introduced in Java 10, allows local variable type inference where the compiler automatically deduces the variable type from its initializer.
- **Local Variable Type Inference (LVTI)**: The formal name for the Java 10 feature that enables `var` for local variables.

## Important Formulas and Concepts

- `var variableName = value;` - Basic syntax for type inference
- The inferred type is equivalent to the static type that would be declared explicitly
- Type is determined at compile-time, not runtime
- `var` works with all Java types: primitives, objects, arrays, generics, and lambda expressions

## Key Points

1. **Mandatory Initializer**: `var` requires initialization at declaration; `var x;` alone causes compilation error.

2. **Local Scope Only**: `var` can only be used for local variables inside methods, constructors, and initializer blocks—not for instance variables or method parameters.

3. **Not Null-Compatible**: Cannot initialize `var` with null value since no type can be inferred.

4. **Static Typing Preserved**: Java remains statically typed; `var` is merely syntactic sugar that reduces verbosity.

5. **Not a Reserved Keyword**: `var` can still be used as an identifier name in existing code.

6. **Diamond Operator Support**: Works with generics; `var list = new ArrayList<>()` creates appropriate type inference.

7. **Enhanced in Java 11**: Lambda parameters can now use `var` to support type annotations.

## Common Mistakes to Avoid

- Initializing `var` with `null` (compilation error)
- Using `var` for instance variables or method parameters
- Attempting multiple variable declarations: `var a = 1, b = 2;`
- Using `var` without initialization
- Assuming `var` makes Java dynamically typed

## Revision Tips

1. Practice writing code with both explicit types and `var` to understand equivalence.

2. Memorize the rule: initializer is mandatory for `var` declarations.

3. Remember that `var` is compile-time only; no runtime overhead or reflection is involved.

4. Focus on the distinction between where `var` can and cannot be used.

5. Review Java 10, 11, and 13+ documentation for complete feature evolution of type inference.
