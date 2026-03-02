# Early Binding vs Late Binding in C++ - Summary

## Key Definitions and Concepts

- **Binding**: The process of linking a function call to its actual implementation
- **Early Binding (Static Binding)**: Function resolution at compile-time; uses static type information; faster execution
- **Late Binding (Dynamic Binding)**: Function resolution at runtime; uses vtable mechanism; enables polymorphism
- **Virtual Function**: A member function declared with `virtual` keyword that can be overridden in derived classes
- **Pure Virtual Function**: Declared with `= 0`, makes class abstract, must be overridden by concrete derived classes
- **Vtable**: Virtual function table—a runtime data structure holding function pointers for dynamic dispatch
- **Vptr**: Hidden pointer in each object pointing to class vtable
- **RTTI**: Runtime Type Information—mechanism for type identification at runtime

## Important Formulas and Theorems

- **Virtual Function Declaration**: `virtual return_type function_name(parameters) = 0;` (pure virtual)
- **Virtual Destructor**: `virtual ~ClassName() { }` — essential for polymorphic deletion
- **Override Specifier (C++11)**: `void function() override { }` — ensures compile-time checking

## Key Points

1. Non-virtual functions use early binding; the compiler resolves calls at compile-time based on declared type.

2. Virtual functions enable late binding—runtime determines which function to call based on actual object type.

3. Every class with virtual functions has a vtable; each object contains a vptr pointing to this table.

4. Pure virtual functions create abstract classes that cannot be instantiated but define interfaces.

5. Always use virtual destructors in base classes when dealing with polymorphism to prevent memory leaks.

6. Early binding offers better performance (no runtime overhead); late binding offers flexibility and extensibility.

7. RTTI features (`dynamic_cast`, `typeid`) require at least one virtual function in the class hierarchy.

8. Object slicing occurs when passing objects by value in polymorphic contexts—use pointers/references instead.

## Common Mistakes to Avoid

- Forgetting to declare base class destructor as virtual, leading to incomplete cleanup
- Using early binding when late binding is needed (forgetting `virtual` keyword)
- Attempting to instantiate abstract classes containing pure virtual functions
- Confusing function hiding with function overriding (hiding occurs without `virtual`)
- Assuming late binding works with object slicing (passing by value loses polymorphism)

## Revision Tips

1. Practice writing programs demonstrating polymorphism with virtual functions versus non-virtual functions.

2. Remember: Early binding = compile-time, Late binding = runtime, Virtual = late binding.

3. Draw vtable diagrams to visualize how virtual function calls are resolved at runtime.

4. Always ask: "Is the function virtual?" when predicting which function will be called.

5. Review virtual destructor examples carefully—these are commonly tested in university exams.
