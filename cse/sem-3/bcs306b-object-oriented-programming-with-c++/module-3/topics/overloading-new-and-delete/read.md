# Overloading new and delete in C++

## Introduction

Memory management is a fundamental aspect of C++ programming that distinguishes it from many other programming languages. Unlike languages with automatic garbage collection, C++ provides programmers with direct control over memory allocation and deallocation through the `new` and `delete` operators. However, the default memory management mechanism provided by the compiler may not always meet the specific requirements of an application. This is where the powerful feature of overloading `new` and `delete` comes into play.

Overloading `new` and `delete` allows programmers to customize memory allocation behavior according to their specific needs. This capability is particularly valuable in scenarios requiring specialized memory pooling, debugging memory leaks, tracking memory usage, or implementing custom memory management strategies. In embedded systems and real-time applications, custom memory allocation can significantly improve performance by reducing fragmentation and providing deterministic allocation times.

Understanding how to overload these operators is essential for advanced C++ programming and is a topic that frequently appears in university examinations. This module explores the mechanisms behind operator overloading for memory allocation, the syntax involved, and practical applications where custom memory management provides significant advantages.

## Key Concepts

### Understanding new and delete Operators

In C++, the `new` operator performs two essential operations: first, it allocates memory from the heap, and second, it constructs an object in that memory. Conversely, the `delete` operator first destructs the object and then deallocates the memory. These operators can be overloaded globally or on a per-class basis, giving programmers fine-grained control over memory management.

The default implementations of `new` and `delete` use `malloc` and `free` respectively, but they provide additional functionality such as calling constructors and destructors automatically. When you overload these operators, you are replacing the memory allocation and deallocation functions while preserving the constructor/destructor calling mechanism.

### Syntax for Overloading new and delete

To overload the `new` operator for a class, you declare a static member function with the following signature:

```cpp
void* operator new(size_t size);
```

The `size` parameter is automatically passed by the compiler and represents the size of the object being allocated. The function must return a `void*` pointer to the allocated memory.

Similarly, to overload the `delete` operator:

```cpp
void operator delete(void* ptr);
```

The pointer passed to `delete` is the memory address that was previously returned by `operator new`.

### Overloading new[] and delete[]

When allocating arrays using `new[]` and `delete[]`, you need to overload the array versions of these operators:

```cpp
void* operator new[](size_t size);
void operator delete[](void* ptr);
```

The compiler automatically calls the appropriate version based on whether you use `new` or `new[]` in your code.

### Global Overloading vs Class-Specific Overloading

You can overload `new` and `delete` either globally or for a specific class. Global overloading affects all allocations in the program, while class-specific overloading affects only allocations for that particular class.

**Global Overloading Example:**

```cpp
void* operator new(size_t size) {
 cout << "Global new called, size: " << size << endl;
 return malloc(size);
}

void operator delete(void* ptr) {
 cout << "Global delete called" << endl;
 free(ptr);
}
```

**Class-Specific Overloading:**

```cpp
class MyClass {
public:
 int data;

 void* operator new(size_t size) {
 cout << "MyClass new called" << endl;
 return malloc(size);
 }

 void operator delete(void* ptr) {
 cout << "MyClass delete called" << endl;
 free(ptr);
 }
};
```

### Memory Pool Allocation

One of the most practical applications of overloading `new` and `delete` is implementing memory pools. A memory pool pre-allocates a large block of memory and then serves allocation requests from this pool. This approach reduces allocation overhead and fragmentation, which is particularly beneficial in real-time systems.

```cpp
class MemoryPool {
private:
 static const int POOL_SIZE = 1024;
 char pool[POOL_SIZE];
 bool allocated[POOL_SIZE];

public:
 MemoryPool() {
 memset(allocated, 0, sizeof(allocated));
 }

 void* allocate(size_t size) {
 for (int i = 0; i <= POOL_SIZE - size; i++) {
 bool canAllocate = true;
 for (int j = 0; j < size; j++) {
 if (allocated[i + j]) {
 canAllocate = false;
 break;
 }
 }
 if (canAllocate) {
 for (int j = 0; j < size; j++) {
 allocated[i + j] = true;
 }
 return &pool[i];
 }
 }
 return nullptr;
 }

 void deallocate(void* ptr, size_t size) {
 char* p = static_cast<char*>(ptr);
 int index = p - pool;
 for (size_t j = 0; j < size; j++) {
 allocated[index + j] = false;
 }
 }
};

class PooledObject {
public:
 int value;
 static MemoryPool pool;

 void* operator new(size_t size) {
 return pool.allocate(size);
 }

 void operator delete(void* ptr) {
 pool.deallocate(ptr, sizeof(PooledObject));
 }

 PooledObject(int v) : value(v) {}
};

MemoryPool PooledObject::pool;
```

### Memory Leak Detection

Overloading `new` and `delete` provides an excellent mechanism for detecting memory leaks during development. By tracking allocation and deallocation, you can identify objects that are never deleted:

```cpp
class MemoryTracker {
 static map<void*, size_t> allocations;
 static size_t totalAllocated;

public:
 static void* trackAlloc(size_t size) {
 void* ptr = malloc(size);
 allocations[ptr] = size;
 totalAllocated += size;
 cout << "Allocated " << size << " bytes at " << ptr << endl;
 return ptr;
 }

 static void trackDealloc(void* ptr) {
 if (allocations.find(ptr) != allocations.end()) {
 totalAllocated -= allocations[ptr];
 cout << "Freed memory at " << ptr << endl;
 allocations.erase(ptr);
 free(ptr);
 } else {
 cout << "Error: Trying to free unallocated memory at " << ptr << endl;
 }
 }

 static void printLeaks() {
 cout << "\nMemory Leaks Detected: " << endl;
 for (auto& pair : allocations) {
 cout << " " << pair.second << " bytes at " << pair.first << endl;
 }
 cout << "Total unfreed memory: " << totalAllocated << " bytes" << endl;
 }
};

map<void*, size_t> MemoryTracker::allocations;
size_t MemoryTracker::totalAllocated = 0;

void* operator new(size_t size) {
 return MemoryTracker::trackAlloc(size);
}

void operator delete(void* ptr) {
 MemoryTracker::trackDealloc(ptr);
}
```

### Passing Additional Arguments to new

You can also overload `new` to accept additional parameters. This is useful for custom initialization or placement allocation:

```cpp
class MyClass {
public:
 int data;
 int initValue;

 // Overload new with an additional parameter
 void* operator new(size_t size, int initVal) {
 void* ptr = malloc(size);
 static_cast<MyClass*>(ptr)->initValue = initVal;
 return ptr;
 }

 // Corresponding delete (optional but recommended)
 void operator delete(void* ptr, int initVal) {
 free(ptr);
 }

 void operator delete(void* ptr) {
 free(ptr);
 }

 MyClass() : data(0), initValue(0) {}
};

// Usage
MyClass* obj = new(42) MyClass(); // Passes 42 as initVal
```

## Examples

### Example 1: Simple Custom Memory Allocation

**Problem:** Create a class that tracks the number of objects allocated and freed using overloaded new and delete.

**Solution:**

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
 static int liveCount;
 static int totalCount;

public:
 int value;

 Counter(int v = 0) : value(v) {
 liveCount++;
 totalCount++;
 }

 ~Counter() {
 liveCount--;
 }

 void* operator new(size_t size) {
 cout << "Allocation request for " << size << " bytes" << endl;
 void* ptr = malloc(size);
 return ptr;
 }

 void operator delete(void* ptr) {
 cout << "Deallocation request" << endl;
 free(ptr);
 }

 static void displayStats() {
 cout << "Live objects: " << liveCount << endl;
 cout << "Total objects created: " << totalCount << endl;
 }
};

int Counter::liveCount = 0;
int Counter::totalCount = 0;

int main() {
 Counter* c1 = new Counter(10);
 Counter* c2 = new Counter(20);
 Counter* c3 = new Counter(30);

 Counter::displayStats();

 delete c2;

 Counter::displayStats();

 delete c1;
 delete c3;

 Counter::displayStats();

 return 0;
}
```

**Output:**

```
Allocation request for 4 bytes
Allocation request for 4 bytes
Allocation request for 4 bytes
Live objects: 3
Total objects created: 3
Deallocation request
Live objects: 2
Total objects created: 3
Deallocation request
Deallocation request
Live objects: 0
Total objects created: 3
```

### Example 2: Implementing a Simple Memory Pool

**Problem:** Implement a fixed-size memory pool for efficient memory allocation.

**Solution:**

```cpp
#include <iostream>
#include <cstring>
using namespace std;

const int BLOCK_SIZE = 64;
const int NUM_BLOCKS = 10;

class MemoryPool {
private:
 char pool[BLOCK_SIZE * NUM_BLOCKS];
 bool used[NUM_BLOCKS];

public:
 MemoryPool() {
 memset(used, 0, sizeof(used));
 }

 void* allocate() {
 for (int i = 0; i < NUM_BLOCKS; i++) {
 if (!used[i]) {
 used[i] = true;
 return &pool[i * BLOCK_SIZE];
 }
 }
 cout << "Pool exhausted!" << endl;
 return nullptr;
 }

 void deallocate(void* ptr) {
 if (ptr >= pool && ptr < pool + sizeof(pool)) {
 int index = (static_cast<char*>(ptr) - pool) / BLOCK_SIZE;
 if (index >= 0 && index < NUM_BLOCKS && used[index]) {
 used[index] = false;
 cout << "Block " << index << " returned to pool" << endl;
 }
 }
 }
};

class PooledData {
public:
 char data[BLOCK_SIZE];
 static MemoryPool pool;

 void* operator new(size_t size) {
 void* ptr = pool.allocate();
 if (!ptr) {
 throw bad_alloc();
 }
 return ptr;
 }

 void operator delete(void* ptr) {
 pool.deallocate(ptr);
 }

 PooledData() {
 memset(data, 0, BLOCK_SIZE);
 }
};

MemoryPool PooledData::pool;

int main() {
 cout << "Creating pooled objects..." << endl;

 PooledData* arr[5];
 for (int i = 0; i < 5; i++) {
 arr[i] = new PooledData();
 cout << "Object " << i << " allocated at: " << arr[i] << endl;
 }

 cout << "\nDeleting some objects..." << endl;
 delete arr[1];
 delete arr[3];

 cout << "\nAllocating more objects..." << endl;
 PooledData* newObj = new PooledData();
 cout << "New object at: " << newObj << endl;

 return 0;
}
```

### Example 3: Debugging Memory Allocation

**Problem:** Implement a debug version of new and delete that prints allocation information.

**Solution:**

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

class DebugMemory {
private:
 static map<void*, pair<size_t, string>> allocMap;
 static size_t currentUsage;
 static size_t peakUsage;

public:
 static void* allocate(size_t size, const char* file, int line) {
 void* ptr = malloc(size);
 allocMap[ptr] = make_pair(size, string(file) + ":" + to_string(line));
 currentUsage += size;
 if (currentUsage > peakUsage) {
 peakUsage = currentUsage;
 }
 cout << "ALLOC: " << size << " bytes at " << ptr
 << " (" << file << ":" << line << ")" << endl;
 return ptr;
 }

 static void deallocate(void* ptr) {
 if (allocMap.find(ptr) != allocMap.end()) {
 currentUsage -= allocMap[ptr].first;
 cout << "FREE: " << allocMap[ptr].first << " bytes at " << ptr << endl;
 allocMap.erase(ptr);
 free(ptr);
 } else {
 cout << "ERROR: Invalid free at " << ptr << endl;
 }
 }

 static void report() {
 cout << "\n=== Memory Report ===" << endl;
 cout << "Current usage: " << currentUsage << " bytes" << endl;
 cout << "Peak usage: " << peakUsage << " bytes" << endl;
 cout << "Leaked blocks: " << allocMap.size() << endl;
 for (auto& pair : allocMap) {
 cout << " " << pair.second.first << " bytes at "
 << pair.first << " (" << pair.second.second << ")" << endl;
 }
 }
};

map<void*, pair<size_t, string>> DebugMemory::allocMap;
size_t DebugMemory::currentUsage = 0;
size_t DebugMemory::peakUsage = 0;

// Overload global new and delete
void* operator new(size_t size) {
 return DebugMemory::allocate(size, "unknown", 0);
}

void operator delete(void* ptr) {
 DebugMemory::deallocate(ptr);
}

// Macro for tracking file and line information
#define new new(__FILE__, __LINE__)

class TestClass {
public:
 int arr[100];
 TestClass() { cout << "Constructor called" << endl; }
 ~TestClass() { cout << "Destructor called" << endl; }
};

int main() {
 TestClass* t1 = new TestClass();
 int* num = new int(42);

 DebugMemory::report();

 delete t1;
 // Intentionally not deleting num to demonstrate leak detection

 DebugMemory::report();

 return 0;
}
```

## Exam Tips

1. **Remember the function signature:** The overloaded `new` must return `void*` and take `size_t` as parameter. The `delete` must return `void` and take `void*` as parameter.

2. **Global vs Class-specific:** Understand when to use global overloading (affects all allocations) versus class-specific overloading (only affects that class). Class-specific is more common and safer.

3. **Constructor/Destructor calls:** When you overload `new` and `delete`, the compiler still automatically calls constructors and destructors. You only replace the memory allocation/deallocation part.

4. **Array versions:** Don't forget that `new[]` and `delete[]` require separate overloading if you want to handle array allocations specially.

5. **Placement new:** Understand placement new syntax `new(address) Type(args)` and how it relates to overloading the `new` operator with additional parameters.

6. **Always pair new with delete:** Memory allocated with `new` must be deallocated with `delete`, and `new[]` with `delete[]`. Mixing these leads to undefined behavior.

7. **Exception handling:** When overloading `new`, always throw `bad_alloc` if allocation fails rather than returning nullptr (unless you overload the nothrow version).

8. **Virtual destructors:** When using polymorphic classes with custom memory management, ensure destructors are virtual to ensure proper cleanup.
