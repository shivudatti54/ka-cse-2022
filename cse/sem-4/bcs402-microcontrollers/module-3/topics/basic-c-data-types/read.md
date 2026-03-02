# Basic C Data Types

## Table of Contents

- [Basic C Data Types](#basic-c-data-types)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Fundamental Data Types in C](#1-fundamental-data-types-in-c)
  - [2. Type Qualifiers and Their Significance in Embedded Systems](#2-type-qualifiers-and-their-significance-in-embedded-systems)
  - [3. Fixed-Width Integer Types (stdint.h)](#3-fixed-width-integer-types-stdinth)
  - [4. Memory Considerations and Optimization](#4-memory-considerations-and-optimization)

## Introduction

In C programming, data types constitute the fundamental framework upon which all programs are constructed. The language's type system provides programmers with mechanisms to represent, store, and manipulate various forms of data, from simple numerical values to complex data structures. Understanding data types is particularly critical in embedded systems and microcontroller programming, where memory constraints are severe, hardware interactions require precise data representation, and the choice of data type directly impacts system performance, code size, and execution efficiency.

For students at the engineering/students level studying microcontroller programming, a comprehensive understanding of C data types extends beyond mere syntax—it encompasses knowledge of memory representation, range limitations, arithmetic behavior, and portability considerations across different microcontroller architectures. This chapter provides an in-depth examination of fundamental C data types, their implementation-defined characteristics, memory requirements, and specific applications in microcontroller environments. Additionally, we explore the standard integer types introduced in C99 and the critical role of type qualifiers in embedded systems development.

## Key Concepts

### 1. Fundamental Data Types in C

The C standard (ISO/IEC 9899) defines several fundamental data types that serve as building blocks for more complex data structures. These primary types can be classified into three principal categories: integer types, floating-point types, and character types. It is imperative to note that the C standard provides minimum guarantees for type sizes rather than fixed sizes, leading to implementation-dependent behavior that is particularly significant in microcontroller contexts.

#### 1.1 Integer Types

The `int` data type represents whole numbers without fractional components. The C standard mandates that an `int` must be at least 16 bits wide, though actual implementation may vary. On most 32-bit systems, `int` occupies 4 bytes (32 bits), while on many 8-bit and 16-bit microcontrollers, `int` is typically 2 bytes (16 bits).

**Signed Integer Representation:** Modern computer systems employ two's complement representation for signed integers. In two's complement, for an n-bit integer, the range of representable values is:

- **Minimum value:** -2^(n-1)
- **Maximum value:** 2^(n-1) - 1

**Proof of Range Calculation:** For a signed integer using two's complement with n bits:

- The most significant bit represents the sign (0 for positive, 1 for negative)
- Positive numbers range from 0 to 2^(n-1) - 1 (all bits except sign bit can be 1)
- Negative numbers: -1 is represented as all bits set to 1, and -2^(n-1) is represented as 100...0
- Therefore, total range spans from -2^(n-1) to +2^(n-1) - 1

For a 16-bit signed integer (typical in 8-bit microcontrollers):

- Range = -2^15 to +2^15 - 1
- Range = -32,768 to +32,767

For a 32-bit signed integer (standard desktop systems):

- Range = -2,147,483,648 to +2,147,483,647

**Type Modifiers:** C provides several modifiers to alter integer characteristics:

```c
short int; // At least 16 bits, typically 2 bytes
long int; // At least 32 bits, typically 4 bytes
long long int; // At least 64 bits, typically 8 bytes
signed int; // Explicit signed representation (default)
unsigned int; // Non-negative values only (0 to 2^n - 1)
```

For unsigned integers with n bits, the range is:

- **Minimum:** 0
- **Maximum:** 2^n - 1

For a 32-bit unsigned integer:

- Range = 0 to 4,294,967,295

#### 1.2 Floating-Point Types

Floating-point types represent numbers with decimal components using IEEE 754 standard representation on virtually all modern systems.

**Float (Single Precision):** Occupies 4 bytes (32 bits) with the following structure:

- 1 bit for sign
- 8 bits for exponent (biased by 127)
- 23 bits for mantissa (fraction)
- Precision: approximately 6-7 significant decimal digits
- Range: approximately ±3.4 × 10^38

**Double (Double Precision):** Occupies 8 bytes (64 bits):

- 1 bit for sign
- 11 bits for exponent (biased by 1023)
- 52 bits for mantissa
- Precision: approximately 15-16 significant decimal digits
- Range: approximately ±1.8 × 10^308

**Microcontroller Considerations:** Many 8-bit microcontrollers (e.g., AVR, PIC) lack native floating-point units (FPUs), causing floating-point operations to be emulated in software. This significantly increases execution time and code size. Consequently, fixed-point arithmetic or scaled integer operations are often preferred in embedded applications.

```c
float temperature = 25.75f; // Note the 'f' suffix for float literals
double precise_voltage = 3.141592653589793;
```

#### 1.3 Character Type (char)

The `char` data type stores a single character and occupies exactly 1 byte (8 bits) on all standard implementations. The C standard permits `char` to be either signed or unsigned by default, though most compilers treat it as unsigned for ARM and signed for x86.

**Range Analysis:**

- Signed char: -128 to +127 (2's complement)
- Unsigned char: 0 to 255

```c
char grade = 'A'; // ASCII value 65
unsigned char byte_data = 0xFF; // Value 255
signed char signed_byte = -1; // Value -1
```

#### 1.4 Void Type

The `void` type represents the absence of a value and serves critical functions in C:

```c
void function_without_return(void); // Function returns nothing
void* generic_pointer; // Pointer to unknown type
```

#### 1.5 Boolean Type (\_Bool and bool)

Since C99, the `_Bool` type (and the `bool` macro from `<stdbool.h>`) represents boolean values:

```c
#include <stdbool.h>

bool flag = true;
bool condition = (x > y);
```

The `_Bool` type converts any non-zero value to 1 and zero to 0 upon assignment.

### 2. Type Qualifiers and Their Significance in Embedded Systems

#### 2.1 const Qualifier

The `const` qualifier declares variables with values that cannot be modified after initialization, enabling compiler optimizations and preventing accidental modifications:

```c
const int ADC_MAX = 4095; // 12-bit ADC maximum value
const float REFERENCE_VOLTAGE = 3.3;
const uint8_t UART_BUFFER_SIZE = 64;
```

In microcontroller applications, `const` variables are typically placed in read-only memory (ROM or flash), conserving precious RAM.

#### 2.2 volatile Qualifier

The `volatile` qualifier is indispensable in embedded systems programming. It instructs the compiler that a variable's value may change at any time without action by the code being compiled, preventing aggressive optimizations that might eliminate necessary reads or writes:

```c
volatile uint8_t* const status_reg = (volatile uint8_t*)0x20;
volatile uint16_t adc_result; // Modified by ADC hardware
volatile bool interrupt_flag; // Modified by ISR
```

**Use Cases for volatile:**

1. Memory-mapped hardware registers
2. Variables shared between main code and interrupt service routines (ISRs)
3. Variables accessed from multiple threads or concurrent processes

### 3. Fixed-Width Integer Types (stdint.h)

The C99 standard introduced `<stdint.h>`, providing exact-width integer types essential for portable embedded code:

| Type               | Bits | Signed Range                                            | Unsigned Range                  |
| ------------------ | ---- | ------------------------------------------------------- | ------------------------------- |
| int8_t / uint8_t   | 8    | -128 to 127                                             | 0 to 255                        |
| int16_t / uint16_t | 16   | -32,768 to 32,767                                       | 0 to 65,535                     |
| int32_t / uint32_t | 32   | -2,147,483,648 to 2,147,483,647                         | 0 to 4,294,967,295              |
| int64_t / uint64_t | 64   | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | 0 to 18,446,744,073,709,551,615 |

**Portability Example:**

```c
#include <stdint.h>

void configure_timer(uint8_t prescaler) {
 // Guaranteed to be 8 bits regardless of architecture
 TCCR1B |= prescaler;
}

uint16_t read_adc(void) {
 // 16-bit result for 10/12-bit ADC
 return ADC;
}
```

### 4. Memory Considerations and Optimization

Understanding data type sizes is crucial for memory-constrained microcontrollers:

| Data Type | AVR (8-bit) | ARM Cortex-M (32-bit) | Desktop (64-bit) |
| --------- | ----------- | --------------------- | ---------------- |
| char      | 1           | 1                     | 1                |
| short     | 2           | 2                     | 2                |
| int       | 2           | 4                     | 4                |
| long      | 4           | 4                     | 8                |
| long long | 8           | 8                     | 8                |
| float     | 4           | 4                     | 4                |
| double    | 4           | 8                     | 8                |

**Optimization Strategies:**

1. Use smallest applicable type (uint8_t for values 0-255)
2. Use unsigned types for non-negative values (avoids sign extension overhead)
3. Pack structures using bit fields or pragma directives for memory-constrained systems

```c
// Packed structure for memory efficiency
typedef struct __attribute__((packed)) {
 uint8_t status;
 uint16_t value;
 uint8_t flags;
} sensor_data_t;
```
