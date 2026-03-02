# Shell Programming: Ordinary and Environment Variables

### Key Concepts

- **Ordinary Variables**: A variable that is defined within a script and retains its value between script executions.
- **Environment Variables**: A variable that is defined outside of a script and is available to all scripts in the environment.
- **Variables in Shell Scripts**:
  - `=` for assignment
  - `=` and `export` for variable declaration and export
  - `unset` for variable deletion
- **Environment Variables in Shell Scripts**:
  - `echo $VARIABLE_NAME` to display value
  - `export VARIABLE_NAME` to set environment variable

### Formulae and Definitions

- **Variable Declaration**: `VARIABLE_NAME=value`
- **Environment Variable Declaration**: `export VARIABLE_NAME=value`

### Theorems/Notes

- **Variable Scope**: Ordinary variables have a scope limited to the script, while environment variables have a scope that extends across all scripts in the environment.
- **Variable Export**: Using `export` with variable declaration allows environment variables to be accessed and modified by other scripts.

### Key Formulas

- `unset VARIABLE_NAME` to delete a variable
- `export -n VARIABLE_NAME` to declare a non-exportable variable

### Quick Revision Tips

- Understand the difference between ordinary and environment variables.
- Learn how to declare and export variables in shell scripts.
- Familiarize yourself with the `unset` command for variable deletion.
