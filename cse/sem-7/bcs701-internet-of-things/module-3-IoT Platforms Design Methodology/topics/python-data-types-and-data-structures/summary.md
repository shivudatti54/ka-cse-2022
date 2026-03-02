# Python Data Types and Data Structures - Summary

## Key Definitions

- **Primitive Data Types**: Fundamental data types including integers (int), floating-point numbers (float), strings (str), and boolean values (bool) that represent basic values in Python.

- **Data Structures**: Composite types that organize collections of data—list (mutable, ordered), tuple (immutable, ordered), dict (mutable, key-value pairs), and set (mutable, unique elements).

- **Mutability**: The property determining whether an object can be modified after creation. Mutable: list, dict, set, bytearray. Immutable: int, float, str, tuple, bool.

- **Circular Buffer (Ring Buffer)**: A fixed-size buffer that overwrites oldest data when full, implemented efficiently using collections.deque in Python.

- **JSON (JavaScript Object Notation)**: Lightweight data interchange format widely used in IoT for human-readable data transmission between devices and servers.

## Important Formulas

- **Memory Size of Integer**: `sys.getsizeof(integer)` returns approximately 28 bytes minimum in CPython
- **List Indexing**: O(1) time complexity for accessing elements by index
- **Dictionary Lookup**: O(1) average-case time complexity for key lookups
- **Set Membership**: O(1) average-case time complexity for checking element existence
- **Struct Format**: `struct.pack(format, values)` and `struct.unpack(format, buffer)` for binary data handling

## Key Points

1. Python's primitive types (int, float, str, bool) form the foundation for all IoT data handling, from sensor readings to device identifiers.

2. Lists provide O(1) indexed access with O(n) insertion/deletion, making them suitable for sensor data arrays requiring frequent read operations.

3. Tuples' immutability enables their use as dictionary keys and ensures data integrity for fixed configuration parameters in IoT devices.

4. Dictionaries provide O(1) lookup performance, ideal for device metadata storage and JSON parsing results in IoT applications.

5. Sets offer O(1) membership testing, essential for tracking unique device identifiers and detecting duplicate sensor readings efficiently.

6. The struct module enables efficient binary protocol parsing critical for low-level IoT device communication.

7. collections.deque with maxlen parameter provides efficient circular buffer implementation for streaming sensor data.

8. JSON remains the standard data interchange format in IoT due to its human-readable nature and widespread platform support.

## Common Mistakes

1. **Confusing list and tuple mutability**: Using lists where immutability is required, or attempting to modify tuples (which raises TypeError).

2. **Using lists for membership testing**: Employing linear search O(n) in lists when sets provide O(1) membership testing for large device collections.

3. **Ignoring integer memory overhead**: Creating millions of integer objects in Python without considering memory constraints in embedded IoT applications.

4. **Incorrect struct format strings**: Misusing endianness markers (> for big-endian, < for little-endian) leading to incorrectly parsed sensor data.

5. **Modifying dictionaries during iteration**: Causing runtime errors by modifying dict size during iteration—iterate over a copy instead.