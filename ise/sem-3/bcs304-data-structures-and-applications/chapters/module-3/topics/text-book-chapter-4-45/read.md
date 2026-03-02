# **Chapter 4: Data Structures and Applications**

## **4.5: Hash Tables**

### Definition

A hash table is a data structure that stores key-value pairs in an array using a hash function to map keys to indices of the array. The hash function takes the key as input and generates a hash value, which is used to index the array.

### Components of a Hash Table

- **Key**: The unique identifier for each element in the hash table.
- **Value**: The data associated with each key.
- **Hash Table**: The array that stores the key-value pairs.
- **Hash Function**: The function that maps keys to indices of the array.

### Operations on Hash Tables

- **Insert**: Adds a new key-value pair to the hash table.
- **Search**: Retrieves the value associated with a given key.
- **Delete**: Removes a key-value pair from the hash table.

### Advantages of Hash Tables

- **Efficient Search**: Hash tables allow for fast search operations with an average time complexity of O(1).
- **Efficient Insertion and Deletion**: Hash tables can insert and delete elements efficiently with an average time complexity of O(1).
- **Good Cache Performance**: Hash tables exhibit good cache performance, leading to faster access times.

### Disadvantages of Hash Tables

- **Collision Resolution**: Hash tables can suffer from collisions, where two keys hash to the same index. Resolving these collisions can be costly.
- **Space Complexity**: Hash tables require additional space to store the hash function and collision resolution data structures.

### Types of Hash Functions

- **Separate Chaining**: A combination of open addressing and chaining to resolve collisions.
- **Open Addressing**: A technique that uses multiple probes to find an empty slot in the hash table.

### Example Implementation in Python

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Example usage:
hash_table = HashTable(10)
hash_table.insert('apple', 5)
hash_table.insert('banana', 7)
print(hash_table.search('apple'))  # Output: 5
hash_table.delete('banana')
print(hash_table.search('banana'))  # Output: None
```

### Key Concepts

- **Hash Function**: A function that maps keys to indices of the array.
- **Collision Resolution**: Techniques used to resolve collisions in hash tables.
- **Open Addressing**: A technique that uses multiple probes to find an empty slot in the hash table.
- **Separate Chaining**: A combination of open addressing and chaining to resolve collisions.
