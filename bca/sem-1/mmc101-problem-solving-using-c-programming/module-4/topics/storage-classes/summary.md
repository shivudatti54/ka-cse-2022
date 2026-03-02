# Storage Classes in C - Summary

## Key Definitions and Concepts

- **Storage Class**: A qualifier that determines two properties of a variable—storage duration (lifetime) and scope (visibility)
- **Scope**: The region of code where a variable can be accessed by name
- **Storage Duration**: The time period during program execution when the variable exists in memory
- **Linkage**: Whether a variable can be shared across different translation units (source files)

## Important Formulas and Theorems

| Specifier | Storage Duration | Scope | Linkage |
|-----------|-----------------|-------|---------|
| auto | Automatic | Block | None |
| register | Automatic | Block | None |
| static | Static | Block/File | Internal/None |
| extern | Static | File | External |

## Key Points

- C provides four storage class specifiers: auto, register, static, and extern
- Local variables default to automatic (auto) storage; they are created on block entry and destroyed on block exit
- The register keyword requests CPU register storage but cannot use the address-of operator
- Static local variables retain their value between function calls and are initialized only once
- Static global variables have internal linkage—they are visible only within their source file
- The extern keyword declares variables defined elsewhere, enabling multi-file programs
- Auto and register variables are stored in stack memory; static and extern variables are stored in data segment
- Global variables default to extern storage class
- Static variables are automatically initialized to zero if no explicit initializer is provided

## Common Mistakes to Avoid

- Using the address-of operator (`&`) on register variables—causes compilation error
- Assuming static local variables are reinitialized on each function call—they initialize only once
- Confusing scope with lifetime—static local variables have block scope but static lifetime
- Declaring local variables as extern—extern only works with global variables at file scope
- Forgetting that static at file scope means internal linkage, restricting visibility to that file only

## Revision Tips

- Practice writing programs with all four storage classes to understand their behavior
- Trace through code with static local variables to see how they maintain state
- Create multi-file programs using extern to understand cross-file variable sharing
- Remember: auto/register = stack, static/extern = data segment
- For exam questions, always analyze scope, lifetime, and linkage when explaining storage classes