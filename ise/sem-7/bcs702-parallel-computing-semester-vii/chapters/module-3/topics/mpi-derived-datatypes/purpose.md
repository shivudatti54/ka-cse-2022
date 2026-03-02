# Learning Objectives
After studying this topic, you should be able to:
1.  Explain the motivation for using MPI derived datatypes and identify scenarios where they are more efficient than manual data packing.
2.  Describe the four-step lifecycle of a derived datatype: construction, commitment, use, and freeing.
3.  Select the appropriate MPI constructor function (contiguous, vector, indexed, struct) for a given data layout pattern.
4.  Construct a derived datatype using `MPI_Type_vector` to communicate rows or columns of a matrix.
5.  Construct a derived datatype using `MPI_Type_create_struct` to communicate a C structure or Fortran derived type, correctly utilizing `MPI_Get_address` for portable displacement calculation.
6.  Utilize a committed derived datatype in point-to-point and collective communication calls.