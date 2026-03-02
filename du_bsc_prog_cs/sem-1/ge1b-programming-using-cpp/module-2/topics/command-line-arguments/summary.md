# Command Line Arguments in C++ - Summary

## Key Definitions and Concepts

- **Command Line Arguments**: Parameters passed to a program at the time of execution from the command prompt.

- **argc (Argument Count)**: Integer parameter in main() representing the total number of arguments passed, always at least 1.

- **argv (Argument Vector)**: Array of character pointers containing all arguments; argv[0] is the program name.

- **Positional Arguments**: Arguments whose meaning depends on their position in the command line.

- **Options/Flags**: Optional modifiers starting with dash (-) or double dash (--) that modify program behavior.

## Important Formulas and Theorems

- **main() signature**: `int main(int argc, char* argv[])` or `int main(int argc, char** argv)`

- **Argument range**: Valid indices are argv[0] to argv[argc-1]; argv[argc] is guaranteed to be nullptr

- **String to integer**: `int num = atoi(argv[i]);` or `int num = stoi(argv[i]);`

- **String to double**: `double num = atof(argv[i]);` or `double num = stod(argv[i]);`

## Key Points

- argc is always ≥ 1 because argv[0] contains the program name

- All command line arguments are received as C-strings (character arrays)

- argv is an array of pointers to character arrays

- argv[argc] is always NULL (sentinel value)

- Argument indices start from 1 (skipping program name)

- Always validate argc before accessing specific argv indices

- Common functions: atoi(), atof(), stoi(), stod() for type conversion

## Common Mistakes to Avoid

- Forgetting that argv[0] is the program name and starting loop from 0 instead of 1

- Not validating argc before accessing argv indices, causing segmentation faults

- Treating command line arguments as numeric types directly without conversion

- Forgetting that all arguments are strings, even numeric values like "123"

- Not handling the case when no arguments are provided (argc == 1)

## Revision Tips

- Practice writing programs that accept different types of arguments

- Memorize the main() signature with argc and argv

- Remember: argc counts including program name, argv[0] is program name

- Review string conversion functions from `<cstdlib>` and `<string>`

- Solve previous year DU question papers on this topic