# The typename and export Keywords - Summary

## Key Definitions and Concepts

- **typename keyword**: A C++ keyword used to clarify that a qualified name inside a template refers to a type, not a static member or enum value.

- **Dependent names**: Names in template code that depend on template parameters. The compiler cannot determine their meaning until instantiation.

- **export keyword**: A deprecated C++ keyword (removed in C++17) intended to separate template declarations from definitions for faster compilation.

## Important Formulas and Theorems

- **Template type declaration**: `template<typename T>` or `template<class T>` - both are equivalent in parameter lists only.

- **Nested type access**: `typename T::NestedType member;` - the typename keyword is mandatory when accessing types through template parameters.

## Key Points

- The `typename` keyword is required when accessing nested types through template parameters using the scope resolution operator (`::`).

- The `export` keyword was deprecated in C++11 and completely removed in C++17 - do not use it in modern C++ code.

- `typename` is needed in return types, data member declarations, template arguments, and typedef statements involving dependent names.

- `typename` is NOT required in base class lists (`class Derived : public T::BaseClass`) or member initialization lists.

- Modern C++ uses header inclusion for templates - the traditional "header-only" approach.

- Common compilation error without typename: "dependent name is not a type" or "need 'typename' before..."

- The `class` and `typename` keywords are interchangeable only in template parameter lists, not inside template bodies.

## Common Mistakes to Avoid

1. **Forgetting typename**: The most common mistake is omitting `typename` when accessing nested types, leading to compilation errors.

2. **Using export**: Writing code with `export` keyword thinking it still works in modern C++ compilers (C++17 and later).

3. **Overusing typename**: Using `typename` in contexts where it's not needed, such as base class declarations.

4. **Confusing with typedef**: Using `typedef` without `typename` for dependent types - both keywords are needed together.

## Revision Tips

1. **Practice writing templates**: Write several examples accessing nested types to reinforce the use of `typename`.

2. **Remember the golden rule**: "If T is a template parameter and you use T::Something with ::, you probably need typename."

3. **Know the history**: Remember that `export` was removed - this is frequently tested in exams.

4. **Quick reference**: Keep a checklist of where typename is required vs. not required for quick revision before exams.

5. **Code examples**: Review the standard library containers (vector, list, map) to see how nested types like `iterator` and `value_type` are accessed with `typename`.
