# Introduction to Structures in C

## 1. What is a Structure?

In the C programming language, an array is a powerful data structure that allows you to store a collection of elements of the _same_ data type. However, real-world data is often more complex. Consider a student record: it contains a name (string), a roll number (integer), and marks (float). An array cannot hold this heterogeneous mix of data types together as a single unit.

This is where **structures** come in. A structure (often called a `struct`) is a user-defined data type that allows you to combine data items of different kinds. It is a composite data type that groups related variables under one name. The variables inside a structure are called its **members**.

**Analogy:** Think of a structure as a "form" or a "blueprint." A "Student Registration Form" has fields for Name, Roll Number, and Grade. Each completed form is an instance (or variable) of that structure type.

## 2. Declaring a Structure

To use a structure, you must first define its format or blueprint. This is done using the `struct` keyword.

**Syntax:**

```c
struct structure_name {
    data_type member1;
    data_type member2;
    // ... more members
};
```

**Note:** The semicolon after the closing brace `}` is mandatory.

**Example:**

```c
struct Student {
    char name[50];
    int roll_number;
    float marks;
};
```

Here, we have defined a new data type called `struct Student`. This blueprint now can be used to create variables (instances) of this type.

## 3. Creating Structure Variables

You can create variables of a structure type in a few ways:

**Method 1: Declare after the structure definition**

```c
struct Student {
    char name[50];
    int roll_number;
    float marks;
};

int main() {
    struct Student student1, student2; // Declares two variables
    return 0;
}
```

**Method 2: Declare along with the structure definition**

```c
struct Student {
    char name[50];
    int roll_number;
    float marks;
} student1, student2; // Variables declared here
```

**Method 3: Using typedef (Highly Recommended)**
The `typedef` keyword allows you to create an alias for a data type. This makes the code cleaner.

```c
typedef struct {
    char name[50];
    int roll_number;
    float marks;
} Student; // 'Student' is now a type alias for 'struct {...}'

int main() {
    Student student1, student2; // Clean declaration without 'struct'
    return 0;
}
```

## 4. Accessing Structure Members

Individual members of a structure variable are accessed using the **dot (`.`)** operator, also known as the member access operator.

**Syntax:**

```c
structure_variable_name.member_name
```

**Example:**

```c
Student student1;

// Assigning values to members
strcpy(student1.name, "Alice Smith"); // For string arrays, use strcpy
student1.roll_number = 101;
student1.marks = 92.5;

// Accessing and printing member values
printf("Name: %s\n", student1.name);
printf("Roll Number: %d\n", student1.roll_number);
printf("Marks: %.2f\n", student1.marks);
```

## 5. Initializing Structures

You can initialize a structure variable at the time of declaration, similar to how you initialize an array.

**Syntax:**

```c
struct StructureName variable = {value1, value2, ..., valueN};
```

The values are assigned to the members in the order they are declared in the structure definition.

**Example:**

```c
// Using our typedef 'Student'
Student student1 = {"Bob Jones", 102, 88.7};
```

## 6. Comparing Structure Variables

You cannot compare two structure variables directly using the `==` operator.

```c
if (student1 == student2) { // ERROR: Invalid operation
    // ...
}
```

Instead, you must compare each member individually.

```c
if ((student1.roll_number == student2.roll_number) &&
    (student1.marks == student2.marks) &&
    (strcmp(student1.name, student2.name) == 0)) {
    printf("The student records are identical.\n");
}
```

## 7. Arrays of Structures

Since a structure is a data type, you can create arrays of structures. This is incredibly useful for managing records for multiple entities (e.g., a class of 50 students).

**Example:**

```c
Student class[50]; // Array of 50 Student structures

// Accessing the 10th student's roll number
class[9].roll_number = 110;

// Looping through the array to initialize all marks to 0
for(int i = 0; i < 50; i++) {
    class[i].marks = 0.0;
}
```

## 8. Structures within Structures (Nested Structures)

A member of a structure can itself be another structure. This is called nesting.

**Example:**

```c
typedef struct {
    int day;
    int month;
    int year;
} Date;

typedef struct {
    char name[50];
    Date birthday; // Nested structure
    int roll_number;
} Student;

int main() {
    Student s1;
    s1.birthday.day = 15; // Accessing nested member
    s1.birthday.month = 8;
    s1.birthday.year = 2002;
    return 0;
}
```

## 9. Introduction to Unions

A **union** is a special data type that allows storing different data types in the same memory location. You can define a union with many members, but **only one member can contain a value at any given time**. The memory allocated for a union is large enough to hold the largest member.

**Syntax and Example:**

```c
union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    union Data data;
    data.i = 10;       // Now holds an integer
    printf("data.i : %d\n", data.i);

    data.f = 220.5;    // Now holds a float, the integer value is overwritten
    printf("data.f : %.2f\n", data.f);

    // data.i is now invalid
    return 0;
}
```

### Key Differences: Structure vs. Union

| Feature           | Structure (`struct`)                                   | Union (`union`)                                                |
| :---------------- | :----------------------------------------------------- | :------------------------------------------------------------- |
| **Memory**        | Each member has its own memory location.               | All members share the same memory location.                    |
| **Size**          | Size >= sum of sizes of all members.                   | Size = size of the largest member.                             |
| **Member Access** | All members can be accessed independently at any time. | Only one member can be accessed meaningfully at a time.        |
| **Purpose**       | To group different data types together.                | To provide efficient memory usage for mutually exclusive data. |

**Memory Diagram:**

```
// Memory layout for 'struct Example'
+----------------+----------------+----------------+
|     int a      |    float b     |     char c     | // Each member has unique address
+----------------+----------------+----------------+
Address: 1000      1004            1008

// Memory layout for 'union Example'
+-----------------------------------------------+
|                  Largest Member               | // All members start at same address
+-----------------------------------------------+
Address: 1000
```

## 10. Size of Structures (`sizeof`)

The `sizeof` operator returns the total memory allocated for a structure. Due to **memory alignment** (or padding), the size of a structure is often larger than the sum of its parts. The compiler may add empty bytes between members to align data on natural address boundaries for the CPU to access them efficiently.

**Example:**

```c
struct Example {
    char a;    // 1 byte
               // 3 bytes padding (assuming 4-byte alignment for int)
    int b;     // 4 bytes
    float c;   // 4 bytes
};             // Total: 1 + 3(pad) + 4 + 4 = 12 bytes

printf("Size of struct: %zu bytes\n", sizeof(struct Example));
```

## Exam Tips

1.  **`typedef` is your friend:** Using `typedef` makes code less verbose and avoids repeatedly writing the `struct` keyword.
2.  **Dot vs. Arrow:** Remember, the dot (`.`) operator is used for accessing members of a structure variable. When you have a _pointer to a structure_, you use the arrow (`->`) operator (`ptr->member` is equivalent to `(*ptr).member`).
3.  **Initialization Order:** When initializing a structure, the order of values must match the order of member declarations.
4.  **No Direct Comparison:** You cannot compare two `struct`s directly. Always compare member by member.
5.  **Union Caution:** Accessing a union member that was not the last one written to leads to undefined behavior. The data will be reinterpreted as the new type, often resulting in garbage values.
6.  **Mind the Padding:** Be aware that `sizeof(struct)` might not be what you expect due to memory alignment. This is crucial for writing portable and efficient code, especially when dealing with hardware or file I/O.
