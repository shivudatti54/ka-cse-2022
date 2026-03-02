# Introduction to Arrays

## What is an Array?

An **array** is a fundamental data structure that stores a collection of elements of the same data type in **contiguous memory locations**. Each element can be accessed directly using its **index** (position number).

Think of an array like a row of numbered lockers - each locker (element) has a unique number (index), and you can directly go to any locker without checking others.

## Key Characteristics

| Property              | Description                                      |
| --------------------- | ------------------------------------------------ |
| **Fixed Size**        | Size is determined at creation and cannot change |
| **Homogeneous**       | All elements must be of the same data type       |
| **Contiguous Memory** | Elements stored in adjacent memory locations     |
| **Random Access**     | Any element accessible in O(1) time using index  |
| **Zero-indexed**      | First element is at index 0 (in most languages)  |

## Memory Representation

When you declare an array of size `n`, the system allocates `n × size_of_element` bytes of contiguous memory.

```
Array: [10, 20, 30, 40, 50]
Index: 0 1 2 3 4

Memory Layout (assuming 4 bytes per integer):
┌──────┬──────┬──────┬──────┬──────┐
│ 10 │ 20 │ 30 │ 40 │ 50 │
└──────┴──────┴──────┴──────┴──────┘
1000 1004 1008 1012 1016 (addresses)
```

### Address Calculation Formula

To find the address of element at index `i`:

```
Address(arr[i]) = Base_Address + (i × Size_of_Element)
```

**Example:** If base address = 1000, element size = 4 bytes

- arr[0] = 1000 + (0 × 4) = 1000
- arr[3] = 1000 + (3 × 4) = 1012

## Time Complexity of Array Operations

| Operation               | Time Complexity | Explanation              |
| ----------------------- | --------------- | ------------------------ |
| **Access**              | O(1)            | Direct index calculation |
| **Search (unsorted)**   | O(n)            | Must check each element  |
| **Search (sorted)**     | O(log n)        | Binary search possible   |
| **Insert at end**       | O(1)            | If space available       |
| **Insert at beginning** | O(n)            | Shift all elements right |
| **Delete at end**       | O(1)            | Simply reduce size       |
| **Delete at beginning** | O(n)            | Shift all elements left  |

## Advantages of Arrays

1. **Fast Access** - O(1) random access using index
2. **Memory Efficient** - No extra memory for pointers
3. **Cache Friendly** - Contiguous memory improves cache performance
4. **Easy Traversal** - Simple iteration using loops

## Disadvantages of Arrays

1. **Fixed Size** - Cannot grow or shrink dynamically
2. **Costly Insertion/Deletion** - O(n) for middle operations
3. **Memory Waste** - Unused allocated space is wasted
4. **Single Data Type** - Cannot mix different types

## Real-World Analogies

1. **Parking Lot** - Each parking spot has a number (index), cars (elements) park in spots
2. **Bookshelf** - Books arranged in order, find by position number
3. **Piano Keys** - Each key has a position, press any key directly

## Summary

- Arrays store **homogeneous elements** in **contiguous memory**
- **O(1) access** using index - fastest for retrieval
- **O(n) insertion/deletion** - costly for dynamic operations
- Address formula: `Base + (Index × Element_Size)`
