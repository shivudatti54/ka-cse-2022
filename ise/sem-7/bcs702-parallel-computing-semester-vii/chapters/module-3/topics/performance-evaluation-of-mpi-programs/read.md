c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    double start_time, end_time;
    int rank;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Barrier(MPI_COMM_WORLD); // Synchronize all processes
    start_time = MPI_Wtime();    // Get the current time

    // ... Core parallel computation and communication happens here ...

    end_time = MPI_Wtime();
    if (rank == 0) {
        printf("Total execution time with %d processes: %f seconds\n", num_procs, end_time - start_time);
    }

    MPI_Finalize();
    return 0;
}