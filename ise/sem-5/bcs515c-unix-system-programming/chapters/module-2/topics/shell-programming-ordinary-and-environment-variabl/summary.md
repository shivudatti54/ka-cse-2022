# Shell Programming: Ordinary and Environment Variables

### Definitions and Key Concepts

- **Ordinary Variables**: Also known as local variables, these are declared within a shell script or command and are only accessible within that scope.
- **Environment Variables**: Pre-defined variables in the operating system's environment that can be accessed and modified by shell scripts and commands.

### Ordinary Variables

- **Declaring Ordinary Variables**:
  - `var_name=value` (e.g., `name="John"`)
  - `var_name=$(expression)` (e.g., `name="John"`)
- **Accessing Ordinary Variables**:
  - `$var_name` (e.g., `echo $name`)
- **Modifying Ordinary Variables**:
  - `var_name=value` (e.g., `name="Jane"`)

### Environment Variables

- **Declaring Environment Variables**:
  - `export var_name=value` (e.g., `export NAME="John"`)
- **Accessing Environment Variables**:
  - `$var_name` (e.g., `echo $NAME`)
- **Modifying Environment Variables**:
  - `export var_name=value` (e.g., `export NAME="Jane"`)

### Important Formulas and Theorems

- **Variable Expansion**:
  - `$(expression)` (e.g., `echo $(name)` = `echo John`)
- **Parameter Expansion**:
  - `${parameter}` (e.g., `echo ${name}` = `echo John`)

### Key Shell Commands

- **echo**: Prints the value of a variable
- **set**: Prints the value of an environment variable
- **unset**: Removes a variable or environment variable

### Example Shell Script

```bash
#!/bin/bash

# Declare ordinary variable
name="John"

# Print ordinary variable
echo $name

# Declare environment variable
export NAME="Jane"

# Print environment variable
echo $NAME

# Modify ordinary variable
name="Emma"

# Print modified ordinary variable
echo $name

# Modify environment variable
export NAME="Oliver"

# Print modified environment variable
echo $NAME
```
