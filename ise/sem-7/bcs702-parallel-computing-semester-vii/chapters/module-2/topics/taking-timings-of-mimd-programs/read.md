c
#include <stdio.h>
#include <time.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank, size;
    struct timespec start, stop;
    double elapsed_time;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Synchronize all processes before starting the timer
    MPI_Barrier(MPI_COMM_WORLD);

    // Only rank 0 takes the start time
    if (rank == 0) {
        clock_gettime(CLOCK_MONOTONIC, &start);
    }

    // --- This is the parallel region whose time we want to measure ---
    // (e.g., your matrix multiplication, numerical simulation, etc.)
    do_parallel_work(rank, size);
    // -----------------------------------------------------------------

    // Synchronize again after work is done
    MPI_Barrier(MPI_COMM_WORLD);

    // Only rank 0 takes the stop time and calculates the difference
    if (rank == 0) {
        clock_gettime(CLOCK_MONOTONIC, &stop);

        // Calculate elapsed time in seconds
        elapsed_time = (stop.tv_sec - start.tv_sec);
        elapsed_time += (stop.tv_nsec - start.tv_nsec) / 1.0e9;

        printf("Parallel execution time: %.6f seconds\n", elapsed_time);
    }

    MPI_Finalize();
    return 0;
}