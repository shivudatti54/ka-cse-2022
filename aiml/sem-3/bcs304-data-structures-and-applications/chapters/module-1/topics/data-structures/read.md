# Data Structures

## Introduction

Data structures are the fundamental building blocks of computer science and software engineering. In simple terms, a data structure is a specialized way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently. The choice of an appropriate data structure can dramatically impact the performance of algorithms and the overall efficiency of software applications.

The study of data structures is crucial for every computer science student because it forms the backbone of all computational processes. When you write a program to solve a real-world problem, you must deal with data—collecting it, storing it, processing it, and retrieving results. How you organize this data determines how quickly your program runs and how effectively it utilizes computer memory. For instance, searching for a phone number in an unordered list takes significantly more time than searching in a well-organized directory. This difference in efficiency is precisely what makes data structures essential knowledge.

In the context of the University of Delhi's Computer Science curriculum, this topic serves as the foundation for understanding more advanced concepts like algorithms, database management systems, operating systems, and software engineering. The eight hours allocated to this module provide sufficient time to grasp both theoretical concepts and practical implementations, preparing students for internal assessments and end-semester examinations.

## Key Concepts

### Definition and Importance

A data structure is a particular way of arranging data in a computer's memory so that it can be used effectively. Data structures are not just about storing data; they are about organizing data in a manner that enables efficient operations such as insertion, deletion, searching, and sorting. The relationship between data elements and the operations that can be performed on them defines the data structure.

The importance of data structures stems from their direct impact on algorithm efficiency. According to classical computer science theory, the choice of data structure can reduce algorithmic complexity from O(n²) to O(n log n) or even O(1), depending on the operation. This efficiency gain becomes critical when dealing with large datasets, which are common in modern applications like social media platforms, e-commerce websites, and scientific computations.

### Classification of Data Structures

Data structures are broadly classified into two categories: primitive and non-primitive data structures.

Primitive data structures are the basic data types provided by programming languages. These include integers, floating-point numbers, characters, and boolean values. Primitive data structures are called "primitive" because they are the fundamental building blocks from which more complex data structures are constructed. In C language, for example, int, float, char, and double are primitive data types.

Non-primitive data structures are derived from primitive data types and are used to organize multiple data items. These are further classified into linear and non-linear data structures. Linear data structures organize data elements in a sequential manner, where each element is connected to its previous and next element. Examples include arrays, linked lists, stacks, and queues. Non-linear data structures, on the other hand, organize data in a hierarchical manner with connections between elements that are not sequential. Trees and graphs are classic examples of non-linear data structures.

### Data Structure Operations

Regardless of the specific type, most data structures support a common set of operations. Understanding these operations is essential for analyzing and comparing different data structures.

The primary operations performed on data structures include:

Traversing involves accessing and processing each element in the data structure exactly once. For example, printing all elements of an array requires traversing the array from the first element to the last.

Searching refers to locating a specific element within the data structure. Searching can be performed using various algorithms, and the efficiency depends heavily on how the data is organized.

Insertion is the process of adding a new element to the data structure. The implementation of insertion varies depending on whether the data structure has any ordering requirements or constraints on capacity.

Deletion involves removing an existing element from the data structure. Care must be taken to maintain the integrity of the remaining data after deletion.

Sorting arranges the elements in a specific order, either ascending or descending. Sorting is one of the most common operations in computer science and has numerous algorithms with different time complexities.

Merging combines elements from two different data structures into a single organized structure. This operation is particularly useful in file processing and database operations.

### Pointers and Dynamic Memory Allocation

Pointers are variables that store the memory address of another variable. In the context of data structures, pointers play a crucial role in creating dynamic data structures like linked lists, trees, and graphs. A pointer variable occupies fixed memory (typically 4 bytes on a 32-bit system or 8 bytes on a 64-bit system) but can reference data of any size.

Dynamic memory allocation is the process of allocating memory at runtime rather than compile time. In C, functions like malloc(), calloc(), and realloc() are used for dynamic memory allocation, while free() is used to deallocate previously allocated memory. Dynamic allocation is essential for creating data structures whose size is not known at compile time or that need to grow and shrink during program execution.

The relationship between pointers and dynamic memory allocation is fundamental. When you allocate memory dynamically, the system returns a pointer to the beginning of the allocated memory block. This pointer then serves as the reference point for accessing the allocated data.

## Examples

### Example 1: Analyzing Time Complexity of Array Operations

Consider an array of n integers. Analyze the time complexity of the following operations:

(a) Accessing the element at index i
(b) Searching for a value in an unsorted array
(c) Inserting an element at the beginning of the array

Solution:

(a) Accessing element at index i: O(1) - Arrays provide direct access to elements through indexing. The element at index i can be accessed using the formula base_address + (i × size_of_element). This is a constant-time operation regardless of the array size.

(b) Searching in unsorted array: O(n) - In the worst case, we may need to check every element in the array to determine whether the target value exists. If the element is found at the last position or does not exist at all, we perform n comparisons.

(c) Inserting at the beginning: O(n) - To insert an element at the beginning, we must shift all existing elements one position to the right to create space at index 0. This requires n element movements in the worst case, making it a linear-time operation.

### Example 2: Memory Layout Analysis

If we have an integer array of size 5 in C, and the integer requires 4 bytes, calculate the total memory required assuming the array starts at memory address 1000. Also, explain what happens if we use dynamic allocation.

Solution:

Memory required of elements × size of each element
 = number= 5 × 4 bytes = 20 bytes

The memory layout would be:
- Element at index 0: address 1000-1003
- Element at index 1: address 1004-1007
- Element at index 2: address 1008-1011
- Element at index 3: address 1012-1015
- Element at index 4: address 1016-1019

With dynamic allocation using malloc(5 × sizeof(int)), the system allocates exactly 20 bytes (or possibly slightly more for bookkeeping) on the heap and returns a pointer to the first byte. The advantage is that this memory can be freed when no longer needed, and the array size can be modified using realloc().

### Example 3: Practical Application Scenario

A university needs to maintain student records for quick lookup by student ID. The student database grows by approximately 1000 records per year, and lookups must be performed frequently throughout the day. Which data structure considerations are important?

Solution:

Several factors need consideration:

First, since lookups are frequent, we need a data structure that supports fast searching. If student IDs are numeric and within a specific range, array-based indexed access provides O(1) lookup. If IDs are arbitrary, a hash table or balanced tree would be more appropriate.

Second, since the database grows over time, dynamic memory allocation becomes essential. We cannot use fixed-size arrays without knowing the maximum capacity in advance.

Third, if insertions and deletions are also frequent alongside searches, we must consider the overhead of each operation. A simple array would be efficient for search but inefficient for frequent insertions and deletions in the middle.

Fourth, if the data must be maintained in sorted order for range queries (like finding all students in a particular ID range), a balanced tree structure might be ideal despite slightly slower individual lookups compared to arrays.

This example illustrates that the "best" data structure depends entirely on the specific requirements of the application, including the types of operations performed, the size of data, and performance constraints.

## Exam Tips

For the University of Delhi examinations, students should focus on the following key areas:

One, understand the fundamental difference between primitive and non-primitive data structures. This classification is frequently tested in objective-type questions and forms the basis for understanding more complex topics.

Two, be able to identify the time and space complexity of basic operations on different data structures. Questions asking for the Big-O notation of operations like insertion, deletion, and search are common in examinations.

Three, clearly understand how pointers work, especially in the context of dynamic memory allocation. Students should be able to trace pointer operations and understand memory layout diagrams.

Four, practice drawing memory representations of arrays and linked structures. Questions involving memory addresses and data storage patterns appear frequently in practical examinations.

Five, understand the concept of abstract data types (ADTs). An ADT defines the data and the operations but hides the implementation details. Knowing how to specify an ADT and implement it using various data structures is important.

Six, be familiar with the trade-offs between different data structures. For example, arrays provide fast access but slow insertion/deletion, while linked lists provide fast insertion/deletion but slow access.

Seven, pay attention to the terminology used in the module. Terms like "homogeneous data structures" (arrays), "heterogeneous data structures" (structures), "static" versus "dynamic" data structures are important distinctions that appear in examinations.

Eight, practice solving numerical problems involving memory calculations and address computations. These are scoring questions if done carefully.