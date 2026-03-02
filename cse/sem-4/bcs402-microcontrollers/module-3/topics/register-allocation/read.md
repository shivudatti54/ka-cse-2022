# Register Allocation in C Compilers

## Table of Contents

- [Register Allocation in C Compilers](#register-allocation-in-c-compilers)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Register Allocation Problem](#the-register-allocation-problem)
  - [Live Variable Analysis](#live-variable-analysis)
  - [Interference Graph Construction](#interference-graph-construction)
  - [Register Allocation Algorithms](#register-allocation-algorithms)
  - [Caller-Saved vs Callee-Saved Conventions](#caller-saved-vs-callee-saved-conventions)
  - [Register Spilling](#register-spilling)
  - [The 'register' Keyword in C](#the-register-keyword-in-c)
  - [Optimization Levels and Register Allocation](#optimization-levels-and-register-allocation)
  - [Pointer Aliasing and Register Allocation](#pointer-aliasing-and-register-allocation)
- [Examples](#examples)
  - [Example 1: Constructing an Interference Graph](#example-1-constructing-an-interference-graph)
  - [Example 2: Register Allocation Decision](#example-2-register-allocation-decision)
  - [Example 3: Spilling Analysis](#example-3-spilling-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Register allocation is a fundamental optimization in compiler design that maps program variables to a limited number of hardware registers available in the target microcontroller. In the context of C compilers and embedded systems, effective register allocation directly impacts code size, execution speed, and power consumption—all critical metrics for microcontroller applications. Unlike general-purpose processors, microcontrollers typically feature a very limited register set (e.g., AVR ATmega series has 32 general-purpose registers, ARM Cortex-M has 16), making efficient register allocation paramount.

The register allocation problem arises from a fundamental mismatch: a C program may contain dozens of variables, but the target architecture provides only a handful of registers. The compiler must determine which variables should reside in registers at each point in the program, when registers can be reused, and when variables must be "spilled" to memory due to register pressure. This optimization becomes particularly challenging in microcontroller environments where memory access is expensive in terms of cycles and power.

This topic examines register allocation from the compiler's perspective, covering the theoretical foundations, algorithms, and practical considerations relevant to embedded C programming. Understanding these concepts enables developers to write code that compilers can optimize more effectively and to make informed decisions about performance-critical sections.

## Key Concepts

### The Register Allocation Problem

Given a program with _n_ variables and _r_ available registers (_r_ << _n_), the compiler must assign each variable to either a register or a memory location such that the program executes correctly. The problem is formalized as follows: at each program point, variables that are simultaneously "live" (will be used in the future) cannot share the same register. Two variables _a_ and _b_ **interfere** if they are live at the same program point and cannot be assigned to the same register.

**Definition (Interference)**: Two variables _v₁_ and _v₂_ interfere if there exists a program point _p_ where both _v₁_ and _v₂_ are live simultaneously.

**Definition (Register Pressure)**: Register pressure at a program point is the number of variables live at that point. If register pressure exceeds the number of available registers, spilling is required.

### Live Variable Analysis

Live variable analysis is the foundation of register allocation. A variable is live at a program point if its current value will be used in some future computation before being redefined. The analysis computes **live ranges** for each variable—the set of program points where the variable is live.

The iterative dataflow equations for live variable analysis are:

- **GEN[p]**: Variables defined (killed) by the instruction at point _p_
- **KILL[p]**: Variables used (generated) by the instruction at point _p_
- **LiveOut[p]**: Variables live after point _p_
- **LiveIn[p]**: Variables live before point _p_

```
LiveIn[p] = Use[p] ∪ (LiveOut[p] - Def[p])
LiveOut[p] = ∪ LiveIn[succ(p)]
```

### Interference Graph Construction

The **interference graph** is a key data structure for register allocation. It is an undirected graph _G = (V, E)_ where:

- Each vertex _v ∈ V_ represents a variable (or virtual register)
- An edge _(u, v) ∈ E_ exists if variables _u_ and _v_ interfere (are simultaneously live)

**Theorem**: A register allocation with _k_ registers exists if and only if the interference graph is _k_-colorable (can be colored with _k_ colors such that no adjacent vertices share a color).

This problem is NP-complete in general, necessitating heuristic approaches in compilers.

### Register Allocation Algorithms

#### Graph Coloring (Chaitin's Algorithm)

Chaitin's algorithm is a widely-used register allocation technique that works as follows:

1. **Build interference graph** from live variable analysis
2. **Simplify**: Repeatedly remove nodes with degree < _k_ (number of available registers), pushing them onto a stack
3. **Select**: Pop nodes from stack, assigning colors not used by colored neighbors
4. **Spill**: If coloring fails (encountering a spilled node), insert memory store/load instructions and retry

The algorithm's effectiveness depends on the heuristics for node selection and the handling of spill code.

#### Linear Scan Allocation

Linear scan allocation, popular in JIT compilers and embedded systems, operates on a linear ordering of program points:

1. **Linearize** the control flow graph
2. **Sort** live intervals by start point
3. **Scan** intervals in order, allocating registers from a pool
4. **Spill** intervals that cannot obtain registers from active intervals

Pseudocode for linear scan:

```
allocate(Intervals):
 active = empty list sorted by end point
 for interval in sorted_intervals:
 expire_old_intervals(interval, active)
 if active.size < num_regs:
 allocate_register(interval, active)
 else:
 spill_at_interval(interval, active)
```

### Caller-Saved vs Callee-Saved Conventions

Calling conventions define which registers must be preserved across function calls:

- **Callee-saved registers**: The called function must preserve these registers' values; if used, the callee saves and restores them
- **Caller-saved registers (volatile)**: The calling function must save these if needed after the call

For ARM Cortex-M (AAPCS):

- **Callee-saved**: R4-R11, SP
- **Caller-saved**: R0-R3, R12, LR

**Example**: In the function below, the compiler must decide which registers to use:

```c
int compute(int a, int b, int c) {
 int x = a + b;
 int y = b * c;
 return x + y;
}
```

Parameters _a_, _b_, _c_ arrive in R0, R1, R2. The compiler may keep _x_ in R0 (return value register) while computing _y_, minimizing register moves.

### Register Spilling

When register pressure exceeds available registers, some variables must be temporarily stored in memory. The compiler inserts:

- **Spill stores**: Save variable to memory before register reuse
- **Spill loads**: Reload variable from memory when needed

**Spill Cost Analysis**: The compiler computes the cost of spilling each variable:

```
SpillCost(v) = LoadCost(v) × Loads(v) + StoreCost(v) × Stores(v)
```

Variables with lower spill costs are prioritized for spilling.

### The 'register' Keyword in C

The C language provides the `register` storage class specifier as a hint to the compiler:

```c
register int counter; // Hint: allocate in register if possible
```

Important notes:

- The hint may be ignored; compilers often make better decisions
- Cannot apply to absolute addresses: `register int *p;` is valid, but `register int a[10];` and taking address of register variable is implementation-defined
- Modern compilers ignore this keyword for optimization, as they perform better register allocation than programmers can hint

### Optimization Levels and Register Allocation

Different optimization levels affect register allocation aggressiveness:

- **-O0 (no optimization)**: Variables typically not allocated to registers; simpler debugging
- **-O1**: Basic register allocation with limited spilling
- **-O2/-O3**: Aggressive allocation, loop-invariant code motion, better register reuse
- **-Os**: Minimizes code size, may accept more spills to reuse registers

**Example**: Consider a loop processing an array:

```c
void process(int *arr, int n) {
 int sum = 0;
 for (int i = 0; i < n; i++)
 sum += arr[i];
}
```

At -O2, the compiler likely allocates _sum_ and _i_ to registers throughout the loop, minimizing memory access. At -O0, each operation may involve memory loads/stores.

### Pointer Aliasing and Register Allocation

Pointer aliasing significantly complicates register allocation. If the compiler cannot determine whether two pointers reference the same memory location, it must assume potential aliasing, restricting optimization:

```c
void update(int *a, int *b, int n) {
 for (int i = 0; i < n; i++)
 a[i] = b[i] + 1; // May alias if a == b
}
```

The compiler cannot keep _b[i]_ in a register across the _a[i]_ write because writing through _a_ might modify the location pointed to by _b_. The sibling topic of **Pointer Aliasing** explores these constraints in detail.

## Examples

### Example 1: Constructing an Interference Graph

Given the following C code fragment:

```c
int a = x;
int b = a + 1;
int c = a + b;
int d = c + 1;
return d;
```

Assuming execution flows sequentially (no branches), we analyze live variables at each point:

| Point           | Defined | Used | Live Variables | Interferences |
| --------------- | ------- | ---- | -------------- | ------------- |
| After a = x     | a       | x    | a              | -             |
| After b = a + 1 | b       | a    | a, b           | a-b           |
| After c = a + b | c       | a, b | b, c           | b-c           |
| After d = c + 1 | d       | c    | d              | -             |

The interference graph has edges: a-b, b-c. With 2 registers, we can color this graph (e.g., assign a and c to register R0, b and d to R1). With only 1 register, we must spill: store a to memory after definition, load before use in b = a + 1.

### Example 2: Register Allocation Decision

Consider the ARM Cortex-M4 function:

```c
long long mul_add(int a, int b, int c) {
 long long result = (long long)a * b + c;
 return result;
}
```

Register allocation decisions:

- Parameters a, b, c arrive in R0, R1, R2
- Multiplication requires 64-bit result: R0-R1 hold a (sign-extended), multiply with R1
- Result in R0-R1 (low), R2-R3 (high for 64-bit)
- Final addition: result (in R0-R1) + c (R2)
- Return: R0-R1

The compiler uses R0-R3 (caller-saved), avoiding callee-saved register save/restore overhead. This demonstrates how calling conventions guide allocation.

### Example 3: Spilling Analysis

For a microcontroller with only 4 general-purpose registers (R0-R3), analyze:

```c
int compute(int a, int b, int c, int d, int e) {
 int x = a + b;
 int y = c + d;
 return x + y + e;
}
```

Live variable analysis at the return expression:

- x, y, e are all live simultaneously
- Register pressure = 3 (fits in 4 registers)

But consider:

```c
int complex(int a, int b, int c, int d, int e, int f) {
 int x = a + b;
 int y = c + d;
 int z = e + f;
 return x + y + z;
}
```

At return: x, y, z live = 3 registers needed. If we add one more live variable at return, we exceed 4 registers and must spill.

## Exam Tips

1. **Distinguish register allocation from register assignment**: Register allocation decides which variables get registers; assignment maps to specific physical registers.

2. **Remember the interference graph is the key data structure**: Most allocation algorithms work by constructing and coloring the interference graph.

3. **Understand when spilling occurs**: Spilling happens when live variable count exceeds register count; the compiler chooses which variables to spill based on spill cost analysis.

4. **Caller-saved vs callee-saved**: The calling function saves caller-saved registers before calls if needed; callee-saved registers are the callee's responsibility.

5. **The register keyword is a hint, not a guarantee**: Modern compilers typically ignore it; they have better allocation algorithms than manual hints.

6. **Connect to sibling topics**: Pointer aliasing restricts allocation because the compiler cannot assume pointers don't reference the same memory; portability issues arise from different architectures having different register counts and calling conventions.

7. **Optimization levels matter**: Higher optimization levels (-O2, -O3) perform more aggressive register allocation than -O0, at the cost of harder debugging.
