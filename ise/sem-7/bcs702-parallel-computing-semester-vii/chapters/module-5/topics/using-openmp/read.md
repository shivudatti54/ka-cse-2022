c
    #include <stdio.h>
    #include <omp.h>

    int main() {
        // Serial code here
        printf("This is serial. Thread ID: %d\n", omp_get_thread_num());

        #pragma omp parallel
        {
            // This code block is executed by all threads in parallel
            printf("Hello from thread %d of %d\n", 
                   omp_get_thread_num(), omp_get_work_thread_num());
        }

        // Back to serial code
        printf("Back to serial.\n");
        return 0;
    }