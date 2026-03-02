# Shell Programming: Ordinary and Environment Variables

## **Introduction**

In shell programming, variables are used to store and manipulate data. There are two types of variables: ordinary variables and environment variables. This topic will cover the definitions, explanations, and examples of ordinary and environment variables.

## **Ordinary Variables**

### Definition

Ordinary variables are stored in the shell's memory and are specific to the current shell session. They are created using the `var_name=value` syntax.

### Characteristics

- Are stored in the shell's memory
- Are specific to the current shell session
- Are created using the `var_name=value` syntax

### Examples

- `name="John"` - creates an ordinary variable `name` with the value "John"
- `age=30` - creates an ordinary variable `age` with the value 30

### Operations

- Assignment: `var_name=value`
- Print: `echo $var_name`
- Modification: `var_name=new_value`

## **Environment Variables**

### Definition

Environment variables are stored outside the shell's memory and are shared among all processes. They are created by the operating system and can be modified by the user.

### Characteristics

- Are stored outside the shell's memory
- Are shared among all processes
- Can be modified by the user

### Examples

- `PATH=/bin:/usr/bin` - creates an environment variable `PATH` with the value `/bin:/usr/bin`
- `HOME=/home/user` - creates an environment variable `HOME` with the value `/home/user`

### Operations

- Assignment: `var_name=value`
- Print: `echo $var_name`
- Modification: `export var_name=new_value`

## **Differences between Ordinary and Environment Variables**

|              | Ordinary Variables                | Environment Variables       |
| ------------ | --------------------------------- | --------------------------- |
| **Storage**  | Stored in shell memory            | Stored outside shell memory |
| **Scope**    | Specific to current shell session | Shared among all processes  |
| **Creation** | Created using `var_name=value`    | Created by operating system |

## **Best Practices**

- Use environment variables for configuration and settings that need to be shared among processes.
- Use ordinary variables for data that is specific to the current shell session.

## **Conclusion**

In this topic, we have covered the definitions, explanations, and examples of ordinary and environment variables. Understanding the differences between these two types of variables is essential for effective shell programming. By following best practices, you can write efficient and scalable shell scripts.
