# Collision Resolution Schemes

## Introduction

When using hash tables, **collision** occurs when two or more keys map to the same hash value. Since perfect hashing is rarely achievable, collision resolution becomes essential for efficient hash table operations. The Delhi University syllabus covers two primary approaches: **Open Addressing** and **Separate Chaining**.

---

## 1. Need for Collision Resolution

- Hash functions distribute keys but cannot guarantee unique mapping
- Load factor (α = n/m) determines collision probability
- Higher α → more collisions → degraded performance

---

## 2. Open Addressing (Closed Hashing)

All elements stored **within the hash table** itself.

### 2.1 Linear Probing
- **Formula**: h(k, i) = (h'(k) + i) mod m, where i = 0, 1, 2, ...
- **Advantage**: Simple to implement
- **Disadvantage**: Suffers from **primary clustering**

### 2.2 Quadratic Probing
- **Formula**: h(k, i) = (h'(k) + c₁i + c₂i²) mod m
- **Advantage**: Reduces primary clustering
- **Disadvantage**: May miss empty slots (secondary clustering)

### 2.3 Double Hashing
- **Formula**: h(k, i) = (h₁(k) + i × h₂(k)) mod m
- **h₂(k)** must be non-zero and relatively prime to table size m
- **Advantage**: Best distribution; eliminates both clustering problems

> **Search Complexity**: O(1/(1-α)) for successful search

---

## 3. Separate Chaining (Open Hashing)

- Each table slot contains a **linked list** of all keys mapping to that index
- New elements added to the front (or rear) of the list
- Table can hold more elements than size m (α can exceed 1)

> **Search Complexity**: O(1 + α) average case

**Advantages**:
- Simple to implement
- Handles overflow without rehashing
- Deletion is straightforward

**Disadvantages**:
- Extra memory for pointers
- Cache performance poor due to pointer chasing

---

## 4. Performance Comparison

| Method | Insert | Search (Avg) | Delete | Clustering Issue |
|--------|--------|--------------|--------|------------------|
| Linear Probing | O(1) | O(1/(1-α)) | Difficult | Primary |
| Quadratic Probing | O(1) | O(1/(1-α)) | Difficult | Secondary |
| Double Hashing | O(1) | O(1/(1-α)) | Difficult | None |
| Separate Chaining | O(1) | O(1+α) | Easy | None |

---

## 5. Rehashing

When load factor exceeds threshold (typically 0.7), create a **new larger table** and re-insert all elements using a new hash function.

- **Purpose**: Maintain performance by keeping α low
- **New size**: Usually double the previous size (prime number preferred)

---

## Conclusion

Collision resolution is fundamental to hash table efficiency. **Open Addressing** suits low load factors and memory-constrained environments, while **Separate Chaining** is preferred for general use due to simplicity and flexibility. For exam preparation, remember the formulas for probing sequences and analyze time complexity in terms of load factor α.

---

*Based on Delhi University BSc (Hons) CS NEP 2024 UGCF Syllabus — Unit: Hashing & Hash Tables*