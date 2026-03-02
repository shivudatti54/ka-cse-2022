c
#include <omp.h>
#define N 1000000

int main() {
    double total_sum = 0.0;
    double partial_sums[4] = {0}; // Assume 4 threads

    #pragma omp parallel num_threads(4)
    {
        int tid = omp_get_thread_num();
        #pragma omp for
        for (int i = 0; i < N; i++) {
            partial_sums[tid] += 1; // All threads write to adjacent elements
        }
    }

    // ... combine partial_sums into total_sum
    return 0;
}