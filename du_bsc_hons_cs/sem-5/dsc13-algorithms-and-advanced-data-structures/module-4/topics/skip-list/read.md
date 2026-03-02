# Skip Lists: A Probabilistic Data Structure

## Introduction

In the realm of data structures, we constantly balance between efficiency and complexity. Arrays provide O(1) random access but suffer from O(n) insertions and deletions in the worst case. Linked lists excel at insertions and deletions with O(1) time but require O(n) traversal for searching. Binary Search Trees (BSTs) offer O(log n) average-case operations but can degrade to O(n) in the worst case without balancing mechanisms like AVL or Red-Black trees.

Enter **Skip Lists** — a brilliant probabilistic data structure invented by William Pugh in 1989 that provides O(log n) average-case performance for search, insertion, and deletion operations, while being significantly simpler to implement than balanced BSTs. Skip lists achieve this elegant balance through a layered architecture of linked lists, where higher layers act as "express lanes" for faster traversal.

In this topic, we will explore the skip list data structure, understanding its design, operations, and the probabilistic reasoning that makes it work. This is particularly relevant for DU students as it demonstrates how randomization can simplify algorithm design — a concept increasingly important in modern computing.

## Key Concepts

### Structure of a Skip List

A skip list is a hierarchical sequence of linked lists. The bottom layer (Level 0) is a regular sorted linked list containing all elements. Each higher layer acts as an "express lane" containing a subset of elements from the layer below. 

Consider looking for element 42 in a sorted list of 1 to 100:
- Without skip list: Traverse 42 nodes in worst case
- With skip list: Jump through express lanes, visiting only 7-8 nodes

Each node in a skip list contains:
1. **Key/Value**: The data being stored
2. **Forward array**: Pointers to next nodes at each level (typically denoted as `forward[i]` for level i)

The structure maintains these invariants:
- List[0] contains all elements in sorted order
- List[i] contains a subset of elements from List[i-1], selected probabilistically
- The highest level is typically log₂(n) for n elements

### Node Structure

```cpp
struct SkipListNode {
    int key;
    int value;
    SkipListNode** forward;  // Array of forward pointers
    
    SkipListNode(int key, int value, int level) {
        this->key = key;
        this->value = value;
        this->forward = new SkipListNode*[level + 1];
        for (int i = 0; i <= level; i++)
            forward[i] = nullptr;
    }
};
```

### Search Operation

The search algorithm works by moving horizontally at the highest level until we find an element greater than our search key, then drop down to the next level. This "电梯" (elevator) like movement allows us to skip large portions of the list.

**Algorithm Steps:**
1. Start at the highest level header
2. While the next node at current level has key ≤ search key:
   - Move forward horizontally
3. If next node's key > search key, move down one level
4. Repeat until we reach Level 0
5. Check if the node at Level 0 has the exact key

### Insertion Operation

The magic of skip lists lies in insertion, which uses randomization to determine node heights:

**Random Level Generation:**
```cpp
int randomLevel() {
    int level = 0;
    while (rand() % 2 == 0 && level < MAX_LEVEL)
        level++;
    return level;
}
```

This creates a geometric distribution where:
- P(level = 0) = 1/2
- P(level = 1) = 1/4
- P(level = 2) = 1/8
- And so on...

**Insertion Algorithm:**
1. Generate random level for new node
2. Find predecessors at each level (using search logic)
3. Create new node with the random level
4. Insert node by updating forward pointers at each level

### Deletion Operation

Deletion is the reverse of insertion:
1. Find the node to delete at all levels where it appears
2. Update forward pointers to bypass the node
3. Free the memory
4. If the node doesn't exist, report error

### Complexity Analysis

**Time Complexity (Average Case):**
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

**Time Complexity (Worst Case):**
- O(n) — occurs when randomization produces unfavorable levels

**Space Complexity:**
- Average: O(n)
- Each element uses approximately 1/(1-p) pointers on average, where p = 1/2 typically

### Why Randomization Works

The key insight is that with probability 1/2, an element appears at level i, and with probability 1/2 it doesn't. This creates an exponential decay in the number of elements at higher levels.

Expected number of elements at level i: n/2^i
Expected height of skip list: log₂(n)

This means:
- Level 0: ~n elements
- Level 1: ~n/2 elements
- Level 2: ~n/4 elements
- ...
- Level log n: ~1 element

## Examples

### Example 1: Searching in a Skip List

Consider building a skip list with elements {3, 6, 7, 9, 12, 19, 21, 25}:

```
Level 3:  HEAD ------------------> 21 ---------> NULL
Level 2:  HEAD --------> 9 -----> 21 ---------> NULL  
Level 1:  HEAD -> 3 -> 6 -> 9 -> 12 -> 19 -> 21 -> 25 -> NULL
Level 0:  HEAD -> 3 -> 6 -> 7 -> 9 -> 12 -> 19 -> 21 -> 25 -> NULL
```

**Search for 19:**
1. Start at Level 3: 21 > 19, move down
2. Level 2: 9 < 19, move to 9; next is 21 > 19, move down
3. Level 1: At 9, next is 12 < 19, move to 12; next is 19 = 19, found!

**Search for 8:**
1. Level 3: 21 > 8, move down
2. Level 2: 9 > 8, move down
3. Level 1: 6 < 8, move to 6; next is 9 > 8, move down
4. Level 0: 7 > 8, stop — not found

### Example 2: Insertion Step-by-Step

Insert 15 into the list above:

**Step 1:** Generate random level (say, level 2)

**Step 2:** Find predecessors at each level:
- Level 3: predecessor of 21 is HEAD
- Level 2: predecessor of 21 is 9
- Level 1: predecessor of 19 is 12
- Level 0: predecessor of 19 is 12

**Step 3:** Insert node:

```
Level 3:  HEAD ------------------> 21 ---------> NULL
Level 2:  HEAD --------> 9 -----> 15 -----> 21 ---------> NULL  
Level 1:  HEAD -> 3 -> 6 -> 9 -> 12 -> 15 -> 19 -> 21 -> 25 -> NULL
Level 0:  HEAD -> 3 -> 6 -> 7 -> 9 -> 12 -> 15 -> 19 -> 21 -> 25 -> NULL
```

### Example 3: Time Complexity Verification

For n = 1000 elements, expected:
- Height ≈ log₂(1000) ≈ 10 levels
- Search examines at most 2 × height = 20 nodes (constant factor)

For n = 1,000,000:
- Height ≈ log₂(1,000,000) ≈ 20 levels
- Search examines at most 40 nodes

This confirms O(log n) behavior — searching a million elements requires only ~40 node visits!

## Exam Tips

1. **Understand the Probabilistic Foundation**: Remember that skip lists use P = 1/2 for each level, giving geometric distribution. This is crucial for deriving expected height.

2. **Compare with Alternatives**: Be prepared to compare skip lists with AVL trees, Red-Black trees, and hash tables. Skip lists offer similar O(log n) performance with simpler implementation.

3. **Pointer Manipulation**: The core of skip list operations is updating forward arrays. Practice drawing diagrams with explicit pointer updates.

4. **Worst Case vs Average Case**: Know that worst-case is O(n) but extremely unlikely. The expected case is O(log n).

5. **Space-Time Tradeoff**: Higher memory usage (multiple pointers per node)换取 faster operations. This is a key design tradeoff.

6. **Random Level Generation**: Understand that `randomLevel()` creates the distribution where probability of level k is (1/2)^(k+1).

7. **Deletion Must Check Existence**: Always verify the element exists before deletion, as attempting to delete a non-existent node corrupts the structure.

8. **Practice Search Trace**: Be able to trace through search operations step-by-step for exam questions.