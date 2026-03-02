## Revision Notes: Chapter 5.1-5.3

### 5.1 Sorted Sets

- **Definition:** A sorted set is a data structure that stores elements in a sorted order.
- **Operations:**
  - Insert: O(log n)
  - Delete: O(log n)
  - Search: O(log n)
- **Applications:** Database indexing, priority queues
- **Important Properties:**
  - Each element is unique
  - Elements are sorted
  - Insertion and deletion do not disturb the sorted order

### 5.2 Tries

- **Definition:** A trie (also known as a prefix tree) is a tree-like data structure that is used to store a collection of strings.
- **Operations:**
  - Insert: O(m), where m is the length of the string
  - Delete: O(m), where m is the length of the string
  - Search: O(m), where m is the length of the string
- **Applications:** Autocomplete, spell checking
- **Important Properties:**
  - All strings that are prefixes of each other are stored in the same node

### 5.3 Suffix Trees

- **Definition:** A suffix tree is a tree-like data structure that presents all the suffixes of a given string in a way that allows for efficient retrieval of all the suffixes that contain a given substring.
- **Operations:**
  - Build: O(n)
  - Search: O(m), where m is the length of the substring
- **Applications:** Pattern searching, data compression
- **Important Properties:**
  - Each internal node represents a common prefix of all its children
  - The root node represents the empty string
