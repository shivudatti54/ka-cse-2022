# Learning Purpose: MPI Derived Datatypes

**1. Why this topic matters**
Real-world data structures such as structs, non-contiguous array sections, and mixed-type records cannot be sent directly using basic MPI datatypes without manual packing and unpacking. MPI derived datatypes provide an efficient mechanism to describe complex data layouts so they can be communicated in a single operation, reducing both programming complexity and communication overhead. This capability is essential for practical MPI programming beyond simple arrays.

**2. What you will learn**
You will learn the four-step lifecycle of MPI derived datatypes: construction, commitment, use, and freeing. You will understand how to select the appropriate constructor (MPI_Type_contiguous, MPI_Type_vector, MPI_Type_indexed, MPI_Type_create_struct) for different data layout patterns, and use committed derived datatypes in both point-to-point and collective communication calls to send complex data structures efficiently.

**3. How it connects to other topics**
MPI derived datatypes extend the core MPI functions and collective communication covered earlier in this module, enabling more sophisticated data exchange patterns. They are particularly important for the parallel sorting algorithm that follows, where non-contiguous data segments must be communicated. This topic also connects to performance evaluation, as derived datatypes can significantly reduce communication overhead.

**4. Real-world relevance**
MPI derived datatypes are used extensively in scientific simulations that communicate structured grid data, particle attributes, or multi-field records between processes. Applications in computational fluid dynamics, weather modeling, and finite element analysis rely on derived datatypes to efficiently exchange complex domain decomposition boundaries and structured data.
