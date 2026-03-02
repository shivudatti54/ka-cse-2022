# MPI Derived Datatypes

## Introduction to Derived Datatypes

In MPI (Message Passing Interface), communication typically involves sending and receiving contiguous blocks of data of a basic datatype (like `MPI_INT`, `MPI_DOUBLE`). However, real-world applications often need to communicate **non-contiguous** data structures—elements scattered throughout memory, such as specific array sections, rows/columns of matrices, or fields within structures.

MPI **Derived Datatypes** solve this problem. They are user-defined datatypes that describe complex data layouts in memory. Instead of manually packing non-contiguous data into a temporary buffer for sending and unpacking it upon receipt (which is inefficient and cumbersome), you can create a derived datatype that describes this layout once. MPI can then use this description to directly gather the scattered data from memory for sending or scatter received data to the correct memory locations.

### Why Use Derived Datatypes?
*   **Efficiency:** Avoids the overhead of creating and managing temporary packing/unpacking buffers.
*   **Performance:** Allows MPI implementations to optimize communication by understanding the data layout, potentially leveraging hardware features like DMA (Direct Memory Access).
*   **Code Clarity and Maintainability:** The communication code becomes cleaner and more intuitive. You send/receive a logical "unit" of data (e.g., a row, a column, a struct) rather than dealing with byte offsets and buffer management.
*   **Portability:** The description of the data layout is abstracted away from specific memory addresses, making code more portable.

## Key Concepts and Constructor Functions

Creating a derived datatype is a two-step process:
1.  **Construction:** Define the new datatype using MPI constructor functions. This creates a *datatype object*.
2.  **Commit:** Before the new datatype can be used for communication, it must be "committed" using `MPI_Type_commit()`. This allows the MPI implementation to optimize its internal representation for communication.
3.  **Use:** Use the committed datatype in communication calls like `MPI_Send`, `MPI_Recv`, `MPI_Bcast`, etc.
4.  **Free:** When the datatype is no longer needed, it should be freed using `MPI_Type_free()` to release associated resources.

Here are the most commonly used constructor functions:

### 1. `MPI_Type_contiguous`
Creates a datatype representing a contiguous block of existing datatypes. It's often used to send a large number of a basic type as a single entity, though its utility is more pronounced when combined with other constructors.

**Function Signature:**
```c
int MPI_Type_contiguous(int count, MPI_Datatype oldtype, MPI_Datatype *newtype);
```
*   `count`: Number of elements in the block.
*   `oldtype`: Datatype of each element (e.g., `MPI_INT`).
*   `newtype`: The new contiguous datatype (output parameter).

**Example:**
```c
// Create a datatype for a contiguous block of 50 integers
MPI_Datatype contig_int50;
MPI_Type_contiguous(50, MPI_INT, &contig_int50);
MPI_Type_commit(&contig_int50);
// Now you can send/receive 50 integers as one unit
MPI_Send(data, 1, contig_int50, dest, tag, MPI_COMM_WORLD);
```

### 2. `MPI_Type_vector`
Creates a datatype representing equally spaced blocks (strides) of an existing datatype. This is perfect for sending rows or columns of a matrix or any regularly strided data.

**Function Signature:**
```c
int MPI_Type_vector(int count, int blocklength, int stride, MPI_Datatype oldtype, MPI_Datatype *newtype);
```
*   `count`: Number of blocks.
*   `blocklength`: Number of elements in each block.
*   `stride`: Number of elements *between the starts* of consecutive blocks (measured in elements of `oldtype`).
*   `oldtype`: Datatype of each element.
*   `newtype`: The new vector datatype.

**Example: Sending a Matrix Row**
Imagine a matrix stored in row-major order. To send a single row, the data is contiguous. But to send a single *column*, the elements are spaced far apart.
```
Matrix (3x4):
Index:  [0]  [1]  [2]  [3]   [4]  [5]  [6]  [7]   [8]  [9] [10] [11]
Value: | a00  a01  a02  a03 | a10  a11  a12  a13 | a20  a21  a22  a23 |
```
To create a datatype for the first column (`a00, a10, a20`):
*   `count = 3` (number of blocks, i.e., rows)
*   `blocklength = 1` (one element per block, i.e., one element per row)
*   `stride = 4` (distance from `a0x` to `a1x`, i.e., the number of columns)

```c
MPI_Datatype column_type;
MPI_Type_vector(3, 1, 4, MPI_DOUBLE, &column_type); // Assumes matrix is 3x4 of doubles
MPI_Type_commit(&column_type);
// 'matrix' is a 1D array of 12 doubles representing the 3x4 matrix
MPI_Send(&matrix[0], 1, column_type, dest, tag, MPI_COMM_WORLD); // Sends a00, a10, a20
```

### 3. `MPI_Type_indexed`
Creates a datatype representing blocks of an existing datatype that can start at arbitrary displacements (offsets). This is more general than `MPI_Type_vector` because the blocks can be of different lengths and have irregular spacing.

**Function Signature:**
```c
int MPI_Type_indexed(int count, const int array_of_blocklengths[], const int array_of_displacements[], MPI_Datatype oldtype, MPI_Datatype *newtype);
```
*   `count`: Number of blocks.
*   `array_of_blocklengths`: Array specifying the number of elements in each block.
*   `array_of_displacements`: Array specifying the *byte displacement* (offset) of the start of each block from the start of the buffer.
*   `oldtype`: Datatype of each element.
*   `newtype`: The new indexed datatype.

**Example: Sending Specific Array Elements**
Send elements at indices 1, 5, and 8-10 from an array.
```c
int blens[3] = {1, 1, 3};    // Block lengths: 1 elem, 1 elem, 3 elems
int displs[3];                // Displacements in bytes
displs[0] = 1 * sizeof(int);  // Offset for index 1
displs[1] = 5 * sizeof(int);  // Offset for index 5
displs[2] = 8 * sizeof(int);  // Offset for index 8

MPI_Datatype indexed_type;
MPI_Type_indexed(3, blens, displs, MPI_INT, &indexed_type);
MPI_Type_commit(&indexed_type);
MPI_Send(array, 1, indexed_type, dest, tag, MPI_COMM_WORLD);
```

### 4. `MPI_Type_create_struct`
The most general constructor. It creates a datatype representing data that may consist of multiple blocks, each of a *different* basic or derived datatype. This is essential for sending C `structs` or Fortran `TYPE`s.

**Function Signature:**
```c
int MPI_Type_create_struct(int count, const int array_of_blocklengths[], const MPI_Aint array_of_displacements[], const MPI_Datatype array_of_types[], MPI_Datatype *newtype);
```
*   `count`: Number of blocks (fields in the structure).
*   `array_of_blocklengths`: Number of elements of each type in each block (often 1 for struct fields).
*   `array_of_displacements`: *Byte displacements* of each field from the start of the struct. **Crucially, use `MPI_Get_address()` to get these portably instead of relying on `sizeof()` and manual calculation.**
*   `array_of_types`: The datatype of each field/block.
*   `newtype`: The new struct datatype.

**Example: Sending a C Structure**
```c
typedef struct {
    int id;
    double value[3];
    char tag;
} Particle;

Polecule part;
// ... populate 'part' ...

// 1. Define the structure of the datatype
int count = 3;
int blocklengths[3] = {1, 3, 1}; // 1 int, 3 doubles, 1 char
MPI_Aint displacements[3];        // Use MPI_Aint for addresses
MPI_Datatype types[3] = {MPI_INT, MPI_DOUBLE, MPI_CHAR};

// 2. Get the actual displacements portably
MPI_Aint base_address;
MPI_Get_address(&part, &base_address); // Get base address of struct
MPI_Get_address(&part.id, &displacements[0]);
MPI_Get_address(&part.value[0], &displacements[1]);
MPI_Get_address(&part.tag, &displacements[2]);

// Calculate displacement from base
displacements[0] = MPI_Aint_diff(displacements[0], base_address);
displacements[1] = MPI_Aint_diff(displacements[1], base_address);
displacements[2] = MPI_Aint_diff(displacements[2], base_address);

// 3. Create and commit the type
MPI_Datatype particle_type;
MPI_Type_create_struct(count, blocklengths, displacements, types, &particle_type);
MPI_Type_commit(&particle_type);

// 4. Use it
MPI_Send(&part, 1, particle_type, dest, tag, MPI_COMM_WORLD);
```

## Communication with Derived Datatypes

Using a derived datatype in communication calls is straightforward. The buffer argument points to the start of the memory region containing the data, and the datatype argument is the committed derived type. The count is typically 1, as the entire complex layout is described by the single datatype.

```c
MPI_Send/MPI_Recv(start_buffer_address, 1, my_derived_type, target, tag, comm);
```
For collective operations:
```c
MPI_Bcast(start_buffer_address, 1, my_derived_type, root, comm);
MPI_Scatter(sendbuf, 1, send_type, recvbuf, 1, recv_type, root, comm);
// ... etc.
```

## Performance Considerations

*   **Overhead vs. Benefit:** Creating and committing a datatype has overhead. It's only beneficial if the datatype is reused multiple times. For a one-time communication pattern, manual packing might be simpler.
*   **Implementation Optimization:** A good MPI implementation can use the layout information in a derived datatype to perform "vector" or "gather" operations directly from memory, which can be much faster than a user-controlled pack/send/unpack sequence.
*   **Matching Datatypes:** The sender and receiver must use **compatible datatypes**. The receiver can use a matching derived datatype or, more commonly, a basic datatype with a sufficiently large count to receive the raw bytes. The layout and meaning are interpreted based on the sender's derived type.

## Summary of Constructor Functions
| Function | Use Case | Key Feature |
| :--- | :--- | :--- |
| `MPI_Type_contiguous` | Simple contiguous blocks | Simplest constructor |
| `MPI_Type_vector` | Rows, columns, strided data | Regular, fixed strides |
| `MPI_Type_indexed` | Arbitrary non-contiguous data | Irregular displacements, same base type |
| `MPI_Type_create_struct` | C structs, Fortran types | Different field types, most general |

## Exam Tips
1.  **Know the Steps:** Always remember the sequence: **Construct -> Commit -> Use -> Free**.
2.  **Displacement Units:** Pay close attention to the units for `stride` (elements) in `MPI_Type_vector` vs. `displacement` (bytes) in `MPI_Type_indexed` and `MPI_Type_create_struct`.
3.  **Use `MPI_Get_address`:** For `MPI_Type_create_struct`, always use `MPI_Get_address` and `MPI_Aint_diff` to calculate displacements. Never hard-code them using `sizeof()`. This is a very common exam point.
4.  **Count Parameter:** In communication calls using a derived datatype, the `count` is the number of *instances* of that derived datatype, not the number of base elements. Often, this count is 1.
5.  **Match Types:** Understand that the receiver's datatype must be able to handle the number of bytes sent. It doesn't have to be an identical derived type.