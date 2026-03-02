# **TEXT BOOK: Sections 5.1**

## **Theory of Computation**

### 5.1 Introduction to Theory of Computation

The Theory of Computation is a branch of computer science that deals with the study of the fundamental limits and properties of computation. It provides a rigorous mathematical framework for understanding the behavior of algorithms and computational systems.

#### History of Theory of Computation

The development of the Theory of Computation dates back to the early 20th century, with contributions from mathematicians such as Alonzo Church and Stephen Kleene. Church's lambda calculus and Kleene's recursive functions were among the first formal systems to be studied in the context of computation.

In the 1950s, the development of the Turing Machine by Alan Turing revolutionized the field of Theory of Computation. The Turing Machine is a simple, abstract device that can simulate the behavior of any algorithm, making it a fundamental model of computation.

#### Key Concepts

There are several key concepts that underlie the Theory of Computation:

- **Computational Model**: A computational model is a formal representation of a computational system. Common models include the Turing Machine, the Finite Automaton, and the Pushdown Automaton.
- **Algorithm**: An algorithm is a set of instructions that can be used to solve a computational problem. Algorithms can be expressed in various forms, including recursively defined functions and iterative algorithms.
- **Computability**: Computability refers to the ability of a computational system to solve problems that are computable by a universal Turing Machine. In other words, a problem is computable if it can be solved by a bounded number of steps, regardless of the size of the input.
- **Decidability**: Decidability refers to the ability of a computational system to determine whether a problem is solvable in a finite number of steps.

### 5.1.1 Turing Machine

The Turing Machine is one of the most influential models of computation in the Theory of Computation. It consists of a read/write head that moves along a tape, reading and writing symbols to the tape.

**Diagram:**

The Turing Machine has several key components:

- **Tape**: The tape is a infinite sequence of cells, each of which can hold a symbol from a finite alphabet.
- **Head**: The head is the read/write head that moves along the tape, reading and writing symbols to the tape.
- **State**: The state is the current configuration of the Turing Machine, including the position of the head and the symbols on the tape.
- **Transition Function**: The transition function determines the next state and the position of the head based on the current state and the symbol read from the tape.

### 5.1.2 Finite Automaton

A Finite Automaton is a computational model that consists of a finite state machine that can recognize regular languages.

**Diagram:**

A Finite Automaton has several key components:

- **States**: The states are the possible configurations of the Finite Automaton, including the current state and the input symbol.
- **Transition Function**: The transition function determines the next state based on the current state and the input symbol.
- **Accepting States**: The accepting states are the states that indicate whether the input is accepted by the Finite Automaton.

### 5.1.3 Pushdown Automaton

A Pushdown Automaton is a computational model that consists of a finite state machine that can recognize regular languages and has a stack.

**Diagram:**

A Pushdown Automaton has several key components:

- **States**: The states are the possible configurations of the Pushdown Automaton, including the current state and the stack.
- **Transition Function**: The transition function determines the next state and the stack based on the current state and the input symbol.
- **Stack**: The stack is a finite sequence of symbols that can be pushed and popped.

### 5.1.4 Decision Problem

A decision problem is a problem that can be solved by a computational system. In the Theory of Computation, decision problems are typically represented as follows:

- **Input**: The input is a finite sequence of symbols.
- **Output**: The output is a yes or no answer to whether the input satisfies a certain property.

### 5.1.5 Complexity Classes

Complexity classes are a way of classifying decision problems based on the resources required to solve them. Common complexity classes include:

- **P**: The class of problems that can be solved in polynomial time.
- **NP**: The class of problems that can be verified in polynomial time.
- **NP-complete**: The class of problems that are both in NP and NP-hard.

### 5.1.6 Reduction

A reduction is a way of transforming one problem into another problem. A reduction can be used to prove that one problem is in a certain complexity class.

**Example:**

Consider the problem of determining whether a graph is connected. We can reduce this problem to the problem of determining whether a binary string is a permutation of the numbers 0 to n. To do this, we can create a graph where each vertex corresponds to a number from 0 to n, and two vertices are connected if the corresponding numbers are adjacent in the binary string.

### 5.1.7 Applications

The Theory of Computation has many applications in computer science and other fields, including:

- **Compiler Design**: The Theory of Computation is used to design compilers for programming languages.
- **Algorithm Design**: The Theory of Computation is used to design efficient algorithms for solving computational problems.
- **Artificial Intelligence**: The Theory of Computation is used to design models of intelligence and to develop intelligent systems.

### Further Reading

- **"Introduction to the Theory of Computation" by Michael Sipser**: This book provides a comprehensive introduction to the Theory of Computation, including the basics of computation, automata theory, and complexity theory.
- **"Algorithms" by Robert Sedgewick and Kevin Wayne**: This book provides a comprehensive introduction to algorithms, including the basics of algorithms, sorting algorithms, and searching algorithms.
- **"Computability Theory" by Jeffrey H. Shoenfield**: This book provides a comprehensive introduction to computability theory, including the basics of computability, decidability, and complexity theory.

### Conclusion

The Theory of Computation is a fundamental branch of computer science that deals with the study of the fundamental limits and properties of computation. It provides a rigorous mathematical framework for understanding the behavior of algorithms and computational systems. The Theory of Computation has many applications in computer science and other fields, and it continues to be an active area of research.
