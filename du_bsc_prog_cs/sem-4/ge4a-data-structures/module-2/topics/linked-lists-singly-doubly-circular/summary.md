# Linked Lists – Singly, Doubly & Circular  
*For BSc Physical Science (CS) – Delhi University, NEP 2024 – Quick Revision*

---

## Introduction
Linked lists are fundamental dynamic data structures that store elements in nodes, each node containing data and a reference (or pointer) to the next/previous node. Unlike arrays, they allow O(1) insertions/deletions at any position and grow/shrink without pre‑allocating memory. The Delhi University syllabus (NEP 2024) covers three primary variants: **Singly Linked List (SLL)**, **Doubly Linked List (DLL)** and **Circular Linked List (CLL)**.

---

## 1. Singly Linked List (SLL)
- **Node structure:** `data` + `next` pointer.  
- **Representation:** Head pointer (first node); `NULL` marks end of list.  
- **Basic operations (all O(1) for head):**  
  - Insertion: at beginning, at end, after a given node.  
  - Deletion: from beginning, by value, by position.  
  - Traversal: iterative walk using `while (ptr != NULL)`.  
- **Advantages:** Simple, memory‑efficient (only one pointer per node).  
- **Limitations:** No backward traversal; must traverse from head for deletions at arbitrary positions.

---

## 2. Doubly Linked List (DLL)
- **Node structure:** `data` + `prev` + `next` pointers.  
- **Representation:** Head and optional Tail pointers; both ends accessible.  
- **Basic operations:**  
  - Insertion/Deletion at head, tail, or any position (requires updating two pointers).  
  - Traversal: forward (`next`) or backward (`prev`).  
- **Advantages:** Bidirectional navigation, easier deletion of previous node.  
- **Disadvantage:** Extra memory for the `prev` pointer.

---

## 3. Circular Linked List
- **Types:**  
  - **Circular Singly:** Last node’s `next` points to head.  
  - **Circular Doubly:** Tail’s `next` → head, head’s `prev` → tail (forms a ring).  
- **Key特性:** No `NULL` at end; traversal must stop after visiting each node once (detect by returning to head).  
- **Operations:** Same as linear lists, but careful handling of the circular nature (e.g., insert after last node points to head).  
- **Applications:** Round‑robin scheduling, buffering, continuous loops.

---

## 4. Common Operations & Complexity (Syllabus Highlights)
| Operation | SLL | DLL | Circular SLL | Circular DLL |
|-----------|-----|-----|--------------|--------------|
| Insert at head | O(1) | O(1) | O(1) | O(1) |
| Insert at tail | O(n) | O(1)* (with tail) | O(1) (if tail known) | O(1) |
| Delete by value | O(n) | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) | O(n) |
| Memory per node | 1 pointer | 2 pointers | 1 pointer | 2 pointers |

*\*DLL with tail pointer.*

---

## 5. Comparison with Arrays
- **Dynamic size** vs. fixed size of arrays.  
- **No waste** of memory; nodes allocated on demand.  
- **No random access** – must traverse to reach index *i*.  
- **Cache‑unfriendly** due to non‑contiguous storage.

---

## Conclusion
Linked lists—singly, doubly, and circular—provide flexible, memory‑efficient ways to manage ordered data that changes frequently. Understanding their node structures, operation complexities, and the subtle differences between variants is essential for the Delhi University Data Structures exam. Master the pointer manipulations, remember the O(1) insertion/deletion benefits, and be ready to contrast them with array‑based storage.  

*Revise: node definition → pointer updates → edge cases (empty list, single node, circular wrap‑around).*