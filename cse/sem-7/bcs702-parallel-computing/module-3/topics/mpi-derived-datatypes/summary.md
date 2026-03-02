# MPI Derived Datatypes

=====================================

### Overview

MPI Derived Datatypes allow communication of non-contiguous and complex data structures without manual packing and unpacking. They describe memory layouts so MPI can directly gather scattered data for sending or scatter received data to correct locations. The process involves construction, commit, use, and free.

### Key Points

- **MPI_Type_contiguous:** Creates a datatype for a contiguous block of existing types (simplest constructor)
- **MPI_Type_vector:** Creates a datatype for equally spaced blocks with fixed strides; ideal for matrix rows/columns
- **MPI_Type_indexed:** Creates a datatype with irregular displacements and variable block lengths
- **MPI_Type_create_struct:** Most general constructor; handles different field types (for C structs)
- **MPI_Type_commit:** Must be called before a derived datatype can be used in communication
- **MPI_Type_free:** Releases resources associated with a derived datatype
- **MPI_Get_address:** Portably obtains memory addresses for displacement calculations in struct types
- **Efficiency:** Avoids overhead of creating temporary packing/unpacking buffers

### Important Concepts

- Lifecycle: Construct -> Commit -> Use -> Free
- In MPI_Type_vector, stride is measured in elements; in MPI_Type_indexed and MPI_Type_create_struct, displacements are in bytes
- When using derived datatypes in Send/Recv, the count is typically 1 (the derived type describes the full layout)
- Always use `MPI_Get_address()` and `MPI_Aint_diff()` for struct displacements, never hard-code with sizeof()

### Notes

- Derived datatypes are only beneficial when reused multiple times (creation has overhead)
- Sender and receiver datatypes must be compatible in total byte count, not necessarily identical types
- For sending matrix columns in row-major storage, use MPI_Type_vector with stride = number of columns
- The count parameter in communication calls refers to instances of the derived type, not base elements
