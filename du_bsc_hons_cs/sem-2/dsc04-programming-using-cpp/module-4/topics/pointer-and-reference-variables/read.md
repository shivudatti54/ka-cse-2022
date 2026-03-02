# Pointer and Reference Variables in C++

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

### 1.1 What Are Pointers and References?

In C++, **pointers** and **references** are fundamental concepts that provide indirect access to memory locations. While variables store actual values, pointers store memory addresses where values reside. References, introduced in C++, provide an alternative mechanism for accessing variables indirectly through aliases.

### 1.2 Why This Topic Matters

This topic is crucial for several reasons:

- **Memory Management**: Understanding how data is stored and accessed in memory is essential for writing efficient C++ programs. The Delhi University syllabus emphasizes memory allocation and deallocation.
- **Data Structures**: Implementation of linked lists, trees, graphs, and other data structures extensively use pointers.
- **System Programming**: Operating systems, drivers, and embedded systems require direct memory manipulation.
- **Dynamic Memory**: Allocating memory at runtime (using `new` and `malloc`) requires understanding pointers.
- **Function Arguments**: Passing large structures efficiently by reference/pointer rather than by value.
- **Modern C++**: Smart pointers in C++11 and later provide safe memory management, reducing memory leaks.

### 1.3 Syllabus Context (NEP 2024 UGCF)

This unit aligns with:
- Unit III: Functions and User-Defined Types (References and Pointers)
- Unit IV: Object-Oriented Programming (Dynamic memory allocation)
- Unit V: Advanced Features (Smart pointers, move semantics)

---

## 2. Pointers: Deep Dive

### 2.1 Pointer Declaration and Initialization

A pointer is a variable that holds a memory address. The syntax uses the asterisk (`*`) operator:

```cpp
int *ptr;           // Pointer to an integer
double *dptr;       // Pointer to a double
char *cptr;         // Pointer to a character
```

**Key Point**: The asterisk can be placed either next to the type or the variable name—both are valid, but consistency matters for readability.

```cpp
int* p1, p2;    // p1 is a pointer, p2 is just an int (common mistake!)
int *p3, *p4;   // Both are pointers (better style)
```

### 2.2 Address-of Operator (`&`)

The `&` operator returns the memory address of a variable:

```cpp
int num = 42;
int *ptr = &num;    // ptr now holds the address of num

cout << "Value of num: " << num << endl;      // 42
cout << "Address of num: " << &num << endl;   // hexadecimal address
cout << "Value of ptr: " << ptr << endl;      // same hexadecimal address
cout << "Value pointed by ptr: " << *ptr << endl;  // 42 (dereferencing)
```

### 2.3 Dereferencing Pointers

The dereference operator (`*`) accesses the value at the memory address stored in the pointer:

```cpp
*ptr = 100;    // Changes the value at the location pointed by ptr
cout << num;   // Now prints 100
```

### 2.4 Null Pointers

A **null pointer** is a pointer that doesn't point to any valid memory location. In modern C++, use `nullptr` (introduced in C++11) instead of `NULL` or `0`.

```cpp
int *ptr1 = nullptr;      // Modern C++ style - preferred
int *ptr2 = NULL;         // C-style (avoid)
int *ptr3 = 0;            // Literal zero (avoid)

if (ptr1 == nullptr) {
    cout << "Pointer is null" << endl;
}
```

**Why `nullptr`?** It has proper type safety and avoids ambiguous overload resolution.

### 2.5 Void Pointers

A `void*` is a generic pointer that can point to any data type. It cannot be dereferenced directly and requires type casting:

```cpp
void *genericPtr;
int num = 10;
double d = 3.14;

genericPtr = &num;
cout << "Integer value: " << *(static_cast<int*>(genericPtr)) << endl;

genericPtr = &d;
cout << "Double value: " << *(static_cast<double*>(genericPtr)) << endl;
```

**Use Cases**: Memory allocation functions (`malloc`, `calloc`), generic data handling, interoperability with C libraries.

### 2.6 Const with Pointers

C++ provides three ways to use `const` with pointers:

```cpp
int x = 10, y = 20;

// 1. Pointer to constant (can't modify value through this pointer)
const int *p1 = &x;    // or int const *p1 = &x;
// *p1 = 30;          // ERROR: Cannot modify value
p1 = &y;               // OK: Can change the address

// 2. Constant pointer (pointer itself is constant - must be initialized)
int *const p2 = &x;
*p2 = 30;              // OK: Can modify value
// p2 = &y;            // ERROR: Cannot change address

// 3. Constant pointer to constant (both are constant)
const int *const p3 = &x;
// *p3 = 40;          // ERROR: Cannot modify value
// p3 = &y;           // ERROR: Cannot change address
```

### 2.7 Pointer-to-Pointer (Double Pointer)

A pointer can point to another pointer, creating a chain of indirection:

```cpp
int num = 42;
int *ptr1 = &num;      // Single pointer
int **ptr2 = &ptr1;    // Double pointer (pointer to pointer)

cout << num << endl;           // 42
cout << *ptr1 << endl;         // 42
cout << **ptr2 << endl;        // 42
```

**Use Cases**: Dynamic 2D arrays, modifying pointer values inside functions, linked list heads.

### 2.8 Pointer Arithmetic

Pointers support limited arithmetic operations:

```cpp
int arr[] = {10, 20, 30, 40, 50};
int *ptr = arr;     // Points to arr[0]

ptr++;              // Now points to arr[1]
cout << *ptr;       // 20

ptr += 2;          // Now points to arr[3]
cout << *ptr;       // 40

// Subtraction gives number of elements between pointers
int *ptr2 = &arr[4];
cout << ptr2 - ptr; // 3 (elements between ptr2 and ptr)
```

**Key Rules**:
- `ptr + n` moves forward by `n * sizeof(type)` bytes
- `ptr - n` moves backward by `n * sizeof(type)` bytes
- Subtraction only valid between two pointers to same array

### 2.9 Dangling Pointers

A **dangling pointer** points to memory that has been freed or deallocated. This is a common source of undefined behavior:

```cpp
int *ptr = new int(42);
cout << *ptr << endl;    // 42

delete ptr;             // Memory freed
// ptr still holds the old address (now invalid)
// cout << *ptr << endl; // UNDEFINED BEHAVIOR!

// Solution: set pointer to nullptr after deletion
ptr = nullptr;
```

### 2.10 Dynamic Memory Allocation

C++ provides `new` and `delete` for heap memory management:

```cpp
// Single variable
int *ptr = new int(100);    // Allocates and initializes
cout << *ptr << endl;
delete ptr;                 // Deallocates memory
ptr = nullptr;              // Avoid dangling pointer

// Arrays
int *arr = new int[10];     // Dynamic array
delete[] arr;               // Note: use delete[] for arrays

// 2D Dynamic Array
int rows = 3, cols = 4;
int **matrix = new int*[rows];
for (int i = 0; i < rows; i++) {
    matrix[i] = new int[cols];
}
// Don't forget to free:
for (int i = 0; i < rows; i++) {
    delete[] matrix[i];
}
delete[] matrix;
```

**Memory Leak**: When allocated memory is never freed, causing gradual memory exhaustion.

---

## 3. References: The C++ Alias Mechanism

### 3.1 Reference Variables

A reference is an alias (alternative name) for an existing variable. It must be initialized at declaration and cannot be rebound:

```cpp
int num = 42;
int &ref = num;    // ref is now an alias for num

ref = 100;         // Modifies num
cout << num;       // Prints 100
cout << ref;       // Also prints 100
```

### 3.2 References vs Pointers

| Feature | References | Pointers |
|---------|-------------|----------|
| Initialization | Must be initialized when declared | Can be null |
| Reassignment | Cannot be rebound | Can be reassigned |
| Syntax | No dereference needed | Requires dereference |
| Null safety | Always valid | Can be null (danger) |
| Memory | Typically same address as variable | Separate storage |
| Operations | Limited (can be used in arithmetic) | Full arithmetic support |

### 3.3 References in Function Parameters

References are commonly used to modify arguments or avoid copying:

```cpp
// Pass by reference - allows modification
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Pass by const reference - efficiency + safety
void printString(const string &s) {
    cout << s << endl;
    // s cannot be modified
}

int main() {
    int x = 5, y = 10;
    swap(x, y);    // x=10, y=5
}
```

### 3.4 Const References

Const references are particularly useful for:
1. Passing large objects efficiently without copying
2. Protecting data from modification

```cpp
void process(const vector<int> &vec) {
    // Can read but not modify vec
    for (int x : vec) {
        cout << x << " ";
    }
}
```

### 3.5 R-Value References (C++11)

Modern C++ introduced r-value references for move semantics:

```cpp
int &&rref = 10;    // Can bind to r-values (temporaries)

string s1 = "Hello";
string s2 = std::move(s1);    // Move s1 into s2 (no copy)
```

---

## 4. Smart Pointers (Modern C++)

Smart pointers (C++11+) automatically manage memory, preventing leaks and dangling pointers.

### 4.1 unique_ptr

Exclusive ownership - only one pointer can own the resource:

```cpp
#include <memory>

std::unique_ptr<int> ptr1 = std::make_unique<int>(42);
// or: std::unique_ptr<int> ptr1(new int(42));

cout << *ptr1 << endl;    // 42

// Transfer ownership
std::unique_ptr<int> ptr2 = std::move(ptr1);
// ptr1 is now nullptr
// ptr2 owns the memory

// Automatic deletion when goes out of scope
```

### 4.2 shared_ptr

Shared ownership using reference counting:

```cpp
std::shared_ptr<int> ptr1 = std::make_shared<int>(42);
std::shared_ptr<int> ptr2 = ptr1;    // Reference count = 2

cout << ptr1.use_count() << endl;    // 2
cout << *ptr2 << endl;               // 42

// Automatically deleted when reference count reaches 0
```

### 4.3 weak_ptr

Non-owning reference to shared_ptr - solves circular references:

```cpp
std::shared_ptr<int> shared = std::make_shared<int>(42);
std::weak_ptr<int> weak = shared;

if (auto locked = weak.lock()) {
    cout << *locked << endl;    // 42
}
```

---

## 5. When to Use Pointers vs References

### 5.1 Use Pointers When:
- You need to reseat the pointer (point to different objects)
- You need pointer arithmetic
- Working with C-style APIs or legacy code
- Implementing data structures (linked lists, trees)
- You intentionally need null capability

### 5.2 Use References When:
- You need an alias for a variable
- Function parameter modification is needed (preferred over pointers for readability)
- Passing large objects without copying (use const reference)
- Returning multiple values from functions
- Operator overloading (e.g., operator[])

---

## 6. Concrete Examples

### Example 1: Implementing a Dynamic Stack

```cpp
#include <iostream>
using namespace std;

class Stack {
private:
    int *arr;
    int top;
    int capacity;

public:
    Stack(int size) {
        capacity = size;
        arr = new int[capacity];
        top = -1;
    }

    ~Stack() {
        delete[] arr;    // Prevent memory leak
    }

    void push(int value) {
        if (top >= capacity - 1) {
            cout << "Stack Overflow" << endl;
            return;
        }
        arr[++top] = value;
    }

    int pop() {
        if (top < 0) {
            cout << "Stack Underflow" << endl;
            return -1;
        }
        return arr[top--];
    }

    int peek() const {
        if (top < 0) return -1;
        return arr[top];
    }

    bool isEmpty() const {
        return top == -1;
    }
};

int main() {
    Stack s(5);
    s.push(10);
    s.push(20);
    s.push(30);
    
    cout << "Top element: " << s.peek() << endl;  // 30
    cout << "Popped: " << s.pop() << endl;        // 30
    cout << "Popped: " << s.pop() << endl;        // 20
    
    return 0;
}
```

### Example 2: Smart Pointer for Resource Management

```cpp
#include <iostream>
#include <memory>
using namespace std;

class Resource {
private:
    string name;
public:
    Resource(string n) : name(n) {
        cout << "Resource acquired: " << name << endl;
    }
    ~Resource() {
        cout << "Resource released: " << name << endl;
    }
    void use() {
        cout << "Using resource: " << name << endl;
    }
};

int main() {
    // Using unique_ptr - automatic cleanup
    {
        unique_ptr<Resource> res1 = make_unique<Resource>("Database");
        res1->use();
        
        // Transfer ownership
        unique_ptr<Resource> res2 = move(res1);
        // res1 is now nullptr
        res2->use();
    }  // res2 automatically deleted here

    // Using shared_ptr
    {
        shared_ptr<Resource> res1 = make_shared<Resource>("Network");
        {
            shared_ptr<Resource> res2 = res1;  // Reference count = 2
            cout << "Reference count: " << res1.use_count() << endl;
            res2->use();
        }  // res2 goes out of scope, count = 1
        cout << "Reference count: " << res1.use_count() << endl;
    }  // Last reference gone, resource deleted

    return 0;
}
```

**Output**:
```
Resource acquired: Database
Using resource: Database
Using resource: Database
Resource released: Database
Resource acquired: Network
Reference count: 2
Using resource: Network
Reference count: 1
Resource released: Network
```

---

## 7. Key Takeaways

1. **Pointers** store memory addresses; **references** are aliases to existing variables
2. Always initialize pointers; prefer `nullptr` over `NULL` or `0`
3. Use `const` correctly with pointers to prevent unintended modifications
4. Avoid dangling pointers by setting them to `nullptr` after `delete`
5. Prefer `const` references for passing large objects to functions
6. Smart pointers (`unique_ptr`, `shared_ptr`) should be used in modern C++ for automatic memory management
7. Void pointers (`void*`) provide generic addressing but require type casting
8. Pointer arithmetic works on array addresses; understand the relationship between pointers and arrays

---

## 8. Assessment Items

### Part A: Challenging Multiple Choice Questions

**Question 1**: Consider the following code:
```cpp
int arr[] = {5, 10, 15, 20, 25};
int *p = arr + 2;
cout << *p << " " << *(p - 1) << " " << *(p + 1);
```
What is the output?
- (a) 15 10 20
- (b) 15 10 25
- (c) 15 20 25
- (d) 10 15 20

**Question 2**: Which of the following statements about references is FALSE?
- (a) A reference must be initialized at declaration
- (b) A reference can be reseated to refer to a different variable
- (c) A reference cannot be null
- (d) sizeof(reference) == sizeof(original variable)

**Question 3**: What will be printed?
```cpp
int x = 10;
int *p = &x;
int **pp = &p;
***pp = 20;
cout << x;
```
- (a) 10
- (b) 20
- (c) Address of x
- (d) Compilation error

**Question 4**: Given:
```cpp
const int *p1;
int *const p2;
int const *p3;
```
Which pointer can be reassigned to point to a different integer variable?
- (a) p1 only
- (b) p2 only
- (c) p1 and p3 only
- (d) p1 and p2 only

**Question 5**: What is the output of this code?
```cpp
int x = 5;
int &ref = x;
int *ptr = &ref;
cout << *ptr;
```
- (a) 5
- (b) Address of x
- (c) Compilation error
- (d) Undefined behavior

**Question 6**: In a function, if you want to modify the caller's pointer itself (not the object it points to), you should:
- (a) Pass by value
- (b) Pass by reference
- (c) Pass by pointer
- (d) Pass by pointer-to-pointer

**Question 7**: What does `delete ptr` do when ptr is a dangling pointer?
- (a) Compiles but has undefined behavior
- (b) Sets ptr to nullptr
- (c) Throws an exception
- (d) Does nothing

**Question 8**: Which smart pointer provides exclusive ownership?
- (a) shared_ptr
- (b) weak_ptr
- (c) unique_ptr
- (d) auto_ptr (deprecated)

### Part B: Output Prediction Questions

**Question 9**: Predict the output:
```cpp
#include <iostream>
using namespace std;

void func(int *&p) {
    static int a = 10;
    p = &a;
}

int main() {
    int x = 5;
    int *ptr = &x;
    cout << *ptr << " ";
    func(ptr);
    cout << *ptr << " ";
    x = 15;
    cout << *ptr << " ";
    return 0;
}
```

**Question 10**: What will be the output?
```cpp
int a = 100;
int *p1 = &a;
int *p2 = p1;
int *p3 = &a;

cout << (p1 == p2) << " " << (p1 == p3) << " " << (*p1 == *p2);
```

### Part C: Debugging and Analysis Questions

**Question 11**: Find the memory leak in the following code and suggest the fix:
```cpp
void createArray() {
    int *arr = new int[10];
    for (int i = 0; i < 10; i++) {
        arr[i] = i * i;
    }
    // Function ends but memory is not freed
}
```

**Question 12**: The following code causes undefined behavior. Identify and fix:
```cpp
int* getPointer() {
    int val = 42;
    int *ptr = &val;
    return ptr;  // Returning pointer to local variable
}
```

**Question 13**: Analyze and explain why this code might produce unexpected results:
```cpp
int *ptr;
if (ptr != NULL) {
    cout << *ptr;  // But ptr was never assigned
}
```

**Question 14**: Convert the following pointer-based code to use smart pointers:
```cpp
class Node {
public:
    int data;
    Node* next;
    Node(int d) : data(d), next(nullptr) {}
};

void processList() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    // ... process list ...
    // How to ensure no memory leak?
}
```

### Part D: Conceptual Analysis

**Question 15**: Explain the difference between passing by value, passing by reference, and passing by pointer. Under what circumstances would you choose each method?

**Question 16**: Why is `const int *p` different from `int *const p`? Provide practical examples of when each would be used in a real-world C++ application.

---

### Answer Key

1. (a) 15 10 20
2. (b) A reference cannot be reseated
3. (b) 20 (triple dereference modifies x)
4. (c) p1 and p3 only (const int* means pointer to const int)
5. (a) 5 (reference can be used where the original variable is expected)
6. (d) Pass by pointer-to-pointer (int**)
7. (a) Undefined behavior
8. (c) unique_ptr
9. 5 10 10 (static variable persists)
10. 1 1 1 (all pointers point to same location)

---

*This study material is prepared in accordance with the BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, Delhi University.*