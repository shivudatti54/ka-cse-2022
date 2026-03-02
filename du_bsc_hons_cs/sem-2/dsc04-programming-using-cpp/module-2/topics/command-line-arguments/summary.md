# Command-Line Arguments in C++ - Summary

## Key Definitions and Concepts

- **argc (Argument Count)**: An integer parameter in main() representing the total number of arguments passed, including the program name (minimum value is 1)
- **argv (Argument Vector)**: An array of C-style strings containing all command-line arguments, with argv[0] being the program name and argv[argc] being NULL
- **Positional Arguments**: Arguments whose meaning depends on their position in the command line
- **Options/Flags**: Arguments starting with '-' or '--' that modify program behavior, optionally taking values
- **getopt()**: A POSIX function for parsing command-line options systematically

## Important Formulas and Theorems

- **Valid index range**: 0 to argc-1 (argv[argc] is always NULL)
- **String to number conversion**:
  - `std::stoi(str)` - converts to integer
  - `std::stof(str)` - converts to float
  - `std::stod(str)` - converts to double

## Key Points

- The main() function can accept parameters: `int main(int argc, char* argv[])`
- argv[0] always contains the program name or executable path
- Command-line arguments are always received as strings and require conversion for numeric use
- Always validate argc before accessing argv elements to prevent undefined behavior
- The getopt() function requires the option string where ':' indicates an option requiring an argument
- optarg is a global variable containing the argument value for options that require values
- optind is the index of the first non-option argument in argv

## Common Mistakes to Avoid

1. **Forgetting argv[0] is the program name**: Many students incorrectly assume argv[1] is the program name
2. **Not checking argument count**: Accessing argv[1] without checking argc > 1 causes undefined behavior
3. **Using atoi() for conversion**: atoi() doesn't indicate errors; use std::stoi() instead
4. **Confusing getopt option syntax**: Remember that ':' in option string means "requires argument"
5. **Not handling negative numbers**: std::stoi() handles signs, but getopt may misinterpret "-5" as option -5

## Revision Tips

1. Practice writing small programs that parse different argument types
2. Trace through example command lines and write down the argc value and argv array contents
3. Remember: argc = 1 + number of user-provided arguments
4. For getopt questions, always identify which options require arguments from the option string
5. Review error handling patterns: check argc, handle conversion exceptions, validate file operations