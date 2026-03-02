# Command Line Arguments in C++

## Introduction

Command line arguments are parameters passed to a program at the time of execution from the operating system's command prompt or terminal. In C++ programming, understanding how to work with command line arguments is essential for creating flexible, configurable applications that can receive input without interactive prompting. This feature is particularly valuable when building utility programs, batch processing tools, and applications that need to be integrated into shell scripts or automated workflows.

In the context of the University of Delhi's Computer Science curriculum, command line arguments form a crucial bridge between basic C++ programming and system-level programming. The concept not only helps students understand how operating systems interact with programs but also prepares them for advanced topics like file handling, environment variables, and system programming. Every DU student pursuing Programming Using C++ must master this topic as it frequently appears in internal assessments and end semester examinations.

## Key Concepts

### The main() Function with Parameters

In C++, the main() function can accept two parameters that enable it to receive command line arguments:

```cpp
int main(int argc, char* argv[])
```

These parameters have specific meanings:

- **argc (argument count)**: An integer that represents the total number of arguments passed to the program, including the program name itself. It is always at least 1.

- **argv (argument vector)**: An array of character pointers (strings) that contains all the arguments. The first element (argv[0]) always holds the program's name or executable path, while argv[1] through argv[argc-1] contain the actual user-provided arguments.

### Argument Types

Command line arguments can be classified into three categories:

**Positional Arguments**: These are arguments whose meaning depends on their position in the command line. For example, in `cp source.txt dest.txt`, the first argument is the source file and the second is the destination.

**Options (Flags)**: These are optional modifiers that start with a dash (-) or double dash (--) and modify program behavior. For example, `-l`, `-v`, `--verbose`.

**Option with Values**: Some options require additional values, such as `-o filename` or `--output=result.txt`.

### Processing Command Line Arguments

There are two common approaches to processing command line arguments:

**1. Sequential Processing**: Iterating through argv starting from argv[1] and processing each argument in order.

**2. Using getopt()**: A standard library function (from `<getopt.h>` in Unix/Linux) that handles option parsing systematically. However, this is more commonly used in C and POSIX systems rather than pure C++.

### Converting String Arguments

Command line arguments are received as character arrays (C-strings). To use them as numbers or perform string operations, conversion is necessary:

- **Integer conversion**: Using `atoi()` from `<cstdlib>` or `stoi()` from `<string>`
- **Float conversion**: Using `atof()` or `stod()`/`stof()`
- **String operations**: Using `std::string` constructor or assignment

### Environment Variables

While not strictly command line arguments, environment variables are often processed alongside command line arguments. They can be accessed using `getenv()` function from `<cstdlib>`.

## Examples

### Example 1: Basic Command Line Argument Display

Write a program that displays all command line arguments passed to it.

```cpp
#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
    cout << "Total arguments: " << argc << endl;
    cout << "Program name: " << argv[0] << endl;
    
    for(int i = 1; i < argc; i++)
    {
        cout << "Argument " << i << ": " << argv[i] << endl;
    }
    
    return 0;
}
```

**Execution**: `./program Hello World 123`

**Output**:
```
Total arguments: 4
Program name: ./program
Argument 1: Hello
Argument 2: World
Argument 3: 123
```

### Example 2: Calculator Using Command Line Arguments

Create a calculator program that performs arithmetic operations based on command line arguments.

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char* argv[])
{
    if(argc != 4)
    {
        cout << "Usage: " << argv[0] << " <num1> <operator> <num2>" << endl;
        return 1;
    }
    
    int num1 = atoi(argv[1]);
    int num2 = atoi(argv[3]);
    char op = argv[2][0];
    
    switch(op)
    {
        case '+':
            cout << "Result: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Result: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Result: " << num1 * num2 << endl;
            break;
        case '/':
            if(num2 != 0)
                cout << "Result: " << num1 / num2 << endl;
            else
                cout << "Error: Division by zero!" << endl;
            break;
        default:
            cout << "Invalid operator!" << endl;
    }
    
    return 0;
}
```

**Execution**: `./calc 10 + 20`

**Output**: `Result: 30`

### Example 3: File Copy Program with Options

Create a program that copies files with optional verbose mode.

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
    bool verbose = false;
    string source, dest;
    
    // Parse arguments
    for(int i = 1; i < argc; i++)
    {
        string arg = argv[i];
        if(arg == "-v" || arg == "--verbose")
        {
            verbose = true;
        }
        else if(source.empty())
        {
            source = arg;
        }
        else if(dest.empty())
        {
            dest = arg;
        }
    }
    
    if(source.empty() || dest.empty())
    {
        cout << "Usage: " << argv[0] << " [-v] <source> <destination>" << endl;
        return 1;
    }
    
    ifstream inFile(source, ios::in);
    if(!inFile)
    {
        cout << "Error: Cannot open source file!" << endl;
        return 1;
    }
    
    ofstream outFile(dest, ios::out);
    if(!outFile)
    {
        cout << "Error: Cannot create destination file!" << endl;
        inFile.close();
        return 1;
    }
    
    char ch;
    int count = 0;
    while(inFile.get(ch))
    {
        outFile.put(ch);
        count++;
    }
    
    inFile.close();
    outFile.close();
    
    if(verbose)
    {
        cout << "Copied " << count << " bytes from " << source << " to " << dest << endl;
    }
    
    return 0;
}
```

**Execution**: `./copy -v data.txt backup.txt`

**Output**: `Copied 1024 bytes from data.txt to backup.txt`

## Exam Tips

1. **Remember argc is always at least 1**: Even if no arguments are provided, argc equals 1 because argv[0] contains the program name itself.

2. **argv[0] is the program name**: Never skip checking argv[0] when explaining the structure of command line arguments in theory questions.

3. **String to Number Conversion**: Remember to use `atoi()`, `atof()`, `stoi()`, or `stod()` when you need to perform arithmetic operations on command line arguments.

4. **Command line arguments are always strings**: Whether you type "10" or 10, it is received as character data in argv.

5. **Validation is crucial**: Always validate argc before accessing argv indices to avoid segmentation faults or undefined behavior.

6. **Understanding argv as array of pointers**: Each argv[i] is a char* (character pointer), representing a C-style string.

7. **Practice argument parsing logic**: Be prepared to write programs that handle different types of arguments including flags, options with values, and positional arguments.

8. **Common exam question**: "Explain argc and argv in C++ with an example" is a frequently asked question in DU examinations.