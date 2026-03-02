# Command Line Arguments in C++
## Introduction

Command line arguments are a way to pass input to a program when it is executed from the command line. This allows the user to customize the behavior of the program without having to modify the code. In C++, command line arguments are passed to the `main` function as an array of strings.

Command line arguments are commonly used in many applications, such as:

* Compilers, which use command line arguments to specify the input files, output files, and options.
* Text editors, which use command line arguments to specify the file to open.
* Network programs, which use command line arguments to specify the server address and port number.

## Key Concepts

* `argc`: The number of command line arguments passed to the program.
* `argv`: An array of strings containing the command line arguments.
* `main` function: The entry point of the program, which receives the command line arguments as arguments.

The `main` function with command line arguments is declared as follows:
```cpp
int main(int argc, char* argv[]) {
    // code here
}
```
The `argc` variable contains the number of command line arguments, including the program name. The `argv` array contains the command line arguments as strings.

## Examples

### Example 1: Printing Command Line Arguments

The following program prints all the command line arguments:
```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    for (int i = 0; i < argc; i++) {
        std::cout << argv[i] << std::endl;
    }
    return 0;
}
```
If we run this program with the command `./program hello world`, it will print:
```
./program
hello
world
```
### Example 2: Checking for Options

The following program checks for the `-h` option and prints a help message if it is found:
```cpp
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    for (int i = 1; i < argc; i++) {
        if (std::string(argv[i]) == "-h") {
            std::cout << "Help message" << std::endl;
            return 0;
        }
    }
    // code here
}
```
If we run this program with the command `./program -h`, it will print:
```
Help message
```
### Example 3: Converting Command Line Arguments to Integers

The following program converts the command line arguments to integers and prints their sum:
```cpp
#include <iostream>
#include <string>
#include <sstream>

int main(int argc, char* argv[]) {
    int sum = 0;
    for (int i = 1; i < argc; i++) {
        std::stringstream ss(argv[i]);
        int num;
        if (ss >> num) {
            sum += num;
        } else {
            std::cerr << "Invalid argument: " << argv[i] << std::endl;
        }
    }
    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
```
If we run this program with the command `./program 1 2 3`, it will print:
```
Sum: 6
```
## Exam Tips

1. Make sure to check the `argc` variable before accessing the `argv` array to avoid out-of-bounds errors.
2. Use `std::string` to compare command line arguments with options.
3. Use `std::stringstream` to convert command line arguments to integers or floats.
4. Always check for errors when converting command line arguments to numbers.
5. Use `std::cerr` to print error messages.
6. Make sure to return an exit status from the `main` function.
7. Use command line arguments to customize the behavior of your program.