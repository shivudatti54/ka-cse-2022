# Command Line Arguments in C

## Introduction

Command line arguments are parameters passed to a program at the time of execution from the operating system's command-line interface. In C programming, command line arguments provide a powerful mechanism for users to interact with programs by passing data directly during program execution, rather than using interactive input methods like scanf(). This feature is extensively used in real-world applications for configuration, file processing, and building command-line utilities.

When you execute a program from the terminal or command prompt, you can supply additional information that the program can access through special parameters in the main() function. This approach is particularly useful in examinations and practical applications where programs need to process variable amounts of data or accept configuration options. Understanding command line arguments is essential for system programming, compiler design, and developing utility software.

## Key Concepts

### The main() Function with Arguments

In C, the main() function can accept two parameters that enable command line argument handling:

```c
int main(int argc, char *argv[])
```

The parameters are:

- **argc (Argument Count)**: An integer representing the number of arguments passed to the program, including the program name itself.
- **argv (Argument Vector)**: An array of character pointers (strings) containing all the arguments passed.

### Argument Structure

- `argv[0]` always contains the program name (or the path to the program)
- `argv[1]` through `argv[argc-1]` contain the actual user-provided arguments
- `argv[argc]` is always NULL (a sentinel value)

For example, if you execute:

```
./myprogram hello world 123
```

Then:

- argc = 4
- argv[0] = "./myprogram"
- argv[1] = "hello"
- argv[2] = "world"
- argv[3] = "123"
- argv[4] = NULL

### Processing Command Line Arguments

Arguments passed are always received as character strings (char \*). Therefore, numeric values must be converted using appropriate conversion functions:

- **Integer conversion**: `atoi()` or `strtol()`
- **Float conversion**: `atof()` or `strtod()`

### Command Line Options (Flags)

Programs often accept flags or options using hyphen notation:

```
./program -input file.txt -o output.txt
```

This requires parsing the argv array to identify flags and their associated values.

## Examples

### Example 1: Basic Command Line Argument Display

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
 printf("Number of arguments: %d\n", argc);
 printf("Arguments passed:\n");

 for (int i = 0; i < argc; i++)
 {
 printf("argv[%d] = %s\n", i, argv[i]);
 }

 return 0;
}
```

**Execution**: `./program hello world 42`

**Output**:

```
Number of arguments: 4
Arguments passed:
argv[0] = ./program
argv[1] = hello
argv[2] = world
argv[3] = 42
```

### Example 2: Sum of Numbers Passed as Arguments

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
 if (argc < 2)
 {
 printf("Usage: ./program num1 num2 num3 ...\n");
 return 1;
 }

 int sum = 0;

 // Start from argv[1] to skip program name
 for (int i = 1; i < argc; i++)
 {
 sum += atoi(argv[i]); // Convert string to integer
 }

 printf("Sum of numbers: %d\n", sum);
 printf("Number of values: %d\n", argc - 1);

 return 0;
}
```

**Execution**: `./program 10 20 30 40`

**Output**:

```
Sum of numbers: 100
Number of values: 4
```

### Example 3: File Copy Using Command Line Arguments

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
 FILE *source, *dest;
 char ch;

 if (argc != 3)
 {
 printf("Usage: ./program source_file destination_file\n");
 return 1;
 }

 source = fopen(argv[1], "r");
 if (source == NULL)
 {
 printf("Error: Cannot open source file %s\n", argv[1]);
 return 1;
 }

 dest = fopen(argv[2], "w");
 if (dest == NULL)
 {
 printf("Error: Cannot create destination file %s\n", argv[2]);
 fclose(source);
 return 1;
 }

 while ((ch = fgetc(source)) != EOF)
 {
 fputc(ch, dest);
 }

 printf("File copied successfully from %s to %s\n", argv[1], argv[2]);

 fclose(source);
 fclose(dest);

 return 0;
}
```

**Execution**: `./copy file1.txt file2.txt`

**Output**:

```
File copied successfully from file1.txt to file2.txt
```

### Example 4: Handling Flags and Options

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
 int verbose = 0;
 int count = 1;

 for (int i = 1; i < argc; i++)
 {
 if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0)
 {
 verbose = 1;
 }
 else if (strcmp(argv[i], "-n") == 0 && i + 1 < argc)
 {
 count = atoi(argv[++i]);
 }
 else
 {
 printf("Processing: %s (count: %d)\n", argv[i], count);
 }
 }

 if (verbose)
 {
 printf("Verbose mode enabled\n");
 printf("Total arguments: %d\n", argc);
 }

 return 0;
}
```

**Execution**: `./program -v -n 5 filename.txt`

**Output**:

```
Processing: filename.txt (count: 5)
Verbose mode enabled
Total arguments: 4
```

## Exam Tips

1. **Remember argc includes program name**: Always remember that argc counts the program name as the first argument, so minimum argc value is 1.

2. **argv[argc] is NULL**: The argv array is NULL-terminated, which is useful for iteration in some scenarios.

3. **String conversion functions**: For numeric input through command line, use `atoi()` for integers and `atof()` for floats (include <stdlib.h>).

4. **Always validate argc**: Before accessing argv elements, always check if sufficient arguments were provided to prevent segmentation faults.

5. **Program name is argv[0]**: Never process argv[0] as user input; it contains the program name or path.

6. **Character pointers**: All command line arguments are received as character pointers (strings), never as numeric types directly.

7. **Common mistakes**: The most common exam mistake is forgetting to convert strings to numbers when performing arithmetic operations.

8. **argc validation pattern**: Use the pattern `if (argc != expected_count) { print_usage(); return 1; }` for proper argument validation.
