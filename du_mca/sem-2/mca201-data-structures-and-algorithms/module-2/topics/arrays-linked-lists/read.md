# Arrays & Linked Lists

## Introduction
Arrays and linked lists form the foundational building blocks of linear data structures in computer science. Arrays provide O(1) random access through contiguous memory allocation but suffer from fixed size limitations. Linked lists use dynamic memory allocation through nodes and pointers, enabling efficient insertions/deletions at the cost of sequential access. 

In industry applications, arrays excel in matrix operations (NumPy), database indexing, and cache-friendly implementations. Linked lists power browser histories, music playlists, and memory management systems. Understanding their time-space tradeoffs is critical for system design - for instance, Python lists are actually dynamic arrays, while blockchain implementations often use linked structures.

## Key Concepts
1. **Array Types**
   - Static: Fixed size (C/C++ arrays)
   - Dynamic: Resizable (Java ArrayList, C++ vector)
   - Memory layout: Contiguous block with calculated offsets (base_address + index * size)

2. **Linked List Variants**
   - Singly: Node {data, next}
   - Doubly: Node {prev, data, next}
   - Circular: Last node points to head
   - Header nodes: Simplify edge cases

3. **Complexity Analysis**
   - Array insertion: O(n) worst-case (shifting)
   - Linked list insertion: O(1) at head/tail (with tail pointer)
   - Cache performance: Arrays benefit from spatial locality

4. **Hybrid Structures**
   - Unrolled linked lists (array blocks + linked structure)
   - XOR linked lists (memory optimization)

## Examples

**1. Dynamic Array Resizing**
```python
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)
    
    def _resize(self, new_cap):
        new_arr = self._make_array(new_cap)
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_cap

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1
```
*Complexity: Amortized O(1) for append operations*

**2. Linked List Reversal (Iterative)**
```java
public Node reverseList(Node head) {
    Node prev = null;
    Node current = head;
    while (current != null) {
        Node next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
```
*Space: O(1), Time: O(n)*

**3. Merge Two Sorted Linked Lists**
```python
def merge_lists(l1, l2):
    dummy = Node(-1)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next
```
*Complexity: O(m+n) time, O(1) space*

## Exam Tips
1. Always specify array vs linked list when asked about "best data structure"
2. For algorithm questions, first clarify edge cases (empty list, single element)
3. When drawing linked lists, clearly distinguish null pointers
4. Remember: Array access is O(1) but insertion/deletion at beginning is O(n)
5. For circular linked lists, check termination condition to avoid infinite loops
6. In doubly linked lists, always update both next and prev pointers
7. When comparing structures, discuss both time complexity and memory layout