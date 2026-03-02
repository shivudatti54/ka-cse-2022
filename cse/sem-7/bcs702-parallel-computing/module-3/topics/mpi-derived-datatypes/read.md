# MPI Derived Datatypes

## 1. Introduction and Theoretical Foundation

In the Message Passing Interface (MPI), standard communication operations such as `MPI_Send` and `MPI_Recv` are designed primarily for transmitting **contiguous** blocks of data with homogeneous datatypes (e.g., `MPI_INT`, `MPI_DOUBLE`, `MPI_FLOAT`). However, parallel scientific and engineering applications frequently operate on **non-contiguous** data structures scattered throughout memory. Examples include:

- Rows or columns of multidimensional arrays stored in row-major or column-major order
- Specific elements from distributed arrays requiring selective communication
- Heterogeneous structures containing multiple primitive fields
- Subarrays embedded within larger global data structures

The **naive approach** to handling non-contiguous communication involves manually **packing** scattered data elements into a temporary contiguous buffer before transmission, followed by **unpacking** received data into the appropriate memory locations. This approach, while functionally correct, introduces significant overhead:

- **Computational overhead**: Additional memory copy operations for packing/unpacking
- **Memory overhead**: Allocation of temporary buffers
- **Programming complexity**: Explicit management of displacement calculations and buffer indices
- **Performance degradation**: Negates potential hardware optimizations (e.g., DMA transfers)

**MPI Derived Datatypes** provide an elegant solution by allowing programmers to **abstract** the logical structure of non-contiguous data into a reusable type object. Once defined and committed, MPI implementations can directly access scattered memory locations, enabling optimized data movement without intermediate buffers.

### 1.1 Formal Definition

A derived datatype is a **user-defined MPI datatype** that describes a collection of basic (or previously derived) datatypes arranged according to a specified **type map**:

```
Type Map = {(type_0, disp_0), (type_1, disp_1), ..., (type_{n-1}, disp_{n-1})}
```

Where each pair `(type_i, disp_i)` specifies:

- `type_i`: A fundamental or derived MPI datatype
- `disp_i`: The byte displacement of this element from the base address

The **extent** of a datatype, denoted as `extent(T)`, is defined as the distance between the first byte of the first element and the first byte of the last element, plus the size of the last element. Formally:

```
extent(T) = max{disp_i + sizeof(type_i)} - min{disp_i}
```

This concept is crucial for understanding how MPI calculates communication buffer sizes and displacement indices.

## 2. Lifecycle of Derived Datatypes

Every derived datatype follows a specific lifecycle:

1. **Construction**: Create the datatype using constructor functions (returns an uncommitted handle)
2. **Commitment**: Call `MPI_Type_commit()` to enable use in communication operations
3. **Application**: Use the committed datatype in send, receive, or collective operations
4. **Deallocation**: Call `MPI_Type_free()` to release resources when no longer needed

### 2.1 Commitment Semantics

The `MPI_Type_commit()` function is mandatory before first use in communication. MPI implementations perform internal optimizations upon commitment:

- Construction of optimized data movement descriptors
- Pre-computation of memory access patterns
- Registration with communication hardware where applicable

```c
int MPI_Type_commit(MPI_Datatype *datatype);
```

### 2.2 Deallocation

```c
int MPI_Type_free(MPI_Datatype *datatype);
```

Upon successful free, the datatype handle is set to `MPI_DATATYPE_NULL`. Note that pending communications using the datatype remain valid.

## 3. Constructor Functions

### 3.1 MPI_Type_contiguous

Creates a new datatype representing `count` contiguous copies of an existing datatype.

**Function Signature:**

```c
int MPI_Type_contiguous(int count, MPI_Datatype oldtype, MPI_Datatype *newtype);
```

**Parameters:**

- `count`: Number of consecutive elements
- `oldtype`: Base MPI datatype (e.g., `MPI_INT`, `MPI_DOUBLE`)
- `newtype`: Output handle to the new contiguous datatype

**Type Map Construction:**
If `oldtype` has type map `{(t, d_0), (t, d_1), ..., (t, d_{k-1})}`, then `newtype` with parameter `count` constructs:

```
{(t, 0), (t, sizeof(t)), (t, 2*sizeof(t)), ..., (t, (count*k-1)*sizeof(t))}
```

**Theorem:** For a contiguous datatype created with `count` copies of `oldtype`, the total byte extent equals `count × sizeof(oldtype)`.

**Proof:** The first element begins at displacement 0. The last element (element number `count-1`) begins at displacement `(count-1) × sizeof(oldtype)`. Adding the size of `oldtype` gives the upper bound: `(count-1) × sizeof(oldtype) + sizeof(oldtype) = count × sizeof(oldtype)`. Since the minimum displacement is 0, the extent is `count × sizeof(oldtype) - 0 = count × sizeof(oldtype)`. ∎

**Example:**

```c
// Create datatype for 100 contiguous doubles
MPI_Datatype contig_100_double;
MPI_Type_contiguous(100, MPI_DOUBLE, &contig_100_double);
MPI_Type_commit(&contig_100_double);

// Communication: send 100 doubles as atomic unit
double buffer[100];
MPI_Send(buffer, 1, contig_100_double, dest, tag, MPI_COMM_WORLD);
```

### 3.2 MPI_Type_vector

The vector datatype addresses **regularly strided** non-contiguous data, where blocks of equal size appear at uniform intervals. This is fundamental for row/column communication in matrix operations.

**Function Signature:**

```c
int MPI_Type_vector(int count, int blocklength, int stride,
                    MPI_Datatype oldtype, MPI_Datatype *newtype);
```

**Parameters:**

- `count`: Number of blocks
- `blocklength`: Number of elements in each block
- `stride`: Number of elements between starts of consecutive blocks (measured in units of `oldtype`)
- `newtype`: Output handle

**Memory Layout Diagram:**

Consider a 4×3 matrix stored in row-major order:

```
Index:    [0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]  [10]  [11]
Matrix:  | a00| a01| a02| a10| a11| a12| a20| a21| a22| a30| a31| a32 |
          |____|    |    |____|    |    |____|    |    |____|    |    |
          block 1         block 2         block 3         block 4
```

To extract column 1 (`a01, a11, a21, a31`):

- `count = 4` (four blocks/rows)
- `blocklength = 1` (one element per row)
- `stride = 3` (distance between elements = number of columns)

**Example: Extracting Matrix Column:**

```c
#define ROWS 4
#define COLS 3

double matrix[ROWS * COLS];  // Row-major storage

// Create datatype for column 1
MPI_Datatype col_type;
MPI_Type_vector(ROWS, 1, COLS, MPI_DOUBLE, &col_type);
MPI_Type_commit(&col_type);

// Send first column (elements at indices 1, 4, 7, 10)
MPI_Send(&matrix[1], 1, col_type, dest, tag, MPI_COMM_WORLD);
```

**Theorem:** For `MPI_Type_vector(count, blocklength, stride, oldtype, &newtype)`, the total extent in bytes equals:

```
extent(newtype) = (count - 1) × stride × sizeof(oldtype) + blocklength × sizeof(oldtype)
```

**Proof:** The first block begins at displacement 0. The first element of block `i` (0-indexed) begins at displacement `i × stride × sizeof(oldtype)`. For the last block (`i = count-1`), the displacement of its first element is `(count-1) × stride × sizeof(oldtype)`. The last element within block `count-1` is at displacement `(count-1) × stride × sizeof(oldtype) + (blocklength-1) × sizeof(oldtype)`. Adding the size of one element gives the upper bound: `(count-1) × stride × sizeof(oldtype) + blocklength × sizeof(oldtype)`. ∎

### 3.3 MPI_Type_indexed

The indexed datatype provides **irregular** block distributions where each block may have different length and arbitrary starting displacements specified in bytes.

**Function Signature:**

```c
int MPI_Type_indexed(int count, const int array_of_blocklengths[],
                     const int array_of_displacements[],
                     MPI_Datatype oldtype, MPI_Datatype *newtype);
```

**Parameters:**

- `count`: Number of blocks
- `array_of_blocklengths[i]`: Number of elements in block `i`
- `array_of_displacements[i]`: Byte displacement from base address for block `i`
- `oldtype`: Base datatype
- `newtype`: Output handle

**Critical Distinction:** Unlike `stride` in vector type (measured in elements), displacements in indexed types are measured in **bytes**.

**Example: Selective Array Elements:**

```c
int data[20] = { /* initialized values */ };

// Send elements at indices 2, 7-9, and 15-17
int blocklens[3] = {1, 3, 3};
int displs[3];

displs[0] = 2 * sizeof(int);      // Index 2
displs[1] = 7 * sizeof(int);      // Indices 7, 8, 9
displs[2] = 15 * sizeof(int);     // Indices 15, 16, 17

MPI_Datatype indexed_type;
MPI_Type_indexed(3, blocklens, displs, MPI_INT, &indexed_type);
MPI_Type_commit(&indexed_type);

MPI_Send(data, 1, indexed_type, dest, tag, MPI_COMM_WORLD);
```

### 3.4 MPI_Type_struct

The structure datatype is the **most general** constructor, allowing combination of different basic datatypes at arbitrary byte displacements—essential for communicating fields within C structures.

**Function Signature:**

```c
int MPI_Type_struct(int count, const int array_of_blocklengths[],
                    const MPI_Aint array_of_displacements[],
                    const MPI_Datatype array_of_oldtypes[],
                    MPI_Datatype *newtype);
```

**Key Differences from Indexed:**

- Uses `MPI_Aint` (signed integer type) for displacements (platform-independent addressing)
- Allows heterogeneous `oldtype` array (different datatypes per block)

**Example: Particle Structure:**

```c
struct Particle {
    double position[3];  // 3 doubles: x, y, z (offset 0)
    double velocity[3];  // 3 doubles (offset 24)
    int    id;           // 1 int (offset 48)
    float  mass;        // 1 float (offset 52)
};
// Total size: 56 bytes (with padding)

struct Particle particles[100];

MPI_Datatype particle_type;
int blocklens[4] = {3, 3, 1, 1};
MPI_Aint displs[4];
MPI_Datatype oldtypes[4] = {MPI_DOUBLE, MPI_DOUBLE, MPI_INT, MPI_FLOAT};

// Calculate displacements using offsetof or explicit calculation
displs[0] = offsetof(struct Particle, position);
displs[1] = offsetof(struct Particle, velocity);
displs[2] = offsetof(struct Particle, id);
displs[3] = offsetof(struct Particle, mass);

MPI_Type_struct(4, blocklens, displs, oldtypes, &particle_type);
MPI_Type_commit(&particle_type);

// Send particle 5
MPI_Send(&particles[5], 1, particle_type, dest, tag, MPI_COMM_WORLD);
```

## 4. Advanced Concepts

### 4.1 Type Extent and Resizing

Sometimes the logical extent of a datatype differs from its physical extent due to padding or alignment requirements. The **extent** determines how MPI calculates buffer positions in structured communications.

```c
int MPI_Type_get_extent(MPI_Datatype datatype, MPI_Aint *lb, MPI_Aint *extent);
```

**MPI_Type_create_resized** modifies the lower bound and extent:

```c
int MPI_Type_create_resized(MPI_Datatype oldtype, MPI_Aint lb, MPI_Aint extent,
                            MPI_Datatype *newtype);
```

This is useful when creating datatypes for subarrays or when padding is required for alignment.

### 4.2 Performance Implications

**Theorem:** Use of derived datatypes provides performance benefits when the ratio of computation to communication is low and the data access pattern is regular.

**Proof Sketch:** Without derived datatypes, non-contiguous communication requires:

1. `N` pack operations: O(N) memory operations
2. Communication of contiguous buffer: O(M) data transfer
3. `N` unpack operations: O(N) memory operations

With derived datatypes, only step 2 occurs, potentially with hardware-assisted scatter/gather. The packing/unpacking overhead O(N) is eliminated. ∎

However, for highly irregular patterns or small data sizes, the overhead of datatype internal representation may exceed manual packing costs.

## 5. Practical Applications

### 5.1 Halo Exchange in Stencil Computations

In finite difference methods, each process exchanges boundary values with neighbors:

```c
void halo_exchange(double *u, int nx, int ny, int rank, int nprocs) {
    MPI_Datatype column, row;

    // Column datatype (for east-west exchange)
    MPI_Type_vector(ny, 1, nx, MPI_DOUBLE, &column);
    MPI_Type_commit(&column);

    // Row datatype (for north-south exchange) - contiguous
    MPI_Type_contiguous(nx, MPI_DOUBLE, &row);
    MPI_Type_commit(&row);

    // Receive from west, send to east (halo width = 1)
    MPI_Sendrecv(&u[1], 1, row, right, 0,
                 &u[nx*(ny-1)+1], 1, row, left, 0,
                 MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    // Vertical exchange using column type
    // ... (similar pattern)

    MPI_Type_free(&column);
    MPI_Type_free(&row);
}
```

### 5.2 Distributed Matrix-Vector Multiplication

For row-partitioned matrix distribution:

```c
// Each process owns consecutive rows
int local_rows = n / nprocs;
MPI_Datatype row_type;
MPI_Type_contiguous(n, MPI_DOUBLE, &row_type);
MPI_Type_commit(&row_type);

// Broadcast entire vector to all processes
MPI_Bcast(x, 1, vector_type, 0, MPI_COMM_WORLD);

// Local matrix-vector multiply: y = A * x
for (int i = 0; i < local_rows; i++) {
    y[i] = 0;
    for (int j = 0; j < n; j++)
        y[i] += A[i*n + j] * x[j];
}
```

## 6. Common Pitfalls and Best Practices

1. **Displacement Unit Confusion**: Vector uses element stride; indexed uses byte displacements
2. **Commitment Forgotten**: Always commit before use; uncommitted datatypes cause runtime errors
3. **Memory Overlap**: Derived datatype regions must not overlap in communication buffers
4. **Extent Miscalculation**: Account for padding when using structures
5. **Type Matching**: Sender and receiver must use matching (or compatible) datatypes
6. **Resource Management**: Free datatypes when done to prevent memory leaks

## 7. Summary

MPI Derived Datatypes provide a powerful abstraction for describing complex, non-contiguous memory layouts. By enabling direct communication of scattered data structures, they significantly improve code readability, maintainability, and often performance. The four primary constructors—`MPI_Type_contiguous`, `MPI_Type_vector`, `MPI_Type_indexed`, and `MPI_Type_struct`—cover the majority of practical scenarios in parallel scientific computing.

Understanding type extent, commitment semantics, and displacement calculations is essential for correct usage. For B.Tech-level studies, mastery of these constructors with ability to compute displacements and analyze communication patterns is expected.
