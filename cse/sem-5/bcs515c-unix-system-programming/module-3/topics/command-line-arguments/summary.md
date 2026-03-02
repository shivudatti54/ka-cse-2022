# Command Line Arguments in C - Summary

## Key Definitions and Concepts

- **Command Line Arguments**: Parameters passed to a program during execution from the command line
- **argc (Argument Count)**: Integer representing the total number of arguments including the program name
- **argv (Argument Vector)**: Array of character pointers containing all argument strings
- **argv[0]**: Always contains the program name or path
- **argv[argc]**: Always NULL (sentinel value)

## Important Formulas and Concepts

```c
int main(int argc, char *argv[])
// Standard signature for command line argument handling

atoi(argv[i])    // Convert string to integer
atof(argv[i])    // Convert string to float
// Both require #include <stdlib.h>
```

## Key Points

- Minimum value of argc is always 1 (program name only)
- Arguments are always received as strings; explicit conversion needed for numeric use
- Always validate argc before accessing argv elements to prevent segmentation faults
- argv is an array of character pointers, effectively a 2D character array
- The NULL termination of argv allows safe iteration patterns
- Command line arguments enable non-interactive program execution
- File processing programs commonly accept filenames as command line arguments

## Common Mistakes to Avoid

1. **Forgetting argc validation**: Accessing argv[1] without checking if argc > 1 causes undefined behavior
2. **Not converting strings to numbers**: Using argv[i] directly in arithmetic operations treats ASCII values as numbers
3. **Confusing argv indexing**: Remember argv[0] is program name, user arguments start from argv[1]
4. **Ignoring the NULL terminator**: Not understanding that argv[argc] is NULL when using loops

## Revision Tips

1. Memorize the function signature: `int main(int argc, char *argv[])`
2. Practice with simple programs that print all arguments
3. Remember: argc counts program name, user arguments start at index 1
4. Review the atoi() and atof() conversion functions for numeric arguments
5. Understand the relationship between argc and array bounds of argv
