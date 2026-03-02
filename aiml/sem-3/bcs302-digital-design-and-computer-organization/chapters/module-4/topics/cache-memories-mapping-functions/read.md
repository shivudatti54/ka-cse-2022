# **Cache Memories – Mapping Functions**

## **Introduction**

Cache memories are small, fast memories that store frequently accessed data in a computer system. They play a crucial role in improving the performance of modern computers by reducing the time it takes to access main memory. In this study material, we will focus on caching techniques, specifically mapping functions, which are used to map virtual addresses to physical addresses.

## **What is Mapping?**

Mapping is the process of allocating a unique identifier, called a tag, to a physical address. The tag is used to identify the location of data in the cache. Mapping functions are used to map virtual addresses to physical addresses.

## **Types of Mapping Functions**

There are two main types of mapping functions:

- **Direct Mapping**
- **Indirect Mapping**
- **Associative Mapping**

### Direct Mapping

In direct mapping, each virtual page is mapped to a single physical frame. The mapping function is simple and fast, but it can lead to poor performance if the cache is small or the memory is large.

**Example:**

Suppose we have 4 virtual pages (0-3) and 4 physical frames (0-3). We can map virtual page 0 to physical frame 0, virtual page 1 to physical frame 1, and so on.

| Virtual Page | Physical Frame |
| ------------ | -------------- |
| 0            | 0              |
| 1            | 1              |
| 2            | 2              |
| 3            | 3              |

### Indirect Mapping

In indirect mapping, each virtual page is mapped to a set of physical frames. The mapping function involves two steps: first, it calculates the index of the physical frame set, and then it calculates the offset within the frame set.

**Example:**

Suppose we have 4 virtual pages (0-3) and 2 physical frame sets (0-1). We can map virtual page 0 to physical frame set 0, index 0, and virtual page 1 to physical frame set 0, index 1.

| Virtual Page | Physical Frame Set | Index | Offset |
| ------------ | ------------------ | ----- | ------ |
| 0            | 0                  | 0     | 0      |
| 1            | 0                  | 0     | 1      |
| 2            | 1                  | 0     | 0      |
| 3            | 1                  | 0     | 1      |

### Associative Mapping

In associative mapping, each virtual page is mapped to a set of physical frames, and the mapping function involves a search to find the correct frame.

**Example:**

Suppose we have 4 virtual pages (0-3) and 4 physical frames (0-3). We can map virtual page 0 to physical frame 0, and virtual page 1 to physical frame 1.

| Virtual Page | Physical Frame |
| ------------ | -------------- |
| 0            | 0              |
| 1            | 1              |
| 2            | 2              |
| 3            | 3              |

**Key Concepts:**

- **Cache hierarchy**: A cache hierarchy consists of multiple levels of caches, each of which is smaller than the previous one.
- **Cache line size**: The size of a cache line, which is the minimum size of data that can be stored in a cache.
- **Cache tag**: The tag or identifier that is associated with a physical address.

## **Advantages and Disadvantages:**

Advantages:

- **Improved performance**: Mapping functions can improve the performance of a computer system by reducing the time it takes to access main memory.
- **Increased capacity**: Mapping functions can increase the capacity of a cache by allowing multiple virtual pages to be mapped to a single physical frame.

Disadvantages:

- **Increased complexity**: Mapping functions can increase the complexity of a cache by requiring more memory and computational resources.
- **Potential for cache thrashing**: Mapping functions can lead to cache thrashing, which occurs when the cache is filled with data that is not being accessed frequently.

## **Conclusion:**

Cache memories and mapping functions are essential components of modern computer systems. Understanding the different types of mapping functions, including direct mapping, indirect mapping, and associative mapping, is crucial for designing and optimizing cache systems. By understanding the advantages and disadvantages of mapping functions, designers and engineers can create more efficient and effective cache systems that improve the performance of computer systems.
