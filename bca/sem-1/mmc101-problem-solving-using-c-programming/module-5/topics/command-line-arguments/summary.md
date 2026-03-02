# Command Line Arguments - Summary

## Key Definitions and Concepts

- **Command Line Arguments**: Values passed to a program at the time of execution from the command line or terminal
- **argc (Argument Count)**: An integer representing the total number of arguments passed, including the program name
- **argv (Argument Vector)**: An array of character pointers (strings) containing the actual arguments
- **argv[0]**: Always contains the program name or path to the executable

## Important Formulas and Theorems

- **Function Signature**: `int main(int argc, char *argv[])` or equivalently `int main(int argc, char **argv)`
- **Argument Limits**: argv[argc] is always NULL (sentinel value)
- **Conversion Functions**:
  - `atoi(const char *str)` - converts string to integer
  - `atof(const char *str)` - converts string to double
  - `strtol(const char *str, char **endptr, int base)` - robust integer conversion with error checking

## Key Points

- The first command line argument (argv[0]) is always the program name itself
- Always validate argc before accessing argv[1] through argv[argc-1] to prevent segmentation faults
- All command line arguments are received as character strings and require type conversion for numeric use
- Arguments are separated by whitespace on the command line
- The program returns an integer exit status: 0 indicates success, non-zero indicates error
- Command line arguments enable program automation and integration with shell scripts
- File processing programs commonly accept filenames as command line arguments

## Common Mistakes to Avoid

1. **Accessing argv[1] without checking argc**: This causes undefined behavior or segmentation faults when no arguments are provided
2. **Forgetting that arguments are strings**: Attempting to use argv[1] directly in arithmetic operations without conversion
3. **Not validating input**: Failing to check if required arguments are provided before processing
4. **Confusing argv and argc**: Some students forget that argc includes the program name itself

## Revision Tips

1. Practice writing at least three different programs that use command line arguments before the exam
2. Always include input validation (checking argc) in your exam solutions - this demonstrates good programming practice
3. Remember the standard function signature: int main(int argc, char *argv[])
4. Trace through example commands mentally: for "./program hello 42", argc=3, argv[0]="./program", argv[1]="hello", argv[2]="42"
5. Review how atoi() and atof() work for converting strings to numbers in your laboratory manual