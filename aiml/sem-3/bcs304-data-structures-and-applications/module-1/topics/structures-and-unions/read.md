# Structures and Unions


## Table of Contents

- [Structures and Unions](#structures-and-unions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Structure Definition and Declaration](#1-structure-definition-and-declaration)
  - [2. Memory Layout and Alignment](#2-memory-layout-and-alignment)
  - [3. Arrays of Structures](#3-arrays-of-structures)
  - [4. Nested Structures](#4-nested-structures)
  - [5. Bit-Fields](#5-bit-fields)
  - [6. Union Definition and Memory Model](#6-union-definition-and-memory-model)
  - [7. Comparison: Structure vs Union](#7-comparison-structure-vs-union)
  - [8. Practical Applications in Data Structures](#8-practical-applications-in-data-structures)
- [Examples](#examples)
  - [Example 1: Structure Size Calculation with Padding](#example-1-structure-size-calculation-with-padding)
  - [Example 2: Union for Type Identification](#example-2-union-for-type-identification)
  - [Example 3: Implementing a Binary Tree Node](#example-3-implementing-a-binary-tree-node)
- [Exam Tips](#exam-tips)

## Introduction

Structures and unions are fundamental composite data types in the C programming language that serve as building blocks for implementing complex data structures. A structure is a user-defined data type that aggregates heterogeneous data elements of possibly different types into a single logical unit, while a union is a special data structure where all members share the same memory location. In the context of data structures and applications, these constructs are essential for creating nodes in linked lists, tree nodes, and various other compound data types used in algorithm implementation. Understanding the memory layout, alignment requirements, and practical applications of structures and unions is crucial for developing efficient and memory-conscious software systems.

This module examines the theoretical foundations of structures and unions, their memory representation, and their applications in data structure implementation. The discussion includes formal definitions, mathematical characterization of memory requirements, and practical examples demonstrating their use in real-world scenarios. Special attention is given to memory alignment, padding, and the implications of these concepts on storage efficiency.

## Key Concepts

### 1. Structure Definition and Declaration

A structure is a composite data type that groups together variables (called members or fields) of possibly different types under a single name. The formal definition follows:

**Definition (Structure):** A structure is a heterogeneous aggregate data type consisting of a set of named members, each of which has its own type. The total size of a structure is determined by the sum of its members' sizes plus any padding required for memory alignment.

The syntax for defining a structure in C is:

```c
struct structure_tag {
    data_type member1;
    data_type member2;
    // ... more members
} [variable_list];
```

For example, a node structure for a linked list can be defined as:

```c
struct Node {
    int data;
    struct Node* next;
};
```

### 2. Memory Layout and Alignment

The memory layout of a structure is a critical consideration in data structure implementation. Each data type has specific alignment requirements that ensure efficient memory access by the processor. The compiler inserts padding bytes between members to satisfy these alignment requirements.

**Alignment Rules:**

- Each data type has an alignment boundary (typically equal to its size for primitive types)
- The structure's alignment is the maximum alignment of any member
- The compiler may add padding at the end of the structure to satisfy alignment when structures are stored in arrays

**Theorem (Structure Size):** The size of a structure is given by:
Size(struct) = Σ(size of member i) + Σ(padding bytes)

_Proof:_ Consider a structure with members requiring alignments a₁, a₂, ..., aₙ. The compiler places each member at the smallest address that satisfies both the member's alignment requirement and the offset from the previous member. Padding bytes are inserted when the cumulative offset is not divisible by the member's alignment requirement. The final structure size is padded to be a multiple of the structure's alignment requirement.

**Example Calculation:**

```c
struct Example {
    char a;      // 1 byte, alignment 1
    // 3 padding bytes
    int b;       // 4 bytes, alignment 4
    char c;      // 1 byte, alignment 1
    // 3 padding bytes for array alignment
};
```

Actual size: 1 + 3 + 4 + 1 + 3 = 12 bytes (on a typical 32-bit system where int = 4 bytes)

### 3. Arrays of Structures

Arrays of structures are extensively used in data structure implementations, particularly for sequential storage of records. When declaring arrays of structures, each structure element occupies consecutive memory locations.

```c
struct Student {
    int rollno;
    char name[30];
    float marks;
};

struct Student class[50];  // Array of 50 student records
```

The total memory required for an array of n structures is n × sizeof(struct), assuming proper alignment.

### 4. Nested Structures

Structures can contain other structures as members, enabling the creation of complex hierarchical data types:

```c
struct Date {
    int day;
    int month;
    int year;
};

struct Employee {
    int emp_id;
    char name[50];
    struct Date join_date;  // Nested structure
    struct Date birth_date; // Another nested structure
};
```

### 5. Bit-Fields

Bit-fields allow specification of the exact number of bits for integer members, enabling compact storage of flag variables and small integers:

```c
struct Flags {
    unsigned int is_active : 1;
    unsigned int is_valid : 1;
    unsigned int priority : 3;  // Values 0-7
    unsigned int reserved : 3;
};
```

The total size of a bit-field structure is implementation-defined but is at least large enough to contain all specified bits plus any necessary padding.

### 6. Union Definition and Memory Model

A union is a special data type where all members share the same memory location. The memory allocated for a union is sufficient to hold the largest member.

**Definition (Union):** A union is a composite data type in which all members overlay the same memory location. The size of a union is equal to the size of its largest member (plus any padding required for alignment).

**Memory Model:** At any given time, only one member of a union can contain meaningful data. Writing to one member overwrites all other members.

```c
union Data {
    int i;
    float f;
    char c;
};

union Data value;
value.i = 10;    // Now value.f and value.c contain undefined values
value.f = 3.14;  // Now value.i contains garbage (overwritten)
```

### 7. Comparison: Structure vs Union

| Aspect         | Structure                             | Union                                  |
| -------------- | ------------------------------------- | -------------------------------------- |
| Memory         | All members occupy separate memory    | All members share same memory          |
| Size           | Sum of all members + padding          | Size of largest member                 |
| Access         | All members accessible simultaneously | Only one member meaningful at a time   |
| Use Case       | Store related heterogeneous data      | Save memory when only one value needed |
| Initialization | Can initialize all members            | Can initialize only first member       |

### 8. Practical Applications in Data Structures

**Application 1: Variant Records**
Unions are used to create variant records where a field can be one of several types:

```c
struct TreeNode {
    int is_leaf;
    union {
        int value;  // If leaf node
        struct {
            struct TreeNode* left;
            struct TreeNode* right;
        } children;  // If internal node
    } node_data;
};
```

**Application 2: Memory-Efficient Storage**
When storing mixed-type data where only one type is used at a time:

```c
struct Symbol {
    char name[20];
    enum {INT_TYPE, FLOAT_TYPE, STRING_TYPE} type;
    union {
        int int_val;
        float float_val;
        char str_val[20];
    } value;
};
```

## Examples

### Example 1: Structure Size Calculation with Padding

Given the structure:

```c
struct Packet {
    char flag;      // 1 byte
    int sequence;   // 4 bytes
    short length;   // 2 bytes
    char checksum;  // 1 byte
};
```

Calculate the size on a system where int = 4 bytes, short = 2 bytes, and alignment = 4 bytes.

**Solution:**

1. `char flag` at offset 0, size = 1, remaining = 3
2. Padding of 3 bytes to align `int sequence` to offset 4
3. `int sequence` at offset 4, size = 4, remaining = 0
4. `short length` at offset 8, size = 2, remaining = 2
5. `char checksum` at offset 10, size = 1, remaining = 1
6. Padding of 1 byte to make total size a multiple of 4

Total size = 1 + 3 + 4 + 2 + 1 + 1 = 12 bytes

### Example 2: Union for Type Identification

```c
#include <stdio.h>

union Number {
    int i;
    float f;
};

int main() {
    union Number num;
    char type = 'i';

    if (type == 'i') {
        num.i = 100;
        printf("Integer value: %d\n", num.i);
    } else {
        num.f = 3.14159;
        printf("Float value: %f\n", num.f);
    }

    // Memory occupied by union: sizeof(union Number) = %zu\n", sizeof(num));
    return 0;
}
```

### Example 3: Implementing a Binary Tree Node

```c
struct TreeNode {
    int key;
    struct TreeNode* left;
    struct TreeNode* right;
    // Additional data for different node types
    union {
        struct {
            // Internal node-specific data
            int height;
        } internal;
        struct {
            // Leaf node-specific data
            int value;
        } leaf;
    } node_type;
};

int calculateHeight(struct TreeNode* node) {
    if (node == NULL) return 0;
    if (node->left == NULL && node->right == NULL)
        return 1;
    int leftHeight = calculateHeight(node->left);
    int rightHeight = calculateHeight(node->right);
    return (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}
```

## Exam Tips

1. **Memory Alignment:** Always consider alignment requirements when calculating structure sizes. Remember that padding is added to satisfy the larger alignment requirement of subsequent members.

2. **Union Size:** The size of a union equals the size of its largest member. This is a common MCQ pattern.

3. **Structure vs Union:** Understand that structures allocate separate memory for each member while unions share memory—use this distinction to solve application-based questions.

4. **Bit-Fields:** Remember that bit-fields save memory but accessing them may require additional CPU instructions. The exact bit representation is implementation-dependent.

5. **Pointer Arithmetic with Structures:** When using pointers to structures, the arrow operator (->) dereferences and accesses members simultaneously. This is essential for linked list implementations.

6. **Nested Structures:** Pay attention to the memory layout of nested structures—the inner structure's members are laid out according to its own alignment rules.

7. **Padding Calculation:** Practice multiple examples of structure padding calculations as this is frequently tested in examinations with specific member arrangements.

8. **Common Mistake:** Don't assume structure members are stored in contiguous memory without considering padding—always recalculate for each unique structure definition.

9. **Union Initialization:** Only the first member of a union can be directly initialized in C. Remember this restriction when writing code.

10. **Practical Application:** In data structure implementations, use structures for nodes with multiple fields and unions when variant data types are needed to optimize memory usage.
