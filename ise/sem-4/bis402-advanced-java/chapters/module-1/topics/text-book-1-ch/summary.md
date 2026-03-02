## Revision Notes: Text Book 1: Ch (Advanced Java)

### Overview

- **Collections Framework**: A high-level view of the Java Collections Framework (JCF)
- **Key Interfaces and Classes**: Overview of the main interfaces and classes in the JCF

### Collection Interfaces

- **List Interface**: Defines a list of elements
  - Methods:
    - `add(E element)`: Adds an element to the list
    - `remove(E element)`: Removes an element from the list
    - `contains(E element)`: Checks if the list contains an element
  - **Important**: `List` is a generic interface
- **Set Interface**: Defines a set of unique elements
  - Methods:
    - `add(E element)`: Adds an element to the set
    - `remove(E element)`: Removes an element from the set
    - `contains(E element)`: Checks if the set contains an element
  - **Important**: `Set` is a generic interface
- **Map Interface**: Defines a mapping of keys to values
  - Methods:
    - `put(K key, V value)`: Adds a key-value pair to the map
    - `get(K key)`: Retrieves the value associated with a key
    - `remove(K key)`: Removes a key-value pair from the map
  - **Important**: `Map` is a generic interface

### Collection Classes

- **ArrayList**: A resizable array-based implementation of the List interface
  - Methods:
    - `add(E element)`: Adds an element to the list
    - `remove(E element)`: Removes an element from the list
    - `get(int index)`: Retrieves an element at a specified index
- **LinkedList**: A doubly-linked list implementation of the List interface
  - Methods:
    - `add(E element)`: Adds an element to the list
    - `remove(E element)`: Removes an element from the list
    - `get(int index)`: Retrieves an element at a specified index
- **HashSet**: A hash table implementation of the Set interface
  - Methods:
    - `add(E element)`: Adds an element to the set
    - `remove(E element)`: Removes an element from the set
    - `contains(E element)`: Checks if the set contains an element
- **HashMap**: A hash table implementation of the Map interface
  - Methods:
    - `put(K key, V value)`: Adds a key-value pair to the map
    - `get(K key)`: Retrieves the value associated with a key
    - `remove(K key)`: Removes a key-value pair from the map

### Key Formulas and Definitions

- **Hash Function**: A function that maps keys to indices in a hash table
- **Collision Resolution**: A mechanism for resolving conflicts when two keys hash to the same index
- **Hash Table**: A data structure that maps keys to values using a hash function

### Important Theorems

- **Pigeonhole Principle**: If `n` items are put into `m` containers, with `n > m`, then at least one container must contain more than one item
- **Caching**: A technique for improving performance by storing frequently accessed data in a fast, easily accessible location
