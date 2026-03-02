# Command-Line Arguments in UNIX System Programming

## Introduction

In the C programming language, the `main()` function serves as the entry point for every program. In a typical non-system programming context, it is often defined without parameters (`int main(void)`). However, when writing programs for a UNIX environment that are intended to be executed from the shell, the ability to accept inputs directly from the command line becomes crucial. These inputs are known as **command-line arguments**. They allow users to customize the program's behavior without modifying its source code, making tools like `ls`, `grep`, and `cp` powerful and flexible.

## Core Concepts

### 1. The `main` Function Signature

To access command-line arguments, the `main()` function is defined with two specific parameters: